class FileParser:
    def parse(self, filepath):
        raise NotImplementedError("Subclass must implement parse method")

class CSVParser(FileParser):
    def parse(self, filepath):
        import csv
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data

class JSONParser(FileParser):
    def parse(self, filepath):
        import json
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

class XMLParser(FileParser):
    def parse(self, filepath):
        import xml.etree.ElementTree as ET
        tree = ET.parse(filepath)
        root = tree.getroot()
        data = []
        for person in root.findall('person'):
            person_data = {
                'name': person.find('name').text,
                'age': person.find('age').text,
                'city': person.find('city').text,
                'hobbies': [hobby.text for hobby in person.find('hobbies').findall('hobby')],
                'passion': person.find('passion').text,
                'career': person.find('career').text
            }
            data.append(person_data)
        return data

def process_file(parser, filepath):
    data = parser.parse(filepath)
    # Process data
    print(f"Processed data from {filepath}:")
    for item in data:
        print(item)
    print('-' * 40)

# Usage
parsers = [CSVParser(), JSONParser(), XMLParser()]
filepaths = ['data.csv', 'data.json', 'data.xml']

for parser, filepath in zip(parsers, filepaths):
    process_file(parser, filepath)
