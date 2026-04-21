# SRE-Gen: Intelligent Infrastructure Architect

SRE-Gen is an autonomous AI-driven Infrastructure-as-Code (IaC) architect designed to generate production-ready, cost-optimized, and secure Terraform configurations.

## Core Features
- **Intelligent IaC Generation:** Generates `main.tf.json` based on industry best practices (Google/AWS Well-Architected).
- **Cost-Aware:** Automatically optimizes instances (e.g., migrating x86 to Graviton/ARM).
- **Security Validation:** Integrated security scanning with Checkov.
- **Modern State Management:** Native S3 locking support (OpenTofu/Terraform compatible).
- **Enterprise-Ready:** CI/CD pipeline integration, automated documentation, and robust logging.

## Getting Started

### Prerequisites
- Python 3.10+
- Terraform/OpenTofu CLI
- Checkov installed (`pip install checkov`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/posesco/infra-agent.git
   cd infra-agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the interactive agent:
```bash
python3 src/core/main.py
```

## Development
- **Run Tests:** `make test`
- **Lint Code:** `make lint`
- **Generate Docs:** `make docs`

---
*Built by Jesús Posada - SRE Specialist*
