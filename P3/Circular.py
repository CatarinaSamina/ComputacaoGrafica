"""Triangle moves along a circular path"""
import math
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle moving in a circular path around the origin """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x, pos.y, pos.z, 2.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        # Specify color used when clearly
        
        # Set up vertex array object - triangle #
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        self.vao_triangleC = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_triangleC)
        position_data_triangleC = [[-0.6,  0.0,  0.0], #A#
                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.7,  0.0,  0.0], #C#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.7,  0.0,  0.0], #C#
                                  [-0.7,  0.15,  0.0], #D#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.7,  0.15 ,  0.0], #D# 
                                  [-0.699,  0.19 ,  0.0], #G#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.699,  0.189 ,  0.0], #G# 
                                  [-0.692,  0.210 ,  0.0], #H#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.692,  0.210 ,  0.0], #H# 
                                  [-0.679,  0.227 ,  0.0], #I#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.679,  0.227 ,  0.0], #I# 
                                  [-0.666,  0.240 ,  0.0], #J#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.666,  0.240 ,  0.0], #J# 
                                  [-0.65,  0.25 ,  0.0], #K#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.65,  0.25 ,  0.0], #K# 
                                  [-0.633,  0.260 ,  0.0], #L#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.633,  0.260,  0.0], #L# 
                                  [-0.619,  0.265,  0.0], #M#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.619,  0.265,  0.0], #M# 
                                  [-0.603,  0.270,  0.0], #N#

                                  [-0.6,  0.15,  0.0], #B#
                                  [-0.603,  0.270,  0.0], #N# 
                                  [-0.587,  0.163,  0.0], #O#

                                  [-0.603,  0.270,  0.0], #N#
                                  [-0.587,  0.163,  0.0], #O# 
                                  [-0.578,  0.275,  0.0], #P#

                                  [-0.587,  0.163,  0.0], #O#
                                  [-0.578,  0.275,  0.0], #P# 
                                  [-0.573,  0.173,  0.0], #Q#

                                  [-0.578,  0.275,  0.0], #P#
                                  [-0.573,  0.173,  0.0], #Q# 
                                  [-0.555,  0.277,  0.0], #R#

                                  [-0.573,  0.173,  0.0], #Q#
                                  [-0.555,  0.277,  0.0], #R# 
                                  [-0.551,  0.178,  0.0], #S#

                                  [-0.555,  0.277,  0.0], #R#
                                  [-0.551,  0.178,  0.0], #S# 
                                  [-0.535,  0.278,  0.0], #T#

                                  [-0.551,  0.178,  0.0], #S#
                                  [-0.535,  0.278,  0.0], #T# 
                                  [-0.533,  0.181,  0.0], #U#

                                  [-0.535,  0.278,  0.0], #T#
                                  [-0.533,  0.181,  0.0], #U# 
                                  [-0.518,  0.278,  0.0], #V#

                                  [-0.533,  0.181,  0.0], #U#
                                  [-0.518,  0.278,  0.0], #V# 
                                  [-0.515,  0.176,  0.0], #W#

                                  [-0.518,  0.278,  0.0], #V#
                                  [-0.515,  0.176,  0.0], #W# 
                                  [-0.498,  0.277,  0.0], #Z#

                                  [-0.515,  0.176,  0.0], #W#
                                  [-0.498,  0.277,  0.0], #Z# 
                                  [-0.502,  0.172,  0.0], #A1#

                                  [-0.498,  0.277,  0.0], #Z#
                                  [-0.502,  0.172,  0.0], #A1# 
                                  [-0.480,  0.272,  0.0], #B1#

                                  [-0.502,  0.172,  0.0], #A1#
                                  [-0.480,  0.272,  0.0], #B1#
                                  [-0.489,  0.162,  0.0], #C1#

                                  [-0.480,  0.272,  0.0], #B1#
                                  [-0.489,  0.162,  0.0], #C1# 
                                  [-0.460,  0.265,  0.0], #D1#

                                  [-0.489,  0.162,  0.0], #C1#
                                  [-0.460,  0.265,  0.0], #D1# 
                                  [-0.476,  0.149,  0.0], #E1#
                                  
                                  [-0.460,  0.265,  0.0], #D1#
                                  [-0.476,  0.149,  0.0], #E1# 
                                  [-0.441,  0.251,  0.0], #F1#

                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.441,  0.251,  0.0], #F1# 
                                  [-0.424,  0.237,  0.0], #G1#

                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.424,  0.237,  0.0], #G1# 
                                  [-0.409,  0.219,  0.0], #H1#

                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.409,  0.219,  0.0], #H1# 
                                  [-0.4,  0.2,  0.0], #I1#

                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.4,  0.2,  0.0], #I1# 
                                  [-0.394,  0.179,  0.0], #J1#

                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.394,  0.179,  0.0], #J1# 
                                  [-0.392,  0.162,  0.0], #K1#


                                  [-0.476,  0.149,  0.0], #E1#
                                  [-0.392,  0.162,  0.0], #K1# 
                                  [-0.392,  0.15,  0.0], #L1#


##
                                  [-0.6,  0.0,  0.0], #A#
                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.7,  0.0,  0.0], #C#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.7,  0.0,  0.0], #C#
                                  [-0.7,  -0.15,  0.0], #D#


                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.7,  -0.15 ,  0.0], #D# 
                                  [-0.699,  -0.19 ,  0.0], #G#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.699,  -0.189 ,  0.0], #G# 
                                  [-0.692,  -0.210 ,  0.0], #H#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.692,  -0.210 ,  0.0], #H# 
                                  [-0.679,  -0.227 ,  0.0], #I#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.679,  -0.227 ,  0.0], #I# 
                                  [-0.666,  -0.240 ,  0.0], #J#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.666,  -0.240 ,  0.0], #J# 
                                  [-0.65,  -0.25 ,  0.0], #K#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.65,  -0.25 ,  0.0], #K# 
                                  [-0.633,  -0.260 ,  0.0], #L#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.633,  -0.260,  0.0], #L# 
                                  [-0.619,  -0.265,  0.0], #M#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.619,  -0.265,  0.0], #M# 
                                  [-0.603,  -0.270,  0.0], #N#

                                  [-0.6,  -0.15,  0.0], #B#
                                  [-0.603,  -0.270,  0.0], #N# 
                                  [-0.587,  -0.163,  0.0], #O#

                                  [-0.603,  -0.270,  0.0], #N#
                                  [-0.587,  -0.163,  0.0], #O# 
                                  [-0.578,  -0.275,  0.0], #P#

                                  [-0.587,  -0.163,  0.0], #O#
                                  [-0.578,  -0.275,  0.0], #P# 
                                  [-0.573,  -0.173,  0.0], #Q#

                                  [-0.578,  -0.275,  0.0], #P#
                                  [-0.573,  -0.173,  0.0], #Q# 
                                  [-0.555,  -0.277,  0.0], #R#

                                  [-0.573,  -0.173,  0.0], #Q#
                                  [-0.555,  -0.277,  0.0], #R# 
                                  [-0.551,  -0.178,  0.0], #S#

                                  [-0.555,  -0.277,  0.0], #R#
                                  [-0.551,  -0.178,  0.0], #S# 
                                  [-0.535,  -0.278,  0.0], #T#

                                  [-0.551,  -0.178,  0.0], #S#
                                  [-0.535,  -0.278,  0.0], #T# 
                                  [-0.533,  -0.181,  0.0], #U#

                                  [-0.535,  -0.278,  0.0], #T#
                                  [-0.533,  -0.181,  0.0], #U# 
                                  [-0.518,  -0.278,  0.0], #V#

                                  [-0.533,  -0.181,  0.0], #U#
                                  [-0.518,  -0.278,  0.0], #V# 
                                  [-0.515,  -0.176,  0.0], #W#

                                  [-0.518,  -0.278,  0.0], #V#
                                  [-0.515,  -0.176,  0.0], #W# 
                                  [-0.498,  -0.277,  0.0], #Z#

                                  [-0.515,  -0.176,  0.0], #W#
                                  [-0.498,  -0.277,  0.0], #Z# 
                                  [-0.502,  -0.172,  0.0], #A1#

                                  [-0.498,  -0.277,  0.0], #Z#
                                  [-0.502,  -0.172,  0.0], #A1# 
                                  [-0.480,  -0.272,  0.0], #B1#

                                  [-0.502,  -0.172,  0.0], #A1#
                                  [-0.480,  -0.272,  0.0], #B1#
                                  [-0.489,  -0.162,  0.0], #C1#

                                  [-0.480,  -0.272,  0.0], #B1#
                                  [-0.489,  -0.162,  0.0], #C1# 
                                  [-0.460,  -0.265,  0.0], #D1#

                                  [-0.489,  -0.162,  0.0], #C1#
                                  [-0.460,  -0.265,  0.0], #D1# 
                                  [-0.476,  -0.149,  0.0], #E1#
                                  
                                  [-0.460,  -0.265,  0.0], #D1#
                                  [-0.476,  -0.149,  0.0], #E1# 
                                  [-0.441,  -0.251,  0.0], #F1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.441,  -0.251,  0.0], #F1# 
                                  [-0.424,  -0.237,  0.0], #G1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.424,  -0.237,  0.0], #G1# 
                                  [-0.409,  -0.219,  0.0], #H1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.409,  -0.219,  0.0], #H1# 
                                  [-0.4,  -0.2,  0.0], #I1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.4,  -0.2,  0.0], #I1# 
                                  [-0.394,  -0.179,  0.0], #J1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.394,  -0.179,  0.0], #J1# 
                                  [-0.392,  -0.162,  0.0], #K1#

                                  [-0.476,  -0.149,  0.0], #E1#
                                  [-0.392,  -0.162,  0.0], #K1# 
                                  [-0.392,  -0.150,  0.0], #L1#
                                  ]
                                
       
        
        self.vertex_count_triangleC = len(position_data_triangleC)
        position_attribute_triangleC = Attribute('vec3', position_data_triangleC)
        position_attribute_triangleC.associate_variable(self.program_ref, 'position')

        
        # Set up uniforms #
        self.translationC = Uniform('vec3', [1.0, 0.0, 0.0])
        self.translationC.locate_variable(self.program_ref, 'translation')
        self.base_colorC = Uniform('vec3', [1.0, 0.0, 0.0])
        self.base_colorC.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        """ Update data """

        self.translationC.data[0] = 0.75 * math.sin(self.time)
        self.translationC.data[1] = 0.75 * math.cos(self.time)
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)

        self.translationC.upload_data()
        self.base_colorC.upload_data()

        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count_triangleC)

# Instantiate this class and run the program
Example().run()