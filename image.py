from PIL import Image, ImageFilter

img = Image.open('./Pokedex/004 pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
# filtered_img.rotate(90)
# filtered_img.resize((300, 300))
# filtered_img.show()
# # filtering
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
print(img.format)
print(img.size)
print(img.mode)
