import json
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import soundfile as sf
from playsound import playsound
import time

wait = time.sleep

ben = "http://benbotfn.tk/api/v1"

nombre = ""
lenguaje = ""

def borrar(file):
    os.close(file)
    os.remove(file)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def buscar(nombre, lenguaje):
    
    parameters = {
        "name": nombre,
        "lang": lenguaje
    }

    response = requests.get("http://benbotfn.tk/api/v1/cosmetics/br/search", params=parameters)
    jprint(response.json())
    imagenDic = response.json()["icons"]
    imagenUrl = imagenDic.get("icon")
    
    r = requests.get(imagenUrl, allow_redirects=True)

    open("C:\\Windows\\Temp\\imagen.png", "wb").write(r.content)
    print ("Buscaste: " + nombre + " \nIdioma: " + lenguaje)

    
    img = mpimg.imread("C:\\Windows\\Temp\\imagen.png")
    imgplot = plt.imshow(img)
    plt.show()
    
    os.remove("C:\\Windows\\Temp\\imagen.png")

def aes(write,numAes):
        
    response = requests.get("http://benbotfn.tk/api/v1/aes")
    jprint(response.json()[numAes])
    if write:
        open("aesKey.txt", "a")
        f = open("aesKey.txt", "w")
        text = json.dumps(response.json()[numAes], sort_keys=True, indent=4)
        f.write(text)
        print("Archivo guardado con la aes key solicitada")

def tienda(lang):
    response = requests.get("http://benbotfn.tk/api/v1/shop/br")
    jprint(response.json())

def export(path, lang, type):
    parameters = {
        "path": path,
        "lang": lang
    }
    response = requests.get(ben + "/exportAsset", params=parameters)
    print(response)

    if type == "image":
        open("C:\\Windows\\Temp\\imagen.png", "wb").write(response.content)
        img = mpimg.imread("C:\\Windows\\Temp\\imagen.png")
        imgplot = plt.imshow(img)
        plt.show()
        os.remove("C:\\Windows\\Temp\\imagen.png")
    elif type == "audio":
        open("C:\\Windows\\Temp\\audio.ogg", "wb").write(response.content)
        # Extract audio data and sampling rate from file 
        data, fs = sf.read(r"C:\\Windows\\Temp\\audio.ogg")
        #Remover audio para evitar gastadera de espacio
        os.remove("C:\\Windows\\Temp\\audio.ogg")
        # Save as wav file at correct sampling rate
        sf.write(r"C:\\Windows\\Temp\\audio.wav", data, fs)
        playsound(r"C:\\Windows\\Temp\\audio.wav")
        wait(2)
        #borrar(r"C:\\Windows\\Temp\\audio.wav")

def newCosmetics():
    response = requests.get(ben + "/newCosmetics")
    jprint(response.json())

def getIcon(name, lang):
    parameters1 = {
        "name": name,
        "lang": lang,
    }
    
    responseName = requests.get("http://benbotfn.tk/api/v1/cosmetics/br/search", params=parameters1)
    path = responseName.json()["path"]
    
    parameters = {
        "path": path,
        "lang": lang
    }
    response = requests.get(ben + "/exportAsset", params=parameters)

    open("C:\\Windows\\Temp\\imagen.png", "wb").write(response.content)
    img = mpimg.imread("C:\\Windows\\Temp\\imagen.png")
    imgplot = plt.imshow(img)
    os.system("open -a Python")
    plt.show()
    os.remove("C:\\Windows\\Temp\\imagen.png")

    print(response)
    print(path)




