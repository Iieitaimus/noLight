from ursina import *


class LoadingScreen:
    def __init__(self):
        self.bg = Entity(
            model='quad',
            texture='llo',
            scale=Vec3(15, 8.5, 0),
        )

    def cleanDel(self):
        destroy(self.bg)
        del self

if __name__ == '__main__':
    app = Ursina()

    a = LoadingScreen()

    app.run()
