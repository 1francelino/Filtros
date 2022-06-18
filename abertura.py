from PIL import Image,ImageFilter
from utils import in_file, out_file

menu = 0
while menu != 5:
    print("Filtros: 1 - Cinza \n 2 - Negativo \n 3 - Something \n 4 - Something Else \n")
    menu = (int(input('Selecione um filtro:')))
    
    def escalacinza(colored):
        w, h = colored.size
        img = Image.new("RGB", (w, h))

        for x in range(w):
            for y in range(h):
                pxl = colored.getpixel((x,y))
                lum = (pxl[0] + pxl[1] + pxl [2])//3
                img.putpixel((x,y), (lum,lum,lum))
        return img
    imagem = Image.open(in_file("hilda.jpg"))
    pb_imagem = escalacinza(imagem)
    pb_imagem.save(out_file("pb_hilda2.jpg"))

    def negative(img:Image) -> Image:
        neg = Image.new(img.mode, img.size, "red")
        w, h = img.size
        for i in range(w):
            for j in range(h):
                r,g,b = img.getpixel((i,j))
                neg.putpixel((i,j), (255-r, 255-g, 255-b))
        return neg
    imagem = Image.open(in_file("selfie.jpg"))
    pb_imagem = negative(imagem)
    pb_imagem.save(out_file("neg_selfie.jpg"))


## esse é um teste de função que copiei de algum lugar ontem,mas nao cheguei a arrumar pra funcionar no nosso
def binarizacao(limiar):
    print("Processando binarização...")
    # Convertendo em escala de cinza
    #cinza()
    # Percorrendo Matriz de Pixels
    w, h = colored.size
    img = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            # Obtendo componentes RGB pixel atual
            R, G, B = imagem.getpixel((x, y))
            # Modificando componentes RGB do pixel atual
            if ((R + G + B) / 3 <= limiar):
                imagem.putpixel((x, y), (0, 0, 0))
            else:
                imagem.putpixel((x, y), (255, 255, 255))
    # Exibindo imagem modificada
    imagem.show()
#}
#binarizacao(120)


if menu == 1:
    escalacinza()
elif menu == 2:
    negative()
elif menu == 3:
    teste()

##elif menu == 4:
