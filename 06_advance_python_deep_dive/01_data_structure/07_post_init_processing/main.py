from dataclasses import dataclass
from club import ClubMember

@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


anna = HackerClubMember(name='Anna Ravenscroft', handle='AnnaRaven')
print(anna)

leo = HackerClubMember(name='Leo Rochael')
print(leo)


try:
    leo2 = HackerClubMember(name='Leo DaVinci')
except ValueError as e:
    print(e)


leo2 = HackerClubMember(name='Leo DaVinci', handle='Neo')
print(leo2)