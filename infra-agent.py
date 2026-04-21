import os
import json
from typing import Dict

def generate_terraform(requirements: str) -> Dict:
    tf_content = {
        "provider": {"aws": {"region": "eu-west-1"}},
        "resource": {
            "aws_instance": {
                "web": {
                    "ami": "ami-0c55b159cbfafe1f0",
                    "instance_type": "t3.micro",
                    "tags": {"Name": "SRE-Gen-Instance"}
                }
            }
        }
    }
    return tf_content

if __name__ == "__main__":
    reqs = "Deploy a simple web server"
    config = generate_terraform(reqs)
    with open("main.tf.json", "w") as f:
        json.dump(config, f, indent=2)
