#include <GL/glut.h>
#include <cmath>

// Ângulo de rotação da Terra
float earthRotation = 0.0f;

// Ângulo de rotação da Lua
float moonRotation = 0.0f;

// Função de renderização
void renderScene() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    // Define a posição da câmera
    gluLookAt(0.0f, 0.0f, 5.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);

    // Desenha a Terra
    glColor3f(0.0f, 0.5f, 1.0f);
    glutSolidSphere(1.0f, 50, 50);

    // Posiciona a Lua em relação à Terra
    glRotatef(earthRotation, 0.0f, 1.0f, 0.0f);
    glTranslatef(2.0f, 0.0f, 0.0f);

    // Desenha a Lua
    glColor3f(1.0f, 1.0f, 1.0f);
    glutSolidSphere(0.3f, 50, 50);

    // Atualiza os ângulos de rotação
    earthRotation += 0.2f;
    moonRotation += 0.4f;

    glutSwapBuffers();
}

// Função de atualização da cena
void update(int value) {
    glutPostRedisplay();
    glutTimerFunc(1, update, 0);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Rotacao da Terra e da Lua");
    glEnable(GL_DEPTH_TEST);
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glutDisplayFunc(renderScene);
    glutTimerFunc(0, update, 0);
    glutMainLoop();
    return 0;
}
