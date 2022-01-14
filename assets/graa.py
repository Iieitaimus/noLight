from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import normals_shader


random.seed(0)
Entity.default_shader = lit_with_shadows_shader

app = Ursina()
player = FirstPersonController()

sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
e = Entity(shader=lit_with_shadows_shader)
Sky()

platform = Entity(model="plane", collider="mesh", texture="grass", scale=200, position=(0, -10, 0), shader=lit_with_shadows_shader)
model = Entity(model="biurk", texture="biurko.png", collider="box", scale=2, position=(-4, -10, -5), rotation= Vec3(0,90,0))
model = Entity(model="szafka", texture="bakeeee.png", collider="mesh", scale=3, position=(5.78, -10, 2))
model = Entity(model="pokojj", texture="baki.png", collider="mesh", scale=3, position=(0, -10, 0))
model = Entity(model="lozko", texture="bak.png", collider="mesh", scale=1.5, position=(-2.7, -10, 1.4), rotation= Vec3(0,90,0))
model = Entity(model="schody", texture="bejk.png", collider="mesh", scale=1.5, position=(-2.7, -10, 1.4), rotation= Vec3(0,90,0))

app.run()