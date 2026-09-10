def calculate_brightness(img):
    if not img or any(len(row) != len(img[0]) for row in img) or any(not (0 <= pixel <= 255) for row in img for pixel in row):
        return -1
    total_brightness = sum(sum(row) for row in img)
    num_pixels = sum(len(row) for row in img)
    return round(total_brightness / num_pixels, 2)


if __name__ == "__main__":
    img = eval(input())
    print(f"{calculate_brightness(img):.2f}")
