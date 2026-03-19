# exercício 1 Print

'''municipio = "Blumenau"
uf = "SC"

print("Municipio:", municipio, "-" + uf)
'''

# exercício 2 Input
'''
print("Insira a latitude:")
print()
print("insira as coordenadas dos pontos")
lat = float(input("insira latitude:"))
long = float (input("insira longitude:"))

print(f"O ponto de coordenadas é latitude: {lat:.2f}, longitude {long:.2f}")

'''

# exercício 3 Cálculo de área de um terreno
'''
print("Vamos calcular a área?")
print("insira as dimensões:")
largura = int(input("insira a largura:"))
comprimento = int(input("insira o comprimento:"))

area = largura*comprimento
perimetro = 2*largura + 2*comprimento

print("A área é:", área, "m²")
print("O perímetro é:", perímetro, "m²")

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
'''

# exercício 4 Dados de um rio
'''
print("insira os dados do rio:")
nome_rio = "Rio Doce"
comprimento_km = float("200" )
eh_navegavel = bool(True)
num_afluentes = int(100)

print(f"o tipo de cada variável é = nome do rio = {type(nome_rio)}, comprimento_km {type(comprimento_km)},eh navegável {type(eh_navegavel)}, número de efluentes {type(num_afluentes)} ")

correção professor

nome_rio = input("insira o nome do rio:")
comprimento_km = float(input("digite comprimento:"))
eh_navegavel = bool(input("digite se é navegável")
num_afluentes = int(input("numero de afluentes")

'''
# exercício 5  Vértices em lista 3 elementos: os nomes de três marcos geodésicos
'''
geodesicos= ["pico", "monte", "quina"]
print(geodesicos)
print (geodesicos[1])

geodesicos.append("poste")
print(geodesicos)
print("número de elementos =", len(geodesicos))

'''

# exercício 6 Ficha de um ponto geográfico 
'''
print("Me fala um ponto de interesse, digite o nome e as coordenadas lat e long")
nome = input("insira o nome de interesse:")
lat = float(input("insira a latitude:"))
long = float(input("insira a longitude:"))

ponto = { "nome": nome, "latitude": lat, "longitude": long }

print("Dicionário:", ponto)
print("Apenas a latitude:", ponto["latitude"])

'''

# exercício 7 Nascente e foz de um rio

nome = input("insira o nome do rio:")
lat = float(input("insira a latitude da nascente:"))
long = float(input("insira a longitude da nascente:"))
latf = float(input("insira a latitude da foz:"))
longf = float(input("insira a longitude da foz:"))

rio = { 
    "nome": nome, 
    "nascente": [lat, long],
    "foz": [latf, longf],
      }

print("Dicionário:", rio)
print("Apenas a longitude da foz:", rio["foz"][1])
