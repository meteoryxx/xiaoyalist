import requests
import json
import ping3

# ZoomEye API URL
url = 'https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB+Alist%22+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bapp%3A%22nginx%22&page=1&t=v4%2Bv6%2Bweb%2Bhost'

# JSON file path
file_path = 'ip.json'

# API test endpoint
test_endpoint = 'http://{ip}:5678/api/fs/get'

# Headers for API test
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "authorization": "",
    "content-type": "application/json;charset=UTF-8"
}

# Body for API test
body = {
    "path": "/元数据/config.mp4",
    "password": ""
}

#"path": "/动漫/儿童/BBC 字母积木 1-4季/积木英语Alphablocks第一季【598.78MB】/Alphablocks_-_1._Alphablocks.avi",
def get_ips_from_zoomeye(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            ips = data.get('matches', [])  # Assuming the IPs are under 'matches'
            return [match['ip'] for match in ips]  # Extract the IP addresses
        except json.JSONDecodeError:
            print("Response content is not valid JSON format")
            return []
    else:
        print(f"Request failed, status code: {response.status_code}")
        return []

def test_api_with_delay(ip_address):
    test_url = test_endpoint.format(ip=ip_address)
    try:
        response = requests.post(test_url, headers=headers, json=body, allow_redirects=True, timeout=5)

        if response.status_code == 200:
            try:
                data = response.json()
                if 'code' in data and data['code'] == 401:
                    print("Guest user is disabled, login please")
                    return False, None
                else:
                    return True, None
            except json.JSONDecodeError:
                print("Response content is not valid JSON format")
                return False, None
        else:
            print(f"Request failed, status code: {response.status_code}")
            return False, None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return False, None

def measure_delay(ip_address):
    try:
        delay = ping3.ping(ip_address)
        if delay is None:
            print(f"Failed to measure delay for {ip_address}")
            return None
        else:
            return delay
    except Exception as e:
        print(f"Error measuring delay for {ip_address}: {e}")
        return None

def check_and_clean_ip_list(ip_list):
    valid_ips_with_delay = []

    for ip in ip_list:
        is_valid, _ = test_api_with_delay(ip)
        if is_valid:
            delay = measure_delay(ip)
            if delay is not None:
                valid_ips_with_delay.append((ip, delay))
        else:
            print(f"IP {ip} failed the test.")

    return valid_ips_with_delay

def read_ips_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [(ip_info['ip'], ip_info['delay']) for ip_info in data.get('ips', [])]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON file format error")
        return []

def write_ips_to_file(file_path, ip_list_with_delay):
    ip_dict_list = [{'ip': ip, 'delay': delay} for ip, delay in ip_list_with_delay]
    data = {'ips': ip_dict_list}

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def get_ips():
        # Read existing IP list from file
    ip_list_json = read_ips_from_file(file_path)

    # Get new IP list from ZoomEye
    ip_list_zoomeye = get_ips_from_zoomeye(url)
    print("Got new IPs")
    print(ip_list_zoomeye)

    # Merge IP lists and remove duplicates
    merged_ips = list(set([ip for ip, _ in ip_list_json] + ip_list_zoomeye))

    # Check and clean IP list, including delay detection
    cleaned_ip_list_with_delay = check_and_clean_ip_list(merged_ips)

    # Write cleaned IP list and delay information to file
    write_ips_to_file(file_path, cleaned_ip_list_with_delay)