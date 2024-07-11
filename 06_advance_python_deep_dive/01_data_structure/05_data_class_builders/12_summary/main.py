from dataclasses import dataclass, fields
from typing import ClassVar

@dataclass
class Resource:
    title: str
    creator: str
    subject: str
    description: str
    publisher: str
    contributor: str
    date: str
    type: str
    format: str
    identifier: str
    source: str
    language: str
    relation: str
    coverage: str
    rights: str

    def __repr__(self):
        field_strs = ', '.join(f"{field.name}={getattr(self, field.name)!r}" for field in fields(self))
        return f"{self.__class__.__name__}({field_strs})"

# Example usage
resource = Resource(
    title="Example Title",
    creator="Author Name",
    subject="Example Subject",
    description="Example Description",
    publisher="Example Publisher",
    contributor="Example Contributor",
    date="2024-07-08",
    type="Example Type",
    format="Example Format",
    identifier="Example Identifier",
    source="Example Source",
    language="English",
    relation="Example Relation",
    coverage="Example Coverage",
    rights="Example Rights"
)
print(resource)
