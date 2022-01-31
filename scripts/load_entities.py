from ursina import *
from UrsinaLighting import LitObject, LitSpotLight


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
    position=(5.4, 2, 1),
    rotation=(0, 90, 0))
szafa = LitObject(
    model="szafa",
    texture="szafa.png",
    collider="box",
    scale=0.7,
    position=(2, 2.5, 2.2),
    rotation=(0, -90, 0))
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
sciany = LitObject(
     model="sciany",
    texture="sciana.jpg",
    collider="mesh", scale=3,
    position=(0, 0, 0))
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
schody2 = LitObject(
    model="schody",
    texture="schody.png",
    collider="mesh",
    scale=Vec3(1, 0.7, 1),
    position=(4.5, 0.8, -11),
    rotation=Vec3(0, 180, 0))
Bschody = LitObject(
    model="Bschody",
    texture="schody.png",
    collider="mesh",
    scale=3,
    position=(7.8, 2, -8.2))
drzwigura = LitObject(
    model="drzwiCL",
    texture="drzwiCL.png",
    collider="mesh",
    scale=3.2,
    position=(15.4, 10, -9),
    rotation=Vec3(0, -90, 0))
BschodyCOL = LitObject(
    model="BschodyCOL",
    collider="mesh",
    scale=3,
    position=(7.8, 2, -8.2),
    visible=False)
podloga = LitObject(
    model="podloga",
    texture="podloga.png",
    collider="mesh", scale=3,
    position=(0, 0.1, 0))
sloik1 = LitObject(
    model="sloiki1",
    texture="sloiki1.png",
    #collider="mesh",
    scale=2.98,
    position=(-0.7, 2, -17.16))
sloik2 = LitObject(
    model="sloiki2",
    texture="sloiki2.png",
    #collider="mesh",
    scale=3,
    position=(-0.7, 2, -17.15))
sloik3 = LitObject(
    model="sloiki3",
    texture="sloiki3.png",
    #collider="mesh",
    scale=3,
    position=(-0.7, 2, -17.15))
podloga2 = LitObject(
    model="podloga2",
    texture="beton.jpg",
    collider="mesh", scale=3,
    position=(0, 0.23, 0))
krzeslo = LitObject(
    model="krzeslo",
    texture="krzeslo.png",
    collider="box",
    scale=2.2,
    position=(-3.5, 0.2, -3.3),
    rotation=Vec3(0, 180, 0))
okno = LitObject(
    model="okno",
    texture="okno.png",
    collider="mesh",
    scale=3,
    position=(-6.3, 4.6, -3.75))
okno2 = LitObject(
    model="okno",
    texture="okno.png",
    collider="mesh",
    scale=3,
    position=(-6.3, 4.6, -12.75))
drzwiO1 = LitObject(
    model="drzwiOP",
    texture="drzwiOP.png",
    collider="mesh",
    scale=Vec3(3, 2.9, 3),
    position=(4.35, 3.3, -6))
drzwiO2 = LitObject(
    model="drzwiOP",
    texture="drzwiOP.png",
    collider="mesh",
    scale=Vec3(3, 2.9, 3),
    position=(4.65, 3.3, -10.5),
    rotation=Vec3(0, 180, 0))
SchodyDach = LitObject(
    model="Bschodydach",
    texture="sciana.jpg",
    collider="mesh", scale=3,
    position=( 0, 0, 0))
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
lampa_light = LitSpotLight(
    position=Vec3(0, 5, -1),
    direction=Vec3(0, -1, 0),
    intensity=0,
    range=10,
    angle=50)
kratka = LitObject(
    model="kratka",
    texture="kratka.png",
    collider="mesh",
    scale=3,
    position=(-6.1, 4.6, 1.335))
kratka2 = LitObject(
    model="kratka",
    texture="kratka.png",
    collider="mesh",
    scale=3,
    position=(-6.1, 4.6, -17.8))
szafki = LitObject(
    model="szafki",
    texture="szafka.png",
    collider="box",
    scale=2.9,
    visible=False,
    position=(-0.7, 2, -17.15))
szafki.collider = BoxCollider(szafki, center=Vec3(-1.5, 0, 0.75), size=Vec3(0.5, 1, 3))
szafki = LitObject(
    model="szafki",
    texture="szafka.png",
    collider="box",
    scale=2.9,
    position=(-0.7, 2, -17.15))
szafki.collider = BoxCollider(szafki, center=Vec3(0, 0, 0), size=Vec3(0.5, 1, 1.5))
rury1 = LitObject(
    model="rury1",
    texture="rury1.png",
    collider="mesh",
    scale=3,
    position=(0.3, 0, -8.1))
rury2 = LitObject(
    model="rury2",
    texture="rury2.png",
    collider="mesh",
    scale=3,
    position=(0.3, 0, -8.1))
kontakt = LitObject(
    model="kontakt",
    texture="kontakt.png",
    collider="box",
    scale=1,
    position=(3, 3.5, -5.9),
    isOn=False)

