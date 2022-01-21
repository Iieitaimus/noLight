from ursina import *
from settings import dev_settings, video_settings, app_settings
from direct.stdpy import thread
from mainn_menu import MainMenu
from loading_screan import LoadingScreen
from load_entities import entities

class Game(Ursina):
    def __init__(self, spawn):
        super().__init__()
        self.spawn = spawn
        self.mm = MainMenu(play=self.play)
        self.load = None

    @staticmethod
    def applyVideoSettings():
        window.show_ursina_splash = dev_settings['ursina_splash']
        window.fullscreen = video_settings['window_fullscreen']
        window.windowed_size = video_settings['window_size']
        window.vsync = video_settings['window_vsync']
        window.borderless = False
        window.exit_button.input = None


    @staticmethod
    def applyAppSettings():
        window.title = app_settings['title']

    def play(self):
        self.load = LoadingScreen()
        self.mm.cleanDel()
        thread.start_new_thread(function=entities(), args='')

    def start(self):
        self.applyAppSettings()
        self.applyVideoSettings()



if __name__ == '__main__':
    game = Game(spawn=Vec3(0,0,0))
    game.start()

    game.run()