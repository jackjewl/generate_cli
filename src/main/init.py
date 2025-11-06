from common import log
import yaml

def init(file_path:str):
    log.info("init.init")

    with open(file_path, 'r') as f:
        cfg = yaml.safe_load(f)
        return cfg