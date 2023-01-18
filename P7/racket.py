from math import pi
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.cylinder import CylinderGeometry
from geometry.ellipsoid import EllipsoidGeometry
from core_ext.object3d import Object3D
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

class Racket(Object3D):
    def __init__(self):
        super().__init__()

        self.raquete_texture = Texture(file_name="images/raquete.jpg")
        self.material1 = TextureMaterial(texture=self.raquete_texture, property_dict={"repeatUV": [100, 100]})
        self.black = SurfaceMaterial(property_dict={"baseColor": [.09, 0.09, 0.09]})
        self.brown = SurfaceMaterial(property_dict={"baseColor": [.8, 0.7, 0.5]})

        self.cilinder = CylinderGeometry(radius=0.5, height=0.1, closed=False)
        self.cilinder = Mesh(self.cilinder, self.black)
        self.cilinder.rotate_x(pi / 2, True)
        self.add(self.cilinder)

        self.face1 = EllipsoidGeometry(width=1, height=1, depth=0)
        self.face1 = Mesh(self.face1, self.material1)
        self.face1.translate(0, 0, 0.05, True)
        self.add(self.face1)

        self.face2 = EllipsoidGeometry(width=1, height=1, depth=0)
        self.face2 = Mesh(self.face2, self.black)
        self.face2.translate(0, 0, -0.05, True)
        self.add(self.face2)

        self.box = BoxGeometry(0.15, 0.35, 0.10)
        self.box = Mesh(self.box, self.brown)
        self.box.translate(0, -0.65, 0, True)
        self.add(self.box)



