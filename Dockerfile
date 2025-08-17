# Use lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app folder into the container
COPY app/ ./app

# Run the main.py inside the app folder
CMD ["python", "app/main.py"]


