# Prompt 38 — Docker & Production Configuration

## Goal

Create Docker setup for production deployment.

## Prompt

```
Create Docker and production configuration for VTP.

1. File: Dockerfile

   FROM python:3.12-slim

   ENV PYTHONDONTWRITEBYTECODE=1
   ENV PYTHONUNBUFFERED=1

   WORKDIR /app

   # Install system dependencies (no mysqlclient C deps needed — using PyMySQL)
   RUN apt-get update && apt-get install -y \
       gcc \
       && rm -rf /var/lib/apt/lists/*

   COPY requirements/production.txt requirements/production.txt
   COPY requirements/base.txt requirements/base.txt
   RUN pip install --no-cache-dir -r requirements/production.txt

   COPY . .
   RUN python manage.py collectstatic --noinput --settings=vtp.settings.production || true

   CMD ["gunicorn", "vtp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]


2. File: docker-compose.yml

   services:
     web:
       build: .
       ports: ["8000:8000"]
       env_file: .env
       depends_on: [db]
       volumes: [media_data:/app/media]
       restart: unless-stopped

     db:
       image: mysql:8.0
       environment:
         MYSQL_DATABASE: ${DATABASE_NAME:-vtp}
         MYSQL_ROOT_PASSWORD: ${DATABASE_PASSWORD:-rootpassword}
       volumes: [mysql_data:/var/lib/mysql]
       restart: unless-stopped

     nginx:
       image: nginx:alpine
       ports: ["80:80"]
       volumes:
         - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
         - media_data:/app/media
       depends_on: [web]
       restart: unless-stopped

   volumes:
     mysql_data:
     media_data:


3. File: nginx/default.conf
   - Proxy pass to web:8000
   - Serve /static/ and /media/
   - Client max body size: 50M

4. File: .env.example
   SECRET_KEY=your-secret-key-here
   DATABASE_NAME=vtp
   DATABASE_USER=root
   DATABASE_PASSWORD=
   DATABASE_HOST=db
   DATABASE_PORT=3306
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   WAGTAILADMIN_BASE_URL=https://yourdomain.com

Note: Using PyMySQL — no need for libmysqlclient-dev system package!
```

## Verification

1. `docker-compose build` succeeds
2. `docker-compose up` starts all services
3. Website accessible at http://localhost

## Expected Result

- Production-ready Docker setup
- Lightweight (no C compiler deps for MySQL)
