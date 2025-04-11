import requests

url = "http://127.0.0.1:5000/upload"
files = {'image': open('test_image.jpg', 'rb')}
response = requests.post(url, files=files)

print("Server Response:", response.text)

