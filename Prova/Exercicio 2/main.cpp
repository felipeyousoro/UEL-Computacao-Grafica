#include <GL/glut.h>
#include <math.h>

#define WIDTH 999
#define HEIGHT 666

#define PI 3.14159265
#define EARTH_RADIUS 1.0
#define MOON_RADIUS 0.420
#define EARTH_ROTATION_SPEED 0.177013
#define MOON_ROTATION_SPEED 4 * 0.69420
#define MOON_ORBIT_RADIUS 3 * 0.666

float g_earth_angle = 0.0;
float g_moon_angle = 0.0;

void handle_resize(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, (float)width / (float)height, 1.0, 200.0);
}

void draw_earth() {
    glColor3f(0.0, 0.0, 1.0);  
    glutWireSphere(EARTH_RADIUS, 20, 20);  
}

void draw_moon() {
    glColor3f(1.0, 1.0, 1.0);  
    glutWireSphere(MOON_RADIUS, 10, 10);  
}

void render() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    gluLookAt(0.0, 0.0, 5.0,  
              0.0, 0.0, 0.0,  
              0.0, 1.0, 0.0);
    glRotatef(g_earth_angle, 0.0, 1.0, 0.0);

    draw_earth();

    glPushMatrix();

    glTranslatef(MOON_ORBIT_RADIUS, 0.0, 0.0);
    glRotatef(g_moon_angle, 0.0, 1.0, 0.0);

    draw_moon();

    glPopMatrix();

    glutSwapBuffers();
}

void update_angles(int value) {
    g_earth_angle += EARTH_ROTATION_SPEED;
    if (g_earth_angle > 360.0) {
        g_earth_angle -= 360.0;
    }

    g_moon_angle += MOON_ROTATION_SPEED;
    if (g_moon_angle > 360.0) {
        g_moon_angle -= 360.0;
    }

    glutPostRedisplay();
    glutTimerFunc(16, update_angles, 0); 
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("Prova Exercicio 2: Terra Plana");

    glEnable(GL_DEPTH_TEST);

    glutDisplayFunc(render);
    glutReshapeFunc(handle_resize);

    glutTimerFunc(16, update_angles, 0);

    glutMainLoop();

    return 0;
}
