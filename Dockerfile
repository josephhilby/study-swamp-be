# -----------------------------------------------
# Base image: lightweight Python 3.11
# -----------------------------------------------
FROM python:3.11-slim

# -----------------------------------------------
# Environment variables
# - PYTHONDONTWRITEBYTECODE: prevents .pyc files
# - PYTHONUNBUFFERED: ensures logs are shown directly in console (no buffering)
# -----------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# -----------------------------------------------
# Set the working directory in the container
# -----------------------------------------------
WORKDIR /app

# -----------------------------------------------
# Copy requirements file and install dependencies
# -----------------------------------------------
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# -----------------------------------------------
# Copy the rest of the application code
# -----------------------------------------------
COPY . .

# -----------------------------------------------
# Expose port 8000 for external access
# -----------------------------------------------
EXPOSE 8000

# -----------------------------------------------
# Default command:
# Run Gunicorn as WSGI server for Django app
# - Binds to all interfaces on port 8000
# - Entry point: your Django WSGI application
# -----------------------------------------------
CMD ["gunicorn", "Study_Swamp_BE.wsgi:application", "--bind", "0.0.0.0:8000"]
