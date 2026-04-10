# Cache en MoveFast

## ¿Qué es el cache?

El cache es un mecanismo que permite almacenar temporalmente datos en memoria para responder más rápido a las solicitudes sin tener que consultar constantemente la base de datos.

## Uso del cache en MoveFast

En el sistema MoveFast, el cache se utiliza de forma simulada mediante estructuras en memoria (listas y diccionarios en Python), donde se almacenan:

- Conductores disponibles
- Viajes en curso
- Estado de los nodos

Esto permite que las consultas sean rápidas y eficientes, simulando el comportamiento de sistemas reales.

## Ejemplo en el sistema

Cuando se solicita un viaje:
- El sistema consulta primero los conductores disponibles en memoria
- Asigna uno sin necesidad de consultar una base de datos externa

De igual manera, los viajes se almacenan en una lista que funciona como cache temporal.

## Ventajas

- Respuesta rápida (baja latencia)
- Menor carga en la base de datos
- Mejor experiencia de usuario

## Desventajas

- Posibles inconsistencias temporales
- Pérdida de datos si el sistema se reinicia
- No es persistente

## Relación con sistemas distribuidos

En arquitecturas reales, el cache se implementa con herramientas como Redis o Memcached, permitiendo:

- Compartir información entre nodos
- Reducir tiempos de respuesta
- Soportar alta concurrencia

En MoveFast, este comportamiento se simula para demostrar cómo el cache mejora el rendimiento dentro de un sistema distribuido.
