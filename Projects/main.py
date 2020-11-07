from PIL import Image,ImageFilter
img=Image.open('./Pokedox/pikachu.jpg')

filtered_img=img.filter(ImageFilter.SHARPEN)
crooked=filtered_img.rotate(96)
filtered_img.save("blur.png","png")

resize=filtered_img.resize((300,300))
resize.save("reduced-size.png",'png')

crooked.save("rotated-img.png",'png')
converted_img=img.convert('L')
converted_img.save("greyImage.png",'png') # gives the new file name followed by the etension
print(img.format)
print(img.size)
print(img.mode)

#filtered_img.show() #displays the real image.
#crooked.show()
#resize.show()
#--------------------------------CROP
boxArea=(100,100,400,400)
croppedRegion=crooked.crop(boxArea)

croppedRegion.save("cropped.png",'png')
croppedRegion.show()

#---------------------Maintain Aspect Ratio.
img2=Image.open('./Pokedox/squirtle.jpg')
img.thumbnail((400, 200))
img.save('thumbnail.jpg')


