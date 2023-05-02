#include <GL/glut.h>

#include <stdio.h>

#define WIDTH 700
#define HEIGHT 700

#define INIT_POSITION 100

GLfloat angles[3] = {0.0, 0.0, 0.0};
int option;

void handle_display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glColor3f(0, 0, 1);

    glutWireSphere(0.5, 50, 50);
    
    glLoadIdentity();    
    glutSwapBuffers();
}

void handle_keyboard(unsigned char key, int x, int y) {
    switch (key) {
        // case 'w':
        // case 'W':
        //     angles[0] += 10.0;
        //     break;

        // case 's':
        //     angles[0] -= 10.0;
        //     break;
        // case 'S':
        //     angles[0] -= 10.0;
        //     break;

        // case 'a':
        // case 'A':
        //     angles[0] += 10.0;
        //     glRotatef(angles[0], 1.0, 0.0, 0.0);
        //     break;

        // case 'd':
        // case 'D':
        //     angles[0] -= 10.0;
        //     glRotatef(angles[0], 1.0, 0.0, 0.0);
        //     break;

        default:
            break;

    }
}

void handle_special_keyboard(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_UP:
            angles[0] += 10.0;
            glTranslatef(10.0, 0.0, 0.0);
            break;
        case GLUT_KEY_DOWN:
            angles[0] -= 10.0;
            glTranslatef(-10.0, 0.0, 0.0);
            break;
        case GLUT_KEY_LEFT:
            angles[1] += 10.0;
            glTranslatef(0.0, 10.0, 0.0);
            break;
        case GLUT_KEY_RIGHT:
            angles[1] -= 10.0;
            glTranslatef(0.0, -10.0, 0.0);
            break;
        default:
            printf("Invalid key pressed: %d\n", key);
            break;
    }
}

void handle_timer(int value) {
    // switch (option) {
    //     case 'w':
    //         angles[0] += 10.0;
    //         break;
    //     case 's':
    //         angles[0] -= 10.0;
    //         break;
    //     case 'a':
    //         angles[1] += 10.0;
    //         break;
    //     case 'd':
    //         angles[1] -= 10.0;
    //         break;
    //     default:
    //         break;
    // }

    glutPostRedisplay();
    glutTimerFunc(100, handle_timer, 1);
}

int main(int argc, char* argv[]) {
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutInitWindowPosition(INIT_POSITION, INIT_POSITION);
    glutCreateWindow("Atividade 4: Transformacoes Geometricas");

    glClearColor(1.0,1.0,1.0,0.0);
    glEnable(GL_DEPTH_TEST); 
    glColor3f(0.0f, 0.0f, 0.0f);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glutDisplayFunc(handle_display);
    glutKeyboardFunc(handle_keyboard);
    glutSpecialFunc(handle_special_keyboard);

    glutTimerFunc(100, handle_timer, 1);

    glutMainLoop();

    return 0;
}