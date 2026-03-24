from my_printer import MyPrinter
from photocopier import PhotoCopier
from mfm import MultiFunctionMachine

if __name__ == "__main__":

    printer = MyPrinter()
    photocopier = PhotoCopier()

    printer.print("Hello from printer")

    photocopier.print("Copy this document")
    photocopier.scan("Scanned document")

    multi = MultiFunctionMachine(printer, photocopier)
    multi.print("Delegated print")
    multi.scan("Delegated scan")