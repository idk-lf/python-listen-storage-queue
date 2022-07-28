# pip install azure-storage-queue

from azure.storage.queue import QueueClient
import os, time
import _thread
from flask import Flask

print("start")

def process():
        connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        queue_name = os.getenv("AZURE_STORAGE_QUEUE_NAME")
        queue_client = QueueClient.from_connection_string(connect_str, queue_name)

        while True:
                message = queue_client.receive_message(visibility_timeout=10) # 20*60 = 20 minutes, 10 = 10 sec
                if message is None:
                        print("no messages")
                        time.sleep(10)
                else:
                        print("start " + message.content)
                        time.sleep(2)
                        print("end " + message.content)
                        queue_client.delete_message(message)
                        time.sleep(1)

_thread.start_new(process, ())

app = Flask(__name__)

@app.route("/health")
def health():
    return "200 OK", 200

if __name__ == "__main__":
    app.run()

