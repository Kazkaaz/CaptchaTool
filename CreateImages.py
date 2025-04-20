from PIL import Image, ImageDraw, ImageFont
import random, string
import os

def generate_captcha(save_path, idx):
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    w, h = 320, 120  # Increased resolution

    # Use bg.png as background
    bg_path = r"C:\Users\kasim\OneDrive\Code\CaptchaImages\bg.png"
    img = Image.open(bg_path).convert("RGB").resize((w, h))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 56)  # Increased font size
    spacing = w // (len(text) + 1)

    for _ in range(14):  # Draw more lines for larger image
        draw.line([random.randint(0, w), random.randint(0, h), random.randint(0, w), random.randint(0, h)],
                  fill=tuple(random.randint(0, 255) for _ in range(3)), width=3)

    # Draw 3 lines on top of the text area
    for _ in range(3):
        y = random.randint(20, 50)
        draw.line( 
            [10, y, w - 10, y + random.randint(-10, 10)],
            fill=tuple(random.randint(0, 255) for _ in range(3)),
            width=3
        )

    for i, c in enumerate(text):
        char_img = Image.new('RGBA', (72, 96), (255, 255, 255, 0))  # Increased char image size
        ImageDraw.Draw(char_img).text((10, 10), c, font=font, fill=tuple(random.randint(0, 150) for _ in range(3)))
        rotated = char_img.rotate(random.randint(-15, 15), expand=1, fillcolor=(255,255,255,0))
        img.paste(rotated,
                  (spacing*(i+1)+random.randint(-6,6), random.randint(10,30)), rotated)

    for _ in range(4):  # More arcs for larger image
        x, y, dx, dy = random.randint(0, w-20), random.randint(10, 40), random.randint(10, 40), random.randint(10, 40)
        draw.arc([x, y, x+dx, y+dy], 0, 360, fill=tuple(random.randint(0, 255) for _ in range(3)))
    for _ in range(40):  # More points for larger image
        draw.point((random.randint(0, w), random.randint(0, h)), fill=tuple(random.randint(0, 255) for _ in range(3)))

    # Save with answer in filename
    img.save(os.path.join(save_path, f"captcha_{text}.png"))

if __name__ == "__main__":
    save_dir = r"C:\Users\kasim\OneDrive\Code\CaptchaImages\images"
    os.makedirs(save_dir, exist_ok=True)
    num_images = int(input("How many images do you want to create? "))
    for i in range(1, num_images + 1):
        generate_captcha(save_dir, i)
        print(f"Created image {i}")
