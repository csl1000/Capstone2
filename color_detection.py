from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
from temp import image_com

sum_list = [0] * 5
ct = ColorThief("C:\\Users\\user\\Desktop\\clothes\\input_1.jpg")
dominant_color = ct.get_color(quality = 1)
(r, g, b) = (dominant_color[0] / 255, dominant_color[1] / 255, dominant_color[2] / 255)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
(h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
print(dominant_color)

index = 0
sum_list[0] = image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_3.jpg")
sum_list[1] = image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_3.jpg")
sum_list[2] = image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_3.jpg")
# sum_list[3] = image_com("C:\\Users\\user\\Desktop\\clothes\\Silk_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Silk_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Silk_3.jpg")
sum_list[3] = image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_3.jpg")

tmp = max(sum_list)
index = sum_list.index(tmp)
if index == 0:
    fabric_type = "Cotton"
elif index == 1:
    fabric_type = "Linen"
elif index == 2:
    fabric_type = "Wool"
# elif index == 3:
    # fabric_type = "Silk"
elif index == 3:
    fabric_type = "Denim"
else:
    fabric_type = "Unknown"
    
sort_list = sorted(sum_list, reverse = True)
for x in sum_list:
    if x == sort_list[1]:
        sec_index = sum_list.index(x)

if sec_index == 0:
    second_type = "Cotton"
elif sec_index == 1:
    second_type = "Linen"
elif sec_index == 2:
    second_type = "Wool"
# elif index == 3:
    # fabric_type = "Silk"
elif sec_index == 3:
    second_type = "Denim"
else:
    second_type = "Unknown"
    
print(fabric_type)
print(second_type)