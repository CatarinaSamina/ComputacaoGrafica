from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.rectangle import RectangleGeometry
from math import pi
from material.surface import SurfaceMaterial
from core_ext.object3d import Object3D
from material.texture import TextureMaterial
from core_ext.texture import Texture
from material.phong import PhongMaterial


class Walls(Object3D):
    def __init__(self):
        super().__init__()

        texture = Texture(file_name="images/wall_tijolo2.jpg")
        texture_material = PhongMaterial(texture=texture)
        #texture_material = TextureMaterial(texture=texture, property_dict={"repeatUV": [10, 10]})

        geometry = RectangleGeometry(width=20, height=20)
        self.parede1 = Mesh(geometry, texture_material)
        self.parede1.translate(x=0, y=1.2, z=-10)
        self.add(self.parede1)

        self.parede2 = Mesh(geometry, texture_material)
        self.parede2.translate(x=10, y=1.2, z=0)
        self.parede2.rotate_y(-pi /2)
        self.add(self.parede2)

        self.parede3 = Mesh(geometry, texture_material)
        self.parede3.translate(x=-10, y=1.2, z=0)
        self.parede3.rotate_y(pi / 2)
        self.add(self.parede3)

        self.parede4 = Mesh(geometry, texture_material)
        self.parede4.translate(x=0, y=1.2, z=10)
        self.parede4.rotate_y(-pi)
        self.add(self.parede4)