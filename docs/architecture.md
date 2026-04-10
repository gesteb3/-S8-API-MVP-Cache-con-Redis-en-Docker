# Arquitectura del Sistema

## Descripción de la Arquitectura

SIMAF está basado en una arquitectura cliente-servidor utilizando una API REST desarrollada con FastAPI. Esta arquitectura permite separar la capa de presentación del procesamiento de datos, facilitando la escalabilidad y el mantenimiento del sistema.

El sistema expone endpoints HTTP que permiten gestionar el flujo principal del negocio: registro de ingresos, registro de egresos, aprobación de egresos y consulta de información. Estos endpoints pueden ser consumidos mediante herramientas como Swagger UI o cualquier cliente HTTP.

Para el MVP, los datos se almacenan en memoria utilizando estructuras simples, lo que permite enfocarse en la lógica del negocio sin depender de una base de datos externa.

---

## Responsabilidades por Bloque

- **Cliente (Usuario):**
  Realiza solicitudes HTTP a la API para interactuar con el sistema.

- **API REST (FastAPI):**
  Recibe las solicitudes, valida los datos de entrada y retorna respuestas en formato JSON.

- **Validación (Pydantic):**
  Se encarga de validar los datos enviados en las solicitudes, asegurando que cumplan con el formato esperado.

- **Lógica de Negocio:**
  Procesa las operaciones principales del sistema, como registrar ingresos, gestionar egresos y aprobar transacciones.

- **Almacenamiento en Memoria:**
  Guarda temporalmente la información de ingresos y egresos durante la ejecución del sistema.

- **Redis (Capa de Cache):**
  Se incorpora como una mejora de rendimiento utilizando el patrón cache-aside para almacenar respuestas frecuentes del endpoint de consulta de egresos.

---

## Diagrama de Arquitectura

```mermaid
graph TD
    Usuario -->|Solicitudes HTTP| API[API REST - FastAPI]

    API --> Redis[(Redis Cache)]

    API --> Validacion[Validacion de datos Pydantic]
    API --> Logica[Logica de negocio]

    Logica --> Ingresos[Gestion de ingresos]
    Logica --> Egresos[Gestion de egresos]
    Egresos --> Aprobacion[Aprobacion de egresos]

    Logica --> Memoria[Almacenamiento en memoria]

    Redis -->|Cache HIT| API
    API -->|Cache MISS| Memoria

    API -->|Respuestas JSON| Usuario
