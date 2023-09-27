# Reto_2

link al repositorio: https://github.com/Jacobo24/Reto_2.git

## A. Dos envases
Problema
Tienes dos recipientes con agua. El primer recipiente contiene a litros de agua, y el segundo recipiente contiene b litros de agua. Ambos recipientes son muy grandes y pueden contener cualquier cantidad de agua.

También tienes una taza vacía que puede contener hasta c litros de agua.

En un movimiento, puedes recoger hasta c litros de agua de cualquier recipiente y verterlo en el otro recipiente. Ten en cuenta que la masa de agua vertida en un movimiento no tiene que ser un número entero.

¿Cuál es el número mínimo de movimientos requeridos para igualar las masas de agua en los recipientes? Ten en cuenta que no puedes realizar ninguna otra acción que no sean los movimientos descritos.

Entrada
Cada prueba contiene múltiples casos de prueba. La primera línea contiene el número de casos de prueba t (1≤t≤1000). La descripción de los casos de prueba sigue a continuación. Cada caso de prueba consta de una sola línea que contiene tres enteros a, b y c (1≤a,b,c≤100) — la masa de agua en los recipientes y la capacidad de la taza, respectivamente.

Salida
Para cada caso de prueba, imprime un solo número: el número mínimo de movimientos requeridos para igualar las masas de agua en los recipientes. Se puede demostrar que siempre es posible.

Ejemplo
entrada

6

3 7 2

17 4 3

17 17 1

17 21 100

1 100 1

97 4 3

salida

1

3

0

1

50

16

## B. Niña ambiciosa
Problema
María, la hija de Enrique, es una niña ambiciosa, así que Enrique le da el siguiente problema para poner a prueba su ambición.

Dado un conjunto de enteros [A1, A2, A3, ..., AN]. En una operación, Chaneka puede elegir un elemento y luego aumentar o disminuir el valor del elemento en 1. Chaneka puede realizar esa operación varias veces, incluso para diferentes elementos.

¿Cuál es el número mínimo de operaciones que deben realizarse para que se cumpla que A1×A2×A3×...×AN=0?

Entrada
La primera línea contiene un solo entero N (1≤N≤105).

La segunda línea contiene N enteros A1, A2, A3, ..., AN (−105≤Ai≤105).

Salida
Para cada caso de prueba, imprime un solo número: el número mínimo de movimientos requeridos para igualar las masas de agua en los recipientes. Se puede demostrar que siempre es posible.

Ejemplos
entrada

3

2 -6 5

salida

2

entrada

1

-3

salida

3

## C. El canal
Problema
Fernando tiene un canal en una red social. Un total de n personas están suscritas a su canal, y Fernando no se considera un suscriptor. Fernando ha subido una nueva publicación a su canal. En el momento de la publicación, había a suscriptores en línea. Suponemos que cada suscriptor siempre lee todas las publicaciones en el canal si están en línea. Después de esto, Fernando comienza a monitorear el número de suscriptores en línea. Recibe consecutivamente q notificaciones en forma de "un suscriptor se desconectó" o "un suscriptor se conectó". Fernando no sabe qué suscriptor en particular se conecta o desconecta. Se garantiza que se podría haber recibido tal secuencia de notificaciones. Fernando se pregunta si todos sus suscriptores han leído la nueva publicación. Ayúdalo determinando una de las siguientes opciones: Es imposible que todos los n suscriptores hayan leído la publicación. Es posible que todos los n suscriptores hayan leído la publicación. Se garantiza que todos los n suscriptores han leído la publicación.

Entrada
Cada prueba contiene múltiples casos de prueba. La primera línea contiene el número de casos de prueba t (1≤t≤500). La descripción de los casos de prueba sigue a continuación. La primera línea de cada caso de prueba contiene tres enteros n, a y q (1≤n≤100, 0≤a≤n, 1≤q≤100) — el número de suscriptores del canal, el número inicial de suscriptores en línea y el número de notificaciones.

La segunda línea de cada caso de prueba contiene una cadena de longitud q, que consiste en los caracteres '+' y '-'. El i-ésimo de estos caracteres es '+', si la i-ésima notificación indica que un suscriptor se conectó, y es '-' en caso contrario.

Salida
Para cada caso de prueba, imprime una sola línea: "YES" si se garantiza que todos los n suscriptores han leído la publicación, "NO" si es imposible que todos los n suscriptores hayan leído la publicación y "MAYBE" en caso contrario.

Ejemplo
entrada

4

5 5 3

--+

5 2 3

++-

5 4 2

-+

5 0 7

++++-++

salida

YES

NO

MAYBE

YES
