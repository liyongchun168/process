from  PIL  import  Image
from  pylab  import  *
from numpy import *

im  =  array(Image.open('lena.jpg'))
#im  =  array(Image.open('tree.jpg'))

#print im.shape,im.dtype

im2 =  255-im
im3 =  (100.0/255) * im +100
im4 = 255.0 * (im/255.0)**2

print int(im2.min()),int(im2.max())

imshow(im4)
#print  'Please  click  3  points'
#x  =  ginput(3)
#print  'you  clicked:',x
show()