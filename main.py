import speedtest
import json

def run_speedtest(server_id, num_measurements):
    results = []
    for _ in range(num_measurements):
        st = speedtest.Speedtest()
        st.get_servers(servers=[server_id])
        #st.get_best_server(servers=[server_id])
        st.download()
        st.upload()
        results.append(st.results.dict())
    return results

def save_results_to_json(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    server_id = 14623
    num_measurements = 1
    results = run_speedtest(server_id, num_measurements)
    save_results_to_json(results, 'speedtest_results.json')
    print("Speed test results saved to speedtest_results.json")