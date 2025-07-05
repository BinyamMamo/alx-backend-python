# Django Messaging App

A comprehensive Django messaging application demonstrating modern CI/CD practices with Jenkins and GitHub Actions.

## Project Overview

This project showcases:
- Django web application development
- Continuous Integration with Jenkins and GitHub Actions
- Docker containerization
- Automated testing with pytest
- Code quality checks with flake8
- MySQL database integration
- Docker Hub image deployment

## Architecture

```
messaging_app/
├── .github/workflows/      # GitHub Actions CI/CD workflows
│   ├── ci.yml             # Testing and quality checks
│   └── dep.yml            # Docker build and deployment
├── messaging/             # Django project directory
│   ├── messaging/         # Main Django app
│   ├── chat/              # Chat application
│   ├── manage.py          # Django management script
│   └── requirements.txt   # Python dependencies
├── tests/                 # Test files
├── Dockerfile            # Docker image configuration
├── Jenkinsfile           # Jenkins pipeline script
├── docker-compose.yml    # Local development setup
└── README.md             # This file
```

## Features

- Real-time messaging functionality
- User authentication and authorization
- MySQL database backend
- RESTful API endpoints
- Automated testing suite
- Code quality enforcement
- Containerized deployment

## Prerequisites

- Python 3.8+
- Django 4.0+
- MySQL 8.0+
- Docker
- Jenkins (for CI/CD)

## Local Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/alx-backend-python.git
cd alx-backend-python/messaging_app
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r messaging/requirements.txt
```

4. **Set up MySQL database:**
```bash
# Create database
mysql -u root -p
CREATE DATABASE messaging_app;
```

5. **Configure environment variables:**
```bash
export DB_NAME=messaging_app
export DB_USER=your_username
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=3306
```

6. **Run migrations:**
```bash
cd messaging
python manage.py migrate
```

7. **Start development server:**
```bash
python manage.py runserver
```

## Docker Setup

1. **Build the Docker image:**
```bash
docker build -t messaging-app .
```

2. **Run with Docker Compose:**
```bash
docker-compose up -d
```

## Jenkins CI/CD Pipeline

The Jenkins pipeline (`Jenkinsfile`) includes the following stages:

1. **Checkout:** Pull source code from GitHub
2. **Setup:** Install Python dependencies
3. **Test:** Run pytest test suite
4. **Quality Check:** Execute flake8 linting
5. **Build:** Create Docker image
6. **Deploy:** Push to Docker Hub

### Jenkins Setup Instructions

1. **Run Jenkins in Docker:**
```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

2. **Access Jenkins:** Navigate to `http://localhost:8080`

3. **Install required plugins:**
   - Git Plugin
   - Pipeline Plugin
   - ShiningPanda Plugin (for Python)

4. **Configure credentials for GitHub and Docker Hub**

5. **Create new Pipeline job pointing to this repository**

## GitHub Actions Workflows

### CI Workflow (`.github/workflows/ci.yml`)
- Runs on every push and pull request
- Sets up Python environment
- Installs dependencies
- Runs Django tests with MySQL
- Performs flake8 code quality checks
- Generates coverage reports

### Deployment Workflow (`.github/workflows/dep.yml`)
- Builds Docker image
- Pushes to Docker Hub
- Uses GitHub Secrets for secure credential management

## Testing

Run the test suite locally:

```bash
cd messaging
python -m pytest
```

Run with coverage:

```bash
python -m pytest --cov=. --cov-report=html
```

## Code Quality

Check code quality with flake8:

```bash
flake8 messaging/
```

## Environment Variables

Required environment variables:

```bash
# Database Configuration
DB_NAME=messaging_app
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

# Django Settings
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1

# Docker Hub (for deployment)
DOCKER_USERNAME=your_docker_username
DOCKER_PASSWORD=your_docker_password
```

## API Endpoints

- `GET /api/messages/` - List all messages
- `POST /api/messages/` - Create new message
- `GET /api/messages/<id>/` - Get specific message
- `PUT /api/messages/<id>/` - Update message
- `DELETE /api/messages/<id>/` - Delete message

## Monitoring and Logs

- Jenkins build logs: Available in Jenkins dashboard
- GitHub Actions logs: Available in repository Actions tab
- Application logs: Check Docker container logs

## Troubleshooting

### Common Issues

1. **Database Connection Error:**
   - Verify MySQL is running
   - Check database credentials
   - Ensure database exists

2. **Jenkins Pipeline Failure:**
   - Check Jenkins logs
   - Verify GitHub credentials
   - Ensure required plugins are installed

3. **Docker Build Issues:**
   - Check Dockerfile syntax
   - Verify base image availability
   - Check network connectivity

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Make changes and add tests
4. Run quality checks (`flake8` and `pytest`)
5. Commit changes (`git commit -am 'Add new feature'`)
6. Push to branch (`git push origin feature/new-feature`)
7. Create Pull Request

## License

This project is part of the ALX Software Engineering program.

## Support

For questions and support, please open an issue in the GitHub repository.
