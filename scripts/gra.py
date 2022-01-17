from ursina import *
from UrsinaLighting import LitSpotLight, LitDirectionalLight, LitObject
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *
import os

print(os.getcwd())
isOn = False
t = 0
delay = 0
c = 0
flash = None

if __name__ == '__main__':
    app = Ursina()

player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0), scale= 1.5) #(model="postac", texture="postac.png", scale=1.5, collider="mesh")
player.cursor = LitObject(parent=camera.ui, model="circle", color =color.black, scale=.009)
gun = LitObject(model='latarka',texture="latarka.png", parent=camera, position=(0.1, -0.1, 0.2), scale=0.1,)


def update():
    global t, delay, c, flash
    t += time.dt
    delay += time.dt
    if isOn:
        if c == 0:
            flash = LitSpotLight(position=gun.position, direction=mouse.world_point, range=50, intensity=1, angle=5)
            c = 1
        if c != 0:
            flash.setPosition(gun.position)
            flash.setDirection(mouse.world_point)
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
    lampka = LitSpotLight(position=Vec3(0, 5, -1), direction=Vec3(.5, -1, -.5), range=50, intensity=1, angle=20)

def entities():
    Entity.default_shader = lit_with_shadows_shader
    platform = LitObject(model="plane", texture="grass", scale = Vec3(10,2,20), position=(-11, 3.5, -4))
    drzewo = LitObject(model="drzewo", texture="drzewo.png", scale=2, position=(-3, 1, 0))
    drzewo = LitObject(model="drzewo", texture="drzewo.png", scale=2, position=(-3, 1, 2))
    szafka = LitObject(model="szafka", texture="szafka.png", collider="box", scale=3, position=(3, 2, 2.2))
    skybox = Sky(model="sphere", double_sided=True, texture="load", rotation=(0, 90, 0))
    biurko = LitObject(model="biurko", texture = "biurko.png", collider="box", scale = Vec3(2.3,4,2.4), position=(-3.51, 0.1, -4.7),
                    rotation=Vec3(0, 90, 0))
    biurko.collider = BoxCollider(biurko, size=Vec3(1.2,3,2))
    sciany = LitObject(model="sciany", texture="sciana.jpg", collider="mesh", scale=3, position=(0, 0, 0))
    sufit = LitObject(model="sufit", texture="sciana.jpg", scale=3, position=(0, 0, 0))
    lozko = LitObject(model="lozko", texture="lozko.png", collider="mesh", scale=1.5, position=(-2.7, 0, 1.4),
                   rotation=Vec3(0, 90, 0))
    schody = LitObject(model="schody", texture="schody.png", collider="mesh", scale = Vec3(1,0.7,1), position=(4.5, 0.8, -5.6),
                   rotation=Vec3(0, 0, 0))
    podloga = LitObject(model="podloga", texture="podloga.png", collider="mesh", scale=3, position=(0, 0.01, 0),
                   rotation=Vec3(0, 0, 0))
    listwa = LitObject(model="listwa", texture="podloga.png", collider="mesh", scale=3, position=(0, 0, 0))
    latarka = LitObject(model="latarka", texture="latarka.png", collider="box", scale=0.3, position=(3.76, 2.1, 2.3), rotation=Vec3(0, 90, 0))
    krzeslo = LitObject(model="krzeslo", texture="krzeslo.png", collider="mesh", scale=2.2, position=(-3.5, 0.2, -3.3), rotation=Vec3(0, 180, 0))
    okno = LitObject(model="okno", texture="okno.png", collider="mesh", scale=3, position=(-6.3, 4.6, -3.75))
    drzwi = LitObject(model="drzwi", texture="drzwi.png", collider="mesh", scale = Vec3(3,2.95,3), position=(0, 0.12, 0))
    listwa = LitObject(model="listwa2", texture="listwa2.png", scale=3, position=(0, 0, 0))
    klawa = LitObject(model="klawa", texture="klawa.png", scale=0.5, position=(-3.4, 1.83, -4.2))
    monitor = LitObject(model="monitor", texture="monitor.png", scale=1.1, position=(-3.4, 2.6, -5), rotation=Vec3(0, 90, 0))
    komputer = LitObject(model="komputer", texture="komputer.png", scale=0.8, position=(-5.3, 2.4, -4.8), rotation=Vec3(0, 90, 0))
    lampa = LitObject(model="lampa", texture="lampa.png", scale=1, position=(0, 5, -1))

def run():

    entities()
    light()

    #EditorCamera()


    if __name__ == '__main__':
        app.run()


def input(key):
    global delay, isOn, flash

    if delay > 0.1 and key == 'e' and isOn == False:
        isOn = True
        delay = 0
        e = Audio('latarka.mp3')

    elif key == 'e' and isOn == True:
        isOn = False
        delay = 0




run()