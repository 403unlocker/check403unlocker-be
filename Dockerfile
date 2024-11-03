FROM docker.arvancloud.ir/python:3.11-slim

# set the working directory
WORKDIR /app

# Copy  requirements 
COPY requirements.txt .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy  rest of the application
COPY . .

# Use a non-root user for security
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Expose the application's port
EXPOSE 8080

# Healthcheck to monitor the application's status
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/|| exit 1

# Run the application
CMD ["python", "run.py"]
