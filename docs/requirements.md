# Requerimientos del Sistema

## Link al Backlog en Trello
https://trello.com/invite/b/69a14f7d3274c47f5694f889/ATTI2619f1fffd6e99a717a90ecd6792c9b7E5B52559/simaf 

---

## Lista de las 8 Historias (Título + Prioridad)

1. Registrar Ingresos Municipales — Must  
2. Registrar Solicitud de Egreso — Must  
3. Aprobar o Rechazar Egresos — Must  
4. Visualizar Saldo por Partida — Must  
5. Generar Reporte Financiero — Should  
6. Consultar Historial de Transacciones — Should  
7. Dashboard Financiero — Could  
8. Portal Público de Transparencia — Wont  

---

## Criterios de Aceptación (Given / When / Then)

### Historia 1: Registrar Ingresos Municipales — Must

Como Contador Municipal  
quiero registrar ingresos con fecha, monto y partida  
para mantener actualizado el presupuesto  

Given que el contador ha iniciado sesión  
When registra un ingreso con todos los campos obligatorios completos  
Then el sistema guarda el ingreso y actualiza el saldo de la partida correspondiente  

Given que falta un campo obligatorio  
When intenta guardar el registro  
Then el sistema muestra un mensaje de validación y no permite guardar la información  

---

### Historia 2: Registrar Solicitud de Egreso — Must

Como Contador Municipal  
quiero registrar solicitudes de egreso  
para que el Director Financiero las revise y apruebe  

Given que el contador ha iniciado sesión  
When registra una solicitud de egreso con datos válidos  
Then el sistema la guarda con estado “Pendiente de aprobación”  

Given que el monto solicitado supera el saldo disponible de la partida  
When intenta registrar la solicitud  
Then el sistema muestra una alerta y bloquea el registro  

---

## Endpoints del MVP

- POST /ingresos — Registrar ingreso  
- POST /egresos — Registrar egreso  
- PUT /egresos/{id}/aprobar — Aprobar egreso  
- GET /egresos/{id} — Consultar egreso  

---

## Contrato de API

El contrato de la API se encuentra definido en:

docs/api/openapi.yaml

---

## MVP Rationale

Las historias clasificadas como Must conforman el Producto Mínimo Viable (MVP) porque permiten ejecutar el flujo financiero esencial del sistema: registro de ingresos, gestión de egresos, aprobación de gastos y control del estado de las transacciones. Sin estas funcionalidades, el sistema no cumpliría su propósito principal de control financiero municipal.

Las historias Should agregan valor analítico y de supervisión, como la generación de reportes y consulta de historial, pero el sistema puede operar sin ellas en una primera versión.

La historia Could representa una mejora de experiencia y apoyo estratégico para la toma de decisiones mediante visualización de datos, pero no es crítica para el control operativo básico.

La historia Wont (Portal Público de Transparencia) se considera una funcionalidad futura orientada a ciudadanos y transparencia externa, por lo que no forma parte del alcance inicial del MVP.
