#include <GL/glut.h>

#include <stdio.h>

#define WIDTH 700
#define HEIGHT 700

#define INIT_POSITION 100

GLfloat angles[3] = {0.0, 0.0, 0.0};

float scale = 1.0;
float translation[3] = {0.0, 0.0, 0.0};

void reset_transformations() {
    angles[0] = 0.0;
    angles[1] = 0.0;
    angles[2] = 0.0;

    scale = 1.0;

    translation[0] = 0.0;
    translation[1] = 0.0;
    translation[2] = 0.0;
}

void handle_display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(0, 0, 1);

    glTranslatef(translation[0], translation[1], translation[2]);

    glScalef(scale, scale, scale);
    
    glRotatef(angles[0], 1.0, 0.0, 0.0);
    glRotatef(angles[1], 0.0, 1.0, 0.0);
    glRotatef(angles[2], 0.0, 0.0, 1.0);

    glutWireSphere(0.3, 10, 10);
    
    reset_transformations();
    
    glutSwapBuffers();
}

void handle_keyboard(unsigned char key, int x, int y) {
    switch (key) {
        case 'w':
        case 'W':
            scale = 1.1;
            break;
        case 's':
        case 'S':
            scale = 0.9;
            break;

        case 'a':
        case 'A':
            angles[1] += 10.0;
            break;

        case 'd':
        case 'D':
            angles[1] -= 10.0;
            break;

        default:
            break;

    }

    glutPostRedisplay();
}

void handle_special_keyboard(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_UP:
            translation[1] += 0.1;
            break;
        case GLUT_KEY_DOWN:
            translation[1] -= 0.1;
            break;
        case GLUT_KEY_LEFT:
            translation[0] -= 0.1;
            break;
        case GLUT_KEY_RIGHT:
            translation[0] += 0.1;
            break;
        default:
            break;
    }

    glutPostRedisplay();

}

int main(int argc, char* argv[]) {
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutInitWindowPosition(INIT_POSITION, INIT_POSITION);
    glutCreateWindow("Atividade 4: Transformacoes Geometricas");

    glClearColor(1.0,1.0,1.0,0.0);
    glColor3f(0.0f, 0.0f, 0.0f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glutDisplayFunc(handle_display);
    glutKeyboardFunc(handle_keyboard);
    glutSpecialFunc(handle_special_keyboard);

    glutMainLoop();

    return 0;
}