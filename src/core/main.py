import os
import json
import logging
from dotenv import load_dotenv
import google.generativeai as genai
from src.utils.logger import get_logger
from src.core.log_analyzer import analyze_logs
from src.utils.gh_integration import create_auto_healing_pr

load_dotenv()
logger = get_logger("SRE-Gen")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class SREGenAgent:
    def __init__(self):
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.model = genai.GenerativeModel(self.model_name)
        self.output_file = "main.tf.json"
        logger.info(f"Agent initialized: {self.model_name}")

    def interact(self, user_input: str):
        logger.info("Generating infrastructure...")
        system_instruction = (
            "You are a Senior SRE Architect. Generate valid Terraform JSON (main.tf.json). "
            "Standards: AWS, cost-aware (t4g/ARM), multi-AZ, encryption at rest. "
            "Return ONLY raw JSON."
        )
        response = self.model.generate_content(
            f"{system_instruction}\n\nUSER: {user_input}",
            generation_config=genai.types.GenerationConfig(response_mime_type="application/json")
        )
        
        try:
            config = json.loads(response.text.strip())
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}\nRaw output: {response.text}")
            return
            
        with open(self.output_file, "w") as f:
            json.dump(config, f, indent=2)
        logger.info("Infra generated.")

    def heal(self, log_file):
        if analyze_logs(log_file):
            logger.warning("Auto-healing triggered.")
            create_auto_healing_pr(f"feat/fix-{log_file}", "fix: auto-remediation")

if __name__ == "__main__":
    agent = SREGenAgent()
    agent.interact("Production web server in AWS")