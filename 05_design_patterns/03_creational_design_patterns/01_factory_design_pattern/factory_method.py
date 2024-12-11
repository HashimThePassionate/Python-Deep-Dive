# ch03/factory/factory_method.py

from typing import Protocol
from pathlib import Path
import json
import xml.etree.ElementTree as ET

class DataExtractor(Protocol):
    @property
    def parsed_data(self):
        ...

class JSONDataExtractor:
    def __init__(self, filepath: Path):
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


