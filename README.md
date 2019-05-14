# CodificacionClavePrivada
Programas python para encriptar y desencriptar texto escrito en hexadecimal.


Dos programas en Pyton, que llamaremos Encriptar y Desencriptar. Cada uno de ellos recibe una clave (16 letras del código hexadecimal) que se introduce directamente y un fichero de texto, y los dos dan como salida un fichero de texto. En ambos casos los ficheros de texto de entrada contienen solo letras del código hexadecimal y el número de letras que contienen es siempre múltiplo de 16 (si no es así el programa avisará de un error). La salida, tembién en ambos casos, será un fichero de texto que tendrá letras del código hexadecimal, tantas como tenía el fichero de entrada. Detallemos un poco más.

El programa Encriptar debe empezar por comprobar si la clave es válida. la clave debe estar formada por 16 letras hexadecimales pero no cualquier combinación de 16 letras hexadecimales es válida (detalles explicados en clase). A continuación divide el fichero de texto en bloques de dieciséis letras (hexadecimales) y aplica el proceso de encriptar explicado en clase (que es una versión muy simplificada del AES) a cada bloque.

El programa Desencriptar también empieza por comprobar si la clave es válida (son válidas las mismas claves que para el progama Encriptar)  y avisar si no lo es. A continuación debe deshacer el proceso que haría el programa Encriptar con la misma clave.
