from PIL import Image, ImageDraw, ImageFont
import random, string, os

print("\n\n\n                                  - CaptchaTool -\n\n\n")

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def generate_captcha(save_path, idx):
    # Configuration
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Generate random text
    w, h = 320, 120  # Increased resolution for better clarity

    # Background image path assumed in the same folder as the script
    bg_path = os.path.join(os.getcwd(), "bg.png")
    if not os.path.exists(bg_path):
        print("Background image 'bg.png' not found in the current folder!")
        return

    # Load and prepare the background
    img = Image.open(bg_path).convert("RGB").resize((w, h))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 56)  # Larger font for visibility
    spacing = w // (len(text) + 1)

    # Add dynamic visual noise (lines and arcs in random colors)
    for _ in range(20):  # Increased number of random lines
        draw.line(
            [random.randint(0, w), random.randint(0, h), random.randint(0, w), random.randint(0, h)],
            fill=random_color(),
            width=random.randint(2, 4)
        )

    for _ in range(5):  # Enhance texture with arcs
        x, y, dx, dy = random.randint(0, w-50), random.randint(0, h-50), random.randint(30, 70), random.randint(30, 70)
        draw.arc([x, y, x+dx, y+dy], 0, 360, fill=random_color())

    # Add random colored characters with slight rotations
    for i, c in enumerate(text):
        char_img = Image.new('RGBA', (72, 96), (255, 255, 255, 0))  # Transparent character image
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((10, 10), c, font=font, fill=random_color())
        
        rotated_char = char_img.rotate(random.randint(-15, 15), expand=True)
        img.paste(rotated_char, (spacing*(i+1)+random.randint(-10, 10), random.randint(15, 30)), rotated_char)

    # Sprinkle random dots in random colors for more distraction
    for _ in range(50):  # Increased density of distraction dots
        draw.point((random.randint(0, w), random.randint(0, h)), fill=random_color())

    # Save the image with the CAPTCHA text in the filename
    filename = f"captcha_{text}.png"
    img.save(os.path.join(save_path, filename))
    print(f"Saved CAPTCHA: {filename}")

def main():
    save_dir = os.path.join(os.getcwd(), "images")  # Dynamic directory creation in current working directory
    os.makedirs(save_dir, exist_ok=True)  # Ensure directory exists
    num_images = int(input("How many CAPTCHA images do you want to create? "))
    for idx in range(1, num_images + 1):
        generate_captcha(save_dir, idx)
        print(f"Generated image {idx}")

if __name__ == "__main__":
    main()
