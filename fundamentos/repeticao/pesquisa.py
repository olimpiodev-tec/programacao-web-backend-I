import webbrowser

print("Olá vamos pesquisar o valor dos produtos na internet")

qtde_produtos = int(input("Quantos produtos deseja pesquisar: "))
produtos = []

for produto in range(1, qtde_produtos+1):
    p = input("Qual nome do produto? ")
    produtos.append(p)

sites = []

print(f"Que legal, armazenei em memória {len(produtos)} produtos")

qtde_sites = int(input("Agora quer pesquisar em quantos sites: "))

for site in range(1, qtde_sites + 1):
    nome_site = input("Qual endereço do site? ")
    sites.append(nome_site)

print("Ok, agora vou abrir o navegador com as informações que você passou")

for site in sites:
    for produto in produtos:
        url = "https://www." + site + "/" + produto
        webbrowser.open_new_tab(url)
