# 🚀 Docker CI/CD Pipeline using Flask + GitHub Actions + Docker Hub + AWS EC2
# 📌 Project Overview

This project demonstrates a complete Docker-based CI/CD pipeline for a Flask web application using GitHub Actions, Docker Hub, and AWS EC2.

The pipeline automates:
- Testing
- Code quality checks
- Docker image build
- Docker image push
- Deployment to AWS EC2

The main objective of this project is to understand how modern DevOps pipelines automate containerized application deployment using Docker and cloud infrastructure.

# 🛠️ Tools & Technologies Used

- GitHub
- GitHub Actions
- Flask
- Docker
- Docker Hub
- AWS EC2

# 🏗️ CI/CD Pipeline Architecture

```text
Developer Pushes Code
        ↓
GitHub Repository
        ↓
GitHub Actions Triggered
        ↓
Install Dependencies
        ↓
Run Pylint
        ↓
Run Pytest
        ↓
Build Docker Image
        ↓
Push Image to Docker Hub
        ↓
SSH into AWS EC2
        ↓
Pull Latest Docker Image
        ↓
Restart Docker Container
        ↓
Application Running on EC2
```

# ⚙️ Pipeline Stages Implemented

## 1. Dependency Installation

Installed Python dependencies using:
pip install -r requirements.txt

## 2. Code Quality Check

Performed static code analysis using `pylint`.

## 3. Testing Stage

Executed automated application tests using `pytest`.

## 4. Docker Image Build

Built Docker image using Dockerfile.

## 5. Docker Hub Integration

Pushed Docker image securely to Docker Hub repository.

## 6. AWS EC2 Deployment

Connected to EC2 instance securely using SSH and deployed latest Docker container.

## 7. Container Management

Stopped old container and started updated application container automatically.

# 🔧 What I Implemented

- Created Flask web application
- Created Dockerfile for containerization
- Configured Docker image build process
- Configured Docker Hub integration
- Created AWS EC2 instance
- Installed Docker on EC2
- Configured secure SSH deployment
- Added GitHub Secrets securely
- Created GitHub Actions workflow
- Implemented automatic Docker deployment pipeline

# ▶️ Steps to Run Project

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd github-actions/docker-cicd-project
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Flask Application

```bash
python3 app.py
```

---

## 4. Build Docker Image

```bash
docker build -t flask-cicd-app:v1 .
```

---

## 5. Run Docker Container

```bash
docker run -d -p 5001:5000 flask-cicd-app:v1
```

Application runs on:

```text
http://localhost:5001
```

---

## 6. Push Code to GitHub

```bash
git add .
git commit -m "Initial Docker CI/CD project"
git push
```

GitHub Actions pipeline starts automatically after push.

# ⚠️ Errors Faced & Fixes
1.Pylint Errors
Fix:Added proper docstrings

2.Pytest Indentation Error
Fix:Corrected indentation inside test_app.py

3.GitHub Actions SSH Authentication Failed
Error:ssh.ParsePrivateKey: ssh: no key found
Fix:Correctly added deployment private key to EC2_SSH_KEY

# 🔑 Key Learnings

# Key Learnings from the Project

* Automated Docker image build, push, and deployment workflow
* Understood Docker Hub integration with CI/CD
* Learned secure EC2 SSH authentication practices
* Understood GitHub Secrets management
* Learned automated deployment to AWS EC2
* Understood workflow triggers and path-based execution
* Gained hands-on experience with cloud deployment and containerization
* Improved debugging and troubleshooting of CI/CD pipelines
  
# 🚀 Final Outcome

- This project helped me understand how Docker, GitHub Actions, Docker Hub, and AWS EC2 work together in a CI/CD pipeline.
- It also improved my understanding of automated container deployment, cloud-based application hosting, and DevOps automation.
````

