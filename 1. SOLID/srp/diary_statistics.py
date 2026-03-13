class DiaryStatistics:
    @staticmethod
    def print_statistics(diary):
        print(f"Sissekannete arv: {len(diary.entries)}")
        lengths = [len(entry) for entry in diary.entries]
        print(f"Keskmine tähemärkide arv sissekannes: {round(sum(lengths) / len(diary.entries))}")