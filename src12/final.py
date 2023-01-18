"""An example of a basic scene: spinning cube"""
import time

from core.base import Base
from core_ext.camera import Camera

from core_ext.renderer import Renderer
from core_ext.scene import Scene

from math import pi, sin, cos

from extras.movement_rig import MovementRig
from extras.grid import GridHelper
from rede import Rede
from mesa import Mesa
from racket import Racket
from bola import Bola
from floor import Floor
from walls import Walls
from extras.object_rig import ObjectRig
from light.light import Light
from light.ambient import AmbientLight
from light.point import PointLight
from light.directional import DirectionalLight



class Example(Base):
    """ Render a basic scene that consists of a spinning cube """

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800 / 600)
        self.camera.set_position([0, 0.9, 2.5])
        self.movement = MovementRig()
        self.movement.add(self.camera)
        self.scene.add(self.movement)
        self.movement1 = ObjectRig()
        self.scene.add(self.movement1)


        ambient = AmbientLight(color=[0.7, 0.7, 0.7])
        self.scene.add(ambient)
        #
        directional = DirectionalLight(color=[1, 1, 1], direction=[0, -1, 0])
        self.scene.add(directional)

        # point = PointLight(color=[0.7, 0.7, 0.7], position=[5, 10, 0.8])
        # self.scene.add(point)

        self.floor = Floor()
        self.scene.add(self.floor)

        self.walls = Walls()
        self.scene.add(self.walls)

        self.bola = Bola()
        self.bola.set_position([0, 0.39, -2])
        #self.bola.scale(s=0.15)
        self.scene.add(self.bola)

        self.mesa = Mesa()
        self.mesa.translate(x=0,y=0,z=-0.5)
        self.mesa.rotate_y(pi/2)
        self.scene.add(self.mesa)

        self.raquete1 = Racket()
        self.raquete1.set_position([0, 0.8, -2])
        #self.movement1.translate(x=-0.5, y=0.8, z=-1.7)
        self.raquete1.scale(s=0.25)
        self.scene.add(self.raquete1)
        #self.movement1.add(self.raquete1)

        self.raquete2 = Racket()
        self.raquete2.set_position([0, 0.8, 1])
        self.raquete2.rotate_y(pi)
        self.raquete2.scale(s=0.25)

        self.scene.add(self.raquete2)

        self.rede = Rede()
        #self.rede.translate(x=0, y=-0.97, z=-2.055)
        self.rede.set_position([0, 0.31, -0.62])
        self.scene.add(self.rede)

        self.limite = 10
        self.limite2 = pi/6
        self.initial_y = 0.39
        self.actual_y = self.initial_y
        self.t = 0
        self.t2 = 0
        self.t3 = 0
        self.speed_z = 4
        self.speed_y = 4
        self.actual_z = -2
        self.right = True
        self.delay = 3
        self.restart = False
        self.i = 0

    def ballmovement(self):
        self.t = self.time - self.t2
        # print(self.t)

        if (self.actual_y + sin(pi/4 + (self.t * self.speed_y * pi / 2)) / 40) > self.initial_y and self.time > self.delay and self.restart == False:
            self.bola.translate(x=0, y=sin(pi/4 + (self.t * self.speed_y * pi / 2)) / 40, z=0)
            self.actual_y += sin(pi/4 + (self.t * self.speed_y * pi/2)) / 40
        elif sin(pi/4 + (self.t * self.speed_y * pi/2)) == 0 and self.time > self.delay and self.restart == False:
            self.actual_y = self.initial_y
        else:
            self.t2 = self.time


    def update(self):
        if self.restart:
             self.bola.set_position([0, 0.39, -2])
             print(f" 1: time:{self.time}, {self.t3}, z:{self.actual_z}")
             if self.time > self.t3:
                self.restart = False
                self.actual_z = -2
                self.initial_y = 0.39
                self.actual_y = self.initial_y
                print(f" 2: {self.actual_z}, {self.time}, {self.restart}")

        if self.actual_z < 0.932 and self.right and self.time > self.delay and self.restart == False :
            self.bola.translate(x=0, y=0, z=self.delta_time * self.speed_z)
            self.actual_z += self.delta_time*self.speed_z
        elif self.actual_z > -1.932 and self.time > self.delay and self.restart == False:
            self.right = False
            self.bola.translate(x=0, y=0, z=-self.delta_time * self.speed_z)
            self.actual_z -= self.delta_time * self.speed_z
        else:
            self.right = True
        self.ballmovement()
        if self.actual_y <= 0.535 and (-0.67 <= self.actual_z <= -0.57):
            self.restart = True
            if self.i == 0:
                self.t3 = self.time
                self.i = self.i + 1
            self.time = 0
            self.time = self.t3
        else:
            self.restart = False

        self.movement.update(input_object=self.input, delta_time=self.delta_time*2)
        self.movement1.update(input_object=self.input, delta_time=self.delta_time)
        self.renderer.render(self.scene, self.camera)

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()