from OpenGL.GL import *
from OpenGL.GLUT import *
import random

direction = 0  # down
time = "D"  # day

raindrop_num = 500
raindrop_len = 15
win_width = 500
win_height = 500

# Initialize raindrop positions
raindrops = []
for rain_drops in range(raindrop_num):
    x = random.randint(0, win_width)
    y = random.randint(0, win_height)
    raindrops.append((x, y))


def iterate():
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, win_width, 0.0, win_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def house():
    glPointSize(20)
    if time == "N":
        glColor3f(1, 1, 1)
    else:
        glColor3f(0, 0, 0)

    glBegin(GL_TRIANGLES)
    glVertex2f(250, 400)
    glVertex2f(150, 320)
    glVertex2f(350, 320)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(170, 320)
    glVertex2f(330, 320)
    glVertex2f(170, 200)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(330, 200)
    glVertex2f(330, 320)
    glVertex2f(170, 200)
    glEnd()

    glBegin(GL_LINES)
    if time == "N":
        glColor3f(0, 0, 0)
    else:
        glColor3f(1, 1, 1)
    glVertex2f(350, 320)
    glVertex2f(150, 320)
    glEnd()


def bg_colour():
    glBegin(GL_TRIANGLES)
    if time == "N":
        glColor3f(0.0, 0.0, 0.0)
    else:
        glColor3f(1, 1, 1)
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(500, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(500, 0)
    glVertex2f(500, 500)
    glVertex2f(0, 500)
    glEnd()


def rain():
    global raindrops, direction

    if time == "D":
        glColor3f(0.0, 0.0, 0.0)
    else:
        glColor3f(1.0, 1.0, 1.0)

    glLineWidth(0.25)
    glBegin(GL_LINES)
    for i in range(raindrop_num):
        x, y = raindrops[i]
        glVertex2f(x, y)
        glVertex2f(x + (5 * direction), y - raindrop_len)
    glEnd()

    # Update raindrop positions
    for i in range(raindrop_num):
        x, y = raindrops[i]
        y -= 5  # Speed of falling
        if y < 0:  # If raindrop is below the window, reset to the top
            y = win_height
            x = random.randint(0, win_width)
        raindrops[i] = (x, y)


def specialKeyListener(key, x, y):
    global direction
    if key == GLUT_KEY_RIGHT:
        direction = 2
    elif key == GLUT_KEY_LEFT:
        direction = -2
    elif key == GLUT_KEY_DOWN:
        direction = 0
    glutPostRedisplay()


def keyboardListener(key, x, y):
    global time
    if key == b'd' or key == b'D':
        time = "D"
    elif key == b'n' or key == b'N':
        time = "N"
    glutPostRedisplay()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # call the draw methods here
    bg_colour()
    house()
    rain()

    glutSwapBuffers()


# Function to continuously update the screen
def update(value):
    glutPostRedisplay()
    glutTimerFunc(8, update, 0)  # 60 FPS


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(win_width, win_height)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"House and Raindrop")
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)

# Set the update function
glutTimerFunc(0, update, 0)

glutMainLoop()  #The main loop of OpenGL
