from PIL import Image
import numpy as np

image_path = 'images/birds.jpg'  
image = Image.open(image_path)
img_array = np.array(image)

flipped = np.flipud(np.fliplr(img_array))

noise = np.random.randint(0, 50, flipped.shape, dtype='uint8')
noisy = np.clip(flipped + noise, 0, 255)

brightened = noisy.copy()
brightened[:, :, 0] = np.clip(brightened[:, :, 0] + 40, 0, 255)  

masked = brightened.copy()
h, w, _ = masked.shape
center_y, center_x = h // 2, w // 2
half_mask = 50  
masked[center_y - half_mask:center_y + half_mask,
       center_x - half_mask:center_x + half_mask] = [0, 0, 0]

final_image = Image.fromarray(masked.astype('uint8'))
final_image.save('modified_birds.jpg')
print("Image manipulation complete. Saved as 'modified_birds.jpg'")
