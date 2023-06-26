# Use case:
# Periodically collects system metrics such as CPU usage, memory utilization, disk space, and network statistics. 
# You can use libraries like psutil to gather this information and log it for later analysis or trigger alerts based on predefined thresholds.

import psutil

def monitor_server():
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = round(memory.used / (1024 * 1024), 2)  # Convert to MB
    memory_total = round(memory.total / (1024 * 1024), 2)  # Convert to MB
    print(f"Memory Usage: {memory_used}MB / {memory_total}MB ({memory_percent}%)")

    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    disk_used = round(disk.used / (1024 * 1024 * 1024), 2)  # Convert to GB
    disk_total = round(disk.total / (1024 * 1024 * 1024), 2)  # Convert to GB
    print(f"Disk Usage: {disk_used}GB / {disk_total}GB ({disk_percent}%)")

    # Network Statistics
    network = psutil.net_io_counters()
    network_bytes_sent = round(network.bytes_sent / (1024 * 1024), 2)  # Convert to MB
    network_bytes_received = round(network.bytes_recv / (1024 * 1024), 2)  # Convert to MB
    print(f"Network Bytes Sent: {network_bytes_sent}MB")
    print(f"Network Bytes Received: {network_bytes_received}MB")

# Example usage
monitor_server()
