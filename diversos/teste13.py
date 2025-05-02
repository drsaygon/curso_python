from string import Template

mensagem = '''
Caro(a) $nome,

Você possui $quantidade mensagem$s não lida$s.
'''

# Substituindo valores no template
dados = {
    "nome": "Sandro",
    "quantidade": 1  # Teste com 1 ou mais mensagens
}

# Criando o sufixo "s" para plural
# O módulo string.Template não aceita expressão ternária
dados["s"] = "s" if dados["quantidade"] > 1 else ""


texto_final = Template(mensagem).substitute(dados)
print(texto_final)
