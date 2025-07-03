#!/bin/bash

# make executable with: chmod +x docker-dev.sh
# Then use:
#   ./container-control.sh build/start/stop...

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
    ;;

  stop)
    echo "Stopping and removing containers..."
    docker compose down
    ;;

  stop-all)
    echo "Stopping containers and deleting volumes (Postgres data will be lost)..."
    docker compose down -v
    ;;

  logs)
    echo "Showing live logs..."
    docker compose logs -f
    ;;

  help|*)
    echo "Usage: $0 {build|start|stop|stop-all|logs}"
    echo ""
    echo "  build      Build containers, start services, and run init"
    echo "  start      Start db and web services (for regular dev use)"
    echo "  stop       Stop all containers"
    echo "  stop-all   Stop all containers and delete volumes"
    echo "  logs       Show container logs"
    exit 1
    ;;
esac