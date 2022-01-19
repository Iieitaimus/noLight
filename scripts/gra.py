from ursina import *
from UrsinaLighting import LitSpotLight, LitDirectionalLight, LitObject, LitInit
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *
from ursina.prefabs.memory_counter import MemoryCounter
from load_entities import entities
isOn = False
t = 0
delay = 0
c = 0
flash = None

if __name__ == '__main__':
    app = Ursina()
mouse.visible = False
player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0),
                               scale=1.5)  # (model="postac", texture="postac.png", scale=1.5, collider="mesh")
player.cursor = LitObject(parent=camera.ui, model="circle", color=color.black, scale=.009)
player.gun = LitObject(model='latarka', texture="latarka.png", parent=camera, position=(0.1, -0.1, 0.2), scale=0.1, )


def update():
    global t, delay, c, flash
    t += time.dt
    delay += time.dt
    print(mouse.world_normal)
    if isOn:
        if c == 0:
            flash = LitSpotLight(position=camera.position, direction=mouse.world_point, range=50, intensity=1, angle=5)
            c = 1
        if c != 0:
            flash.setPosition(camera.position)
            flash.setDirection(
                mouse.world_point)  # (mouse.world_point.x, -90, mouse.world_point.z) if mouse.world_point.y <= .190324 else mouse.world_point)

            flash.setIntensity(1)
    else:
        try:
            flash.setIntensity(0)
        except:
            pass

    if held_keys['c']:
        player.scale = .5
        player.jump_height = 0

    else:
        player.scale = 1.5
        player.jump_height = 2

    if held_keys['shift']:
        player.speed = 10
    else:
        player.speed = 5


def light():
    sun = LitDirectionalLight(direction=Vec3(3, -1, -3))
    lampka = LitSpotLight(position=Vec3(0, 5, -1), direction=Vec3(5.91282, 3.33286, -2.2778), range=50, intensity=1,
                          angle=20)  # .5, -1, -.5    0, 5, -1



def run():
    entities()
    light()
    # EditorCamera()

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
