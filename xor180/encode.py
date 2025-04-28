# Usage : python3 encode.py file_to_encode.jpg encoded_file.png

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
    print("Usage: python3 encode.py file_to_encode.jpg encoded_file.png")
    exit(1)

img_input_filename = sys.argv[1]
img_output_filename = sys.argv[2]

img_input = cv2.imread(img_input_filename)
print(img_input.shape)

# Generate a random noise
r = 255 * np.random.rand(*img_input.shape)
img_random = r.astype(np.uint8)
print(img_random.shape)
img_random_rot180 = np.flip(np.flip(img_random, 1), 0) # 2 symmetries along each direction = rot180
print(img_random_rot180.shape)

# case A xor B = C
img_output = cv2.bitwise_xor(img_input, img_random, mask = None)

img_output = np.concatenate((img_output, img_random_rot180))

cv2.imwrite(img_output_filename, img_output)

cv2.imshow("img_input", img_input)
cv2.imshow("img_output", img_output)

print("Press any key to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()
