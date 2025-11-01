
from src.main.main import main as main

from common import log

if __name__ == "__main__":
    log.init()
    log.info("__main__ start")
    main()