import requests


def send_data(data):
    url = 'http://example.com/your-api-endpoint'  # 替换为实际的 API 端点 URL

    # 构建代理配置
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }

    # 发送请求时设置代理
    response = requests.post(url, json=data, proxies=proxies)

    # 处理响应
    if response.status_code == 200:
        print('Data sent successfully.')
    else:
        print('Failed to send data. Status code:', response.status_code)


# 构建要发送的数据
data = {
    'data': [
        'base64_image_data',
        'selected_version'
    ]
}

# 发送数据
send_data(data)
