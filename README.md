# django-cassandra-prototype

## Summary

This is a sample project that integrates [Django](https://www.djangoproject.com/) and more specifically [Django Rest Framework](http://www.django-rest-framework.org/) with a Cassandra backend [django-cassandra-engine](https://github.com/r4fek/django-cassandra-engine).

## Installation

    $docker pull cassandra  # Installs Cassandra with Docker
    $pip install -r requirements.txt  # Installs requirements

## Run Cassandra on Docker and run Django

    docker run —name cassandra -p 9042:9042 -d cassandra  # Run Cassandra on port 9042 as background process
    python manage.py sync_cassandra  # Sync Cassandra database
    python manage.py runserver  # Run Django Server

## What should I see?

Go to the links below:

    http://localhost:8000/api/reddit/blog/  # See the DRF API GUI
    http://localhost:8000/docs/  # Swagger Docs that show all DRF API endpoints

## Contributors

Feel free to make a Pull Request.
