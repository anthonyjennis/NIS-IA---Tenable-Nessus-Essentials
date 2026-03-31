import requests
import urllib3

# Suppress insecure request warnings (since Nessus uses a self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

NESSUS_URL = "https://127.0.0.1:8834"
ACCESS_KEY = "f8e4553439306293d224b8bebc721b8c95e125a93efd0aaee65d699b605f3c19"
SECRET_KEY = "a5cdd14ab03106259b5592de4d8e8ed0dead8d98e1c52638389704896fb62a6a"


def get_nessus_scans():
    endpoint = f"{NESSUS_URL}/scans"

    headers = {
        "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}",
        "Content-Type": "application/json"
    }

    print("Authenticating and fetching scan data from Nessus API...\n")

    try:
        # verify=False bypasses SSL certificate validation for localhost
        response = requests.get(endpoint, headers=headers, verify=False)

        if response.status_code == 200:
            scans = response.json().get("scans", [])
            if not scans:
                print("No scans found.")
            else:
                print(f"Success! Found {len(scans)} configured scans. Here is the current status:\n")
                print("-" * 60)
                for scan in scans:
                    name = scan.get("name")
                    status = scan.get("status")
                    scan_id = scan.get("id")
                    print(f"Scan ID: {scan_id: <4} | Status: {status: <10} | Name: {name}")
                print("-" * 60)
        else:
            print(f"Failed to fetch scans. Status Code: {response.status_code}")
            print(f"Error Message: {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_nessus_scans()