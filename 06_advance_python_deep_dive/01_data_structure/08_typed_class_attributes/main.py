from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)


@dataclass
class HackerClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__  # Get the class of the current instance
        if self.handle == '':
            # Take the first part of the name
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            raise ValueError(f'handle {self.handle!r} already exists.')
        cls.all_handles.add(self.handle)
