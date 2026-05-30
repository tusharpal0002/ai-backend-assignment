# AI Backend Assignment

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- Docker
- Docker Compose
- NGINX
- GitHub Actions

## Run Project

```bash
docker compose up -d --build


## CI/CD Pipeline

The repository includes a GitHub Actions workflow for automated builds.

For production deployment, configure:

- SERVER_IP
- SERVER_SSH_KEY

and connect the workflow to a Linux VPS.