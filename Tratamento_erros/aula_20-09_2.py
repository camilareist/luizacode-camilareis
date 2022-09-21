import requests

site = requests.get('https://www.google.com.br/')

def valida_site(site):
    if site.status_code == 200:
        print('O site informado está funcionando normalmente')
        
valida_site(site)
        