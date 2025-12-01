from PIL import Image
while True:
    try:
        img=input ("Введите название изображения из папки Photo (без .jpg) ")
        im = Image.open("Photo/"+img+".jpg")
        im.show()
        print(im.format, im.size, im.mode)
        break
    except Exception as e:
        print("Попробуйте снова ошибка-", e)
while True:
    try:
        a = input("Инвертировать цвета(1), зеркально отобразить(2), черно-белое (3)")
        if a == "1":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
            im.show()
            break
        elif a == "2":
            pixels = list(im.getdata())
            w, h = im.size
            rows = [pixels[i * w: (i + 1) * w] for i in range(h)]
            flipped_rows = [row[::-1] for row in rows]
            new_pixels = [pix for row in flipped_rows for pix in row]
            new_img = Image.new(im.mode, (w, h))
            new_img.putdata(new_pixels)
            new_img.show()
            im = new_img
            im.show()
            break
        elif a=="3":
            im = im.convert("L")
            im.show()
            break
        else:
            print("1,2 или 3!!!")
    except Exception as e:
        print("Попробуй снова ошибка-", e)