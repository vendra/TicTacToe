from tkinter import *
from tkinter import ttk, messagebox
import os
import random


class TicTacToe:
    def __init__(self):
        # Create window and main frame
        self.root = Tk()
        self.root.title("TicTacToe")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry('800x800')
        self.root.resizable(0, 0)
        self.mainframe = ttk.Frame(self.root, padding="3 3 3 3")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.grid_propagate(0)

        # Load cross and circle with variants
        self.cross_images = []
        self.cross_path = 'media/cross/'
        for cross in os.listdir(self.cross_path):
            self.cross_images.append(PhotoImage(file=self.cross_path+cross))

        self.circle_images = []
        self.circle_path = 'media/circle/'
        for circle in os.listdir(self.circle_path):
            self.circle_images.append(PhotoImage(file=self.circle_path+circle))

        # Ugly trick to avoid button resizing when setting the image
        self.empty_image = PhotoImage(file='media/empty.png')

        self.player = ['X']
        self.turn = 1
        self.field = [[None for i in range(3)] for j in range(3)]

        # Handle to the buttons to update image from the "select" callback
        self.button_field = []
        for row in range(3):
            self.button_field.append([])
            for col in range(3):
                self.button_field[row].append(ttk.Button(self.mainframe, text=' '))
                self.button_field[row][col].configure(command=lambda row_=row, col_=col: self.__select(row_, col_))
                self.button_field[row][col].configure(padding='0 0 0 0', image=self.empty_image)
                self.button_field[row][col].grid(row=row, column=col, sticky=N + S + E + W)
                self.button_field[row][col].grid_propagate(0)
                self.mainframe.columnconfigure(row, weight=1)
                self.mainframe.rowconfigure(col, weight=1)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def __select(self, x, y):
        if self.field[x][y] is None:
            self.turn += 1
            self.field[x][y] = self.player
            if self.player == 'O':
                self.player = 'X'
                self.button_field[x][y].config(image=self.cross_images[random.randint(0, len(self.cross_images) - 1)])
                self.field[x][y] = self.player
            else:
                self.player = 'O'
                self.button_field[x][y].config(image=self.circle_images[random.randint(0, len(self.circle_images) - 1)])
                self.field[x][y] = self.player
        print("Field: ", self.field)

        if self.__check_field():
            print(self.player)
            self.__reset()
            print(self.player)
        elif self.turn > 9:
            messagebox.showinfo(message='Tie Game!')
            print(self.player)
            self.__reset()
            print(self.player)

    def __check_field(self):
        # Check diagonals
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[1][1] is not None:
            messagebox.showinfo(message='Player ' + str(self.field[1][1]) + " won!")
            return True
        elif self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[1][1] is not None:
            messagebox.showinfo(message='Player ' + str(self.field[1][1]) + " won!")
            return True

        # Check rows
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] and self.field[i][0] is not None:
                messagebox.showinfo(message='Player ' + str(self.field[i][0]) + " won!")
                return True
            elif self.field[0][i] == self.field[1][i] == self.field[2][i] and self.field[0][i] is not None:
                messagebox.showinfo(message='Player ' + str(self.field[0][i]) + " won!")
                return True
        return False

    def __reset(self):
        self.turn = 1
        for x in range(3):
            for y in range(3):
                self.button_field[x][y].config(image=self.empty_image)
                self.field[x][y] = None
        return

    def run(self):
        self.root.mainloop()


def main():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.run()


if __name__ == "__main__":
    main()