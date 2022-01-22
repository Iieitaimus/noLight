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
    lampka = LitPointLight(position=Vec3(0, 4.7, -1), range=5, intensity=1,)
    lampka2 = LitPointLight(position=Vec3(-1.9, 2.7, -4.6), range=1, intensity=1)
    #test= LitObject(model="cube", position=Vec3(0, 4.8, -1), color=color.light_g\ray, scale=0.1)
    #test2= LitObject(model="cube", position=Vec3(-1.9, 2.7, -4.6), color=color.light_gray, scale=0.1)



def run():
    entities()
    light()

    #EditorCamera()

    if __name__ == '__main__':
        app.run()


run()
