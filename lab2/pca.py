import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

image_raw = imread("photo1.jpg")
print(image_raw.shape)


image_sum = image_raw.sum(axis = 2)
print(image_sum.shape)
image_bw = image_sum/image_sum.max()
print(image_bw.max())

# PCA для чорно-білого зображення
image_flat = image_bw.flatten()
image_matrix = np.reshape(image_flat, (image_bw.shape[0], image_bw.shape[1]))

pca = PCA()
pca.fit(image_matrix)

# Кумулятивна дисперсія
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# кількість компонент, які покривають 95% дисперсії
num_components = np.argmax(cumulative_variance >= 0.95) + 1

print("Number of components to cover 95% variance:", num_components)

# графік процесу
plt.figure(figsize=(10, 6))
plt.plot(cumulative_variance, marker='o')
plt.axhline(y=0.95, color='r', linestyle='--')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Variance')
plt.title('Cumulative Variance vs. Number of Components')
plt.grid()
plt.show()

# Реконструкція зображення
pca = PCA(n_components=num_components)
image_transformed = pca.fit_transform(image_matrix)
image_reconstructed = pca.inverse_transform(image_transformed)

# Візуалізація оригінального, ч/б та реконструйованого 
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image_raw)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Original Image')
plt.imshow(image_bw, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Reconstructed Image with {} Components'.format(num_components))
plt.imshow(image_reconstructed, cmap='gray')
plt.axis('off')

plt.show()