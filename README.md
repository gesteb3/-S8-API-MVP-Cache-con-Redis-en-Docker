# SIMAF
Sistema Integrado de Administración Financiera

## Resumen del Sistema

SIMAF es una plataforma web diseñada para municipalidades que centraliza la gestión de ingresos, egresos y presupuesto en un solo sistema.

El sistema permite registrar ingresos municipales, gestionar solicitudes de egreso, controlar aprobaciones por parte del Director Financiero y visualizar el saldo disponible por partida presupuestaria en tiempo real.

Su objetivo principal es fortalecer el control interno, mejorar la trazabilidad de las transacciones y optimizar la toma de decisiones financieras dentro de la municipalidad.

SIMAF implementa control por roles (Contador, Encargado de Presupuesto, Director Financiero y Auditor), asegurando que cada usuario acceda únicamente a las funcionalidades correspondientes a su perfil.

La versión inicial (MVP) se enfoca en garantizar el registro y control básico del flujo financiero municipal, dejando funcionalidades avanzadas como portal público de transparencia y dashboards estratégicos para futuras versiones.

---

## API del Sistema

El sistema cuenta con una API REST desarrollada con FastAPI que implementa el flujo principal del negocio relacionado con la gestión financiera.

### Endpoints disponibles

- POST /ingresos — Registrar ingreso  
- POST /egresos — Registrar egreso  
- PUT /egresos/{id}/aprobar — Aprobar egreso  
- GET /egresos/{id} — Consultar egreso  

---

## Ejecución del Proyecto

1. Instalar dependencias:

pip install fastapi uvicorn

2. Ejecutar la API:

python -m uvicorn main:app --reload

3. Abrir en navegador:

http://127.0.0.1:8000/docs

---

## Contrato de API

La especificación OpenAPI del sistema se encuentra en:

docs/api/openapi.yaml

---

