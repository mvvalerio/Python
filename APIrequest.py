import requests

def obterIdArea():
    idArea = input("Escolha uma região 3 - Arq. Açores | 7 - Continente, Arq. Madeira: ")
    
    match(idArea):
        case "3":
            idArea = "3"
            url = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}.json"
            response = requests.get(url)

            if response.status_code == 200:
                seismic_data = response.json()
                return seismic_data
            
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return None
            
        case "7":
            idArea = "7"  
            url = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}.json"
            response = requests.get(url)

            if response.status_code == 200:
                seismic_data = response.json()
                return seismic_data
            
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                return None
            
        case _:
            print("Input incorreto! Tente novamente.")
            return None

data = obterIdArea()
if data:
    print("Dados sísmicos obtidos:", data)
else:
    print("Falha ao obter dados.")

