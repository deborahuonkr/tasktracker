import psutil
import time
import datetime

class TaskTracker:
    def __init__(self, log_interval=5):
        self.log_interval = log_interval
        self.running = True

    def log_system_stats(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        log_message = (f"Timestamp: {timestamp} | "
                       f"CPU Usage: {cpu_usage}% | "
                       f"Memory Usage: {memory_info.percent}% | "
                       f"Disk Usage: {disk_usage.percent}%")
        
        print(log_message)

    def start_monitoring(self):
        print("Starting TaskTracker...")
        try:
            while self.running:
                self.log_system_stats()
                time.sleep(self.log_interval)
        except KeyboardInterrupt:
            print("Stopping TaskTracker...")
            self.running = False

if __name__ == '__main__':
    tracker = TaskTracker(log_interval=5)
    tracker.start_monitoring()