import time

from FA.JEngines.JarticleEnhancer import RUN

THREE_HOURS = 10800

if __name__ == '__main__':
    while True:
        print(f"Running Jarticle Enhancements...")
        RUN(saveToDB=True)
        print(f"Sleeping for {THREE_HOURS} seconds...")
        time.sleep(THREE_HOURS)