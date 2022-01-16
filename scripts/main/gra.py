from ursina import *
from swiatlo.UrsinaLighting import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

if __name__ == '__main__':
    app = Ursina()

player = FirstPersonController(scale=1.5) #(model="postac", texture="postac.png", scale=1.5, collider="mesh")
player.cursor = Entity(parent=camera.ui, model ="circle", scale=0.01, color =color.black)
gun = Entity(model='latarka',texture="latarka.png", parent=camera, position=(0.1, -0.1, 0.2), scale=0.1,)

player = FirstPersonController()
player.cursor = Entity(parent=camera.ui, model="circle", color =color.black, scale=.009)

def update():
    if held_keys['shift']:
        player.speed = 10
    else:
        player.speed = 5


def light():

     sun = LitDirectionalLight(direction = Vec3(3, -1, -3))


def entities():
    Entity.default_shader = lit_with_shadows_shader
    platform = LitObject(model="plane", texture="grass", scale = Vec3(10,2,20), position=(-11, 3.5, -4))
    drzewo = LitObject(model="drzewo", texture="drzewo.png", scale=2, position=(-3, 1, 0))
    drzewo = LitObject(model="drzewo", texture="drzewo.png", scale=2, position=(-3, 1, 2))
    szafka = LitObject(model="szafka", texture="szafka.png", collider="box", scale=3, position=(3, 2, 2.2))
    skybox = Sky(model="sphere", double_sided=True, texture="load", rotation=(0, 90, 0))
    biurko = LitObject(model="biurko", texture = "biurko.png", collider="box", scale = Vec3(2.3,2,2.4), position=(-3.51, 0.1, -4.7),
                    rotation=Vec3(0, 90, 0))
    sciany = LitObject(model="sciany", texture="sciana.jpg", collider="mesh", scale=3, position=(0, 0, 0))
    sufit = LitObject(model="sufit", texture="sciana.jpg", collider="mesh", scale=3, position=(0, 0, 0))
    lozko = LitObject(model="lozko", texture="lozko.png", collider="mesh", scale=1.5, position=(-2.7, 0, 1.4),
                   rotation=Vec3(0, 90, 0))
    schody = LitObject(model="schody", texture="schody.png", collider="mesh", scale = Vec3(1,0.7,1), position=(4.5, 0.8, -5.6),
                   rotation=Vec3(0, 0, 0))
    podloga = LitObject(model="podloga", texture="podloga.png", collider="mesh", scale=3, position=(0, 0.01, 0),
                   rotation=Vec3(0, 0, 0))
    listwa = LitObject(model="listwa", texture="podloga.png", collider="mesh", scale=3, position=(0, 0, 0))
    krzeslo = LitObject(model="krzeslo", texture="krzeslo.png", collider="box", scale=2.2, position=(-3.51, 0.2, -3.7), rotation=Vec3(0, 180, 0))
    latarka = LitObject(model="latarka", texture="latarka.png", collider="mesh", scale=0.3, position=(3.76, 2.1, 2.3), rotation=Vec3(0, 90, 0))
    krzeslo = LitObject(model="krzeslo", texture="krzeslo.png", collider="box", scale=2.2, position=(-3.51, 0.2, -3.7), rotation=Vec3(0, 180, 0))
    okno = LitObject(model="okno", texture="okno.png", collider="mesh", scale=3, position=(-6.3, 4.6, -3.75))
    drzwi = LitObject(model="drzwi", texture="drzwi.png", collider="mesh", scale = Vec3(3,2.95,3), position=(0, 0.12, 0))
    listwa = LitObject(model="listwa2", texture="listwa2.png", collider="mesh", scale=3, position=(0, 0, 0))
#toDo okno naprawic bo jest zjebane

def run():



    entities()
    light()


    #EditorCamera()




    if __name__ == '__main__':
        app.run()


run()


