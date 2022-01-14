from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import *

if __name__ == '__main__':
    app = Ursina()


def light():
    sun = DirectionalLight()
    sun.look_at(Vec3(1, -1, 0))
    Sky()


def entities():
    Entity.default_shader = lit_with_shadows_shader
    platform = Entity(model="plane", collider="mesh", texture="grass", scale=50, position=(0, 0, 0))
    biurko = Entity(model="biurk", texture="biurko.png", collider="box", scale=2, position=(-4, 0, -5),
                    rotation=Vec3(0, 90, 0))
    szafka = Entity(model="szafka", texture="szafka.png", collider="mesh", scale=3, position=(5.9, 0, 2))
    pokoj = Entity(model="pokoj", texture="Plaster17_COL_VAR1_6K.jpg", collider="mesh", scale=3, position=(0, 0, 0))



def run():

    entities()
    light()
    player = FirstPersonController()
    EditorCamera()

    if __name__ == '__main__':
        app.run()


