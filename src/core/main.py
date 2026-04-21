import json
import logging
from typing import Dict

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SREGenAgent:
    def __init__(self):
        self.output_file = "main.tf.json"

    def interact(self):
        print("--- SRE-Gen Interactive Mode ---")
        cloud = input("Preferred Cloud (AWS/GCP): ")
        service = input("Service Name: ")
        budget = input("Budget Sensitive? (y/n): ")
        
        config = {
            "provider": {cloud.lower(): {"region": "eu-west-1"}},
            "resource": {
                f"{cloud.lower()}_instance": {
                    "app": {
                        "name": service,
                        "type": "t3.small" if budget.lower() == 'y' else "t3.medium"
                    }
                }
            }
        }
        
        with open(self.output_file, "w") as f:
            json.dump(config, f, indent=2)
        print(f"Configuration generated: {self.output_file}")

if __name__ == "__main__":
    agent = SREGenAgent()
    agent.interact()
