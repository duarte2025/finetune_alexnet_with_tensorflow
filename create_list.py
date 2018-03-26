import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
import glob
import pickle


if __name__ == '__main__':
    """
    for testing
    """

    folder = 'bus'
    #img = [im for im in os.scandir('bus')][0]
    pathBus = '/home/duarte/projetinho/Dataset/MIO-TCD-Classification/train/bus/*.jpg'
    pathTruck = '/home/duarte/projetinho/Dataset/MIO-TCD-Classification/train/articulated_truck/*.jpg'
    busIm = glob.glob(pathBus)
    truckIm = glob.glob(pathTruck)
    arq_train = open("train.txt", "w")
    arq_test = open("test.txt", "w")
    p = int(0.1*len(busIm)) + int(0.1*len(truckIm))
    cont = 0
    for img in busIm:
        if cont < p:
            arq_test.write(img)
            arq_test.write(' 1')
            arq_test.write('\n')
        else:
            arq_train.write(img)
            arq_train.write(' 1')
            arq_train.write('\n')
        cont+=1
    cont = 0
    for img in truckIm:
        if cont < p:
            arq_test.write(img)
            arq_test.write(' 0')
            arq_test.write('\n')
        else:
            arq_train.write(img)
            arq_train.write(' 0')
            arq_train.write('\n')
        cont+=1
        #arq.write(img)
        #arq.write('\n')
    arq_test.close()
    arq_train.close()
