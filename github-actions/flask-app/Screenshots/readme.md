🚀 GitHub Actions CI/CD Pipeline using Flask + Self-Hosted Runner

📌 Project Overview

This project demonstrates a CI/CD pipeline for a Flask application using GitHub Actions and a Self-Hosted Runner.
The pipeline automates:
- testing
- linting
- deployment
- service management
  
📚 Core Concepts Learned

- GitHub Actions:GitHub Actions is a CI/CD automation platform inside GitHub.
  
  It automatically runs workflows when code is pushed to the repository.
 
  Workflows help automate testing, validation, and deployment.

- Workflow:A workflow is an automated process defined inside YAML files.

   Workflow files are stored inside .github/workflows/
  
   GitHub automatically detects workflows from this folder.
  
   GitHub Actions workflows run automatically based on events.
  
- Examples:
  - push
  - pull_request
  - release
  - schedule
  - YAML Workflow File

- Jobs:Jobs are separate sections inside a workflow.
  
  Each job performs a specific task.

  **Example:
    - test job
    - deploy job

  Jobs can run independently or depend on other jobs.

- Steps:Steps are individual commands executed inside a job.

- Runner is the machine that executes GitHub Actions workflows.
  
  -Types:
     - GitHub-hosted runner
     - Self-hosted runner
   
**In this project:

- Ubuntu/Linux machine acts as self-hosted runner.
- Self-Hosted Runner:A self-hosted runner is your own machine connected to GitHub Actions.
- It allows:
 -local deployments
 -custom software installation
 -better environment control

- systemd:systemd is a Linux service manager.
It keeps applications running as background services.

Benefits:
 - automatic restart
 - survives reboot
 - centralized logs
 - stable process management

**🛠️ Tools & Technologies Used
- GitHub
- GitHUb Actions
- Flask
- Pylint 
- Pytest
- Systemd 

🏗️ CI/CD Pipeline Architecture
Developer Pushes Code
        ↓
GitHub Repository
        ↓
GitHub Actions Triggered
        ↓
Test Job (GitHub Hosted Runner)
        ↓
Install Dependencies
        ↓
Run Pylint
        ↓
Run Pytest
        ↓
Deploy Job (Self-Hosted Runner)
        ↓
Restart Flask Service
        ↓
Application Running

⚙️ Pipeline Stages Implemented
1. Dependency Installation
Installed project dependencies using pip install -r requirements.txt
2. Code Quality Check
Performed code analysis using pylint
3. Testing Stage
Executed application tests using pytest
4. Deployment Stage
Automatically deployed Flask application on self-hosted runner
5. Service Management
Managed Flask application using systemd
Ensured application survives reboot and workflow completion

🔧 What I Implemented
- Created Flask web application
- Configured GitHub repository
- Created GitHub Actions workflow
- Configured Self-Hosted Runner
- Added automated testing and linting
- Configured Linux systemd service
- Implemented automatic deployment pipeline
- Configured deployment verification commands

⚠️ Errors Faced & Fixes
1.Working directory issue	
- fix:Added defaults.run.working-directory
2.Pylint warnings	
- fix:Added proper docstrings and formatting
3.Flask app stopped after deploy	
- fix:Configured systemd service
4.Process killed after workflow	
- fix:Used systemd instead of nohup

🔑 Key Learnings
- Learned GitHub Actions workflow structure
- Understood CI/CD automation process
- Learned Self-Hosted Runner setup
- Learned YAML workflow configuration
- Understood Linux service management using systemd
- Improved understanding of deployment automation

🚀 Final Outcome
- This project helped me understand how GitHub Actions automates testing, code quality checks, deployment, and service management in a CI/CD pipeline.
- It also improved my understanding of DevOps automation, faster deployments, reliability, and better software quality.
