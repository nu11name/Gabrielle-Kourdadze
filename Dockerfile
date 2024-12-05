# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 8000

# Set environment variable for Django settings
ENV PYTHONUNBUFFERED 1

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
