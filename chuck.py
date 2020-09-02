import requests

api = "https://api.chucknorris.io/jokes/random"

def getJoke(url):
    r = requests.get(url)
    rjson = r.json()
    return rjson

if __name__ == "__main__":
    joke = getJoke(api)
    print(joke['value'])

