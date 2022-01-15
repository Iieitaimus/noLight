from ursina import *

if __name__ == '__main__':
    app = Ursina()

ads = Entity(model='quad', texture='bg', parent=camera.ui, scale=(camera.aspect_ratio, 1),
                        color=color.white,
                        z=1)


if __name__ == '__main__':
    app.run()