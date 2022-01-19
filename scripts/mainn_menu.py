from ursina import *


class MainMenu:
    def __init__(self, play):
        self.bg = Entity(
            model='quad',
            texture='bg',
            scale=Vec3(15, 8.5, 0),
        )
        self.play = Button(
            scale=(.50, .15),
            position=(-.6, -.4, 0),
            icon="start",
            on_click=play,
            tooltip=Tooltip("Play")
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
        # self.settings = Button(
        #     texture='btn_sett',
        #     position=Vec3(),
        #     enabled=False,
        # )
        # self.quit = Button(
        #     texture='btn_quit',
        #     position=Vec3(),
        #     enabled=False,
        # )

    def cleanDel(self):
        destroy(self.bg)
        destroy(self.quit)
        destroy(self.play)
        # destroy(self.settings)
        # destroy(self.quit)
        del self