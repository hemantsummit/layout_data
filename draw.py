from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


newImg  = Image.open("./abc.jpg").convert("RGB")
image = ImageDraw.Draw(newImg)
box = [92.0, 58.0, 165.0, 44.0]
image.rectangle(box, outline="blue", width=2)


newImg.show()