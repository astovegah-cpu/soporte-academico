# Sistema de Orientacion y Registro de Atenciones

## Curso
Fundamentos de Programacion

## Lenguaje
Python

## Caso practico
Sistema de orientacion y registro de atenciones para el modulo de soporte academico.

## Integrante
- Hillary Mishelle Asto Vega

## Uso de parámetros

El programa utiliza parámetros para enviar datos entre funciones sin depender de variables globales.

Por ejemplo, la función `mostrar_resumen()` recibe como parámetros el código, nombre, tipo de consulta, descripción y prioridad de la solicitud.

## Alcance de variables

Las variables utilizadas para registrar una solicitud se encuentran dentro de la función `registrar_solicitud()`, por lo que son variables locales.

El programa evita utilizar variables globales innecesarias y pasa los datos mediante parámetros entre las funciones.