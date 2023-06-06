from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
from temp import image_com

input_image = "C:\\Users\\user\\Desktop\\clothes\\input_3.jpg"
sum_list = [0] * 10
ct = ColorThief(input_image)
dominant_color = ct.get_color(quality = 1)
(r, g, b) = (dominant_color[0] / 255, dominant_color[1] / 255, dominant_color[2] / 255)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
(h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
print(dominant_color)

index = 0
sum_list[0] = image_com("C:\\Users\\user\\Desktop\\clothes\\Acrylic_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Acrylic_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Acrylic_3.jpg")
sum_list[1] = image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Cotton_3.jpg")
sum_list[2] = image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Denim_3.jpg")
sum_list[3] = image_com("C:\\Users\\user\\Desktop\\clothes\\Gimo_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Gimo_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Gimo_3.jpg")
sum_list[4] = image_com("C:\\Users\\user\\Desktop\\clothes\\Leather_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Leather_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Leather_3.jpg")
sum_list[5] = image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Linen_3.jpg")
sum_list[6] = image_com("C:\\Users\\user\\Desktop\\clothes\\Nylon_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Nylon_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Nylon_3.jpg")
sum_list[7] = image_com("C:\\Users\\user\\Desktop\\clothes\\Poly_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Poly_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Poly_3.jpg")
sum_list[8] = image_com("C:\\Users\\user\\Desktop\\clothes\\Rayon_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Rayon_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Rayon_3.jpg")
sum_list[9] = image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_1.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_2.jpg") + image_com("C:\\Users\\user\\Desktop\\clothes\\Wool_3.jpg")

tmp = max(sum_list)
index = sum_list.index(tmp)
if index == 0:
    fabric_type = "Acrylic"
elif index == 1:
    fabric_type = "Cotton"
elif index == 2:
    fabric_type = "Denim"
elif index == 3:
    fabric_type = "Gimo"
elif index == 4:
    fabric_type = "Leather"
elif index == 5:
    fabric_type = "Linen"
elif index == 6:
    fabric_type = "Nylon"
elif index == 7:
    fabric_type = "Poly"
elif index == 8:
    fabric_type = "Rayon"
elif index == 9:
    fabric_type = "Wool"    
else:
    fabric_type = "Unknown"
    
sort_list = sorted(sum_list, reverse = True)
for x in sum_list:
    if x == sort_list[1]:
        sec_index = sum_list.index(x)

if dominant_color[2] > dominant_color[0]:
    if dominant_color[2] > dominant_color[1]:
        sec_index = 2

if sec_index == 0:
    second_type = "Acrylic"
elif sec_index == 1:
    second_type = "Cotton"
elif sec_index == 2:
    second_type = "Denim"
elif sec_index == 3:
    second_type = "Gimo"
elif sec_index == 4:
    second_type = "Leather"
elif sec_index == 5:
    second_type = "Linen"
elif sec_index == 6:
    second_type = "Nylon"
elif sec_index == 7:
    second_type = "Poly"
elif sec_index == 8:
    second_type = "Rayon"
elif sec_index == 9:
    second_type = "Wool"  
else:
    second_type = "Unknown"     
    
print("The fabric type is : ", fabric_type)
print("Recommendation : ", second_type)
#return dominant_color[0], dominant_color[1], dominant_color[2], fabric_type, second_type