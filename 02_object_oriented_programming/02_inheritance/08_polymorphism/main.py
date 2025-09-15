class FileParser:
    def parse(self, file_path):
        raise NotImplementedError("Subclasses should implement this method")


class CSVParser(FileParser):
    def parse(self, file):
        import csv
        print(f"Parsing CSV file: {file}")
        rows = []
        try:
            with open(file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    rows.append(dict(row))
            return rows
        except Exception as e:
            print(f"Error parsing CSV file: {e}")
            return []  # ← return list, not None


class JSONParser(FileParser):
    def parse(self, filepath):
        import json
        print(f"Parsing JSON file: {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # Normalize to list
            if isinstance(data, list):
                return data
            return [data]
        except Exception as e:
            print(f"Error parsing JSON file: {e}")
            return []


class XMLParser(FileParser):
    def parse(self, filepath):
        import xml.etree.ElementTree as ET

        print(f"Parsing XML file: {filepath}")
        data = []
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            def _text(elem, default=None):
                return elem.text.strip() if (elem is not None and elem.text) else default

            for person in root.findall('person'):
                hobbies_parent = person.find('hobbies')
                hobbies = []
                if hobbies_parent is not None:
                    hobbies = [
                        _text(hobby, "")
                        for hobby in hobbies_parent.findall('hobby')
                        if _text(hobby) is not None
                    ]

                person_data = {
                    'name': _text(person.find('name'), ""),
                    'age': _text(person.find('age')),
                    'city': _text(person.find('city'), ""),
                    'hobbies': hobbies,
                    'passion': _text(person.find('passion')),
                    'career': _text(person.find('career')),
                }

                if person_data['age'] is not None:
                    try:
                        person_data['age'] = int(person_data['age'])
                    except ValueError:
                        pass

                data.append(person_data)

            return data
        except Exception as e:
            print(f"Error parsing XML file: {e}")
            return []


def process_file(parser, filepath):
    data = parser.parse(filepath) or []  # ensure iterable
    print(f"Processed data from {filepath}:")
    if not data:
        print("(no records)")
    else:
        for item in data:
            print(item)
    print('-' * 40)


parsers = [CSVParser(), JSONParser(), XMLParser()]
filepaths = ['data.csv', 'data.json', 'data.xml']

for parser, filepath in zip(parsers, filepaths):
    process_file(parser, filepath)
