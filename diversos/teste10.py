import json

string_json = '''
{
    "title": "O Senhor dos Anéis",
    "original_title": "The Lord of the Rings",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

# Carregar JSON como dicionário
data = json.loads(string_json)

# Acessar uma propriedade específica
print("Título original:", data["original_title"])
print("Ano de lançamento:", data["year"])

# Alterando o valor de uma propriedade
data["year"] = 2003
data["budget"] = 93000000  # Adicionando um valor ao campo null

# Convertendo de volta para string JSON formatada
novo_json = json.dumps(data, indent=4)

print("JSON atualizado:")
print(novo_json)
