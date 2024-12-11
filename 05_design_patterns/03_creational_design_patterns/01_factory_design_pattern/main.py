from factory_method import JSONDataExtractor, XMLDataExtractor, DataExtractor
from pathlib import Path

def extract_factory(filepath: Path) -> DataExtractor:
    ext = filepath.suffix.lower()
    if ext == ".json":
        return JSONDataExtractor(filepath)
    elif ext == ".xml":
        return XMLDataExtractor(filepath)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def extract(case: str) -> None:
    dir_path = Path(__file__).parent
    if case == "json":
        path = dir_path / "movies.json"
        factory = extract_factory(path)
        data = factory.parsed_data
        for movie in data:
            print(f"- {movie['title']}")
            director = movie.get("director")
            if director:
                print(f"  Director: {director}")
            genre = movie.get("genre")
            if genre:
                print(f"  Genre: {genre}")
    elif case == "xml":
        path = dir_path / "person.xml"
        factory = extract_factory(path)
        data = factory.parsed_data
        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"- {first} {last}")
            for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib.get("type", "unknown")
                pn_val = pn.text
                phone = f"  {pn_type}: {pn_val}"
                print(phone)
    else:
        print(f"Unknown case: {case}")

if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")
    print("* XML case *")
    extract(case="xml")
