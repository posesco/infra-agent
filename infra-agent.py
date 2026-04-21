import os
import json
import logging
from typing import Dict

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class InfraArchitect:
    def __init__(self):
        self.output_file = "main.tf.json"

    def generate_config(self, cloud: str, service: str) -> Dict:
        """Genera configuración de infraestructura según nube y servicio."""
        logging.info(f"Generating infra for {service} on {cloud}")
        
        # Mapeo simple de configuraciones productivas
        configs = {
            "aws": {
                "provider": {"aws": {"region": "eu-west-1"}},
                "resource": {
                    "aws_instance": {
                        "app": {
                            "ami": "ami-0c55b159cbfafe1f0",
                            "instance_type": "t3.small",
                            "tags": {"Environment": "Production", "ManagedBy": "SRE-Gen"}
                        }
                    }
                }
            }
        }
        return configs.get(cloud.lower(), {})

    def save_and_commit(self, config: Dict):
        with open(self.output_file, "w") as f:
            json.dump(config, f, indent=2)
        
        os.system("git add main.tf.json")
        os.system("git commit -m 'Update infrastructure configuration'")
        logging.info("Infrastructure updated and committed.")

if __name__ == "__main__":
    architect = InfraArchitect()
    # Simulación de interacción con cliente
    config = architect.generate_config("aws", "web_server")
    architect.save_and_commit(config)
