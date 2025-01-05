# Use Python 3.10 slim image as the base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make the entrypoint script executable
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:///site.db

# Create volume for database persistence
VOLUME ["/app/instance"]

# Expose the port the app runs on
EXPOSE 5000

# Use the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]