import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_list.append(new_color)

print(rgb_list)
