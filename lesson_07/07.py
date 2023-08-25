import time
import logging


class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        processing_time = end_time - self.start_time
        logging.info(f"Processing time is: {processing_time}.")


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


with TimerContext():
    time.sleep(2)
