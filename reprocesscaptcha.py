import cv2
import collections

def dominant_color_image(image_path):
  """
  This function takes an image path as input and returns a new image containing
  only the dominant color found in the grayscale version of the original image.

  Args:
      image_path: The path to the image file.

  Returns:
      A new image containing only the dominant color (BGR format).
  """

  # Read the image in grayscale
  image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

  # Count pixel occurrences for each intensity value
  color_counts = collections.Counter(image.flatten())

  # Find the most frequent intensity value (dominant color in grayscale)
  dominant_intensity = color_counts.most_common(2)[1][0]
  #print(dominant_intensity)
  # Read the image again in color
  image = cv2.imread(image_path,  cv2.IMREAD_GRAYSCALE)

  # Create a mask where only pixels with dominant intensity remain non-zero
  mask = cv2.inRange(image, int(dominant_intensity)-1, int(dominant_intensity)+1)
  dominant_color_image = cv2.bitwise_and(image, image, mask=mask)

  return dominant_color_image

# Example usage
image_path = "test_captcha.png"
dominant_image = dominant_color_image(image_path)

# Save or display the dominant color image (BGR format)
cv2.imwrite("dominant_color.jpg", dominant_image)
# Or use cv2.imshow to display the image
