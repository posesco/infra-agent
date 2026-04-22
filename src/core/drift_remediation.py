import subprocess
import logging
from src.core.main import SREGenAgent

logger = logging.getLogger("DriftRemediator")

def remediate():
    logger.info("Drift detected. Initiating remediation flow...")
    agent = SREGenAgent()
    # Re-generar infraestructura basada en el estado deseado original
    agent.interact("Re-apply last known production architecture state")
    subprocess.run(["terraform", "apply", "-auto-approve"])
    logger.info("Remediation complete.")
