from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.cylinder import CylinderGeometry
from core_ext.object3d import Object3D
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class Table(Object3D):
    def __init__(self):
        super().__init__()

        material = SurfaceMaterial(property_dict={"baseColor": [1, 1, 1]})
        material2 = SurfaceMaterial(property_dict={"baseColor": [0.15, 0.25, 0.5]})
        texture = Texture(file_name="images/image.png")
        texture_material = TextureMaterial(texture=texture)

        geometry = BoxGeometry(width=1.5, height=0.61, depth=1.22)
        self.mesh = Mesh(geometry, material)
        self.add(self.mesh)

        geometry = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=0.75, y=0, z=0.61, local=True)
        self.add(self.mesh)

        geometry = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=-0.75, y=0, z=0.61, local=True)
        self.add(self.mesh)

        geometry = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=0.75, y=0, z=-0.61, local=True)
        self.add(self.mesh)

        geometry = CylinderGeometry(closed=False, height=0.61, radius=0.1)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=-0.75, y=0, z=-0.61, local=True)
        self.add(self.mesh)

        geometry = BoxGeometry(width=2.74, height=0.001, depth=1.525)
        self.mesh = Mesh(geometry, texture_material)
        self.mesh.translate(x=0, y=0.355, z=0, local=True)
        self.add(self.mesh)

        geometry = BoxGeometry(width=2.74, height=0.10, depth=1.525)
        self.mesh = Mesh(geometry, material2)
        self.mesh.translate(x=0, y=0.305, z=0, local=True)
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.2525, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=0, y=0.375, z=-0.7925, local=True)
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.2525, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(x=0, y=0.375, z=0.7925, local=True)
        self.add(self.mesh)