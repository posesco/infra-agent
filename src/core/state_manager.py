import json

def get_modern_backend_config(bucket_name: str, key: str):
    """Genera configuración de backend S3 con bloqueo nativo (S3 native locking)."""
    return {
        "terraform": {
            "backend": {
                "s3": {
                    "bucket": bucket_name,
                    "key": key,
                    "region": "eu-west-1",
                    "use_lockfile": True  # Característica moderna de OpenTofu/Terraform
                }
            }
        }
    }
