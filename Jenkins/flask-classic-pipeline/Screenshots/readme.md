# 🚀 Flask CI/CD Pipeline using Jenkins

## 📌 Project Overview
This project demonstrates a complete CI/CD pipeline implementation for a Python Flask application using Jenkins.
The pipeline automates:
* Application build process
* Dependency installation
* Unit testing
* Static code analysis
* Security scanning
* Deployment
The goal of this project is to understand how modern DevOps pipelines automate software delivery and improve deployment reliability.

# 🛠️ Tools & Technologies Used

- Jenkins
- Github
- pytest
- pylint
- bandit

## CI/CD Pipeline Architecture

Developer Pushes Code
↓
GitHub Repository
↓
Jenkins Pipeline Triggered
↓
Build Stage
↓
Testing Stage
↓
Code Analysis Stage
↓
Security Scan Stage
↓
Deployment Stage
↓
Flask Application Running

# ⚙️ Pipeline Stages Implemented

## 1. Build Stage

* Created Python virtual environment
* Installed dependencies using `requirements.txt`

## 2. Test Stage

* Executed unit tests using `pytest`

## 3. Code Analysis Stage

* Performed static code analysis using `pylint`

## 4. Security Scan Stage

* Performed vulnerability scanning using `bandit`

## 5. Deployment Stage

* Deployed Flask application automatically

## What I Implemented
- Created Flask web application
- Configured GitHub repository
- Installed and configured Jenkins
- Created Jenkins pipeline job
- Implemented Jenkinsfile pipeline
- Automated testing process
- Integrated static code analysis
- Integrated security scanning
- Automated Flask application deployment
- Connected Jenkins with GitHub repository

##⚠️ Errors Faced & Fixes

## Jenkinsfile Not Found
✔ Fixed incorrect Jenkinsfile path configuration inside Jenkins pipeline.

## requirements.txt File Not Found
✔ Fixed pipeline working directory using correct `dir()` path.

## Pipeline Stages Skipped
✔ Resolved earlier stage failures to allow complete pipeline execution.

## ✅ Validation

- Jenkins pipeline executed successfully
- Dependencies installed successfully
- Unit tests passed successfully
- pylint analysis executed successfully
- Security scan executed successfully
- Flask application deployed successfully

## 🔑 Key Learnings

- Understood complete CI/CD workflow
- Learned Jenkins pipeline automation
- Learned GitHub and Jenkins integration
- Learned automated testing and deployment
- Understood static code analysis and security scanning
- Improved understanding of DevOps pipeline architecture

# 🚀 Final Outcome

CI/CD and Jenkins gave me practical understanding of how modern applications are automatically tested, validated, and deployed.
Main advantages I learned:
- Automation
- Faster releases
- Reliability
- Scalability
- Better software quality
- Continuous delivery process
