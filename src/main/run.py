
from common import log

import src.cron as cron

def run(cfg):
    log.info("run.run")

    cron.init(cfg)
    cron.run(cfg)


