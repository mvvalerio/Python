import requests

urlBase = "https://api.agify.io?name="

def getNameInfo(name):
    url = f"{urlBase}{name}"
    response = requests.get(url)
    print(response)
# To Be Continued