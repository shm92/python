import tkinter as tk
from tkinter import messagebox
import random

class SeatShufflerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seat Shuffler")

        # 학생 목록
        self.students[4][5] = ["Student1", "Student2", "Student3", "Student4", "Student5",
                         "Student6", "Student7", "Student8", "Student9", "Student10", "Student11"]

        # 랜덤 좌석 배치 버튼
        shuffle_button = tk.Button(root, text="랜덤 좌석 배치", command=self.shuffle_seats)
        shuffle_button.pack(pady=10)

        # 좌석 배치 결과를 표시할 프레임
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

        # 초기 좌석 배치
        self.seats = [tk.Label(self.result_frame, text=student) for student in self.students]
        self.display_seats()

    def shuffle_seats(self):
        shuffled_seats = self.students.copy()
        random.shuffle(shuffled_seats)

        # 새로운 좌석 배치로 업데이트
        for seat, student in zip(self.seats, shuffled_seats):
            seat.config(text=student)

        messagebox.showinfo("랜덤 좌석 배치", "좌석이 랜덤으로 배치되었습니다.")

    def display_seats(self):
        # 초기 좌석 배치 표시
        for seat in self.seats:
            seat.pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = SeatShufflerApp(root)
    root.mainloop()
