# Usage : python3 decode.py file_to_decode.jpg decoded_file.png

# XOR an image with its 180 rotated version, here below B is simple the 180-rotation of A
# A xor B = C
# C xor B = A
# A xor C = B
# C xor A = B

import cv2
import numpy as np
import sys

#print(sys.argv, len(sys.argv))
if len(sys.argv) != 3:
    print("Usage: python3 decode.py file_to_decode.jpg decoded_file.png")
    exit(1)

img_input_filename = sys.argv[1]
img_output_filename = sys.argv[2]

img_input = cv2.imread(img_input_filename)
#print(img_input.shape)
img_input_rot180 = cv2.rotate(img_input, cv2.ROTATE_180)

# case A xor B = C
img_output_xor = cv2.bitwise_xor(img_input, img_input_rot180, mask = None)
cv2.imwrite(img_output_filename, img_output_xor)

cv2.imshow("img_input", img_input)
cv2.imshow("img_output_xor", img_output_xor)

print("Press any key to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()
