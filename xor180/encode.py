"""Encode a photo with XOR+180+RANDOM operations"""

import sys
import cv2
import numpy as np

# Check parameters
if len(sys.argv) != 3:
    print(sys.argv[0], ": Encode a photo with XOR+180+RANDOM operations")
    print("Usual image formats are supported (jpg, png, gif...).")
    print("Usage: python3", sys.argv[0], "file_to_encode.jpg encoded_file.png")
    sys.exit(1)

# Get parameter filenames
img_input_filename = sys.argv[1]
img_output_filename = sys.argv[2]

# Read input photo
img_input = cv2.imread(img_input_filename)
#print(img_input.shape)

# Generate a random noise
r = 255 * np.random.rand(*img_input.shape)
img_random = r.astype(np.uint8)
#print(img_random.shape)

# Duplicate the random noise photo with a 180° rotation
img_random_rot180 = np.flip(np.flip(img_random, 1), 0) # 2 symmetries along each direction = rot180
#print(img_random_rot180.shape)

# Perform the xor operation between the input photo and the random noise
img_output = cv2.bitwise_xor(img_input, img_random, mask = None)

# Concatenate the above xor result photo with the 180° random noise photo
img_output = np.concatenate((img_output, img_random_rot180))

# Save the result in the output photo file
cv2.imwrite(img_output_filename, img_output)

# Display results
cv2.imshow("img_input", img_input)
cv2.imshow("img_output", img_output)

print("Press any key to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()
