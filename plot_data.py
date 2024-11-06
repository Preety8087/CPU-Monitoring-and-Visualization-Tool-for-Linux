import matplotlib.pyplot as plt
from datetime import datetime

def parse_log_file(log_file='system_monitor.log'):
    """Parse the log file and extract time, CPU, and memory usage."""
    times = []
    cpu_usages = []
    memory_usages = []

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split('|')
            timestamp = parts[0].split(": ", 1)[1].strip()
            cpu_usage = float(parts[1].split(": ", 1)[1].strip().replace('%', ''))
            memory_usage = float(parts[2].split(": ", 1)[1].strip().replace('%', ''))
            
            # Append data to lists
            times.append(datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f'))
            cpu_usages.append(cpu_usage)
            memory_usages.append(memory_usage)
    
    return times, cpu_usages, memory_usages

def plot_usage(times, cpu_usages, memory_usages):
    """Plot CPU and Memory usage over time."""
    plt.figure(figsize=(12, 6))
    
    # CPU and Memory usage plots
    plt.plot(times, cpu_usages, label='CPU Usage (%)', color='blue')
    plt.plot(times, memory_usages, label='Memory Usage (%)', color='red')
    
    # Labeling and formatting
    plt.xlabel('Time')
    plt.ylabel('Usage (%)')
    plt.title('CPU and Memory Usage Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    times, cpu_usages, memory_usages = parse_log_file()
    plot_usage(times, cpu_usages, memory_usages)
