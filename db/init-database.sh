#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until pg_isready -U "$POSTGRES_USER"; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Create databases
psql -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = 'user_service_db'" | grep -q 1 || psql -U "$POSTGRES_USER" -c "CREATE DATABASE user_service_db;"
psql -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = 'task_service_db'" | grep -q 1 || psql -U "$POSTGRES_USER" -c "CREATE DATABASE task_service_db;"

echo "Databases user_service_db and task_service_db created successfully!"
