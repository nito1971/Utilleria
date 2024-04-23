from cryptography.fernet import Fernet

# Generar una clave para el cifrado y descifrado
key = Fernet.generate_key()

# Crear un conjunto de cifrado
cipher_suite = Fernet(key)

def encrypt_string(input_string):
    # Convertir la cadena de entrada a bytes
    input_bytes = input_string.encode()

    # Cifrar los bytes de entrada
    encrypted_bytes = cipher_suite.encrypt(input_bytes)

    # Convertir los bytes cifrados a cadena y devolver
    return encrypted_bytes.decode()

# Probar la función
test_string = "Hello, World!"
encrypted_string = encrypt_string(test_string)
print(f"La cadena cifrada de '{test_string}' es '{encrypted_string}'")
