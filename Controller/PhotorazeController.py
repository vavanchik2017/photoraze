from Model.PhotorazeModel import ImageModel

URL = '../images/1.jpg'
img = ImageModel(URL, 'baza.jpg', ['paper', 'info'])

#img.save()
#img.delete()
#img.update('test tes test st st')
print(img.read())