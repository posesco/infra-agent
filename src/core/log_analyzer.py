import re
import logging
from src.utils.logger import get_logger

logger = get_logger("LogAnalyzer")

def analyze_logs(log_file):
    logger.info(f"Analyzing {log_file} for critical errors...")
    error_pattern = re.compile(r"ERROR|CRITICAL|FAIL")
    with open(log_file, "r") as f:
        for line in f:
            if error_pattern.search(line):
                logger.error(f"Critical issue found: {line.strip()}")
                return True
    return False
