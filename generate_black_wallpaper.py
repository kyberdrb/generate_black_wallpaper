#!/usr/bin/python

# create a repository to generate a black wallpaper of custom resolution if provided (default: current screen resolution) to custom path if provided (default: script dir)

from PIL import Image
img = Image.new('RGB', (720, 1280), (0, 0, 0))
img.save("/home/laptop/Downloads/black_wallpaper-720x1280.png", "PNG")

# Sources
# - https://duckduckgo.com/?q=generate+single+solid+color+image+python&ia=web
# - https://stackoverflow.com/questions/38900511/how-to-create-a-new-color-image-with-python-imaging#38900699
# - https://duckduckgo.com/?q=python+PIL+save+image+as+png&ia=web&iax=qa
# - https://stackoverflow.com/questions/19651055/saving-image-with-pil#19651233
# - https://www.gsmarena.com/compare.php3?idPhone1=8438&idPhone2=7760&idPhone3=8596#j330f-ds,j320f,g3121
