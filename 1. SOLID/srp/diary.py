class Diary:
    def __init__(self):
        self.entries = []
        self.count = 0


    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1


    def remove_entry(self, index):
        del self.entries[index]


    def __str__(self):
        return "\n".join(self.entries)


    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()


    def load(self, filename):
        file = open(filename, "r")
        content = file.read()
        self.entries = content.split("\n")
        file.close()


    def print_statistics(self):
        print(f"Sissekannete arv: {len(self.entries)}")
        lengths = [ len(entry) for entry in self.entries ]
        print(f"Keskmine tähemärkide arv sissekannes: {round(sum(lengths) / len(self.entries))}")