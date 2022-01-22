from ursina import *
from UrsinaLighting import LitSpotLight, LitDirectionalLight, LitObject, LitPointLight
from first_person_controller import FirstPersonController
from load_entities import entities
from ursina.mesh import *


if __name__ == '__main__':
    app = Ursina()
mouse.visible = False
player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0),scale=1.5)
player.cursor = LitObject(parent=camera.ui, model="circle", color=color.black, scale=.012)
window.fullscreen = True

kontakt = LitObject(
        model="kontakt",
        texture="kontakt.png",
        collider="box",
        scale=1,
        position=(3, 3.5, -5.9))


def update():
    # print(mouse.find_collision(kontakt.collision))
    if mouse.world_point == kontakt.screen_position:
        print('tak')


def light():
    moon = LitDirectionalLight(direction=Vec3(1.6, -1, 0), color=color.gray, intensity=0.15)
    # lampka1 = LitSpotLight(position=Vec3(0, 4.7, -1), range=3, intensity=2, direction=Vec3(0, -2, 0), angle=50)
    lampka2 = LitSpotLight(position=Vec3(-1.9, 2.71, -4.55), range=0.5, intensity=1, direction=Vec3(-0.7, -2, 0.7),
                           angle=30)
    lampka22 = LitPointLight(position=Vec3(-1.9, 2.71, -4.55), range=0.1, intensity=0.5)
    # test= LitObject(model="cube", position=Vec3(0, 4.8, -1), color=color.light_gray, scale=0.1)
    # test2= LitObject(model="cube", position=Vec3(-1.9, 2.71, -4.55), color=color.light_gray, scale=0.1)


def run():
    entities()
    light()

    #drzwiok = FrameAnimation3d('drzwiok', fps=60, loop=True, autoplay=True, texture="drzwi.png", position=(4.5, 3.5, -6), scale=3, collider="mesh")

    #EditorCamera()

    if __name__ == '__main__':
        app.run()


run()
