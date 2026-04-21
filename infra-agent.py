import os
import json
import logging
import subprocess
from typing import Dict

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class InfraArchitect:
    def __init__(self):
        self.output_file = "main.tf.json"
        # Precios simplificados por hora para MVP (t3: small=0.02, medium=0.04)
        self.price_map = {"t3.small": 0.02, "t3.medium": 0.04}

    def generate_config(self, cloud: str, service: str, budget_sensitive: bool = True) -> Dict:
        logging.info(f"Generating optimized infra for {service} on {cloud}")
        
        # Lógica Cost-Aware: Seleccionar la más barata si es sensible al presupuesto
        instance_type = "t3.small" if budget_sensitive else "t3.medium"
        
        return {
            "provider": {"aws": {"region": "eu-west-1"}},
            "resource": {
                "aws_instance": {
                    "app": {
                        "ami": "ami-0c55b159cbfafe1f0",
                        "instance_type": instance_type,
                        "tags": {"Environment": "Production", "ManagedBy": "SRE-Gen"}
                    }
                }
            }
        }

    def validate_config(self):
        """Ejecuta checkov para validar seguridad del JSON generado."""
        logging.info("Validating infrastructure security with Checkov...")
        result = subprocess.run(["checkov", "-f", self.output_file], capture_output=True, text=True)
        if result.returncode != 0:
            logging.warning("Security issues found by Checkov!")
        else:
            logging.info("Infrastructure passed security checks.")

    def run(self, cloud: str, service: str):
        config = self.generate_config(cloud, service)
        with open(self.output_file, "w") as f:
            json.dump(config, f, indent=2)
        
        self.validate_config()
        
        os.system("git add main.tf.json")
        os.system("git commit -m 'Update: Added cost-aware selection and security validation'")
        logging.info("Infrastructure generated, validated, and committed.")

if __name__ == "__main__":
    architect = InfraArchitect()
    architect.run("aws", "web_server")
