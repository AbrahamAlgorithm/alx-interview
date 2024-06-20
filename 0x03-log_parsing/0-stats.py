#!/usr/bin/python3
import sys
import signal

# Initialize counters
total_size = 0
status_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0

def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

def signal_handler(sig, frame):
    """Signal handler for keyboard interruption"""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        # Extract and validate status code and file size
        status_code = parts[-2]
        file_size = parts[-1]

        try:
            file_size = int(file_size)
            total_size += file_size
        except ValueError:
            continue

        if status_code in status_counts:
            status_counts[status_code] += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

