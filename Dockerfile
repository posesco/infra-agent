FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY main.tf.json .

ENV GOOGLE_API_KEY=${GOOGLE_API_KEY}
CMD ["python", "src/core/main.py"]
