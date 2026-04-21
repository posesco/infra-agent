import json

def optimize_terraform_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Lógica de optimización: forzar uso de tipos de instancia más eficientes (ARM-based)
    for res_type, resources in data.get("resource", {}).items():
        if "instance" in res_type:
            for _, config in resources.items():
                if "t3" in config.get("instance_type", ""):
                    config["instance_type"] = config["instance_type"].replace("t3", "t4g")
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    optimize_terraform_json("main.tf.json")
