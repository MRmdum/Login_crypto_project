# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .

# Install required dependencies
RUN apt-get update && apt-get install -y protobuf-compiler
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the Python script
CMD ["python", "test_crypto1.py"]