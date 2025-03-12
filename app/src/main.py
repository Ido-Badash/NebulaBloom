import sys
import logging
from nbloom_app import NBloomApp

def catch_it(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            sys.exit(1)
    return wrapper

@catch_it
def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    
    logging.info("Program started")

    nbloom_app = NBloomApp()
    nbloom_app.run()

    logging.info("Program ended")
    sys.exit(0)

if __name__ == "__main__":
    main()