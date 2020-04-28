import requests

if __name__ == '__main__':
    filename = 'default_eight_image.jpg'

    url = 'http://127.0.0.1:5000/v1/predict'
    #url = 'http://34.242.4.54:5000/v1/predict'
    files = {'image': open(filename, 'rb')}
    #files = {}
    resp = requests.post(url, files=files)
    print(resp.json())