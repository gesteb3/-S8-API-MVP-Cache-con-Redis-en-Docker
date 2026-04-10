## Implementación de Cache en SIMAF

### Descripción General
Se implementó una capa de cache utilizando Redis con el objetivo de mejorar el rendimiento del sistema al reducir consultas repetitivas hacia la fuente principal de datos.

---

### Endpoint(s) que usan cache
El endpoint que implementa cache es:

- GET /egresos/{id}

Este endpoint fue seleccionado debido a que representa una operación de consulta frecuente dentro del sistema.

---

### Claves de Redis generadas
Las claves en Redis siguen el siguiente formato:

egreso:{id}

Ejemplo:
egreso:1

Esto permite identificar de manera única cada registro almacenado en cache.

---

### TTL definido
Se configuró un TTL (Time To Live) de:

60 segundos

Esto garantiza que los datos almacenados en cache expiren automáticamente, evitando el uso de información desactualizada por largos periodos.

---

### Estrategia de cache utilizada
Se implementa el patrón:

cache-aside

Flujo de funcionamiento:

1. La API recibe la solicitud del cliente.
2. Se consulta Redis para verificar si el dato existe.
3. Si existe → se retorna desde cache (cache hit).
4. Si no existe → se consulta la fuente principal (memoria).
5. Se almacena el resultado en Redis con TTL.
6. Se retorna la respuesta al cliente.

---

### Comportamiento del sistema

#### Cache HIT
- El dato existe en Redis.
- Se retorna directamente desde cache.
- Reduce el tiempo de respuesta.
- Evita procesamiento adicional.

#### Cache MISS
- El dato no existe en Redis.
- Se consulta la fuente principal.
- Se almacena en Redis con TTL.
- Se retorna al cliente.

---

### Responsabilidad del cache
La capa de cache tiene como responsabilidad:

- Almacenar temporalmente datos de acceso frecuente.
- Reducir la latencia en consultas repetidas.
- Disminuir la carga sobre la fuente principal de datos.
- Mejorar el rendimiento general del sistema.

---

### Riesgos o limitaciones

- Posible inconsistencia de datos durante el tiempo de vida del TTL.
- No se implementa invalidación de cache al actualizar datos.
- Dependencia de Redis como componente crítico.
- Almacenamiento principal en memoria (no persistente en este MVP).
