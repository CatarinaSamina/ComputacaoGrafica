from core.base import Base
from core_ext.camera import Camera
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.grid import GridHelper
from extras.axes import AxesHelper
from extras.movement_rig import MovementRig
from extras.movement_alternative import MovementAlt
from racket import Racket
from table import Table
from net import Net


class Example(Base):

    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800 / 600)
        self.camera.set_position([0.0, 0.5, 3.0])

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)

        self.grid = GridHelper(grid_color=[0, 0, 1], center_color=[1, 0, 0], line_width=2)
        self.scene.add(self.grid)

        self.axes = AxesHelper()
        self.scene.add(self.axes)

        ########################## MESA 
        self.table = Table()
        
        self.scene.add(self.table)

        ########################## Raquete 
        self.raquete = Racket()
        self.raquete.translate(x=1, y=0.8, z=0)
        self.raquete.scale(s=0.25)
        self.scene.add(self.raquete)
        

        ########################### REDE 
        self.alt = MovementAlt()
        self.rede = Net()
        self.rede.translate(x=-0.5, y=0.5, z=0)
        self.rede.scale(s=0.3)
        # self.rede.rotate_y(pi/2)
        self.scene.add(self.alt)
        self.alt.add(self.rede)
        

    def update(self):
        self.alt.update(input_object=self.input, delta_time=self.delta_time)  
        self.rig.update(input_object=self.input, delta_time=self.delta_time)  
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
