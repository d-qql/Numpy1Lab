from PIL import Image
import numpy as np

imgname = "lunar03"
# считаем картинку в numpy array
img = Image.open("lunar_images/" + imgname + "_raw.jpg")
data = np.array(img)

minelem = data[0][0]
maxelem = data[0][0]
for i in data:
    for j in i:
        if j>maxelem:
            maxelem = j
        if j<minelem:
            minelem = j
newdata = np.array([[np.uint8((j-minelem)*255/(maxelem-minelem)) for j in i] for i in data])
res_img = Image.fromarray(newdata)
res_img.save(imgname + "_res.jpg")


