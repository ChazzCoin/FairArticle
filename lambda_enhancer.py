import time

import schedule
from FA.JEngines.JarticleEnhancer import RUN

def start():
    RUN(saveToDB=True)

# schedule.every().hour.do(start)
if __name__ == '__main__':
    while True:
        start()
        time.sleep(7200)