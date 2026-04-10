# SIMAF
## Sistema Integrado Municipal de Administración Financiera

---

## Problema que resuelve

Las municipalidades suelen gestionar ingresos, egresos y presupuesto mediante procesos manuales o sistemas aislados que no están integrados entre sí. Esto genera inconsistencias contables, duplicidad de información y retrasos en la generación de reportes financieros.  
Además, la falta de trazabilidad dificulta las auditorías internas y externas, afectando la transparencia institucional.  
La ausencia de controles automatizados también incrementa el riesgo de errores humanos y aprobaciones sin validación presupuestaria.  
SIMAF centraliza la información financiera en una sola plataforma, permitiendo control presupuestario en tiempo real, registro auditado de transacciones y flujos de aprobación formales.

---

## Usuarios / Stakeholders

- Director Financiero Municipal  
- Encargado de Presupuesto  
- Contador Municipal  
- Auditor Municipal  

---

## Objetivos de éxito

1. Reducir en al menos 60% los errores contables derivados de registros manuales.  
2. Generar reportes financieros en menos de 5 segundos.  
3. Garantizar trazabilidad completa del 100% de las transacciones.  
4. Reducir tiempos de aprobación de egresos en al menos 40%.  

---

## Alcance (Incluye)

- Registro digital de ingresos municipales.  
- Registro y gestión de solicitudes de egresos.  
- Flujo de aprobación multinivel para egresos.  
- Control de presupuesto por partidas.  
- Validación automática de disponibilidad presupuestaria.  
- Generación de reportes financieros por periodo.  
- Bitácora de auditoría de todas las acciones del sistema.  
- Panel de control con ejecución presupuestaria en tiempo real.  

---

## Fuera de Alcance (No incluye)

- Cobro en línea para ciudadanos.  
- Gestión de nómina municipal.  
- Sistema completo de compras públicas.  
- Integración bancaria en tiempo real.  
- Portal público de transparencia para ciudadanos.  

---

## Supuestos

- La municipalidad cuenta con conexión estable a internet.  
- Los usuarios recibirán capacitación básica del sistema.  
- El presupuesto inicial será cargado manualmente en la versión 1.  
- Cada usuario tendrá un rol claramente definido.  
- No se requiere integración con sistemas gubernamentales externos en la primera versión.  

---

## Riesgos y Mitigaciones

**1. Resistencia al cambio del personal**  
Mitigación: Capacitación inicial y manual de usuario digital.

**2. Errores en la carga inicial del presupuesto**  
Mitigación: Validación doble y revisión por el Director Financiero.

**3. Accesos no autorizados a información financiera**  
Mitigación: Sistema de autenticación con roles y permisos estrictos.

---

## Requerimientos v1

### Requerimientos Funcionales (FR)

- FR-01: El sistema debe permitir registrar ingresos con fecha, monto, fuente y partida presupuestaria.  
- FR-02: El sistema debe permitir registrar solicitudes de egreso asociadas a una partida.  
- FR-03: El sistema debe validar automáticamente si existe saldo disponible antes de aprobar un egreso.  
- FR-04: El sistema debe permitir aprobar o rechazar egresos según el rol del usuario.  
- FR-05: El sistema debe mostrar el saldo actualizado por partida presupuestaria.  
- FR-06: El sistema debe generar reportes financieros por rango de fechas.  
- FR-07: El sistema debe registrar en bitácora cada acción realizada por los usuarios.  

---

### Requerimientos No Funcionales (NFR)

- NFR-01: El sistema debe soportar al menos 20 usuarios concurrentes sin degradación perceptible.  
- NFR-02: El tiempo de respuesta no debe superar 3 segundos en operaciones estándar.  
- NFR-03: La disponibilidad mensual debe ser igual o mayor al 99%.  
- NFR-04: Los datos deben almacenarse con cifrado AES-256 en base de datos.  
- NFR-05: El sistema debe generar respaldos automáticos diarios.

---

## Diagrama de Contexto

```mermaid
flowchart LR
    Director[Director Financiero Municipal]
    Presupuesto[Encargado de Presupuesto]
    Contador[Contador Municipal]
    Auditor[Auditor Municipal]

    Sistema[SIMAF]

    Director -->|Aprueba egresos e ingresos| Sistema
    Presupuesto -->|Gestiona partidas| Sistema
    Contador -->|Registra ingresos y egresos| Sistema
    Auditor -->|Consulta y audita| Sistema

