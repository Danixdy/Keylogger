# Keylogger
Keylogger Básico (Proyecto Educativo)

Este proyecto implementa un keylogger simple utilizando Python con fines exclusivamente educativos y de concientización sobre seguridad informática. El objetivo es entender cómo se capturan las pulsaciones del teclado y se registran en un archivo.

Propósito:

Comprender la mecánica de la captura de eventos de teclado.

Reforzar la importancia de la seguridad y el uso ético de las herramientas de software.

## Requisitos del Proyecto

Asegúrate de tener Python instalado (versión 3.10+ recomendada). La única dependencia externa necesaria es la librería keyboard.

Instalación

Instalar la librería keyboard:

pip install keyboard


(Si prefieres usar un requirements.txt, su contenido sería simplemente keyboard)

Archivos Principales

Archivo

Descripción

main.py

Contiene el código fuente del keylogger.

keylogResults.txt

Archivo de salida. Aquí se registran las pulsaciones. Se crea automáticamente al iniciar el programa.

## Ejemplos de Ejecución

1. Iniciar la Captura

Ejecuta el script principal desde tu terminal:

python main.py


El programa comenzará a ejecutarse inmediatamente y a registrar las pulsaciones de teclado en segundo plano.

2. Detener la Captura

El script está configurado para detenerse de forma segura cuando el usuario presiona la tecla ESC.

Una vez presiones ESC, verás el siguiente mensaje en la consola:

Ya está, mira keylogResults.txt


3. Revisar el Registro (keylogResults.txt)

El archivo keylogResults.txt contendrá todas las pulsaciones capturadas.

Ejemplo de entrada del teclado:

Hola mundo. 123
(Se presiona la tecla Enter)
Esto es una prueba.

Contenido de keylog.txt resultante:

Hola mundo. 123
[ENTER]Esto es una prueba.[.]


## Manejo de Teclas Especiales en el Log:

Espacio (space): Se registra como un espacio normal (     ).

Enter (enter): Se registra como un salto de línea (\n).

Borrar (backspace): Se registra como [BORRAR].

Otras teclas (shift, ctrl, alt): Se registran encapsuladas y en mayúsculas, por ejemplo: [SHIFT] o [CTRL].
