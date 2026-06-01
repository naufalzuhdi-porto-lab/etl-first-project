import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

config_path = BASE_DIR / "config" /"config.yaml"

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)
print(config)