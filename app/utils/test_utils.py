import requests
import time

def stress_test(url, headers, duration, frequency):
    start_time = time.time()
    results = []
    
    while time.time() - start_time < duration:
        response = requests.get(url, headers=headers)
        results.append(response.status_code)
        time.sleep(1/frequency)
        
    return results

def flow_test(steps, headers):
    results = []
    for step in steps:
        response = requests.request(
            method=step['method'],
            url=step['url'],
            headers=headers,
            json=step.get('data')
        )
        results.append(response)
    return results
