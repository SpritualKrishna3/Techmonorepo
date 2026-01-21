# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for some python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first → better caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Create media & static folders (sometimes needed)
RUN mkdir -p media static

# Default command will be overridden in docker-compose
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]