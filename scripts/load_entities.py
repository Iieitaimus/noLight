from ursina import *
from ursina.shaders import *
from UrsinaLighting import LitObject


def entities():
    Entity.default_shader = lit_with_shadows_shader
    platform = LitObject(
        model="plot",
        texture="plot.png",
        scale=1,
        position=(-9, 3.5, -4))
    szafka = LitObject(
        model="szafka",
        texture="szafka.png",
        collider="box",
        scale=Vec3(2.4, 3, 2.1),
        position=(5.4, 2, 1), rotation=(0, 90, 0))
    szafa = LitObject(
        model="szafa",
        texture="szafa.png",
        collider="box",
        scale=0.7,
        position=(2, 2.5, 2.2), rotation=(0, -90, 0))
    skybox = Sky(
        model="sphere",
        double_sided=True,
        texture="load",
        rotation=(0, 90, 0))
    biurko = LitObject(
        model="biurko",
        texture="biurko.png",
        collider="box",
        scale=Vec3(2.3, 4, 2.4),
        position=(-3.51, 0.1, -4.7),
        rotation=Vec3(0, 90, 0))
    biurko.collider = BoxCollider(biurko, size=Vec3(1.2, 3, 2))
    sciany = LitObject(
        model="sciany",
        texture="sciana.jpg",
        collider="mesh", scale=3,
        position=(0, 0, 0))
    sufit = LitObject(
        model="sufit",
        texture="sciana.jpg",
        scale=3,
        position=(0, 0, 0),
        collider="mesh")
    lozko = LitObject(
        model="lozko",
        texture="lozko.png",
        collider="box",
        scale=1.5,
        position=(-2.7, 0, 1.4),
        rotation=Vec3(0, 90, 0))
    schody = LitObject(
        model="schody",
        texture="schody.png",
        collider="mesh",
        scale=Vec3(1, 0.7, 1),
        position=(4.5, 0.8, -5.6),
        rotation=Vec3(0, 0, 0))
    podloga = LitObject(
        model="podloga",
        texture="podloga.png",
        collider="mesh", scale=3,
        position=(0, 0.1, -1.5))
    krzeslo = LitObject(
        model="krzeslo",
        texture="krzeslo.png",
        collider="mesh",
        scale=2.2,
        position=(-3.5, 0.2, -3.3),
        rotation=Vec3(0, 180, 0))
    okno = LitObject(
        model="okno",
        texture="okno.png",
        collider="mesh",
        scale=3,
        position=(-6.3, 4.6, -3.75))
    drzwi = LitObject(
        model="drzwi",
        texture="drzwi.png",
        collider="box",
        scale=3,
        position=(4.5, 3.5, -6))
    listwa = LitObject(
        model="listwa2",
        texture="sciana.jpg",
        scale=3,
        position=(0, 0, 0),
        collider="mesh")
    klawa = LitObject(
        model="klawa",
        texture="klawa.png",
        scale=0.5,
        position=(-3.4, 1.83, -4.2))
    monitor = LitObject(
        model="monitor",
        texture="monitor.png",
        scale=1.1,
        position=(-3.4, 2.6, -4.8),
        rotation=Vec3(0, 90, 0))
    lampeczka = LitObject(
        model="lampeczka",
        texture="lampeczka.png",
        scale=2,
        position=(-1.7, 2.5, -4.8),
        rotation=Vec3(0, -45, 0))
    komputer = LitObject(
        model="komputer",
        texture="komputer.png",
        scale=0.8,
        position=(-5.3, 2.4, -4.8),
        rotation=Vec3(0, 90, 0))
    lampa = LitObject(
        model="lampa",
        texture="lampa.png",
        scale=1,
        position=(0, 5, -1),
        collider="mesh")
    kratka = LitObject(
        model="kratka",
        texture="kratka.png",
        collider="mesh",
        scale=3,
        position=(-6.1, 4.6, 1.335))

    drzwi.animate_rotation(value=(1, 0, 0), duration= 10000)