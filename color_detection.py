from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import cv2
import numpy as np

def image_com(image):
    from color_detection import input_image
    result = 0
    imgs = []
    imgs.append(cv2.imread(image, cv2.COLOR_BGR2GRAY))
    imgs.append(cv2.imread(input_image, cv2.COLOR_BGR2GRAY))
    
    hists = []
    for img in imgs:
        # BGR -> HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # 히스토그램 연산 (파라미터 순서 : 이미지, 채널, Mask, 크기, 범위)
        hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        # 정규화 (파라미터 순서 : 정규화 전 데이터, 정규화 후 데이터, 시작 범위, 끝 범위, 정규화 알고리즘)
        cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
        hists.append(hist)
    
    # 1번째 이미지 : 원본 비교 대상
    query = hists[0]
    
    # 비교 알고리즘의 이름들을 리스트에 저장
    methods = ['CORREL', 'CHISQR', 'INTERSECT', 'BHATTACHARYYA', 'EMD']
    
    # 5회 반복(5개 비교 알고리즘)
    for index, name in enumerate(methods):
        # 비교 알고리즘 이름 출력(문자열 포맷팅 및 탭 적용)
        #print('%-10s' % name, end = '\t')  
        
        # 2회 반복(2장의 이미지에 대해 비교 연산 적용)
        for i, histogram in enumerate(hists):
            ret = cv2.compareHist(query, histogram, index) 
            
            if index == cv2.HISTCMP_INTERSECT:
                ret = ret/np.sum(query)                          # 1로 정규화
                
            if index == cv2.HISTCMP_BHATTACHARYYA:
                if i == 1:
                    result = ret
                
            #print("img%d :%7.2f"% (i+1 , ret), end='\t')
    
        #print()     
    
    return result

# 입력 사진이 들어가는 부분. 이 부분만 수정하면 됩니다
input_image = "input_3.jpg"

sum_list = [0] * 10
ct = ColorThief(input_image)
dominant_color = ct.get_color(quality = 1)
(r, g, b) = (dominant_color[0] / 255, dominant_color[1] / 255, dominant_color[2] / 255)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
(h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
#print(dominant_color)

index = 0
sum_list[0] = image_com("Acrylic_1.jpg") + image_com("Acrylic_2.jpg") + image_com("Acrylic_3.jpg")
sum_list[1] = image_com("Cotton_1.jpg") + image_com("Cotton_2.jpg") + image_com("Cotton_3.jpg")
sum_list[2] = image_com("Denim_1.jpg") + image_com("Denim_2.jpg") + image_com("Denim_3.jpg")
sum_list[3] = image_com("Gimo_1.jpg") + image_com("Gimo_2.jpg") + image_com("Gimo_3.jpg")
sum_list[4] = image_com("Leather_1.jpg") + image_com("Leather_2.jpg") + image_com("Leather_3.jpg")
sum_list[5] = image_com("Linen_1.jpg") + image_com("Linen_2.jpg") + image_com("Linen_3.jpg")
sum_list[6] = image_com("Nylon_1.jpg") + image_com("Nylon_2.jpg") + image_com("Nylon_3.jpg")
sum_list[7] = image_com("Poly_1.jpg") + image_com("Poly_2.jpg") + image_com("Poly_3.jpg")
sum_list[8] = image_com("Rayon_1.jpg") + image_com("Rayon_2.jpg") + image_com("Rayon_3.jpg")
sum_list[9] = image_com("Wool_1.jpg") + image_com("Wool_2.jpg") + image_com("Wool_3.jpg")

tmp = max(sum_list)
index = sum_list.index(tmp)

if dominant_color[2] > dominant_color[0]:
    if dominant_color[2] > dominant_color[1]:
        index = 2

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
        sec_index = sum_list.index(tmp)

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
    
#print("The fabric type is :", fabric_type)
#print("Recommendation :", second_type)
def result_return():
    return dominant_color[0], dominant_color[1], dominant_color[2], fabric_type, second_type

result_return()