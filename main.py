from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from exif import Image

import os

def watermark_photo(input_image_path,
                    watermark_image_path):

    from PIL import Image
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    # add watermark to your image
    watermark = watermark.resize(size=(200, 200))
    base_image.paste(watermark, (0, base_image.height - watermark.height))
    # base_image.show()
    base_image.save(input_image_path)


def watermark_text(input_image_path,
                   output_image_path,
                   text,
                   font):

    from PIL import Image
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    font = ImageFont.truetype(font, 40)
    drawing.text((photo.width - len(text) * 22, photo.height - 50), text, fill="orange", font=font)
    # photo.show()
    photo.save(output_image_path)


def getTime(img):
    with open(img, "rb") as palm_1_file:
        palm_1_image = Image(palm_1_file)
        print(f"{palm_1_image.datetime_original}")
        time2 = f"{palm_1_image.datetime_original}"
        return time2


if __name__ == '__main__':
    print("Привет омлет!")
    print("Это генератор ватермарки на твои фотки от")
    print("░█████╗░░█████╗░██████╗░████████╗░█████╗░██╗███╗░░██╗  ██╗░░██╗██████╗░██╗░░░██╗░██████╗░░█████╗░")
    print("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║████╗░██║  ██║░██╔╝██╔══██╗╚██╗░██╔╝██╔════╝░██╔══██╗")
    print("██║░░╚═╝███████║██████╔╝░░░██║░░░███████║██║██╔██╗██║  █████═╝░██████╔╝░╚████╔╝░██║░░██╗░███████║")
    print("██║░░██╗██╔══██║██╔═══╝░░░░██║░░░██╔══██║██║██║╚████║  ██╔═██╗░██╔══██╗░░╚██╔╝░░██║░░╚██╗██╔══██║")
    print("╚█████╔╝██║░░██║██║░░░░░░░░██║░░░██║░░██║██║██║░╚███║  ██║░╚██╗██║░░██║░░░██║░░░╚██████╔╝██║░░██║")
    print("░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝")
    print("ps ищите меня в телеграмме https://www.t.me/captainkryga")
    print("#####################################")
    print("#####################################")
    print("#####################################")

    WaterMark = 'watermark.jpg'
    Format = 'jpg'
    Font = "font.ttf"
    # Rotate = 90

    import sys
    if (len(sys.argv) > 1 and sys.argv[1] == "-h"):
        print("Если у тебя изменились вводные данные используй инструкции ниже, заменяя то что в кавычках")
        print(f">>> стандартный формат файлов {Format}, для замены в командной строке допиши вот это")
        print("-f${формат файлов}")
        print(f">>> стандартный шрифт должен быть в папке и называется {Font}, для замены в командной строке допиши вот это")
        print("-t${название и путь к шрифту полностью}")
        print(f">>> стандартная ватермарка должна быть в папке и называтся {WaterMark}, для замены в командной строке допиши вот это")
        print("-w${название и путь к ватермарке}")
        # print(f">>> стандартный поворот {Rotate} градусов, для замены в командной строке допиши вот это")
        # print("-r${градус}")
        exit(0)



    for arg in sys.argv:
        if (len(arg) > 3 and arg[0] == '-' and arg[1] == 'f'):
            Format = arg.split('$')[1]
        if (len(arg) > 3 and arg[0] == '-' and arg[1] == 't'):
            Font = arg.split('$')[1]
        if (len(arg) > 3 and arg[0] == '-' and arg[1] == 'w'):
            WaterMark = arg.split('$')[1]
        # if (len(arg) > 3 and arg[0] == '-' and arg[1] == 'r'):
        #     Rotate = float(arg.split('$')[1])

    print(f"Формат на эту сессию: {Format}")
    print(f"Шрифт на эту сессию: {Font}")
    print(f"Ватермарка на эту сессию: {WaterMark}")
    # print(f"Угол поворота: {Rotate}")


    FolderImport = input("Напиши название папки где храняться фотки: ")
    FolderExport = input("Напиши название папки сохранять файлы: ")

    if not os.path.exists(FolderImport):
        os.mkdir(FolderImport)
    if not os.path.exists(FolderExport):
        os.mkdir(FolderExport)

    import os

    for file in os.listdir(FolderImport):
        if file.endswith(Format):
            print(os.path.join(FolderImport, file))
            watermark_text(os.path.join(FolderImport, file),
                           os.path.join(FolderExport, file),
                           getTime(os.path.join(FolderImport, file)),
                           Font)
            watermark_photo(os.path.join(FolderExport, file), WaterMark)