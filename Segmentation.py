from  PIL  import  Image
from  pylab  import  *
from numpy import *


im  =  array(Image.open('lena.jpg').convert('L'))

    
imshow(im)

show()
