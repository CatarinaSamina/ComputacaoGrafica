from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from core_ext.object3d import Object3D
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class Net(Object3D):
    def __init__(self):
        super().__init__()

        texture = Texture(file_name="images/rede.jpg")
        material = TextureMaterial(texture=texture)

        # Cada figura Horizontal
        geometry = BoxGeometry(width=4.5, height=0.11, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 1, 0.4])
        self.add(self.mesh)

        # Cada figura Vertical
        geometry = BoxGeometry(width=0.11, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-2.2, 0.55, 0.4])
        self.add(self.mesh)

        # Cada figura Vertical
        geometry = BoxGeometry(width=0.11, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.2, 0.55, 0.4])
        self.add(self.mesh)

        # Cada figura Horizontal
        geometry = BoxGeometry(width=4.5, height=0.11, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.1, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.83, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.65, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.47, 0.4])
        self.add(self.mesh)

        # linhas finas horizontais
        geometry = BoxGeometry(width=4.5, height=0.1, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0, 0.28, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.9, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.6, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.3, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-1.0, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.7, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.4, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([-0.1, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.2, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.5, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([0.8, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.1, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.4, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([1.7, 0.55, 0.4])
        self.add(self.mesh)

        # Linhas finas Verticais
        geometry = BoxGeometry(width=0.1, height=1.0, depth=0.05)
        self.mesh = Mesh(geometry, material)
        self.mesh.translate(0.5, 0, 0)
        self.mesh.set_position([2.0, 0.55, 0.4])
        self.add(self.mesh)
