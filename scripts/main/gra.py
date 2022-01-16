from ursina import *
from swiatlo.UrsinaLighting import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

if __name__ == '__main__':
    app = Ursina()

player = FirstPersonController()
player.cursor = Entity(parent=camera.ui, model="lozko", scale=.008)

def update():
    if held_keys['shift']:
        player.speed = 10
    else:
        player.speed = 5


def light():

     sun = LitDirectionalLight(direction = Vec3(1, -1, -1))


def entities():
    Entity.default_shader = lit_with_shadows_shader
    skybox = Sky(model="sphere", double_sided=True, texture="load", rotation=(0, 90, 0))
    platform = LitObject(model="plane", collider="mesh", texture="grass", scale=50, position=(0, 0, 0))
    biurko = LitObject(model="biurko", texture = "biurko.png", collider="box", scale = Vec3(2.3,2,2.4), position=(-3.51, 0.1, -4.7),
                    rotation=Vec3(0, 90, 0))
    szafka = LitObject(model="szafka", texture="szafka.png", collider="mesh", scale=3, position=(5.76, 0, 1.9))
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
    okno = LitObject(model="okno", texture="okno.png", collider="mesh", scale=3, position=(0, 0, 0))
    drzwi = LitObject(model="drzwi", texture="drzwi.png", collider="mesh", scale = Vec3(3,2.95,3), position=(0, 0.12, 0))
    listwa = LitObject(model="listwa2", texture="listwa2.png", collider="mesh", scale=3, position=(0, 0, 0))


def run():

    entities()
    light()


    #EditorCamera()

    if __name__ == '__main__':
        app.run()

run()


