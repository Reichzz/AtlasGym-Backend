FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    libssl-dev \
    libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements.txt and install Python packages
COPY requirements.txt /app/
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Copy .env file
COPY .env /app/

# Ensure the virtual environment is activated
ENV PATH="/opt/venv/bin:$PATH"

# Collect static files and run migrations
RUN . /opt/venv/bin/activate && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Backend.wsgi:application"]
