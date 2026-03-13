from diary import Diary

class DiaryPersistence:
    @staticmethod
    def save(diary, filename):
        file = open(filename, "w")
        for entry in diary.entries:
            file.write(entry.split(":")[1].strip() + "\n")
        file.close()

    @staticmethod
    def load(filename):
        diary = Diary()
        file = open(filename, "r")
        content = file.readlines()
        for line in content:
            diary.add_entry(line.strip())
        file.close()
        return diary