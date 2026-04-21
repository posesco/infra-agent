import os
import json
import logging
from dotenv import load_dotenv
import google.generativeai as genai
from src.utils.logger import get_logger

# Cargar configuración desde .env si existe
load_dotenv()

logger = get_logger("SRE-Gen")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class SREGenAgent:
    def __init__(self):
        # El modelo ahora es configurable via variable de entorno
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self.model = genai.GenerativeModel(self.model_name)
        self.output_file = "main.tf.json"
        logger.info(f"Agent initialized using model: {self.model_name}")

    def interact(self, user_input: str):
        logger.info("Generating infrastructure via Gemini...")
        
        # Mitigación de Prompt Injection usando delimitadores y estructura clara
        system_instruction = (
            "You are a specialized SRE Infrastructure Architect. "
            "Generate a valid Terraform configuration in JSON format (main.tf.json). "
            "Standards: AWS, cost-aware (t4g/ARM), multi-AZ, encryption at rest. "
            "CRITICAL: Return ONLY raw JSON. No markdown blocks, no explanations."
        )
        
        prompt = (
            f"{system_instruction}\n\n"
            f"USER_REQUEST: <<<{user_input}>>>\n"
        )
        
        try:
            response = self.model.generate_content(prompt)
            # Extraer JSON eliminando bloques de código markdown si existen
            clean_json = response.text.replace("```json", "").replace("```", "").strip()
            config = json.loads(clean_json)
            
            with open(self.output_file, "w") as f:
                json.dump(config, f, indent=2)
            
            logger.info(f"Configuration written to {self.output_file}. Validating...")
            self._validate_config()
            
        except json.JSONDecodeError:
            logger.error("Failed to parse Gemini response as JSON. Check model output.")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")

    def _validate_config(self):
        """Valida la configuración generada usando terraform validate."""
        import subprocess
        try:
            # Terraform requiere un init previo para validar backends/providers, 
            # pero para sintaxis básica json este check es útil.
            result = subprocess.run(
                ["terraform", "validate", "-json"], 
                capture_output=True, 
                text=True
            )
            if result.returncode != 0:
                logger.warning(f"Validation failed: {result.stderr}")
            else:
                logger.info("Infrastructure validation successful.")
        except FileNotFoundError:
            logger.error("Terraform CLI not found. Skipping automated validation.")

if __name__ == "__main__":
    agent = SREGenAgent()
    # Ejemplo de uso
    agent.interact("Production web server in AWS")
