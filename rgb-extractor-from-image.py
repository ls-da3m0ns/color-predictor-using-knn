from colorthief import ColorThief

path = input("path to image :")
color_thief = ColorThief(path)
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)
print("Most prominant colour is :{}".format(palette[0]))
print("other colors were ")
for color in palette[1:]:
    print(color)