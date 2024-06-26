from datetime import datetime
import requests
import json
import subprocess

# ZoomEye API URL
url = 'https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB+Alist%22+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bapp%3A%22nginx%22&page=1&t=v4%2Bv6%2Bweb%2Bhost'

urls_o = ['https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB+Alist%22+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bapp%3A%22nginx%22&page=1&t=v4%2Bv6%2Bweb%2Bhost','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bcity%3A%E5%B9%BF%E5%B7%9E&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bcity%3A%E6%B7%B1%E5%9C%B3%E5%B8%82&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E6%B5%99%E6%B1%9F&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E4%B8%8A%E6%B5%B7&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3ACN+%2Bsubdivisions%3A%E5%8C%97%E4%BA%AC&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22%E5%B0%8F%E9%9B%85%E7%9A%84%E5%88%86%E7%B1%BB%2BAlist%22+%2Bport%3A5678+%2Bcountry%3AJP&page=1&pageSize=50&t=v4%2Bv6%2Bweb','https://www.zoomeye.org/api/search?q=title%3A%22alist%22+%2Bcountry%3ACN+%2Bport%3A5678&page=1&t=v4%2Bv6%2Bweb%2Bhost']

urls=['https://www.zoomeye.org/api/search?q=title%3A%22alist%22+%2Bcountry%3ACN+%2Bport%3A5678&page=1&t=v4%2Bv6%2Bweb%2Bhost','https://www.zoomeye.org/api/search?q=title%3A%22alist%22+%2Bcountry%3ACN+%2Bport%3A5678+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bcity%3A%E6%B7%B1%E5%9C%B3%E5%B8%82&page=1&t=v4%2Bv6%2Bweb%2Bhost',"https://www.zoomeye.org/api/search?q=title%3A%22alist%22+%2Bcountry%3ACN+%2Bport%3A5678+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bcity%3A%E6%B7%B1%E5%9C%B3&page=1&t=v4%2Bv6%2Bweb%2Bhost","https://www.zoomeye.org/api/search?q=title%3A%22alist%22+%2Bcountry%3ACN+%2Bport%3A5678+%2Bsubdivisions%3A%E5%B9%BF%E4%B8%9C+%2Bcity%3A%E6%B7%B1%E5%9C%B3+%2Bafter%3A%222024-01-01%22+%2Bbefore%3A%222025-01-01%22&page=1&t=v4%2Bv6%2Bweb%2Bhost"]

# JSON file path
file_path = 'ip.json'

# API test endpoint
test_endpoint = 'http://{ip}:5678/api/fs/get'
test_endpoint2 = 'http://{ip}:5678/api/me'

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
            print_with_timestamp("Response content is not valid JSON format")
            return []
    else:
        print(f"Request failed, status code: {response.status_code}")
        return []

def get_ips_from_zoomeye_urls(urls):
    ip_list = []

    for url in urls:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                ips = data.get('matches', [])  # Assuming the IPs are under 'matches'
                ip_list+=[match['ip'] for match in ips]  # Extract the IP addresses
            except json.JSONDecodeError:
                print_with_timestamp("Response content is not valid JSON format")
                
        else:
            print(f"Request failed, status code: {response.status_code}")
    return ip_list




def test_api_with_delay(ip_address):
    test_url = test_endpoint.format(ip=ip_address)
    test_url2 = test_endpoint2.format(ip=ip_address)

    
    try:
        #先进行匿名用户测试
        response0 = requests.get(test_url, headers=headers, timeout=4)
        if response0.status_code == 200:
            try:
                data = response0.json()
                if 'code' in data and data['code'] == 401:
                    print_with_timestamp("Guest user is disabled, login please")
                    return False, None
            except json.JSONDecodeError:
                print_with_timestamp("Response content is not valid JSON format")
                return False, None
        #进行播放链接测试
        response = requests.post(test_url, headers=headers, json=body, allow_redirects=True, timeout=4)
        response_delay_ms = response.elapsed.total_seconds() * 1000
        if response.status_code == 200:
            try:
                data = response.json()
                if 'code' in data and data['code'] != 200:
                    print_with_timestamp("Guest user is disabled, login please")
                    return False, None
                else:
                    if 'ali' in data['data']['raw_url']:
                        return True, response_delay_ms
                    return  False, None
            except json.JSONDecodeError:
                print_with_timestamp("Response content is not valid JSON format")
                return False, None
        else:
            print(f"Request failed, status code: {response.status_code}")
            return False, None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return False, None





def check_and_clean_ip_list(ip_list):
    valid_ips_with_delay = []
    for ip in ip_list:
        is_valid, delay = test_api_with_delay(ip)
        if is_valid:
            if delay is not None:
                valid_ips_with_delay.append((ip, delay))
                print(f"IP {ip} pass the test.{delay}")
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
        print_with_timestamp("JSON file format error")
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
    ip_list_zoomeye = get_ips_from_zoomeye_urls(urls)
    print_with_timestamp("获取到zoomeye新IP")
    print(ip_list_zoomeye)

    # Merge IP lists and remove duplicates
    merged_ips = list(set([ip for ip, _ in ip_list_json] + ip_list_zoomeye))

    # Check and clean IP list, including delay detection
    cleaned_ip_list_with_delay = check_and_clean_ip_list(merged_ips)

    # Write cleaned IP list and delay information to file
    write_ips_to_file(file_path, cleaned_ip_list_with_delay)
    print_with_timestamp("以下IP可用")
    print(cleaned_ip_list_with_delay)
    get_ips_change_nginx()


def get_ips_change_nginx():
    data = read_ips_from_file(file_path)
    # 假设端口号是5678
    port_number = 5678
    data.sort(key=lambda x: x[1])
    # 使用列表推导式将IP地址和端口号组合成字符串
    formatted_data = [f"{ip}:{port_number}" for ip, _ in data[0:3]]
    generate_nginx_config(formatted_data)



def generate_nginx_config(ip_list):
    print_with_timestamp("开始创建nginx配置")
    # Nginx 配置文件路径
    #nginx_config_path = "nginx.conf"
    nginx_config_path = "/etc/nginx/nginx.conf"

    # 生成新的 Nginx 配置内容
    nginx_config = """
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    upstream backend {
        least_conn;
"""
    for ip in ip_list:
        nginx_config += f"""        server {ip} max_fails=3 fail_timeout=30s;
"""
    
    nginx_config += """
       keepalive 16;
    }

    server {
        listen       80;
        server_name  localhost;

        location / {
            proxy_pass http://backend;
            # 添加反代节点的 IP 地址到响应头
            add_header X-Upstream-Addr $upstream_addr;
            # 配置节点失效检测
            proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        }

    }
}
"""

    #写入新的 Nginx 配置文件
    with open(nginx_config_path, 'w', encoding='utf-8') as file:
        print_with_timestamp("更新nginx")
        print(nginx_config)
        file.write(nginx_config)
         # 重新加载 Nginx 配置
        subprocess.run(["nginx", "-s", "reload"])
        print_with_timestamp("更新nginx完成")





def print_with_timestamp(message):
    # 获取当前UTC时间
    current_time = datetime.utcnow()
    # 格式化时间戳
    timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # 打印带时间戳的消息
    print(f'{timestamp} - {message}')