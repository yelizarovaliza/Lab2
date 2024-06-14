import numpy as np

def input_matrix():
    n = int(input("Введіть розмір матриці (для n x n матриці): "))
    matrix = []
    
    print("Введіть елементи матриці по рядкам, розділені пробілом:")
    for i in range(n):
        row = list(map(float, input(f"Рядок {i + 1}: ").split()))
        matrix.append(row)
    
    return np.array(matrix)

def eigenvalues_and_eigenvectors(matrix):
    
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i]
        λ = eigenvalues[i]
        Av = np.dot(matrix, v)
        λv = λ * v
        
        if not np.allclose(Av, λv):
            print(f"Рівність не виконується для власного значення {λ} та вектора {v}")
        else:
            print(f"Рівність виконується для власного значення {λ} та вектора {v}")
    
    return eigenvalues, eigenvectors

def round_values(value):
    if value.is_integer():
        return int(value)
    return round(value, 1)

def format_eigenvectors(eigenvectors):
    formatted_vectors = []
    for vector in eigenvectors.T:
        formatted_vector = ", ".join(map(str, [round_values(val) for val in vector]))
        formatted_vectors.append(f"[{formatted_vector}]")
    return formatted_vectors

# Основна частина
matrix = input_matrix()
eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(matrix)

rounded_eigenvalues = [round_values(value) for value in eigenvalues]
formatted_eigenvectors = format_eigenvectors(eigenvectors)

print("Власні значення:", ", ".join(map(str, rounded_eigenvalues)))
print("Власні вектори:")
for vec in formatted_eigenvectors:
    print(vec)
