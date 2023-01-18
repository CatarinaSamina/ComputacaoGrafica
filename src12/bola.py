from core_ext.mesh import Mesh
from core_ext.object3d import Object3D
from geometry.sphere import SphereGeometry
from core_ext.texture import Texture
from material.phong import PhongMaterial
from  material.flat import FlatMaterial


class Bola(Object3D):
    def __init__(self):
        super().__init__()

        texture = Texture(file_name="images/white.jpg")
        texture_material = FlatMaterial(texture=texture)
        material = PhongMaterial(property_dict={"baseColor":[1,0.3,0.3]})
        geometry = SphereGeometry(radius= 0.04)
        self.mesh = Mesh(geometry, texture_material)
        self.add(self.mesh)