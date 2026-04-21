import os
import json
import logging
import google.generativeai as genai
from src.utils.logger import get_logger

logger = get_logger("SRE-Gen")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class SREGenAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.output_file = "main.tf.json"

    def interact(self, prompt: str):
        logger.info("Generating infrastructure via Gemini...")
        response = self.model.generate_content(
            f"Generate a terraform main.tf.json for: {prompt}. "
            "Use industry standards (AWS, cost-aware t4g, multi-az). "
            "Return ONLY JSON."
        )
        
        # Extraer JSON de la respuesta (limpieza básica)
        clean_json = response.text.replace("", "").strip()
        config = json.loads(clean_json)
        
        with open(self.output_file, "w") as f:
            json.dump(config, f, indent=2)
        logger.info(f"Configuration generated: {self.output_file}")

if __name__ == "__main__":
    agent = SREGenAgent()
    # Ejemplo de uso
    agent.interact("Production web server in AWS")
