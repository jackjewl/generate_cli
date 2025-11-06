from pathlib import Path

from src.main.main import main as main

from common import log, profile

if __name__ == "__main__":
    log.init()
    log.info("__main__ start")
    profile.profile("profile", main, visual_profile=True, print_stats=False)
