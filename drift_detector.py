import subprocess
import logging

def check_drift():
    logging.info("Running drift detection...")
    # Ejecuta terraform plan para detectar cambios no autorizados
    result = subprocess.run(["terraform", "plan", "-detailed-exitcode"], capture_output=True)
    if result.returncode == 2:
        logging.warning("Drift detected! Infrastructure has been manually modified.")
        return True
    return False
