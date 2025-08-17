from time import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.is_paused = False

    def start(self):
        self.start_time = time()
        self.reset()

    def pause(self):
        self.pause_time = time()
        self.is_paused = True

    def resume(self):
        elapsed_time = time() - self.pause_time
        self.start_time += elapsed_time
        self.is_paused = False

    def reset(self):
        self.pause_time = 0
        self.is_paused = False

    def get_time(self):
        if self.is_paused:
            return int(round(self.pause_time - self.start_time,2) * 1000)
        else:
            return int(round(time() - self.start_time,2) * 1000)

    