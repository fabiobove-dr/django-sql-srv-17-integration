# Use an official Python runtime as a parent image
FROM python:3.9

# Install ODBC Driver 17 for SQL Server
RUN apt-get update && \
    apt-get install -y unixodbc unixodbc-dev curl && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . ./app
