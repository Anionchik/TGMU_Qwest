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

