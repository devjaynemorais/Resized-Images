import os, sys
from PIL import Image
import glob, os

#Tamanho desejado para redimensionamento
size = 128, 128

#Diretório onde as imagens que serão redimensionadas se encontram
files = os.listdir("/home/jayne/Documentos/ECOMAPSS/Historia")
print(files)
count = 0
for infile in files:
    count = count + 1
    print "----------------------"
    print count
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            #Extensão do arquivo
            im.save(outfile, "PNG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
