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

## Pruebas realizadas

| Prueba | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| 1. Datos válidos | Código válido y matrícula | Registrar solicitud | Correcto |
| 2. Código vacío | Código vacío | Rechazar código | Correcto |
| 3. Tipo incorrecto | Tipo "nota" | Rechazar tipo | Correcto |
| 4. Prioridad alta | Tipo "pagos" | Asignar prioridad Alta | Correcto |
| 5. Prioridad baja | Tipo "constancia" | Asignar prioridad Baja | Correcto |

Las pruebas permitieron comprobar las validaciones del código, el tipo de consulta y la asignación de prioridades.

## Relación entre funciones y requisitos

| Función | Requisitos relacionados |
|---|---|
| `validar_codigo()` | Req. 2 |
| `validar_tipo_consulta()` | Req. 3 |
| `mostrar_menu()` | Req. 4 |
| `asignar_prioridad()` | Req. 5 |
| `validar_texto()` | Req. 6 |
| `mostrar_resumen()` | Req. 7 y Req. 8 |
| `registrar_solicitud()` | Req. 1, Req. 6 y Req. 9 |
| Estructura `for` del programa principal | Req. 10 |

La función `validar_codigo()` valida que el código no esté vacío y tenga como mínimo 8 caracteres.

La función `validar_tipo_consulta()` comprueba que el tipo de consulta pertenezca a las opciones permitidas.

La función `asignar_prioridad()` devuelve la prioridad según el tipo de consulta.

La función `validar_texto()` comprueba que los campos obligatorios no estén vacíos.

La función `mostrar_resumen()` recibe los datos mediante parámetros y muestra la información registrada.

La función `registrar_solicitud()` reúne los datos de cada solicitud y utiliza las funciones de validación y prioridad.

El programa principal utiliza una estructura `for` para registrar tres solicitudes durante una misma ejecución.
## Resultados de las pruebas

Se realizaron cinco pruebas para comprobar el funcionamiento del sistema:

1. Datos válidos: la solicitud fue registrada correctamente.
2. Código vacío: el sistema rechazó el código y solicitó ingresarlo nuevamente.
3. Tipo incorrecto: el sistema rechazó el tipo "nota" y solicitó un tipo válido.
4. Prioridad alta: el tipo "pagos" obtuvo prioridad Alta.
5. Prioridad baja: el tipo "constancia" obtuvo prioridad Baja.

Las pruebas fueron realizadas ejecutando el programa y verificando manualmente los resultados obtenidos.