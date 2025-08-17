from settings.settings import *
import customtkinter as ctk


class ControlButtons(ctk.CTkFrame):
    def __init__(self, parent, font, start, pause, resume, reset, create_lap):
        super().__init__(master=parent, corner_radius=0, fg_color= 'transparent')
        self.grid(column = 0, row = 1, sticky = 'news')

        self.start_button_states = {'start': start, 'pause': pause, 'resume': resume}
        self.lap_button_states = {'reset': reset, 'create_lap': create_lap}
        self.states_mapper = {'off': 'on', 'on': 'pause', 'pause': 'on'}

        self.state = 'off'

        

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((1,3), weight=9, uniform = 'c')
        self.columnconfigure((0,2,4), weight=1, uniform = 'c')

        # lap/reset button
        self.lap_button = ctk.CTkButton(
            master=self, 
            text='Lap', 
            command= self.lap_handler, 
            state= 'disabled',
            font=font,
            fg_color = GREY
            )
        # start/stop button
        self.start_button = ctk.CTkButton(
            master=self,
            text='Start',
            command= self.start_handler,
            font = font,
            fg_color=GREEN,
            hover_color=GREEN_HIGHLIGHT,
            text_color=GREEN_TEXT
        )


        # buttons
        self.lap_button.grid(row=0, column=1, sticky = 'news')
        self.start_button.grid(row=0, column=3, sticky = 'news')


    def start_handler(self):
        

        match self.state:
            case 'off': 
                self.start_button_states['start']()
            case 'on' : 
                self.start_button_states['pause']()
            case 'pause': 
                self.start_button_states['resume']()

        self.state = self.states_mapper[self.state]
        self.update_buttons()

    def lap_handler(self):
        match self.state:
            case 'on': 
                self.lap_button_states['create_lap']()
            case _ : 
                self.lap_button_states['reset']()
                self.state = 'off'


        self.update_buttons()

    def update_buttons(self):
        match self.state:
            case 'off':
                self.lap_button.configure(state='disbaled', text='Lap', fg_color=GREY)
                self.start_button.configure(text='Start')

            case 'pause':
                self.lap_button.configure(text='Reset')
                self.start_button.configure(text='Resume', fg_color=GREEN, hover_color=GREEN_HIGHLIGHT,text_color=GREEN_TEXT)
            
            case 'on' : 
                self.lap_button.configure(state='normal', fg_color=ORANGE_DARK, hover_color=ORANGE_HIGHLIGHT, text_color=ORANGE_DARK_TEXT)
                self.start_button.configure(text='Stop', fg_color=RED, hover_color=RED_HIGHLIGHT,text_color=RED_TEXT)
