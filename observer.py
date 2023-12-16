import time, pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# def on_created(event):
#     print("Created")

# def on_deleted(event):
#     print("Deleted")

def on_modified(event):

    # Step 1: Pre-Process the new Data
    data = pd.read_csv("world_bank_preprocessed.csv")

# def on_moved(event):
#     print("Moved")

if __name__ == "__main__":
    
    event_handler = FileSystemEventHandler()

    event_handler.on_modified = on_modified

    path = r"C:\Users\DELL\Desktop\Taiyo-Testing"

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            print("Monitoring...")
            time.sleep(1)      # This increases computational costs but this can be fixed by using any cloud services like AWS
    except KeyboardInterrupt:
        observer.stop()
    observer.join()