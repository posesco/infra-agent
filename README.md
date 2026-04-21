# SRE-Gen v0.2.0 | Autonomous Infrastructure Architect 🚀

SRE-Gen is an autonomous AI-driven Infrastructure-as-Code (IaC) architect that leverages **Gemini AI** to generate production-ready, cost-optimized, and secure Terraform configurations.

[![Deploy static content to Pages](https://github.com/posesco/infra-agent/actions/workflows/deploy-pages.yml/badge.svg?branch=develop)](https://github.com/posesco/infra-agent/actions/workflows/deploy-pages.yml)

## 🌟 Core Features
- **Intelligent IaC Generation:** Generates `main.tf.json` based on AWS/Google Well-Architected frameworks.
- **Security Hardening:** Native protection against Prompt Injection and automated `terraform validate` checks.
- **Cost Optimization:** Automatic instance migration (x86 to ARM/t4g) for up to 20% cost reduction.
- **Modern State Management:** Native S3 locking support (OpenTofu compatible).
- **Dynamic Configuration:** Fully configurable via environment variables (Model, Region, etc.).
- **Professional UI:** Includes a high-tech minimalist web interface for project showcase.

## 🛠️ Tech Stack
- **AI Engine:** Google Gemini (Configurable via `GEMINI_MODEL`).
- **Language:** Python 3.11+.
- **IaC:** Terraform / OpenTofu.
- **Security:** Checkov integration & Prompt Shielding.
- **Infrastructure:** Docker (Multi-stage, No-root).

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Terraform/OpenTofu CLI
- Google Gemini API Key

### Installation
1. **Clone & Setup:**
   ```bash
   git clone https://github.com/posesco/infra-agent.git
   cd infra-agent
   cp .env.example .env
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the intelligent agent:
```bash
# Set your GOOGLE_API_KEY in .env first
python3 src/core/main.py
```

## 🐳 Docker Deployment
```bash
docker build -t sre-gen .
docker run --env-file .env sre-gen
```

## 📈 Development & Quality
- **Test Suite:** `make test`
- **Static Analysis:** `make lint`
- **Security Audit:** `checkov -d .`
- **Version Management:** `make version-[patch|minor|major]`

---
*Developed by **Jesús Posada** - SRE Specialist & Cloud Architect*
