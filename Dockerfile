# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir temporalio pytest pytest-asyncio

# Default command to run CLI
CMD ["python", "main.py", "sample.json"]

