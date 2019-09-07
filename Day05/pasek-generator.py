from PIL import ImageDraw, ImageFont, Image

image = Image.open("pasek.jpg")
font = ImageFont.truetype("trebuc.ttf", size=44)

text = "python jest super"
draw = ImageDraw.Draw(image)
draw.text( (200,480), text.upper(), font=font, fill='rgb(255,255,255)' )

image.save('wynik.jpg')

print("Done!")

