import random

# Função para gerar os parâmetros de Diffie-Hellman
def diffie_hellman_params():
    # Escolha de um número primo (n) e uma base (g)
    n = 23  # exemplo de número primo
    g = 5   # exemplo de base
    return n, g

# Função para gerar a chave pública com base na chave privada e nos parâmetros n, g
def generate_public_key(private_key, n, g):
    return pow(g, private_key, n)

# Função para gerar a chave secreta compartilhada
def generate_shared_secret(public_key, private_key, n):
    return pow(public_key, private_key, n)

# Função simplificada de criptografia DES (para efeito de ilustração)
def simple_des_encrypt(plaintext, key):
    # Aqui seria implementado o algoritmo DES completo
    # Para simplificação, estamos apenas fazendo uma substituição simples
    encrypted = ''.join(chr(ord(c) ^ key) for c in plaintext)  # Exemplo de operação XOR
    return encrypted

# Parâmetros de Diffie-Hellman
n, g = diffie_hellman_params()

# Geração da chave privada (sender)
private_key_sender = random.randint(1, n-1)

# Geração da chave pública (sender)
public_key_sender = generate_public_key(private_key_sender, n, g)
print(f"Chave pública do Sender: {public_key_sender}")

# Supondo que o sender recebeu a chave pública do receiver (essa chave seria trocada via canal inseguro)
public_key_receiver = int(input("Insira a chave pública do Receiver: "))

# Cálculo da chave secreta compartilhada
shared_secret_sender = generate_shared_secret(public_key_receiver, private_key_sender, n)
print(f"Chave secreta compartilhada calculada pelo Sender: {shared_secret_sender}")

# Criptografia da mensagem usando a chave compartilhada
message = "Funcionou!"
encrypted_message = simple_des_encrypt(message, shared_secret_sender)
print(f"Mensagem criptografada: {encrypted_message}")