import numpy as np

message = input("Enter a phrase: ")
key_matrix = np.random.randint(0, 256, (len(message), len(message)))


eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))

def encrypt_massage(message):
    
    message_vector = np.array([ord(char) for char in message])
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    
    return encrypted_vector

def decrypt_message(encrypted_vector):
    decrypted_vector = np.dot(np.linalg.inv(diagonalized_key_matrix), encrypted_vector)
    decrypted_message = ''.join([chr(int(np.round(num))) for num in decrypted_vector.real])
    return decrypted_message


print(f"Original Mesage:{message}")
encrypted_message = encrypt_massage(message)
print(f"Encrypt Message: {encrypted_message}")
decrypted_message = decrypt_message(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")