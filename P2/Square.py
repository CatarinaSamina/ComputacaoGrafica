import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute


class Example(Base):
    """ Render two shapes """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(1.0, 0.0, 0.0, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings #
        GL.glLineWidth(4)

       
       #Quadrado

        self.vao_square = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_square)
        position_data_square = [[0.50, 0.50, 0.0],
                                [0.50, 0.30, 0.0],
                                [0.30, 0.30, 0.0],
                                [0.30, 0.50, 0.0],]
        self.vertex_count_square = len(position_data_square)
        position_attribute_square = Attribute('vec3', position_data_square)
        position_attribute_square.associate_variable(self.program_ref, 'position')

        color_data_square = [[1.0, 0.0, 0.0],
                            [1.0, 0.0, 0.0],
                            [1.0, 0.0, 0.0],
                            [1.0, 0.0, 0.0],
                            ]
        color_attribute = Attribute("vec3", color_data_square)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        # Using same program to render both shapes
        GL.glUseProgram(self.program_ref)
        # Draw the square
        GL.glBindVertexArray(self.vao_square)
        GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_square)


# Instantiate this class and run the program
Example().run()
