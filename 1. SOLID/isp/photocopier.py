from printer import Printer
from scanner import Scanner

class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print(document)
