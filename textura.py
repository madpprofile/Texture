from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 1
dy = 2
dz = 0

texture = []

def LoadTextures():
    global texture
    faces = [ open("textures/face-1.rgb", "rb").read(), open("textures/face-2.rgb", "rb").read(), open("textures/face-3.rgb", "rb").read(),
              open("textures/face-4.rgb", "rb").read(), open("textures/face-5.rgb", "rb").read(), open("textures/face-6.rgb", "rb").read() ]
    

    ix = 682
    iy = 512    
    texture = glGenTextures(6)
    
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[0])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[1])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[2])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[3])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[4])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    
    glBindTexture(GL_TEXTURE_2D, texture[5])
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, faces[5])
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0,-5.0)            

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    # Front Face
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)              
    
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)

    glEnd()
    
    # Back Face
    glBindTexture(GL_TEXTURE_2D, texture[5])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)   
    glEnd()

    # Top Face
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_QUADS)  
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)   
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)   
    glEnd()

    # Bottom Face
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)   
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glEnd()  

    # Right face
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)  
    glEnd()  

    # Left Face
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)   
    glEnd()                # Done Drawing The Cube
    
    #xrot  = xrot + 0.01                # X rotation
    #yrot = yrot + 0.01                 # Y rotation
    #zrot = zrot + 0.01                 # Z rotation

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
