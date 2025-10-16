from cryptography.fernet import Fernet

# 1. Gerar a chave (faça isso apenas uma vez e armazene-a com segurança!)
chave = "chave"
fernet = Fernet(chave)