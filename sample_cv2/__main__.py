# coding: utf-8

import cv2


print("Please input file path")
input_filepath = input()
img1 = cv2.imread(input_filepath)

print("Please template file path")
template_filepath = input()
img2 = cv2.imread(template_filepath)

result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(result)  # min_val, max_val, min_loc, max_loc

print("result: " + str((max_loc[0], max_loc[1])))
