from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Function to convert an image to grayscale
def convert_to_grayscale(image_path):
    
    # Open the image and convert it to grayscale
    original_image = Image.open(image_path)
    grayscale_image = original_image.convert("L")
    
    # Convert the image to a NumPy array
    image_array = np.array(grayscale_image)
    
    # Show the original and grayscale images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_image)
    
    plt.subplot(1, 2, 2)
    plt.title("Grayscale Image")
    plt.imshow(grayscale_image, cmap='gray')
    
    plt.show()
    
    # Display the matrix representation of the grayscale image
    print("Matrix Representation of Grayscale Image:")
    print(image_array)

# Path of the image file
image_path = 'D:\\ImageConversion\\images\\boat.jpg'
convert_to_grayscale(image_path)
