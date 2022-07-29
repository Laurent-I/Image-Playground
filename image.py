from PIL import Image, ImageFilter
img = Image.open('./Pokedex/004 pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
print(img.format)
print(img.size)
print(img.mode)
