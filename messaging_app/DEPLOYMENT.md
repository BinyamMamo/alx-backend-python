# Deployment Guide

This guide provides comprehensive instructions for deploying the Django messaging app in various environments.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Setup](#environment-setup)
3. [Local Development](#local-development)
4. [Production Deployment](#production-deployment)
5. [Docker Deployment](#docker-deployment)
6. [CI/CD Pipeline](#cicd-pipeline)
7. [Monitoring and Maintenance](#monitoring-and-maintenance)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

- Python 3.9+
- MySQL 8.0+
- Docker and Docker Compose
- Git
- Jenkins (for CI/CD)
- GitHub account
- Docker Hub account

## Environment Setup

### Required Environment Variables

Create a `.env` file based on `.env.example`:

```bash
# Django Configuration
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database Configuration
DB_NAME=messaging_app
DB_USER=messaging_user
DB_PASSWORD=secure_password_here
DB_HOST=localhost
DB_PORT=3306

# Docker Hub (for CI/CD)
DOCKER_USERNAME=your_dockerhub_username
DOCKER_PASSWORD=your_dockerhub_password
```

## Local Development

### 1. Clone Repository

```bash
git clone https://github.com/your-username/alx-backend-python.git
cd alx-backend-python/messaging_app
```

### 2. Setup Virtual Environment

```bash
cd messaging
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Create MySQL database
mysql -u root -p
CREATE DATABASE messaging_app;
CREATE USER 'messaging_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON messaging_app.* TO 'messaging_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 4. Django Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

### 5. Using Docker Compose (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Production Deployment

### 1. Server Preparation

#### Ubuntu/Debian Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip python3-venv nginx mysql-server git

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo pip3 install docker-compose
```

### 2. Application Deployment

```bash
# Clone repository
git clone https://github.com/your-username/alx-backend-python.git
cd alx-backend-python/messaging_app

# Create production environment file
cp .env.example .env
# Edit .env with production values

# Build and start services
docker-compose -f docker-compose.prod.yml up -d
```

### 3. Nginx Configuration

Create `/etc/nginx/sites-available/messaging-app`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/messaging_app/messaging/staticfiles/;
    }

    location /media/ {
        alias /path/to/messaging_app/messaging/media/;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/messaging-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 4. SSL Certificate (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Docker Deployment

### 1. Build Production Image

```bash
# Build image
docker build -t messaging-app:latest .

# Tag for registry
docker tag messaging-app:latest your-username/messaging-app:latest

# Push to registry
docker push your-username/messaging-app:latest
```

### 2. Production Docker Compose

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - mysql_prod_data:/var/lib/mysql
    restart: unless-stopped

  web:
    image: your-username/messaging-app:latest
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DEBUG=False
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_HOST=db
      - SECRET_KEY=${SECRET_KEY}
      - ALLOWED_HOSTS=${ALLOWED_HOSTS}
    restart: unless-stopped

volumes:
  mysql_prod_data:
```

### 3. Deploy with Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.prod.yml messaging-app

# Check services
docker service ls
```

## CI/CD Pipeline

### 1. GitHub Actions Setup

The repository includes two workflows:
- `.github/workflows/ci.yml` - Testing and quality checks
- `.github/workflows/dep.yml` - Build and deployment

### 2. Required GitHub Secrets

In your GitHub repository, add these secrets:
- `DOCKER_USERNAME` - Your Docker Hub username
- `DOCKER_PASSWORD` - Your Docker Hub password/token

### 3. Jenkins Setup

Follow the `JENKINS_SETUP.md` guide for complete Jenkins configuration.

### 4. Automated Deployment Flow

1. Developer pushes code to `main` branch
2. GitHub Actions runs tests and quality checks
3. If successful, builds and pushes Docker image
4. Jenkins or deployment script pulls new image
5. Rolling update deployed to production

## Monitoring and Maintenance

### 1. Health Checks

```bash
# Check application health
curl http://yourdomain.com/api/

# Check database connection
docker exec messaging-app-db mysql -u root -p -e "SELECT 1"

# Check container status
docker ps
```

### 2. Log Management

```bash
# View application logs
docker logs messaging-app-web

# View database logs
docker logs messaging-app-db

# Real-time logs
docker logs -f messaging-app-web
```

### 3. Backup Strategy

```bash
# Database backup
docker exec messaging-app-db mysqldump -u root -p messaging_app > backup_$(date +%Y%m%d).sql

# Automated backup script
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
docker exec messaging-app-db mysqldump -u root -p${DB_ROOT_PASSWORD} messaging_app > ${BACKUP_DIR}/messaging_app_${DATE}.sql
find ${BACKUP_DIR} -name "messaging_app_*.sql" -mtime +7 -delete
```

### 4. Scaling

```bash
# Scale web service
docker service scale messaging-app_web=3

# Using Docker Compose
docker-compose up -d --scale web=3
```

## Troubleshooting

### Common Issues

#### 1. Database Connection Issues

```bash
# Check database status
docker exec messaging-app-db mysqladmin ping

# Reset database connection
docker restart messaging-app-db messaging-app-web
```

#### 2. Permission Issues

```bash
# Fix file permissions
sudo chown -R www-data:www-data /path/to/messaging_app
sudo chmod -R 755 /path/to/messaging_app
```

#### 3. Memory Issues

```bash
# Check memory usage
docker stats

# Increase memory limits in docker-compose.yml
services:
  web:
    deploy:
      resources:
        limits:
          memory: 1G
```

#### 4. SSL Certificate Issues

```bash
# Renew certificate
sudo certbot renew

# Test certificate
sudo certbot certificates
```

### Performance Optimization

#### 1. Database Optimization

```sql
-- Add database indexes
CREATE INDEX idx_message_timestamp ON chat_message(timestamp);
CREATE INDEX idx_message_sender ON chat_message(sender_id);
CREATE INDEX idx_message_recipient ON chat_message(recipient_id);
```

#### 2. Caching

Add Redis for caching:

```yaml
# Add to docker-compose.yml
redis:
  image: redis:alpine
  restart: unless-stopped
```

#### 3. Load Balancing

```nginx
# Nginx upstream configuration
upstream messaging_app {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}

server {
    location / {
        proxy_pass http://messaging_app;
    }
}
```

## Security Considerations

### 1. Environment Variables

- Never commit secrets to version control
- Use secure secret management systems
- Rotate secrets regularly

### 2. Database Security

```bash
# Secure MySQL installation
sudo mysql_secure_installation

# Create limited user for application
CREATE USER 'app_user'@'%' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON messaging_app.* TO 'app_user'@'%';
```

### 3. Container Security

```dockerfile
# Use non-root user
RUN adduser --disabled-password --gecos '' appuser
USER appuser
```

### 4. Network Security

```bash
# Use Docker networks
docker network create messaging-network

# Firewall rules
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

## Backup and Recovery

### 1. Automated Backups

```bash
#!/bin/bash
# backup.sh
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Database backup
docker exec messaging-app-db mysqldump -u root -p${DB_ROOT_PASSWORD} messaging_app > ${BACKUP_DIR}/db_${DATE}.sql

# Application files backup
tar -czf ${BACKUP_DIR}/app_${DATE}.tar.gz /path/to/messaging_app

# Upload to cloud storage (optional)
aws s3 cp ${BACKUP_DIR}/db_${DATE}.sql s3://your-backup-bucket/
```

### 2. Recovery Procedure

```bash
# Database recovery
docker exec -i messaging-app-db mysql -u root -p${DB_ROOT_PASSWORD} messaging_app < backup.sql

# Application recovery
tar -xzf app_backup.tar.gz -C /
docker-compose restart
```

This deployment guide provides a comprehensive approach to deploying and maintaining the Django messaging application in production environments.
