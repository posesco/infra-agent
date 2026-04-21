FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

# Copiar solo lo necesario y desde el builder para seguridad
COPY --from=builder /root/.local /root/.local
COPY . .

# Asegurar que el PATH incluya los binarios de python instalados por el usuario
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Configuración por defecto del modelo
ENV GEMINI_MODEL=gemini-1.5-flash

# No ejecutar como root (Principio de Mínimo Privilegio)
RUN useradd -m sreuser && chown -R sreuser /app
USER sreuser

CMD ["python", "src/core/main.py"]
