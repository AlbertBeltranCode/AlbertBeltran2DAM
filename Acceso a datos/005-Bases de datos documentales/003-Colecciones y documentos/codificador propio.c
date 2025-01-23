#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define N 128  // Tamaño de la tabla de sustitución

// Tabla de sustitución basada en nombres de dioses nórdicos
char nords_table[N] = "OdinThorLokiFreyaBaldurHodrHeimdallTyrNjordSkadi";

void generar_tabla(unsigned char *tabla) {
    // Generar una tabla de sustitución simple basada en un desorden de nords_table
    for (int i = 0; i < N; i++) {
        tabla[i] = nords_table[i % strlen(nords_table)];
    }
}

// Función para codificar una cadena
char *codifica(const char *entrada) {
    size_t len = strlen(entrada);
    unsigned char tabla[N];
    generar_tabla(tabla);

    char *codificado = malloc(len + 1);
    if (!codificado) return NULL;

    for (size_t i = 0; i < len; i++) {
        codificado[i] = tabla[(unsigned char)entrada[i]];
    }
    codificado[len] = '\0';

    return codificado;
}

// Función para decodificar una cadena
char *descodifica(const char *entrada) {
    size_t len = strlen(entrada);
    unsigned char tabla[N];
    generar_tabla(tabla);

    char *descodificado = malloc(len + 1);
    if (!descodificado) return NULL;

    for (size_t i = 0; i < len; i++) {
        for (int j = 0; j < N; j++) {
            if (tabla[j] == entrada[i]) {
                descodificado[i] = (char)j;
                break;
            }
        }
    }
    descodificado[len] = '\0';

    return descodificado;
}

int main() {
    const char *contrasena = "Valhalla123";
    printf("La contraseña es: %s\n", contrasena);

    char *codificado = codifica(contrasena);
    if (!codificado) {
        fprintf(stderr, "Error al codificar.\n");
        return 1;
    }
    printf("La contraseña codificada es: %s\n", codificado);

    char *descodificado = descodifica(codificado);
    if (!descodificado) {
        fprintf(stderr, "Error al decodificar.\n");
        free(codificado);
        return 1;
    }
    printf("La contraseña decodificada es: %s\n", descodificado);

    free(codificado);
    free(descodificado);

    return 0;
}
