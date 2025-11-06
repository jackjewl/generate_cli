
from pathlib import Path
from . import init_app
from . import init
from . import run
from common import log


#当前工作路径
cwd=Path.cwd()

def main():
    log.info("main.main")
    cfg = init.init("./settings/settings.yaml")
    init_app.init_app(cfg)
    run.run(cfg)