import re
import numpy as np
from datetime import datetime


def extract_post_requests(log_file):
    timestamps = []
    with open(log_file, 'r') as file:
        for line in file:
            if 'POST' in line:
                match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                if match:
                    timestamp = match.group(0)
                    timestamps.append(timestamp)
    return timestamps


def count_requests_per_second(timestamps):
    time_objects = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]
    np_times = np.array(time_objects)
    unique_times, counts = np.unique(np_times, return_counts=True)
    return unique_times, counts


def post_request_count_per_second(log_file):
    timestamps = extract_post_requests(log_file)
    unique_times, counts = count_requests_per_second(timestamps)
    count_array = []
    for time, count in zip(unique_times, counts):
        count_array.append((time, count))
    return count_array


def main():
    log_file = './qa_ExpTester_PreInterview_Assigment.log'
    count_array = post_request_count_per_second(log_file)
    print("POST Requests per second:")
    for (time, count) in count_array:
        print(f"{time}: {count} requests")


if __name__ == "__main__":
    main()
