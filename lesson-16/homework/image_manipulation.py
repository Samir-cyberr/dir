from PIL import Image
import numpy as np

# Load the image using PIL
image_path = "your_image.png"  # Replace with your actual image path
image = Image.open(image_path)
image_np = np.array(image)

# Function to flip the image horizontally and vertically
def flip_image(img_np):
    return np.flipud(np.fliplr(img_np))

# Function to add random noise
def add_noise(img_np, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level + 1, img_np.shape, dtype='int16')
    noisy_image = img_np.astype('int16') + noise
    return np.clip(noisy_image, 0, 255).astype('uint8')

# Function to brighten RGB channels
def brighten_channels(img_np, brightness_increase=40):
    brightened = img_np.astype('int16') + brightness_increase
    return np.clip(brightened, 0, 255).astype('uint8')

# Function to apply a black rectangular mask at the center
def apply_mask(img_np, mask_size=(100, 100)):
    h, w = img_np.shape[:2]
    top_left_y = h // 2 - mask_size[0] // 2
    top_left_x = w // 2 - mask_size[1] // 2
    img_np[top_left_y:top_left_y + mask_size[0], top_left_x:top_left_x + mask_size[1]] = 0
    return img_np

# Apply all manipulations
flipped_image = flip_image(image_np)
noisy_image = add_noise(flipped_image)
brightened_image = brighten_channels(noisy_image)
final_image = apply_mask(brightened_image)

# Convert final NumPy array back to image and save it
final_pil_image = Image.fromarray(final_image)
final_pil_image.save("modified_dog_image.png")
