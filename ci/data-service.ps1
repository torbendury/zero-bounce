docker compose -f .\data-service-test-compose.yml down
docker volume prune -f
docker compose -f .\data-service-test-compose.yml up --build --abort-on-container-exit