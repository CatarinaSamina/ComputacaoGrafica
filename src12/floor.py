from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.rectangle import RectangleGeometry
from math import pi
from material.surface import SurfaceMaterial
from core_ext.object3d import Object3D
from material.texture import TextureMaterial
from core_ext.texture import Texture
from material.phong import PhongMaterial



class Floor(Object3D):
    def __init__(self):
        super().__init__()

        geometry = RectangleGeometry(width=100, height=100)
        texture = Texture(file_name="images/wood_floor.jpg", )
        texture_material = PhongMaterial(texture=texture)
        #texture_material = TextureMaterial(texture=texture, property_dict={"repeatUV": [70, 70]})

        self.floor = Mesh(geometry, texture_material)
        self.floor.translate(x=0, y=-0.31, z=0)
        self.floor.rotate_x(pi / 2)
        self.add(self.floor)