import secrets
import string

def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    sr = secrets.SystemRandom()  # Instanciando SystemRandom
    senha = ''.join(sr.choices(caracteres, k=tamanho))  # Gerando senha segura
    return senha

print("Senha segura:", gerar_senha(16))
