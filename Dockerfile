FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev \
    libssl-dev \
    libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/mysql -lmysqlclient"


WORKDIR /app

COPY requirements.txt /app/

RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

ENV PATH="/opt/venv/bin:$PATH"

RUN python manage.py migrate && \
    python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]