# Tarea de analisís de problemas de diseño
### Juan David Londoño

##### Resumen del problema: 
Se requiere realizar un sistema de ordenes que haga distintas autenticaciones de forma secuencial:
1. Autenticar usuario
2. Autenticar administrador
3. Realizar sondeo de datos
4. Verificar ataque de fuerza bruta
5. Verificar ordenes por cache

Este programa es una posible solcion para lo que se necesita utilizando la estrategia Cadena de responsabilidad, el codigo es suficientemente flexible para implementar nuevas verificaciones, o realizar arreglos en las viejas sin afectar el codigo que aun sirve.

#### Diagrama UML de la solucion
![Image](https://github.com/user-attachments/assets/2fa09576-5bcd-4994-9dba-18e36410408c)

#### [Video explicativo](https://www.youtube.com/watch?v=l18ogCOa0vY)

#### [Video explicativo](https://colab.research.google.com/drive/135vaS2YjSSRANAEl0BRc_DKRJAYWucF0?usp=sharing)
