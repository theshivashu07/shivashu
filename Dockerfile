# Use an official Python runtime as a parent image.  We'll use a slim version to keep the image size down.
FROM python:3.12-slim-buster

# Set environment variables.  These are used by Python and Django.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container.  All subsequent commands will be executed from here.
WORKDIR /app

# Copy the requirements file into the container.  This is done separately to take advantage of Docker's caching.  If only your application code changes, Docker can reuse the cached 'pip install' layer.
COPY requirements.txt /app/

# Install project dependencies.  Use --no-cache-dir to prevent pip from storing downloaded packages in the container, further reducing its size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project source code into the container.  This includes your Django project, apps, static files, media files, etc.
COPY . /app/websiteverse/

# Change the working directory to the Django project's root.  This is where 'manage.py' is located.
WORKDIR /app/websiteverse/Website

# Collect static files.  This is essential for serving static assets in a production-like environment.  The --noinput flag prevents Django from prompting for user input.
RUN python manage.py collectstatic --noinput

# Set the DJANGO_SETTINGS_MODULE environment variable.  This tells Django which settings module to use.
ENV DJANGO_SETTINGS_MODULE=Website.settings

# Expose the port that the application will listen on.  While Gunicorn will bind to this port inside the container, you'll also need to map this port when running the container.
EXPOSE 8000

# Command to run the application using Gunicorn.  Gunicorn is a production-ready WSGI server.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Website.wsgi:application"]
