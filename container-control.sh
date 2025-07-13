#!/bin/bash

# ------------------------------------------------------
# INSTRUCTIONS
# make executable with: chmod +x container-control.sh
# Then use:
#   ./container-control.sh build/start/stop...
# ------------------------------------------------------

set -e

COMMAND=$1

case $COMMAND in
    build)
        echo "Building Docker images..."
        docker compose build --no-cache
        echo "Starting DB and web containers..."
        docker compose up -d db web
        echo "Running initial migrations and fixture loading..."
        docker compose run --rm init
        ;;

    start)
        echo "Starting containers (DB + web)..."
        docker compose up -d db web
        echo "Containers started!"
        echo "API:     http://localhost:8000/api/v1/"
        echo "Swagger: http://localhost:8000/api/schema/swagger-ui/"
        echo "Login with: admin1 / password1"
        ;;

    stop)
        echo "Stopping and removing containers..."
        docker compose down
        ;;

    stop-all)
        echo "Stopping containers and deleting volumes (Postgres data will be lost)..."
        docker compose down -v
        ;;

    init)
        echo "Running migrations and fixture loading..."
        docker compose run --rm init
        ;;

    logs)
        echo "Showing live logs..."
        docker compose logs -f
        ;;

    cleanup)
        echo "Stopping and removing all containers, volumes, and images for this project..."
        docker compose down -v --rmi all --remove-orphans
        echo "Pruning dangling volumes (if any)..."
        docker volume prune -f
        ;;

    help|*)
        echo ""
        echo "Usage: $0 {build|start|stop|stop-all|init|logs|cleanup}"
        echo ""
        echo "  build      Build, start, and run initial setup for database and web services"
        echo "  start      Start services (for regular use)"
        echo "  stop       Stop services (for regular use)"
        echo "  stop-all   Stop services and delete volumes (db data)"
        echo "  init       Run initial setup for database (run after stop-all)"
        echo "  logs       Show container logs"
        echo "  cleanup    Remove containers, volumes, and images (complete reset)"
        echo ""
        exit 1
        ;;
esac