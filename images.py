import cv2
import sys


image_path = "Images/image1.jpg" 

# Load the image using OpenCV
img = cv2.imread(image_path)

# Verify that the image loaded successfully
if img is None:
    print(f"Error: Could not load image from {image_path}.")
    print("Ensure you have an image named 'image1.jpg' inside the 'Images' folder.")
    sys.exit()

print("Image loaded successfully. Press any key on the image window to close it.")

# Display the image in a new window
cv2.imshow("Loaded Image", img)

# Wait for a key press infinitely, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
