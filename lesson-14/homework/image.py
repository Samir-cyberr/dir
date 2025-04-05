from PIL import Image
import numpy as np

def load_image(path):
    """Load image using PIL and convert to numpy array"""
    img = Image.open(path)
    return np.array(img)

def save_image(array, path):
    """Convert numpy array to PIL Image and save"""
    img = Image.fromarray(array)
    img.save(path)

def flip_image(img_array):
    """Flip image horizontally and vertically"""
    # Flip left-right (horizontal)
    flipped_lr = img_array[:, ::-1, :]
    # Flip up-down (vertical)
    flipped_ud = flipped_lr[::-1, :, :]
    return flipped_ud

def add_noise(img_array, intensity=25):
    """Add random noise to image"""
    noise = np.random.randint(-intensity, intensity, img_array.shape)
    noisy_img = img_array + noise
    # Clip values to 0-255 range
    return np.clip(noisy_img, 0, 255).astype(np.uint8)

def brighten_channels(img_array, value=40):
    """Increase brightness of each channel by fixed value"""
    brightened = img_array + value
    # Clip values to 0-255 range
    return np.clip(brightened, 0, 255).astype(np.uint8)

def apply_mask(img_array, center_x, center_y, width=100, height=100):
    """Apply black rectangular mask to image"""
    masked_img = img_array.copy()
    half_w, half_h = width // 2, height // 2
    x_start = max(0, center_x - half_w)
    x_end = min(img_array.shape[1], center_x + half_w)
    y_start = max(0, center_y - half_h)
    y_end = min(img_array.shape[0], center_y + half_h)
    
    masked_img[y_start:y_end, x_start:x_end] = 0
    return masked_img

# Main image processing
def process_image(input_path, output_path):
    # Load the image
    img_array = load_image(input_path)
    
    # Apply transformations
    img_flipped = flip_image(img_array)
    img_noisy = add_noise(img_flipped)
    img_bright = brighten_channels(img_noisy)
    
    # Get center coordinates for mask
    height, width = img_bright.shape[:2]
    img_masked = apply_mask(img_bright, width//2, height//2)
    
    # Save the final image
    save_image(img_masked, output_path)

# Example usage (assuming 'birds.jpg' exists in images folder)
# process_image('images/birds.jpg', 'images/processed_birds.jpg')