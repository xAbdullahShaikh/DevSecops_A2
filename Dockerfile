FROM python:3.10-slim

RUN adduser --disabled-password appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER appuser

CMD ["python", "app.py"]
