import psutil
import time
from datetime import datetime

def log_system_usage(log_file='system_monitor.log', cpu_threshold=80, memory_threshold=80):
    """Log CPU, memory, disk, and network usage, with alerts for high CPU and memory."""
    with open(log_file, 'a') as file:
        while True:
            # System metrics retrieval
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            net = psutil.net_io_counters()

            # Formatting log data
            log_data = (
                f"Time: {datetime.now()} | "
                f"CPU Usage: {cpu_usage}% | "
                f"Memory: {memory.percent}% | "
                f"Disk: {disk.percent}% | "
                f"Bytes Sent: {net.bytes_sent} | "
                f"Bytes Received: {net.bytes_recv}"
            )

            # Console output and file logging
            print(log_data)
            file.write(log_data + '\n')

            # Threshold-based alerts
            if cpu_usage > cpu_threshold:
                print(f"ALERT: High CPU usage detected at {cpu_usage}%!")
            if memory.percent > memory_threshold:
                print(f"ALERT: High Memory usage detected at {memory.percent}%!")

            # Interval between log entries
            time.sleep(5)

if __name__ == "__main__":
    log_system_usage()
