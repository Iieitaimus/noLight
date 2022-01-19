import time
from ursina import *
#from gra import entities
from mainn_menu import MainMenu
from loading_screan import LoadingScreen


class Game(Ursina):
    def __init__(self, spawn):
        super().__init__()
        self.spawn = spawn
        self.mm = MainMenu(play=self.play)      #Sequence(Wait(.01), Func(sys.exit))
        self.load = None

    def play(self):
        self.mm.cleanDel()
        self.load = LoadingScreen()

        #entities()
        # time.sleep(2)
        # self.load.cleanDel()
if __name__ == '__main__':
    game = Game(spawn=Vec3(0,0,0))


    game.run()