import requests

def testa_site(url):
    try:
        resposta = requests.get(url,  timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está online!")
        else:
            print(f"O site {url} respondeu com código {resposta.status_code}")
    except requests.ConnectionError:
        print(f"O site {url} não está acessível (erro de conexão).")
    except requests.Timeout:
        print(f"O site {url} demorou demais para resoponder (timeout).")
    except Exception as e:
        print(f"Ocorreu um erro ao acessar {url}: {e}")

# Testando com o site do pudim
testa_site("http://pudim.com.br")