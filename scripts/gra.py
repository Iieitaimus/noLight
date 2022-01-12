from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

platform = Entity(model="assets/mappa", collider="mesh", texture="assets/mappa.mtl", scale=10, position=(0, -10, 0))
model =Entity(model="cos.obj", collider="mesh", position=(-2, -9.5, 0))

app.run()