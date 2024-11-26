FROM postgres:13

# Copy initialization script to the container
COPY init-database.sh /docker-entrypoint-initdb.d/

# Ensure the script is executable
RUN chmod +x /docker-entrypoint-initdb.d/init-database.sh
