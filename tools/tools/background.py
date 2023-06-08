import cv2
import numpy as np

def remove_background(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Create a mask to specify the areas to be marked as background or foreground
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangle that contains the foreground object
    rectangle = (10, 10, image.shape[1]-10, image.shape[0]-10)

    # Apply the GrabCut algorithm to segment the foreground object
    cv2.grabCut(image, mask, rectangle, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where 0 and 2 indicate background, while 1 and 3 indicate foreground
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)

    # Apply the mask to the original image
    result = image * mask[:, :, np.newaxis]

    # Set the background to white
    result[np.where((result == [0, 0, 0]).all(axis=2))] = [255, 255, 255]

    return result

# Path to the image file
image_path = "test.JPEG"

# Call the function to remove the background
result_image = remove_background(image_path)

# Display the original image and the result
cv2.imshow("Original Image", cv2.imread(image_path))
cv2.imshow("Result", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the resulting image as "final.jpg"
cv2.imwrite("final.jpg", result_image)
print("Result saved as final.jpg")