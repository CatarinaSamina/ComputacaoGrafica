"""An example of a basic scene: spinning cube"""

from audioop import add
from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.box import BoxGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from geometry.rectangle import RectangleGeometry
from geometry.cylinder import CylinderGeometry
from geometry.ellipsoid import EllipsoidGeometry
from material.texture import TextureMaterial
from core_ext.texture import Texture
from extras.movement_rig import MovementRig
from core_ext.object3d import Object3D
from math import pi



class Example(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        grid_texture = Texture(file_name="images/corda.jpg")
        material = TextureMaterial(texture=grid_texture)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)


  #REDE      
#base

        self.rede = Object3D()
        #Cada figura Horizontal
        geometry = BoxGeometry(width=4.5, height=0.11, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 1, 0.4])
        self.rede.add(self.mesh)


       #Cada figura Vertical
        geometry = BoxGeometry(width=0.11, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-2.2, 0.55, 0.4])
        self.rede.add(self.mesh)

          #Cada figura Vertical
        geometry = BoxGeometry(width=0.11, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.2, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Cada figura Horizontal
        geometry = BoxGeometry(width=4.5, height=0.11, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.1, 0.4])
        self.rede.add(self.mesh)

    #linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.83, 0.4])
        self.rede.add(self.mesh)

#linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.65, 0.4])
        self.rede.add(self.mesh)

        #linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.47, 0.4])
        self.rede.add(self.mesh)

        #linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.28, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.9, 0.55, 0.4])
        self.rede.add(self.mesh)

#Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.6, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.3, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.0, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.7, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.4, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.1, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.2, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.5, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.8, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.1, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.4, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.7, 0.55, 0.4])
        self.rede.add(self.mesh)

        #Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material) 
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.0, 0.55, 0.4])
        self.rede.add(self.mesh)
        self.rede.scale(0.3)
        self.rede.translate(0, 2, 0)
        self.scene.add(self.rede)
#MESA

        self.obj = Object3D()
        material2 = SurfaceMaterial(property_dict={"baseColor":[1, 1, 1]})

        geometry = BoxGeometry(width=1.5, height=0.61, depth=1.22)
        self.mesh = Mesh(geometry, material2)
        self.obj.add(self.mesh)

        geometry2 = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh2 = Mesh(geometry2, material2)
        self.mesh2.translate(x=0.75, y=0, z=0.61, local=True)
        self.obj.add(self.mesh2)

        geometry3 = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh3 = Mesh(geometry3, material2)
        self.mesh3.translate(x=-0.75, y=0, z=0.61, local=True)
        self.obj.add(self.mesh3)

        geometry4 = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh4 = Mesh(geometry4, material2)
        self.mesh4.translate(x=0.75, y=0, z=-0.61, local=True)
        self.obj.add(self.mesh4)

        geometry5 = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh5 = Mesh(geometry5, material2)
        self.mesh5.translate(x=-0.75, y=0, z=-0.61, local=True)
        self.obj.add(self.mesh5)

        geometry6 = BoxGeometry(width=2.74, height=0.10, depth=1.525)
        self.mesh6 = Mesh(geometry6, material2)
        self.mesh6.translate(x=0, y=0.305, z=0, local=True)
        self.obj.add(self.mesh6)

        geometry7 = BoxGeometry(width=0.05, height=0.2525, depth=0.05)
        self.mesh7 = Mesh(geometry7, material2)
        self.mesh7.translate(x=0, y=0.375, z=-0.7925, local=True)
        self.obj.add(self.mesh7)

        geometry8 = BoxGeometry(width=0.05, height=0.2525, depth=0.05)
        self.mesh8 = Mesh(geometry8, material2)
        self.mesh8.translate(x=0, y=0.375, z=0.7925, local=True)
        self.obj.add(self.mesh8)

        self.scene.add(self.obj)

#RAQUETE

        self.raquete = Object3D()
        cilinder = CylinderGeometry(radius=0.5, height=0.1, closed=False)
        self.cilinder = Mesh(cilinder, material2)
        self.cilinder.add(self.cilinder )
        self.cilinder .rotate_x(pi / 2, True)

        face1 = EllipsoidGeometry(width=1,height=1,depth=0)
        self.face1 = Mesh(face1, material2)
        self.face1 .translate(0, 0, 0.05,True)
        self.raquete.add(self.face1 )

        face2 = EllipsoidGeometry(width=1, height=1, depth=0)
        self.face2 = Mesh(face2, material2)
        self.face2 .translate(0, 0, -0.05, True)
        self.raquete.add(self.face2 )

        box = BoxGeometry(0.15, 0.35, 0.10)
        self.box  = Mesh(box, material2)
        self.box .translate(0, -0.65, 0, True)
        self.raquete.add(self.box )

        self.scene.add(self.raquete) 
        self.raquete.scale(0.3)
        self.raquete.translate(4, 3, 0)



    def update(self):
        #self.rede.rotate_y(0.02514)
        #self.mesh.rotate_x(0.01337)
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.delta_time)
        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
