# Use the official Python image from the DockerHub
FROM python:3

# Set the working directory in docker
WORKDIR /usr/src/app

# Copy all the files into the working directory
COPY . /usr/src/app/

# Install any dependencies
RUN pip install -r requirements.txt

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]