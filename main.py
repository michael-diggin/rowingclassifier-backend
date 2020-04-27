import requests

if __name__ == '__main__':
    filename = 'default_eight_image.jpg'

    url = 'http://127.0.0.1:5000/v1/predict'
    files = {'image': open(filename, 'rb')}
    resp = requests.post(url, files=files)
    print(resp)