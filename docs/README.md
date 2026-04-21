# SRE-Gen: Intelligent Infrastructure Architect

SRE-Gen is an autonomous AI-driven Infrastructure-as-Code (IaC) architect designed to generate production-ready, cost-optimized Terraform configurations based on natural language requirements.

## Features
- **Prompt-to-IaC:** Translates user requirements into structured `main.tf.json`.
- **Cost-Aware:** Default selection of efficient instance types (e.g., T3/T4g).
- **Git-Integrated:** Automatically tracks all infrastructure changes.
- **Production-Ready:** Generates modular and scalable Terraform output.

## Getting Started
1. Run `python3 infra-agent.py`.
2. Review the generated `main.tf.json`.
3. Plan and apply via Terraform.

## Roadmap
- [ ] Multi-cloud support (AWS, GCP, Azure).
- [ ] Cost-estimation module integration.
- [ ] Interactive requirement gathering agent.
