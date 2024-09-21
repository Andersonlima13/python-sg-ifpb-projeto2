import random

# Função para gerar os parâmetros de Diffie-Hellman
def diffie_hellman_params():
    # Os parâmetros devem coincidir com os usados pelo Sender
    n = 23  # número primo
    g = 5   # base
    return n, g

# Função para gerar a chave pública com base na chave privada e nos parâmetros n, g
def generate_public_key(private_key, n, g):
    return pow(g, private_key, n)

# Função para gerar a chave secreta compartilhada
def generate_shared_secret(public_key, private_key, n):
    return pow(public_key, private_key, n)

# Função simplificada de descriptografia DES (para efeito de ilustração)
def simple_des_decrypt(ciphertext, key):
    # Descriptografar utilizando a mesma lógica de XOR simplificada
    decrypted = ''.join(chr(ord(c) ^ key) for c in ciphertext)
    return decrypted

# Parâmetros de Diffie-Hellman
n, g = diffie_hellman_params()

# Geração da chave privada (receiver)
private_key_receiver = random.randint(1, n-1)

# Geração da chave pública (receiver)
public_key_receiver = generate_public_key(private_key_receiver, n, g)
print(f"Chave pública do Receiver: {public_key_receiver}")

# Supondo que o receiver recebeu a chave pública do sender (essa chave seria trocada via canal inseguro)
public_key_sender = int(input("Insira a chave pública do Sender: "))

# Cálculo da chave secreta compartilhada
shared_secret_receiver = generate_shared_secret(public_key_sender, private_key_receiver, n)
print(f"Chave secreta compartilhada calculada pelo Receiver: {shared_secret_receiver}")

# Supondo que o receiver recebeu a mensagem criptografada do sender
encrypted_message = input("Insira a mensagem criptografada: ")

# Descriptografia da mensagem usando a chave compartilhada
decrypted_message = simple_des_decrypt(encrypted_message, shared_secret_receiver)
print(f"Mensagem descriptografada: {decrypted_message}")