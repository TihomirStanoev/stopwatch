import customtkinter as ctk 
from settings.settings import *
from control_buttons import ControlButtons


class App(ctk.CTk):
    def __init__(self):
        # window
        super().__init__(fg_color=BLACK)
        self.title('Stopwatch')
        self.geometry('300x600')
        self.resizable(False, False)

        # grid layout
        self.rowconfigure(0, weight = 5, uniform='a')
        self.rowconfigure(1, weight = 1, uniform='a')
        self.rowconfigure(2, weight = 4, uniform='a')
        self.columnconfigure(0, weight = 1, uniform = 'b')

        #fonts
        self.button_font = ctk.CTkFont(family = FONT ,size = BUTTON_FONT_SIZE)

        # widgets
        self.control_buttons = ControlButtons(
            parent= self, 
            font=self.button_font,
            start = self.start,
            pause = self.pause,
            resume = self.resume,
            reset = self.reset,
            create_lap = self.create_lap            
            )


    def start(self):
        print('start')

    def pause(self):
        print('pause')

    def resume(self):
        print('resume')

    def reset(self):
        print('reset')

    def create_lap(self):
        print('lap')










if __name__ == '__main__':
    stopwatch = App()
    stopwatch.mainloop()