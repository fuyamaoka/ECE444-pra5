import requests
import time
import csv

# Define the API URL
url = "http://ece444-pra5-env.eba-qb5kuex2.us-east-2.elasticbeanstalk.com/predict"

# Define the test cases
test_cases = [
    {"text": "Uoft course averages at an all time high."},  
    {"text": "George washington is the new president."},
    {"text": "Aliens land on earth."},
    {"text": "Toronado warning in Toronto, Canada."},  
]

# Open a CSV file to store the latency results
with open('api_performance.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Case", "Response Time (ms)"])

    # Send 100 requests and record the latency
    for i in range(100):
        for idx, test_case in enumerate(test_cases):
            start_time = time.time()
            response = requests.post(url, json=test_case)
            latency = (time.time() - start_time) * 1000  # Convert to milliseconds

            # Write the result to the CSV file
            writer.writerow([f"Test Case {idx + 1}", latency])

print("API performance data recorded in api_performance.csv.")
