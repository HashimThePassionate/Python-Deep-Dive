class RECCell:
    def __init__(self, content):
        self.content = content  # Initialize the cell content
        
    def __repr__(self):
        return f"RECCell(content={self.content})"  # Representation of the cell for debugging

class RECRow:
    def __init__(self):
        self.cells = []  # Initialize an empty list of cells
        
    def add_cell(self, cell):
        self.cells.append(cell)  # Add a cell to the row
        
    def __repr__(self):
        return f"RECRow(cells={self.cells})"  # Representation of the row for debugging

class RECTable:
    def __init__(self, caption=None):
        self.caption = caption if caption else []  # Initialize the caption, default to an empty list if None
        self.rows = []  # Initialize an empty list of rows
        
    def add_row(self, row):
        self.rows.append(row)  # Add a row to the table
        
    def __repr__(self):
        return f"RECTable(caption={self.caption}, rows={self.rows})"  # Representation of the table for debugging

      ---

      import re

def parse_file_content(file_content):
    # Regular expression patterns for keywords and strings
    table_pattern = re.compile(r'\btable\b', re.IGNORECASE)  # Match the keyword 'table' case insensitively
    row_pattern = re.compile(r'\brow\b', re.IGNORECASE)  # Match the keyword 'row' case insensitively
    cell_pattern = re.compile(r'\bcell\b', re.IGNORECASE)  # Match the keyword 'cell' case insensitively
    string_pattern = re.compile(r'%([^%]*)%')  # Match strings enclosed by percentage signs

    tables = []  # List to store all tables
    current_table = None  # Variable to store the current table being processed
    current_row = None  # Variable to store the current row being processed

    # Tokenize the file content
    tokens = re.findall(r'\btable\b|\brow\b|\bcell\b|%[^%]*%|\s+', file_content, re.IGNORECASE)  # Find all keywords, strings, and whitespace

    for token in tokens:
        token = token.strip()  # Remove leading and trailing whitespace
        if not token:
            continue  # Skip empty tokens

        if table_pattern.fullmatch(token):  # Check if the token is a 'table' keyword
            if current_table:
                tables.append(current_table)  # Append the current table to the list of tables
            current_table = RECTable()  # Create a new RECTable instance
            current_row = None  # Reset the current row
        elif row_pattern.fullmatch(token):  # Check if the token is a 'row' keyword
            if not current_table:
                raise ValueError("Row found outside of a table.")  # Error if a row is found outside a table
            current_row = RECRow()  # Create a new RECRow instance
            current_table.add_row(current_row)  # Add the new row to the current table
        elif cell_pattern.fullmatch(token):  # Check if the token is a 'cell' keyword
            if not current_row:
                raise ValueError("Cell found outside of a row.")  # Error if a cell is found outside a row
            current_row.add_cell(RECCell(""))  # Add a new empty cell to the current row
        else:
            match = string_pattern.fullmatch(token)  # Check if the token is a string
            if match:
                content = match.group(1).replace("%%", "%")  # Replace '%%' with '%' in the string content
                if current_table and not current_row:
                    current_table.caption.append(content)  # Add the string to the table's caption if in a table but not in a row
                elif current_row:
                    if current_row.cells:
                        current_row.cells[-1].content += content  # Append the string content to the last cell in the current row
                    else:
                        current_row.add_cell(RECCell(content))  # Add a new cell with the string content if no cells exist
            else:
                raise ValueError(f"Unexpected token: {token}")  # Error for unexpected tokens

    if current_table:
        tables.append(current_table)  # Append the last table to the list of tables

    return tables  # Return the list of tables

# Example usage
file_content = """
table %First table%
row
cell %A1%
cell %B1%
cell%C1%
cell%D1%
ROW
row
CELL %The previous row was blank%
cell %B3%
row
cell %A4% %second line%
cEll %B4% %second line%
cell %C4 second line%
row
cell %%%string%%%
cell %%
cell %%%%
cell %%%%%%
"""

tables = parse_file_content(file_content)
for table in tables:
    print(table)
