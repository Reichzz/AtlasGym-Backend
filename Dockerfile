FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev && \
    APT-GET clean && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

RUN python manage.py migrate && \
    python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Backend.wsgi:application"]
