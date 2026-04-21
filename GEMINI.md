# SRE-Gen: Intelligent Infrastructure Architect

SRE-Gen es un arquitecto autónomo de Infraestructura como Código (IaC) impulsado por IA, diseñado para generar configuraciones de Terraform listas para producción, optimizadas en costos y seguras.

## Descripción General del Proyecto

- **Propósito:** Automatizar la creación y gestión de infraestructura en la nube utilizando modelos de lenguaje avanzados (Gemini).
- **Arquitectura:**
  - **Core (`src/core/`):** Lógica del agente con mitigación de Prompt Injection, detección de deriva y gestión de estado moderno.
  - **Utils (`src/utils/`):** Logging estandarizado y optimización automática de recursos.
  - **Infra (`public/` & `docs/`):** Interfaz estática y documentación técnica.

## Tecnologías Principales

- **Lenguaje:** Python 3.11+
- **IA:** Google Generative AI (Configurable vía `GEMINI_MODEL`).
- **IaC:** Terraform / OpenTofu (JSON).
- **Contenedor:** Docker (Multi-stage, No-root).

## Configuración y Variables de Entorno

El proyecto utiliza un archivo `.env` para la configuración local. Ver `.env.example`.

| Variable | Descripción | Default |
| :--- | :--- | :--- |
| `GOOGLE_API_KEY` | API Key de Google AI Studio | (Requerido) |
| `GEMINI_MODEL` | Modelo de Gemini a utilizar | `gemini-1.5-flash` |
| `AWS_REGION` | Región por defecto para el backend | `eu-west-1` |

## Comandos de Uso Frecuente

### Ejecución
- **Local:** `python3 src/core/main.py`
- **Docker:** `docker build -t sre-gen . && docker run --env-file .env sre-gen`

### Desarrollo (Makefile)
- **Tests:** `make test`
- **Linting:** `make lint`
- **Versión:** `make version-[patch|minor|major]`

## Estándares de Seguridad y SRE

1. **Prompt Security:** Entradas de usuario delimitadas y procesadas mediante plantillas para evitar inyecciones.
2. **Validación Automática:** Se ejecuta `terraform validate` inmediatamente después de generar cualquier archivo de configuración.
3. **Mínimo Privilegio:** El contenedor Docker no se ejecuta como root.
4. **Estado Robusto:** Uso de `use_lockfile: True` para evitar colisiones en despliegues concurrentes.
