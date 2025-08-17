import customtkinter as ctk 
from settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BLACK)
        self.title('Stopwatch')
        self.geometry('300x600')
        self.resizable(False, False)



if __name__ == '__main__':
    stopwatch = App()
    stopwatch.mainloop()