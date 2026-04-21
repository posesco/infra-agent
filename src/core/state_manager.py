import os
import json

def get_modern_backend_config(bucket_name: str, key: str, region: str = None):
    """Genera configuración de backend S3 con bloqueo nativo.
    Prioriza el argumento 'region', luego la variable de entorno 'AWS_REGION', 
    y finalmente usa 'eu-west-1' como fallback.
    """
    final_region = region or os.getenv("AWS_REGION", "eu-west-1")
    
    return {
        "terraform": {
            "backend": {
                "s3": {
                    "bucket": bucket_name,
                    "key": key,
                    "region": final_region,
                    "use_lockfile": True
                }
            }
        }
    }
