from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

platform = Entity(model="mappa", collider="mesh", texture="mappa.mtl", scale=10, position=(0, -150, 0))
model = Entity(model="cos.obj", collider="mesh", position=(-2, - 105, 0))

app.run()