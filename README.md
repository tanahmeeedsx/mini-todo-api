# 🚀 Mini Todo API

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="180"/>
</p>

<p align="center">
  <strong>A hands-on FastAPI project for practicing Git, CI/CD, security, Linux, and AWS EC2 deployment.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS EC2"/>
  <img src="https://img.shields.io/badge/Linux-Server-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
</p>

---

## 📌 About the Project

**Mini Todo API** is a deliberately small **Python FastAPI application** created primarily as a practical DevOps learning environment.

The application itself is intentionally simple. The main objective was to understand how an application moves from **source code to a live server** while practicing real-world development and DevOps workflows.

This project covers:

* Git & GitHub workflows
* Branching and Pull Requests
* Merge conflicts and Git history
* GitHub Actions
* Continuous Integration
* Automated testing
* Dependency and security checks
* Secure secrets handling
* Linux server administration
* AWS EC2
* `systemd` service management
* Application deployment
* Live API verification

---

## 🔄 Git-to-Deployment Workflow

```mermaid
flowchart LR
    A[💻 Local Development] --> B[Git]
    B --> C[GitHub]
    C --> D[Pull Request]
    D --> E[GitHub Actions]
    E --> F[🧪 Automated Testing]
    F --> G[🔐 Security Checks]
    G --> H[✅ CI]
    H --> I[☁️ AWS EC2]
    I --> J[🐧 Linux Server]
    J --> K[⚙️ systemd]
    K --> L[🚀 Live FastAPI API]
```

### Workflow in simple terms

```text
Code
 ↓
Git
 ↓
GitHub
 ↓
Pull Request
 ↓
GitHub Actions
 ↓
Testing & Security Checks
 ↓
Continuous Integration
 ↓
AWS EC2
 ↓
Linux + systemd
 ↓
Live API
```

---

## 🛠️ Technologies & Tools

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| 🐍 **Python**         | Application development        |
| ⚡ **FastAPI**         | REST API framework             |
| 🔧 **Git**            | Version control                |
| 🐙 **GitHub**         | Source code & collaboration    |
| ⚙️ **GitHub Actions** | CI automation                  |
| 🧪 **Pytest**         | Automated testing              |
| ☁️ **AWS EC2**        | Cloud infrastructure           |
| 🐧 **Linux**          | Server environment             |
| ⚙️ **systemd**        | Application service management |
| 🔗 **REST API**       | Application communication      |

---

## 📂 Project Structure

```text
mini-todo-api/
│
├── .github/
│   └── workflows/
│       └── ...
│
├── app/
│   └── main.py
│
├── tests/
│   └── ...
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧩 What I Practiced

### 1. Git & GitHub

Practiced the complete Git workflow, including:

* Feature branches
* Branch merging
* Pull Requests
* Merge conflicts
* Commit history
* Reset
* Revert
* Squash
* Cherry-pick
* Stash
* GitHub repository management

---

### 2. CI with GitHub Actions

Implemented **Continuous Integration** using GitHub Actions.

The CI workflow automatically performs validation when changes are pushed or submitted through Pull Requests.

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Install Dependencies
        ↓
Run Tests
        ↓
Security / Dependency Checks
        ↓
CI Result
```

I also intentionally worked through failed CI runs to understand how pipeline failures can be investigated, debugged, and fixed.

---

### 3. Testing & Security

Practiced:

* Automated testing with `pytest`
* Dependency management
* Dependency/security checks
* Secure secrets handling
* Dependabot
* CODEOWNERS
* CI validation

---

### 4. AWS EC2 & Linux

Deployed the application to an **AWS EC2 Linux server**.

Practiced:

* EC2 instance configuration
* SSH access
* Linux administration
* Python environment setup
* Application process management
* Port configuration
* Troubleshooting
* Server-side application verification

---

### 5. systemd & Deployment

Configured the FastAPI application as a Linux **systemd service**.

This allowed the application to run as a managed background service rather than depending on an active SSH session.

The deployment was then verified through live API endpoints.

---

# 🖼️ Project Screenshots

## GitHub Repository

<p align="center">
  <img src="docs/images/github-repository.png" alt="GitHub Repository" width="900"/>
