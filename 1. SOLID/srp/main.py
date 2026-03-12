from diary import Diary

if __name__ == "__main__":
    d = Diary()
    d.add_entry("Täna oli ilus ilm.")
    d.add_entry("Õppisin programmeerimist.")
    print(d)
    d.save("diary.txt")
    d.load("diary.txt")
    print(d)
    d.print_statistics()