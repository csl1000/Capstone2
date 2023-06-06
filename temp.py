import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지 읽어오기
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