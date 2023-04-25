#include <GL/glut.h>
 
#define WIDTH 700
#define HEIGHT 500

#define INIT_POSITION 100

enum COLORS {
    BLACK,
    WHITE,
    RED,
    GREEN,
    BLUE,
    YELLOW,
    ORANGE,
    PURPLE,
    GRAY,
    BROWN,
    PINK,
};

void handle_keyboard(unsigned char key, int x, int y) {
    switch(key) {
        case 'd':
            glClear(GL_COLOR_BUFFER_BIT);
            glFlush();
            break;
        case 'D':
            glClear(GL_COLOR_BUFFER_BIT);
            glFlush();
            break;
        default:
            break;
    }

}

void handle_mouse_click(GLint button, GLint state, GLint x, GLint y) {
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        glBegin(GL_POINTS);
        glVertex2i(x, HEIGHT - y);
        glEnd();
        glFlush();
    }
    else if(button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN) {
        return;
    }
}

void handle_mouse_motion(GLint x, GLint y) {
    glBegin(GL_POINTS);
    glVertex2i(x, HEIGHT - y);
    glEnd();
    glFlush();
}

void handle_display() {
    
}

void properties_main_menu(GLint op) {
    
}

void properties_color_menu(GLint op) {
    switch(op) {
        case BLACK:
            glColor3f(0.0,0.0,0.0);
            break;
        case WHITE:
            glColor3f(1.0,1.0,1.0);
            break;
        case RED:
            glColor3f(1.0,0.0,0.0);
            break;
        case GREEN:
            glColor3f(0.0,1.0,0.0);
            break;
        case BLUE:
            glColor3f(0.0,0.0,1.0);
            break;
        case YELLOW:
            glColor3f(1.0,1.0,0.0);
            break;
        case ORANGE:    
            glColor3f(1.0,0.5,0.0);
            break;
        case PURPLE:
            glColor3f(1.0,0.0,1.0);
            break;
        case GRAY:  
            glColor3f(0.0,0.0,0.0);
            break;
        case BROWN:
            glColor3f(0.5,0.25,0.0);
            break;
        case PINK:
            glColor3f(1.0,0.0,0.5);
            break;
        default:
            glColor3f(0.0,0.0,0.0);
            break;
    }
}

void properties_thickness_menu(GLint op) {
    switch(op) {
        case 0:
            glPointSize(2.5);
            break;
        case 1:
            glPointSize(5.0);
            break;
        case 2:
            glPointSize(7.5);
            break;
        case 3:
            glPointSize(10);
            break;
        case 4:
            glPointSize(12.5);
            break;
        case 5:
            glPointSize(15.0);
            break;
        default:
            glPointSize(2.5);
            break;
    }
}

void glut_initialize_menus() {
    GLint main_menu, color_menu, thickness_menu;

    color_menu = glutCreateMenu(properties_color_menu);
    glutAddMenuEntry("Black", BLACK);
    glutAddMenuEntry("White", WHITE);
    glutAddMenuEntry("Red", RED);
    glutAddMenuEntry("Green", GREEN);
    glutAddMenuEntry("Blue", BLUE);
    glutAddMenuEntry("Yellow", YELLOW);
    glutAddMenuEntry("Orange", ORANGE);
    glutAddMenuEntry("Purple", PURPLE);
    glutAddMenuEntry("Gray", GRAY);
    glutAddMenuEntry("Brown", BROWN);
    glutAddMenuEntry("Pink", PINK);

    thickness_menu = glutCreateMenu(properties_thickness_menu);
    glutAddMenuEntry("2.5", 0);
    glutAddMenuEntry("5.0", 1);
    glutAddMenuEntry("7.5", 2);
    glutAddMenuEntry("10", 3);
    glutAddMenuEntry("12.5", 4);
    glutAddMenuEntry("15.0", 5);

    main_menu = glutCreateMenu(properties_main_menu); 
    glutAddSubMenu("Color", color_menu);
    glutAddSubMenu("Thickness", thickness_menu);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}   

int main(int argc, char* argv[]) {
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutInitWindowPosition(INIT_POSITION, INIT_POSITION);
    glutCreateWindow("Atividade 3: FakePaint");

    glClearColor(1.0, 1.0, 1.0, 0.0);
    glColor3f(0.0f, 0.0f, 0.0f);
    glPointSize(4.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, (GLdouble) WIDTH, 0.0, (GLdouble) HEIGHT);

    glut_initialize_menus();

    glutDisplayFunc(handle_display);
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
    glutKeyboardFunc(handle_keyboard);
    glutMouseFunc(handle_mouse_click);
    glutMotionFunc(handle_mouse_motion);
    
    glutMainLoop();

    return 0;
}