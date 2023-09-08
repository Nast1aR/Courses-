import time
import threading
import multiprocessing
import requests
import os


# CPU-bound task (heavy computation)
class TaskManager:
    @staticmethod
    def encrypt_file(path: str):
        print(f"Processing file from {path} in process {os.getpid()}")
        # Simulate heavy computation by sleeping for a while
        _ = [i for i in range(100_000_000)]

    @staticmethod
    def download_image(image_url):
        print(
            f"Downloading image from {image_url} in thread {threading.current_thread().name}"
        )
        response = requests.get(image_url)
        with open("image.jpg", "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    start_time = time.perf_counter()

    encryption_process = multiprocessing.Process(
        target=TaskManager.encrypt_file, args=("rockyou.txt",)
    )

    download_thread = threading.Thread(
        target=TaskManager.download_image,
        args=("https://picsum.photos/1000/1000",),
    )

    image_url = "https://picsum.photos/1000/1000"
    tasks = [encryption_process, download_thread]

    try:
        for task in tasks:
            task.start()

        for task in tasks:
            task.join()

        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time:.2f} seconds")

    except Exception as e:
        print(f"Error occurred: {e}")
