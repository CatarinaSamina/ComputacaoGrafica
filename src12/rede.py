
from core_ext.mesh import Mesh

from geometry.box import BoxGeometry

from core_ext.object3d import Object3D
from material.texture import TextureMaterial
from core_ext.texture import Texture
from material.phong import PhongMaterial


class Rede(Object3D):
    def __init__(self):
        super().__init__()

        grid_texture = Texture(file_name="images/rede.jpg")
        material = PhongMaterial(texture=grid_texture)
        # base
        # Cada figura Horizontal
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.925, 0.4])
        self.add(self.mesh)
        self.add(self.mesh)

        # Cada figura Vertical
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.set_position([-2.53, 0.55, 0.4])
        self.add(self.mesh)

        # Cada figura Vertical
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.53, 0.55, 0.4])
        self.add(self.mesh)

        # Cada figura Horizontal
        geometry = BoxGeometry(width=5.01,  height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.175, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.83, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.74, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.65, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.56, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.47, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.37, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=5.01, height=0.05, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.28, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-2.35, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-2.2, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-2.05, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.9, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.75, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.6, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.45, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.3, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.15, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.0, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.0, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.85, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.7, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.55, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.4, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.25, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.1, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.05, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.2, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.35, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.5, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.65, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.8, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.95, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.1, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.25, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.4, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.55, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.7, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.85, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.0, 0.55, 0.4])
        self.add(self.mesh)
        self.scale(0.3)
        self.translate(0, 2, 0)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.15, 0.55, 0.4])
        self.add(self.mesh)

        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.3, 0.55, 0.4])
        self.add(self.mesh)
        geometry = BoxGeometry(width=0.05, height=0.8, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.42, 0.55, 0.4])
        self.add(self.mesh)