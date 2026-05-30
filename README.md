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


## API Endpoints


### Home Endpoint

```bash
http://localhost
```

Response:

```json
{
  "message": "FastAPI Backend Running"
}
```

---

### Health Check Endpoint

```bash
http://localhost/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Swagger API Documentation

```bash
http://localhost/docs
```

Use this URL to test and explore all available API endpoints through the FastAPI Swagger UI.
