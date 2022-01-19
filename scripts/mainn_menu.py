from ursina import *


class MainMenu:
    def __init__(self, play):
        self.bg = Entity(
            model='quad',
            texture='bg',
            scale=Vec3(15, 8.5, 0),
        )
        self.play = Button(
            icon= 'bg',
            scale=(.25, .075),
            color=color.azure,
            on_click=play,
            tooltip=Tooltip("Play")
        )
        self.quit = Button(
            text='quit',
            scale=(.25, .075),
            color=color.azure,
            on_click=Sequence(Wait(.01), Func(sys.exit)),
            position= self.play.position + Vec3(0, -0.1, 0)
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
        destroy(self.play)
        destroy(self.quit)
        del self