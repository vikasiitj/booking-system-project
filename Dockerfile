# Use official Python image
FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Copy project files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
