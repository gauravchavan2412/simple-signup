# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Flask and Boto3
RUN pip install flask boto3

# Make port 5000 available to the world outside this container
EXPOSE 7447

# Define environment variable for Flask app
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=7447"]
