import requests

if __name__ == '__main__':
    filename = 'default_eight_image.jpg'
    PUBLIC_IP = '52.213.49.123'

    #url = 'http://192.168.99.100:5000/v1/predict'
    url = 'http://'+PUBLIC_IP+':5000/v1/predict'
    files = {'image': open(filename, 'rb')}
    #files = {}
    resp = requests.post(url, files=files)
    print(resp.json())