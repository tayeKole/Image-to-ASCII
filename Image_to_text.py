from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # Open and resize the image
    img = Image.open(image)
    w, h = img.size
    img = img.resize((w // scale, h // scale))
    w, h = img.size  # Update dimensions after resizing

    # Convert to grayscale for easier brightness comparison
    img = img.convert("L")
    pix = img.load()

    # Define ASCII characters for different brightness levels
    chars = ["#", "X", "%", "&", "*", "+", "/", "(", "'", " "]

    # Create ASCII grid
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            brightness = pix[x, y]
            index = min(brightness // 25, len(chars) - 1)  # Ensure index is within bounds
            row.append(chars[index])
        grid.append("".join(row))

    # Write ASCII art to file
    with open(saveas, "w") as art:
        for row in grid:
            art.write(row + "\n")

if __name__ == '__main__':
    asciiConvert("image.jpg", "jpg", "text.txt", 2)
