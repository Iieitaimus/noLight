from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

if __name__ == '__main__':
    app = Ursina()

player = FirstPersonController()


def update():
    if held_keys['shift']:
        player.speed = 10
    else:
        player.speed = 5


def light():
    sun = DirectionalLight()
    sun.look_at(Vec3(1, -1, -1))
    Sky()


def entities():
    Entity.default_shader = lit_with_shadows_shader
    platform = Entity(model="plane", collider="mesh", texture="grass", scale=50, position=(0, 0, 0))
    biurko = Entity(model="biurko", texture = "biurko.png", collider="box", scale=2, position=(-4, 0, -5),
                    rotation=Vec3(0, 90, 0))
    szafka = Entity(model="szafka", texture="szafka.png", collider="mesh", scale=3, position=(5.78, 0, 2))
    pokoj = Entity(model="pokoj", texture="pokoj.png", collider="mesh", scale=3, position=(0, 0, 0))
    lozko = Entity(model="lozko", texture="lozko.png", collider="mesh", scale=1.5, position=(-2.7, 0, 1.4),
                   rotation=Vec3(0, 90, 0))
    model = Entity(model="schody", texture="schody.png", collider="mesh", scale=0.8, position=(4.7, 0.8, -5.6),
                   rotation=Vec3(0, 0, 0))


def run():

    entities()
    light()


    #EditorCamera()

    if __name__ == '__main__':
        app.run()

run()


