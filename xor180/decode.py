import cv2
import sys

# Check parameters
if len(sys.argv) != 3:
    print(sys.argv[0], ": Decode a XOR+180 encoded photo")
    print("Usual image formats are supported (jpg, png, gif...).")
    print("Usage: python3", sys.argv[0], "file_to_decode.jpg decoded_file.png")
    exit(1)

# Get parameter filenames
img_input_filename = sys.argv[1]
img_output_filename = sys.argv[2]

# Read input photo
img_input = cv2.imread(img_input_filename)
#print(img_input.shape)

# Duplicate input photo to a 180 version
img_input_rot180 = cv2.rotate(img_input, cv2.ROTATE_180)

# Perform the xor operation between the 2 photos
img_output_xor = cv2.bitwise_xor(img_input, img_input_rot180, mask = None)

# Save the result in the output photo file
cv2.imwrite(img_output_filename, img_output_xor)

# Display results
cv2.imshow("img_input", img_input)
cv2.imshow("img_output_xor", img_output_xor)

print("Press any key to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()
