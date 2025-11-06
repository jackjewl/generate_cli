
from common import log
def init_app(cfg):
    log.info("init_app.init_app finished")
    log.info("this is config setting")
    log.init(cfg)
