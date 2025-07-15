la organizacion del proyecto por carpetas:

proyecto_reloj/
│
├── reloj/                   <- carpeta que agrupa módulos relacionados
│   ├── __init__.py          <- para hacer módulo Python
│   ├── reloj_base.py        <- clase abstracta RelojBase
│   ├── reloj_24h.py         <- clase Reloj24h aquí
│   └── builder.py           <- builder en archivo separado
├── main.py
├── test_reloj.py
├── utils.py
└── README.md

explicacion del proyecto:

1. Clases principales:

a) RelojBase (abstracta)

Define la interfaz (contrato) que deben cumplir todos los relojes.

Métodos abstractos: mostrar(), adelantar_minuto(), actualizar_hora(), es_igual().

b) Reloj24h (concreta)

Implementa un reloj de 24 horas con atributos privados: hora, minutos, segundos.

Métodos:

mostrar(): devuelve la hora en formato "HH:MM:SS".

adelantar_minuto(): suma un minuto, ajustando horas y minutos correctamente.

actualizar_hora(): modifica la hora manualmente.

es_igual(): compara si dos relojes tienen la misma hora.

c) RelojBuilder

Patrón de diseño Builder para crear objetos Reloj24h de forma flexible.

Métodos encadenables para configurar hora, minutos y segundos.

Método construir() que devuelve el objeto Reloj24h.

2. Módulo de consola (main.py):

Clase ConsolaReloj que maneja la interacción con el usuario vía consola.

Permite:

Crear relojes.

Mostrar todos los relojes creados.

Adelantar un minuto en un reloj seleccionado.

Modificar la hora de un reloj.

Comparar si dos relojes son iguales.

Salir del programa.

Implementa un menú simple que se repite hasta que el usuario elija salir.

3. Archivo de pruebas test_reloj.py:

Contiene pruebas unitarias para verificar que:

El método adelantar_minuto() funcione con casos límites.

La función mostrar() devuelva el formato correcto.

El método actualizar_hora() actualice correctamente.

La comparación es_igual() funcione para igualdad y diferencia.

4. Archivo auxiliar utils.py:

Funciones para validar datos ingresados (hora, minutos, segundos).

Función para formatear tiempo.

Mejora la organización y evita repetir código.

5. Buenas prácticas implementadas:

Encapsulamiento: atributos privados en las clases.

Abstracción: interfaz clara con clase abstracta.

Polimorfismo: diferentes implementaciones posibles con la clase base.

Builder Pattern: construcción flexible de objetos.

Separación de responsabilidades: lógica del reloj en clases, lógica de interacción en consola.

Tests unitarios para asegurar calidad y evitar regresiones.

Documentación y comentarios para facilitar comprensión.


