from ursina import *


class MainMenu:
    def __init__(self, play):
        self.bg = Entity(
            model='quad',
            texture='bg',
            scale=Vec3(15, 8.5, 0),
        )
        self.play = Button(
            icon= 'start',
            scale=(.5, .15),
            color=color.azure,
            position=(-.6, -.4, 0),
            on_click=play,
        )
        self.options = Button(
            scale=(.50, .15),
            icon="options",
            on_click=Sequence(Wait(.01), Func(sys.exit)),
            position= self.play.position + Vec3(0.6, 0, 0)
        )
        self.quit = Button(
            scale=(.50, .15),
            icon="quit",
            on_click=Sequence(Wait(.01), Func(sys.exit)),
            position=self.options.position + Vec3(0.6, 0, 0)
        )

    def cleanDel(self):
        destroy(self.bg)
        destroy(self.play)
        destroy(self.options)
        destroy(self.quit)
        del self