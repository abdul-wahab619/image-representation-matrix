from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Function to load and display an RGB image
def display_rgb_image(image_path):
    # Open the RGB image
    rgb_image = Image.open(image_path)

    # Convert the image to a NumPy array
    image_array = np.array(rgb_image)

    # Display the RGB image using Matplotlib
    plt.imshow(image_array)
    # plt.axis('off')
    plt.title("RGB Image")
    plt.show()

    # Print the shape and matrix representation of the RGB image
    print("Shape of RGB Image Array:", image_array.shape)
    print("Matrix Representation of RGB Image:")
    print(image_array)

# Replace 'path/to/your/image.jpg' with the path to your RGB image file
image_path = 'D:\\ImageConversion\\images\\ball.jpg'
display_rgb_image(image_path)
