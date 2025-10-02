from dataclasses import dataclass, field
from typing import List, Dict, Optional
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
import os


@dataclass
class Student:
    student_id: int
    name: str
    major: str
    credits_completed: int = 0
    gpa: float = 0.0
    enrolled_courses: List[str] = field(default_factory=list)
    grades: Dict[str, str] = field(default_factory=dict)

    def enroll_course(self, course_name: str) -> str:
        """Enroll student in a course"""
        try:
            if not course_name or course_name.strip() == "":
                raise ValueError("Course name cannot be empty")

            course_name = course_name.strip()
            if course_name in self.enrolled_courses:
                return f'⚠️  {self.name} is already enrolled in {course_name}'

            self.enrolled_courses.append(course_name)
            return f'✅ {self.name} has successfully enrolled in {course_name}.'
        except ValueError as e:
            return f'❌ Error: {str(e)}'
        except Exception as e:
            return f'❌ Unexpected error: {str(e)}'

    def complete_course(self, course_name: str, credits: int, grade: str = 'P') -> str:
        """Complete a course and add credits"""
        try:
            if not course_name or course_name.strip() == "":
                raise ValueError("Course name cannot be empty")

            if credits <= 0:
                raise ValueError("Credits must be a positive number")

            course_name = course_name.strip()
            if course_name not in self.enrolled_courses:
                return f"❌ {self.name} is not enrolled in {course_name}, so it cannot be completed."

            self.enrolled_courses.remove(course_name)
            self.credits_completed += credits
            self.grades[course_name] = grade
            self._update_gpa()

            return f"🏆 {self.name} has completed {course_name} with grade {grade} and earned {credits} credits."
        except ValueError as e:
            return f'❌ Error: {str(e)}'
        except Exception as e:
            return f'❌ Unexpected error: {str(e)}'

    def drop_course(self, course_name: str) -> str:
        """Drop an enrolled course"""
        try:
            if not course_name or course_name.strip() == "":
                raise ValueError("Course name cannot be empty")

            course_name = course_name.strip()
            if course_name not in self.enrolled_courses:
                return f"❌ {self.name} is not enrolled in {course_name}"

            self.enrolled_courses.remove(course_name)
            return f"🗑️  {self.name} has dropped {course_name}"
        except ValueError as e:
            return f'❌ Error: {str(e)}'
        except Exception as e:
            return f'❌ Unexpected error: {str(e)}'

    def _update_gpa(self):
        """Calculate GPA based on grades"""
        grade_points = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                        'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0, 'P': 3.0}

        if self.grades:
            total_points = sum(grade_points.get(grade, 0.0)
                               for grade in self.grades.values())
            self.gpa = round(total_points / len(self.grades), 2)

    def get_transcript(self) -> str:
        """Get student's academic transcript"""
        if not self.grades:
            return f"📄 {self.name} has no completed courses yet."

        transcript = f"\n📄 Academic Transcript for {self.name}\n{'='*50}\n"
        for course, grade in self.grades.items():
            transcript += f"  • {course}: {grade}\n"
        transcript += f"{'='*50}\n"
        return transcript
    
    def generate_pdf_transcript(self, filename: str = None) -> str:
        """Generate a professional PDF transcript"""
        try:
            if not self.grades:
                return "❌ No completed courses to generate transcript."
            
            # Create filename if not provided
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"Transcript_{self.student_id}_{self.name.replace(' ', '_')}_{timestamp}.pdf"
            
            # Ensure .pdf extension
            if not filename.endswith('.pdf'):
                filename += '.pdf'
            
            # Create PDF
            doc = SimpleDocTemplate(filename, pagesize=letter,
                                    rightMargin=72, leftMargin=72,
                                    topMargin=72, bottomMargin=18)
            
            # Container for the 'Flowable' objects
            elements = []
            
            # Define styles
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1a237e'),
                spaceAfter=30,
                alignment=TA_CENTER,
                fontName='Helvetica-Bold'
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=16,
                textColor=colors.HexColor('#283593'),
                spaceAfter=12,
                spaceBefore=12,
                fontName='Helvetica-Bold'
            )
            
            normal_style = ParagraphStyle(
                'CustomNormal',
                parent=styles['Normal'],
                fontSize=11,
                textColor=colors.black,
                spaceAfter=6
            )
            
            # Add University Header
            title = Paragraph("<b>ACADEMIC TRANSCRIPT</b>", title_style)
            elements.append(title)
            elements.append(Spacer(1, 0.2*inch))
            
            # Add horizontal line
            from reportlab.platypus import HRFlowable
            elements.append(HRFlowable(width="100%", thickness=2, 
                                       color=colors.HexColor('#1a237e'),
                                       spaceAfter=20, spaceBefore=10))
            
            # Student Information Section
            info_heading = Paragraph("<b>Student Information</b>", heading_style)
            elements.append(info_heading)
            
            # Student info table
            student_data = [
                ['Student ID:', str(self.student_id)],
                ['Name:', self.name],
                ['Major:', self.major],
                ['Credits Completed:', str(self.credits_completed)],
                ['GPA:', f"{self.gpa:.2f}"],
                ['Issue Date:', datetime.now().strftime('%B %d, %Y')]
            ]
            
            student_table = Table(student_data, colWidths=[2*inch, 4*inch])
            student_table.setStyle(TableStyle([
                ('FONT', (0, 0), (0, -1), 'Helvetica-Bold', 10),
                ('FONT', (1, 0), (1, -1), 'Helvetica', 10),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#283593')),
                ('TEXTCOLOR', (1, 0), (1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f5f5f5')),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
            ]))
            elements.append(student_table)
            elements.append(Spacer(1, 0.3*inch))
            
            # Academic Record Section
            record_heading = Paragraph("<b>Academic Record</b>", heading_style)
            elements.append(record_heading)
            
            # Courses table
            course_data = [['Course Name', 'Grade', 'Grade Points']]
            
            grade_points_map = {
                'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
                'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 
                'F': 0.0, 'P': 3.0
            }
            
            for course, grade in sorted(self.grades.items()):
                grade_point = grade_points_map.get(grade, 0.0)
                course_data.append([course, grade, f"{grade_point:.1f}"])
            
            # Add summary row
            course_data.append(['', '', ''])
            course_data.append(['Total Courses Completed:', str(len(self.grades)), ''])
            course_data.append(['Cumulative GPA:', f"{self.gpa:.2f}", ''])
            
            course_table = Table(course_data, colWidths=[3.5*inch, 1.5*inch, 1.5*inch])
            course_table.setStyle(TableStyle([
                # Header row styling
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a237e')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('TOPPADDING', (0, 0), (-1, 0), 12),
                
                # Data rows styling
                ('FONT', (0, 1), (-1, -4), 'Helvetica', 10),
                ('ALIGN', (0, 1), (0, -4), 'LEFT'),
                ('ALIGN', (1, 1), (-1, -4), 'CENTER'),
                ('GRID', (0, 0), (-1, -4), 0.5, colors.grey),
                ('ROWBACKGROUNDS', (0, 1), (-1, -4), [colors.white, colors.HexColor('#f5f5f5')]),
                ('TOPPADDING', (0, 1), (-1, -4), 8),
                ('BOTTOMPADDING', (0, 1), (-1, -4), 8),
                
                # Summary rows styling
                ('FONT', (0, -2), (0, -1), 'Helvetica-Bold', 11),
                ('FONT', (1, -2), (1, -1), 'Helvetica-Bold', 11),
                ('TEXTCOLOR', (0, -2), (-1, -1), colors.HexColor('#1a237e')),
                ('ALIGN', (0, -2), (0, -1), 'RIGHT'),
                ('ALIGN', (1, -2), (1, -1), 'CENTER'),
                ('TOPPADDING', (0, -2), (-1, -1), 10),
                ('BOTTOMPADDING', (0, -2), (-1, -1), 10),
                ('BACKGROUND', (0, -2), (-1, -1), colors.HexColor('#e8eaf6')),
                ('LINEABOVE', (0, -2), (-1, -2), 2, colors.HexColor('#1a237e')),
            ]))
            elements.append(course_table)
            elements.append(Spacer(1, 0.5*inch))
            
            # Add footer note
            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=9,
                textColor=colors.grey,
                alignment=TA_CENTER
            )
            footer_text = f"""<i>This is an official academic transcript generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}.<br/>
            For verification purposes, please contact the registrar's office.</i>"""
            footer = Paragraph(footer_text, footer_style)
            elements.append(footer)
            
            # Build PDF
            doc.build(elements)
            
            return f"✅ PDF transcript generated successfully: {filename}"
            
        except Exception as e:
            return f"❌ Error generating PDF: {str(e)}"

    def __str__(self) -> str:
        courses = ', '.join(
            self.enrolled_courses) if self.enrolled_courses else 'None'
        return f"""
{'='*50}
📋 Student Information
{'='*50}
🆔 ID: {self.student_id}
👤 Name: {self.name}
🎓 Major: {self.major}
📚 Credits Completed: {self.credits_completed}
⭐ GPA: {self.gpa}
📝 Currently Enrolled: {courses}
🏆 Completed Courses: {len(self.grades)}
{'='*50}
"""


class StudentManagementSystem:
    """Professional Student Management System"""

    def __init__(self):
        self.students: Dict[int, Student] = {}

    def add_student(self, student_id: int, name: str, major: str) -> str:
        """Add a new student to the system"""
        try:
            if student_id in self.students:
                raise ValueError(
                    f"Student with ID {student_id} already exists")

            if not name or name.strip() == "":
                raise ValueError("Student name cannot be empty")

            if not major or major.strip() == "":
                raise ValueError("Major cannot be empty")

            student = Student(student_id=student_id,
                              name=name.strip(), major=major.strip())
            self.students[student_id] = student
            return f"✅ Student {name} (ID: {student_id}) added successfully!"
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"

    def remove_student(self, student_id: int) -> str:
        """Remove a student from the system"""
        try:
            if student_id not in self.students:
                raise ValueError(f"Student with ID {student_id} not found")

            student_name = self.students[student_id].name
            del self.students[student_id]
            return f"🗑️  Student {student_name} (ID: {student_id}) removed successfully!"
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"

    def get_student(self, student_id: int) -> Optional[Student]:
        """Get a student by ID"""
        try:
            if student_id not in self.students:
                raise ValueError(f"Student with ID {student_id} not found")
            return self.students[student_id]
        except ValueError as e:
            print(f"❌ Error: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
            return None

    def list_all_students(self) -> str:
        """List all students in the system"""
        if not self.students:
            return "📭 No students in the system."

        result = f"\n{'='*50}\n📚 All Students in System ({len(self.students)} total)\n{'='*50}\n"
        for student in self.students.values():
            result += f"🆔 {student.student_id} | 👤 {student.name} | 🎓 {student.major} | ⭐ GPA: {student.gpa}\n"
        result += f"{'='*50}\n"
        return result

    def search_students_by_major(self, major: str) -> str:
        """Search students by major"""
        try:
            if not major or major.strip() == "":
                raise ValueError("Major cannot be empty")

            major = major.strip()
            matching_students = [
                s for s in self.students.values() if s.major.lower() == major.lower()]

            if not matching_students:
                return f"📭 No students found in major: {major}"

            result = f"\n{'='*50}\n🔍 Students in {major} ({len(matching_students)} found)\n{'='*50}\n"
            for student in matching_students:
                result += f"🆔 {student.student_id} | 👤 {student.name} | ⭐ GPA: {student.gpa}\n"
            result += f"{'='*50}\n"
            return result
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"

    def get_statistics(self) -> str:
        """Get system statistics"""
        if not self.students:
            return "📭 No students in the system to generate statistics."

        total_students = len(self.students)
        total_credits = sum(
            s.credits_completed for s in self.students.values())
        avg_gpa = sum(s.gpa for s in self.students.values()) / total_students

        majors = {}
        for student in self.students.values():
            majors[student.major] = majors.get(student.major, 0) + 1

        stats = f"""
{'='*50}
📊 System Statistics
{'='*50}
👥 Total Students: {total_students}
📚 Total Credits Completed: {total_credits}
⭐ Average GPA: {avg_gpa:.2f}
🎓 Majors Distribution:
"""
        for major, count in majors.items():
            stats += f"   • {major}: {count} student(s)\n"
        stats += f"{'='*50}\n"
        return stats


def get_integer_input(prompt: str) -> Optional[int]:
    """Safely get integer input from user"""
    try:
        value = input(prompt).strip()
        if value == "":
            raise ValueError("Input cannot be empty")
        return int(value)
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def get_string_input(prompt: str) -> Optional[str]:
    """Safely get string input from user"""
    try:
        value = input(prompt).strip()
        if value == "":
            raise ValueError("Input cannot be empty")
        return value
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🎓 STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. ➕ Add New Student")
    print("2. 🗑️  Remove Student")
    print("3. 📋 View Student Details")
    print("4. 📚 Enroll Student in Course")
    print("5. 🏆 Complete Course")
    print("6. 🗑️  Drop Course")
    print("7. 📄 View Student Transcript")
    print("8. � Generate PDF Transcript")
    print("9. �📝 List All Students")
    print("10. 🔍 Search Students by Major")
    print("11. 📊 View System Statistics")
    print("0. 🚪 Exit")
    print("="*50)


def main():
    """Main program loop"""
    sms = StudentManagementSystem()

    print("\n" + "🎓"*25)
    print("   WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("🎓"*25 + "\n")

    while True:
        try:
            display_menu()
            choice = get_string_input("Enter your choice (0-11): ")

            if choice is None:
                continue

            if choice == "0":
                print("\n👋 Thank you for using the Student Management System!")
                print("🎓 Goodbye!\n")
                break

            elif choice == "1":
                print("\n➕ ADD NEW STUDENT")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                name = get_string_input("Enter Student Name: ")
                if name is None:
                    continue

                major = get_string_input("Enter Major: ")
                if major is None:
                    continue

                print(sms.add_student(student_id, name, major))

            elif choice == "2":
                print("\n🗑️  REMOVE STUDENT")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID to remove: ")
                if student_id is None:
                    continue

                print(sms.remove_student(student_id))

            elif choice == "3":
                print("\n📋 VIEW STUDENT DETAILS")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    print(student)

            elif choice == "4":
                print("\n📚 ENROLL IN COURSE")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    course_name = get_string_input("Enter Course Name: ")
                    if course_name is None:
                        continue

                    print(student.enroll_course(course_name))

            elif choice == "5":
                print("\n🏆 COMPLETE COURSE")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    course_name = get_string_input("Enter Course Name: ")
                    if course_name is None:
                        continue

                    credits = get_integer_input("Enter Credits: ")
                    if credits is None:
                        continue

                    grade = get_string_input(
                        "Enter Grade (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ")
                    if grade is None:
                        continue

                    print(student.complete_course(course_name, credits, grade))

            elif choice == "6":
                print("\n🗑️  DROP COURSE")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    course_name = get_string_input(
                        "Enter Course Name to drop: ")
                    if course_name is None:
                        continue

                    print(student.drop_course(course_name))

            elif choice == "7":
                print("\n📄 STUDENT TRANSCRIPT")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    print(student.get_transcript())

            elif choice == "8":
                print("\n📑 GENERATE PDF TRANSCRIPT")
                print("-" * 50)
                student_id = get_integer_input("Enter Student ID: ")
                if student_id is None:
                    continue

                student = sms.get_student(student_id)
                if student:
                    print("\n📝 Enter custom filename (or press Enter for auto-generated name):")
                    try:
                        custom_filename = input("Filename: ").strip()
                        if custom_filename == "":
                            custom_filename = None
                        result = student.generate_pdf_transcript(custom_filename)
                        print(result)
                    except Exception as e:
                        print(f"❌ Error: {str(e)}")

            elif choice == "9":
                print(sms.list_all_students())

            elif choice == "10":
                print("\n🔍 SEARCH BY MAJOR")
                print("-" * 50)
                major = get_string_input("Enter Major to search: ")
                if major is None:
                    continue

                print(sms.search_students_by_major(major))

            elif choice == "11":
                print(sms.get_statistics())

            else:
                print("❌ Invalid choice! Please enter a number between 0 and 11.")

        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            print("👋 Goodbye!\n")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {str(e)}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
