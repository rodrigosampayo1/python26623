# Use cases
# To scans log files (e.g., Apache access logs, system logs) and provides useful insights or automates specific actions based on log patterns. 
# For example, you can extract important information, generate reports, or even send notifications for specific log events.
def analyze_access_log(log_file):
    log_data = {}

    with open(log_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue

            fields = line.split()
            if len(fields) < 7:
                continue

            ip_address = fields[0]
            datetime = fields[3][1:] + ' ' + fields[4][:-1]
            method = fields[5][1:]
            url = fields[6]
            status_code = fields[8]

            if status_code not in log_data:
                log_data[status_code] = 1
            else:
                log_data[status_code] += 1

    print(f"Log file: {log_file}")
    print("Status Code Count:")
    for status_code, count in log_data.items():
        print(f"Status Code: {status_code} - Count: {count}")


# Example usage
log_file_path = '/path/to/access.log'  # Update with the actual path to the Apache access log file

analyze_access_log(log_file_path)
