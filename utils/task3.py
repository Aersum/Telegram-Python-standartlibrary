import requests


def get_image(url: str):
    file_name = 'task3.png'
    res = requests.get(url)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(res.content)
    print(f'File {file_name} downloaded')


if __name__ == "__main__":
    url = "https://dummyimage.com/600x400/000/fff"
    get_image(url)
