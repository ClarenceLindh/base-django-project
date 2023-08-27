#!/bin/bash

# Start Docker
echo "Starting Docker..."
systemctl start docker

# Check if Docker has the latest PostgreSQL image, if not pull it
echo "Checking if the latest PostgreSQL image is available..."
docker pull postgres:latest

# Check if a container named article-shop-db is already running
echo "Checking if the article-shop-db container is already running..."
if [[ "$(docker ps -q -f name=article-shop-db)" ]]; then
    # If it's already running, just start it
    echo "Found existing container. Starting the container..."
    docker start article-shop-db
else
    # If it's not running, create a new container and start it
    echo "Did not find existing container. Creating a new container..."
    docker run --name article-shop-db -e POSTGRES_PASSWORD=password -p 5432:5432 --network my-network -d postgres
    echo "Starting the container..."
    docker start article-shop-db
fi

# Show the logs of the container
echo "Showing logs of the container..."
docker logs -f article-shop-db
