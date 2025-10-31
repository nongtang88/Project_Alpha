import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.size = 4  # 4x4 grid
        self.values = list(range(1, self.size * self.size // 2 + 1)) * 2
        random.shuffle(self.values)
        self.buttons = []
        self.first = None
        self.second = None
        self.matched = set()
        self.create_board()

    def create_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(self.root, text="?", width=6, height=3,
                                command=partial(self.reveal, i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def reveal(self, i, j):
        idx = i * self.size + j
        if idx in self.matched or (self.first and self.second):
            return
        self.buttons[i][j]['text'] = str(self.values[idx])
        if not self.first:
            self.first = (i, j)
        elif not self.second and (i, j) != self.first:
            self.second = (i, j)
            self.root.after(1000, self.check_match)

    def check_match(self):
        i1, j1 = self.first
        i2, j2 = self.second
        idx1 = i1 * self.size + j1
        idx2 = i2 * self.size + j2
        if self.values[idx1] == self.values[idx2]:
            self.matched.add(idx1)
            self.matched.add(idx2)
        else:
            self.buttons[i1][j1]['text'] = "?"
            self.buttons[i2][j2]['text'] = "?"
        self.first = None
        self.second = None
        if len(self.matched) == self.size * self.size:
            messagebox.showinfo("Memory Game", "You Win!")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()