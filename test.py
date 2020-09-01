import math
import requests
import sys

def makeReq():
    r = requests.get(url="https://google.com")
    print(r.headers)
    print(r.raw)
    

if __name__ == "__main__":
    makeReq()