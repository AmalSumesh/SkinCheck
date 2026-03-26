FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${PORT:-5000}

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT:-10000} --timeout 180 --workers 1 --preload app:app"]