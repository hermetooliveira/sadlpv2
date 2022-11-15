import os
import tkinter.font as tkFont
from tkinter import *
import requests
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import imutils
import numpy as np
import easyocr

image1 = cv2.imread('images/car1.jpg')
image2 = cv2.imread('images/car2.jpg')
image3 = cv2.imread('images/car3.jpg')

def veiculo01():
    recognitionPlate(image1)

def veiculo02():
    recognitionPlate(image2)  

def veiculo03():
    recognitionPlate(image3)         

def recognitionPlate(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    plt.show()
    bfilter = cv2.GaussianBlur(gray, (11, 11), 0)
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    plt.show()
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:40]
    location = None

    for contour in contours:

        peri = cv2.arcLength(contour, True) 

        if 120 < peri < 2000:   
    
            approx = cv2.approxPolyDP(contour, 0.05*peri, True)        
            if len(approx) == 4:
            
                x,y,w,h = cv2.boundingRect(contour)
                if 2.46 < float(w/h) < 3.70 :                 
                    location = approx
                    break

    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2-10, y1:y2+1]

    ret, cropped_image = cv2.threshold(cropped_image, 60, 255, 0)

    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.show()

    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
   
    #função para remover caracteres especiais
    def removerChar(placa):
        characteres = "!@#$:;'"
        for i in range(0, len(characteres)):
            placa = placa.replace(characteres[i], "")
        return placa

    def substituiChar(placa):
        characteres = "|"
        placa = placa.replace(characteres, "1")
        return placa

    text = result[len(result)-1][-2]

    placa = text.replace(" ", "")
    placa = removerChar(placa)
    placa = substituiChar(placa)

    buscar_veiculo(placa)


def janelaArquivo():
    
    janela = Toplevel()
    janela.title('Arquivo')
    root.geometry('300x300')
    labelFont1 = tkFont.Font(family="Helvetica", size=12, weight=tkFont.BOLD, underline=0, overstrike=0)

    botao = Button(janela, text="Veículo 01", command=veiculo01, width=20, font=labelFont1)
    botao.grid(column=0, row=0, padx=10,pady=10)
    botao.configure(bg='gray', fg='black')

    botao2 = Button(janela, text="Veículo 02", command=veiculo02, width=20, font=labelFont1)
    botao2.grid(column=0, row=1, padx=10,pady=10)
    botao2.configure(bg='gray', fg='black')

    botao3 = Button(janela, text="Veículo 03", command=veiculo03, width=20, font=labelFont1)
    botao3.grid(column=0, row=2, padx=10,pady=10)
    botao3.configure(bg='gray', fg='black')


def buscar_veiculo(texto_placa):
    
    #placa = input('Digite a placa do veículo: ')
    placa = texto_placa
    data = {'placa':placa}
    res = requests.get('http://127.0.0.1:9001/veiculos', json=data)
    returned_data = res.json()
    
    placar = returned_data[0]['placa']
    proprietario = returned_data[0]['proprietario']
    chassi = returned_data[0]['chassi']
    situacao = returned_data[0]['situacao'] 
    marca_modelo_cor = returned_data[0]['marca_modelo_cor']
    
    criarJanelaConsulta(placar,marca_modelo_cor, chassi, situacao)

def criarJanelaConsulta(texto_placa, texto_marca_modelo_cor, texto_chassi, texto_situacao):
    janela = Toplevel()
    janela.title("SADLPV")
    janela.geometry('600x300')

    labelFont3 = tkFont.Font(family="Helvetica", size=20, weight=tkFont.BOLD,
                                underline=0, overstrike=0)

    labelFont1 = tkFont.Font(family="Helvetica", size=12, weight=tkFont.BOLD,
                                underline=0, overstrike=0)  
    labelFont2 = tkFont.Font(family="Helvetica", size=20, weight=tkFont.BOLD,
                                underline=0, overstrike=0)
                                                   
    situacao = Label(janela, text=texto_situacao, width=50, height=2, font=labelFont1)
    situacao.grid(column=0, row=0, padx = 45, pady=10)
    if (texto_situacao == 'VEICULO REGULAR'):
        situacao.configure(bg='green', fg='white')
    if (texto_situacao=="CNH SUSPENSA"):
        situacao.configure(bg='yellow', fg='black')    
    if (texto_situacao=="ROUBO/FURTO!"):
        situacao.configure(bg='red', fg='white')

    botao = Button(janela, text="Efetuar nova Busca", command=janela.destroy, width=20, font=labelFont1)
    botao.grid(column=0, row=4, padx=10,pady=10)
    botao.configure(bg='green', fg='white')

    placa = Label(janela, text=texto_placa, width=10, height=2, font=labelFont3)
    placa.grid(column=0, row = 1, padx=45,pady=10)
    placa.configure(bg='white')
    marca_modelo_cor = Label(janela, text=texto_marca_modelo_cor, font=labelFont1)
    marca_modelo_cor.grid(column=0, row = 2, padx=10,pady=10)

    chassi = Label(janela, text='CHASSI '+ texto_chassi, font=labelFont1)
    chassi.grid(column=0, row = 3, padx=10,pady=10)


    texto_cotacoes = Label(janela, text='')
    texto_cotacoes.grid(column=0, row=5,padx=10,pady=10)

root = Tk()
labelFont1 = tkFont.Font(family="Helvetica", size=12, weight=tkFont.BOLD,
                                underline=0, overstrike=0)
root.title('Teste PhotoImage')
root.geometry('300x300')

textLabel1 = Label(root, text='Busque por uma placa!', font=labelFont1)
textLabel1.grid(column=0, row=0, padx=10, pady=10)
textLabel1.configure(fg='blue')

python_image = PhotoImage(file='images/car.png')

image_label = Label(root, image=python_image)
image_label.grid(column=0,row=1, padx=10, pady=10)

botao = Button(root, text = 'Buscar', command=janelaArquivo, width=20, font=labelFont1)
botao.grid(column=0, row=2, padx=10, pady=10)
botao.configure(bg='green', fg='white')

root.mainloop() 







