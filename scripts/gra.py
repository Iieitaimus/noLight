from ursina import *
from UrsinaLighting import LitSpotLight, LitDirectionalLight, LitObject, LitInit
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.memory_counter import MemoryCounter
from load_entities import entities
from ursina.mesh import *

isOn = False
t = 0
delay = 0
c = 0
flash = None


if __name__ == '__main__':
    app = Ursina()
mouse.visible = False
player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0),scale=1.5)  # (model="postac", texture="postac.png", scale=1.5, collider="mesh")
player.cursor = LitObject(parent=camera.ui, model="circle", color=color.black, scale=.009)
player.gun = LitObject(model='latarka', texture="latarka.png", parent=camera, position=(0.1, -0.1, 0.2), scale=0.1, )



def update():
    global t, delay, c, flash
    t += time.dt
    delay += time.dt
    if isOn:
        if c == 0:

            flash = LitSpotLight(position=camera.forward, direction=mouse.world_point, range=5, intensity=0.05,
                                 angle=10)
            c = 1
        if c != 0:
            flash.setPosition(camera.rotation)
            flash.setDirection(mouse.world_point)
            flash.setIntensity(1)
    else:
        try:
            flash.setIntensity(0)
        except:
            pass

    if held_keys['c']:
        player.scale = .8
        player.jump_height = 0

    else:
        player.scale = 1.5
        player.jump_height = 1

    if held_keys['shift']:
        player.speed = 10
    else:
        player.speed = 5


def light():
    sun = LitDirectionalLight(direction=Vec3(3, -1, -3))
    lampka = LitSpotLight(position=Vec3(0, 5, -1), direction=Vec3(.5, -1, -.5), range=50, intensity=1,
                          angle=20)


def run():
    entities()
    light()
    EditorCamera()

    if __name__ == '__main__':
        app.run()


def input(key):
    global delay, isOn

    if delay > 0.1 and key == 'e' and isOn == False:
        isOn = True
        delay = 0
        e = Audio('latarka.mp3')

    elif key == 'e' and isOn == True:
        isOn = False
        delay = 0
        e = Audio('latarka.mp3')


MemoryCounter()
run()
