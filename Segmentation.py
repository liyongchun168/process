from  PIL  import  Image
from  pylab  import  *
from numpy import *


im  =  array(Image.open('lena.jpg'))


for i in range(0,im.shape[0]):
    for j in range(0,im.shape[1]):
        grey  =   (int(im[i,j,0])+int(im[i,j,1])+int(im[i,j,2]))/3  
        im[i,j,0]   =   grey
        im[i,j,1]   =   grey
        im[i,j,2]   =   grey
    
    
imshow(im)

show()

