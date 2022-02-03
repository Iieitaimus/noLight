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
    lampka2 = SpotLight(position=Vec3(-1.9, 2.71, -4.55), range=0.5, intensity=1, direction=Vec3(-0.7, -2, 0.7),
    angle=30)
    lampka22 = PointLight(position=Vec3(-1.9, 2.71, -4.55), range=0.1, intensity=0.5)
    # lampka1 =(position=Vec3(0, 4.7, -1), range=3, intensity=10, direction=Vec3(0, -2, 0), angle=50)
    # test= LitObject(model="cube", position=Vec3(0, 4.8, -1), color=color.light_gray, scale=0.1)
    # test2= LitObject(model="cube", position=Vec3(-1.9, 2.71, -4.55), color=color.light_gray, scale=0.1)


def lampaOn(lights):
    for light in lights:
        #light.setIntensity(1)
        #l#ight.intensity(1)
        pass
def lampaOff(lights):
    for light in lights:
        #light.setIntensity(0)
        pass

def switch(target, dist, lights):
    global t, c
    t += time.dt
    c += time.dt

    if distance_xz(player.position, target.position) < dist and not target.isOn and c >2:
        lampaOn(lights)
        target.isOn = True
        Audio('switchOn.mp3')
        c = 0

    if distance_xz(player.position, target.position) < dist and target.isOn and c > 2:
        lampaOff(lights)
        target.isOn = False
        Audio('switchOn.mp3')
        c = 0


def update():
    # switch(kontakt, dist=3, lights=[lampa_light])
    # switch(kontakt2, dist=3, lights=[lampa51_light, lampa52_light])
    if kontakt.hovered:
        switch(kontakt, dist=3, lights=[lampa_light])

mouse.visible = False
player = FirstPersonController(x=-4, z=-2, rotation=(0, 180, 0), scale=1.5)
player.cursor = LitObject(parent=camera.ui, model="circle", color=color.black, scale=.012)

#window.fullscreen = True
from load_entities import *
light()

scene.fog_color = color.gray
scene.fog_density = .1

# EditorCamera()


if __name__ == '__main__':
    app.run()
