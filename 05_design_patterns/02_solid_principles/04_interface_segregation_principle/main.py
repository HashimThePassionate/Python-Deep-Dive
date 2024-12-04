from typing import Protocol

class Printer(Protocol):
    def print_document(self) -> None:
        ...

class Scanner(Protocol):
    def scan_document(self) -> None:
        ...

class Fax(Protocol):
    def fax_document(self) -> None:
        ...

class AllInOnePrinter:
    def print_document(self) -> None:
        print("Printing")

    def scan_document(self) -> None:
        print("Scanning")

    def fax_document(self) -> None:
        print("Faxing")

class SimplePrinter:
    def print_document(self) -> None:
        print("Simply Printing")

def do_the_print(printer: Printer) -> None:
    printer.print_document()

if __name__ == "__main__":
    all_in_one = AllInOnePrinter()
    all_in_one.scan_document()
    all_in_one.fax_document()
    do_the_print(all_in_one)
    
    simple = SimplePrinter()
    do_the_print(simple)
