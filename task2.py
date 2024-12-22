from PIL import Image
import random
def load_image(image_path):
    img = Image.open(image_path)
    return img
def save_image(image, save_path):
    image.save(save_path)
def apply_math_operation(img, operation="add", value=10):
    pixels = img.load()  # Access the pixels
    width, height = img.size  
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            if operation == "add":
                r = (r + value) % 256
                g = (g + value) % 256
                b = (b + value) % 256
            elif operation == "subtract":
                r = (r - value) % 256
                g = (g - value) % 256
                b = (b - value) % 256
            elif operation == "multiply":
                r = (r * value) % 256
                g = (g * value) % 256
                b = (b * value) % 256
                
            pixels[x, y] = (r, g, b)
    return img
def swap_pixels(img):
    pixels = img.load()
    width, height = img.size
    x1, y1 = random.randint(0, width-1), random.randint(0, height-1)
    x2, y2 = random.randint(0, width-1), random.randint(0, height-1)
    pixel1 = pixels[x1, y1]
    pixel2 = pixels[x2, y2]
    pixels[x1, y1] = pixel2
    pixels[x2, y2] = pixel1

    return img
def encrypt_image(img, operation="add", value=10, swap=True):
    img = apply_math_operation(img, operation, value)
    if swap:
        img = swap_pixels(img)
    
    return img

if __name__ == "__main__":
    image_path = "input_image.jpg" 
    img = load_image("D:\\task 2\\New folder\\eagle.png")
    encrypted_img = encrypt_image(img, operation="add", value=50, swap=True)
    
    save_path = "encrypted_image.jpg"
    save_image(encrypted_img, save_path)
    
    print(f"Image encrypted and saved as {save_path}")
