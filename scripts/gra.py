from ursina import *
from ursina.raycaster import raycast
from UrsinaLighting import LitSpotLight, LitDirectionalLight, LitObject, LitPointLight
from first_person_controller import FirstPersonController
from ursina.mesh import *

t = 0
c = 0
if __name__ == '__main__':
    app = Ursina()


def light():
    moon = LitDirectionalLight(direction=Vec3(1.6, -1, 0), color=color.gray, intensity=0.15)
    lampka2 = LitSpotLight(position=Vec3(-1.9, 2.71, -4.55), range=0.5, intensity=1, direction=Vec3(-0.7, -2, 0.7),
    angle=30)
    lampka22 = LitPointLight(position=Vec3(-1.9, 2.71, -4.55), range=0.1, intensity=0.5)
    # lampka1 =(position=Vec3(0, 4.7, -1), range=3, intensity=10, direction=Vec3(0, -2, 0), angle=50)
    # test= LitObject(model="cube", position=Vec3(0, 4.8, -1), color=color.light_gray, scale=0.1)
    # test2= LitObject(model="cube", position=Vec3(-1.9, 2.71, -4.55), color=color.light_gray, scale=0.1)


def lampaOn(lights):
    for light in lights:
        light.setIntensity(1)


def lampaOff(lights):
    for light in lights:
        light.setIntensity(0)


def switch(target, dist, lights):
    global t, c
    t += time.dt
    c += time.dt

    if t > .1:
        ray = raycast(player.camera_pivot.world_position, player.camera_pivot.forward, traverse_target=target,
                      distance=dist, debug=False)
        t = 0

    try:
        c += time.dt
        if ray.hit and held_keys['e'] and not target.isOn and c > 2:
            lampaOn(lights)
            target.isOn = True
            Audio('switchOn.mp3')
            c = 0

        if ray.hit and held_keys['e'] and target.isOn and c > 2:
            lampaOff(lights)
            target.isOn = False
            Audio('switchOff.mp3')
            c = 0
    except:
        pass


def update():
    switch(kontakt, dist=3, lights=[lampa_light])
    switch(kontakt2, dist=3, lights=[lampa51_light, lampa52_light])


mouse.visible = False
player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0), scale=1.5)
player.cursor = LitObject(parent=camera.ui, model="circle", color=color.black, scale=.012)

window.fullscreen = True
from load_entities import *
light()
# drzwiok = FrameAnimation3d('drzwiok', fps=60, loop=True, autoplay=True, texture="drzwi.png", position=(4.5, 3.5, -6), scale=3, collider="mesh")
EditorCamera()
scene.fog_density = 1
scene.fog_color = color.gray
scene.fog = True

if __name__ == '__main__':
    app.run()