</p>

---

## GitHub Actions — CI Pipeline

<p align="center">
  <img src="docs/images/github-actions.png" alt="GitHub Actions CI Pipeline" width="900"/>
</p>

---

## AWS EC2 — Linux Server

<p align="center">
  <img src="docs/images/aws-ec2.png" alt="AWS EC2 Linux Server" width="900"/>
</p>

---

## 🚀 Live FastAPI Deployment

<p align="center">
  <img src="docs/images/live-deployment.png" alt="Live FastAPI Deployment" width="900"/>
</p>

---

# 💻 Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/tanahmeeedsx/mini-todo-api.git
cd mini-todo-api
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Start the application

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running, open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger UI to explore and test the API endpoints directly from your browser.

OpenAPI specification:

```text
http://127.0.0.1:8000/openapi.json
```

---

# 🧪 Run Tests

Run the automated test suite:

```bash
pytest
```

The same type of automated validation is also performed through the CI workflow.

---

# ☁️ AWS EC2 Deployment

The application was deployed to an AWS EC2 Linux server as part of the DevOps practice workflow.

### Deployment process

```text
AWS EC2
   ↓
SSH Access
   ↓
Linux Environment
   ↓
Python Virtual Environment
   ↓
Application Dependencies
   ↓
FastAPI + Uvicorn
   ↓
systemd Service
   ↓
Live API
```

The application was verified after deployment through API endpoints.

---

# ⚙️ systemd Service

The FastAPI application is managed using `systemd`.

This provides:

* Background service execution
* Automatic service management
* Restart capability
* Service status monitoring
* Independence from an active SSH session

Useful commands:

```bash
sudo systemctl status mini-todo-api
```

```bash
sudo systemctl restart mini-todo-api
```

```bash
sudo systemctl stop mini-todo-api
```

```bash
sudo systemctl start mini-todo-api
```

---

# 🎯 Learning Objectives

The main purpose of this project was to gain practical experience with:

* Git workflows
* GitHub collaboration
* Pull Requests
* Branch management
* CI/CD concepts
* GitHub Actions
* Automated testing
* Security practices
* Secrets management
* Linux administration
* AWS EC2
* systemd
* REST APIs
* Cloud deployment
* CI/CD troubleshooting

---

# 💡 Key Takeaway

The main lesson from this project was understanding that **DevOps is not simply about deploying an application**.

It is about connecting different stages of the software lifecycle:

```text
Development
    ↓
Version Control
    ↓
Collaboration
    ↓
Testing
    ↓
Security
    ↓
Continuous Integration
    ↓
Infrastructure
    ↓
Deployment
    ↓
Verification
```

This small FastAPI application provided a practical environment for understanding how these components work together in an industry-style workflow.

---

# 🗺️ Future Improvements

Possible future improvements include:

* [ ] Add database integration
* [ ] Add authentication and authorization
* [ ] Add Docker containerization
* [ ] Build a dedicated CD pipeline
* [ ] Provision infrastructure with Terraform
* [ ] Add Nginx reverse proxy
* [ ] Configure HTTPS / SSL
* [ ] Add application monitoring
* [ ] Add centralized logging
* [ ] Increase test coverage

---

# 📊 Project Status

**Status:** ✅ Completed

The project successfully demonstrates a practical **Git-to-Deployment workflow** using GitHub, GitHub Actions, Linux, AWS EC2, systemd, and FastAPI.

---

# 🔗 Repository

<p align="center">

<a href="https://github.com/tanahmeeedsx/mini-todo-api">
<img src="https://img.shields.io/badge/GitHub-Mini%20Todo%20API-181717?style=for-the-badge&logo=github" alt="GitHub Repository"/>
</a>

</p>

---

# 👨‍💻 Author

**Tanjim Ahmed**

DevOps / Cloud & Infrastructure Enthusiast

<p align="center">
  <a href="https://github.com/tanahmeeedsx">
    <img src="https://img.shields.io/badge/GitHub-tanahmeeedsx-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/tanahmedd/">
    <img src="https://img.shields.io/badge/LinkedIn-Tanjim%20Ahmed-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
  </a>
</p>
