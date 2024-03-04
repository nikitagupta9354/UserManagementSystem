# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Python (you can customize as needed)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the Django app runs on
EXPOSE 800
# Run Django app when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]