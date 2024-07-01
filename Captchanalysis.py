from PIL import Image
import numpy as np
import collections

def count_pixel_colors(image_path):
  """
  This function takes an image path as input and returns a dictionary containing
  the number of pixels for each unique color in the image.

  Args:
      image_path: The path to the image file.

  Returns:
      A dictionary where keys are tuples representing RGB values and values are
      integers representing the number of pixels with that color.
  """
  # Open the image and convert it to RGB mode
  image = Image.open(image_path).convert('RGB')

  # Get the image data as a NumPy array
  image_data = np.array(image)

  print(image_data.shape)
  image_data = image_data.reshape(-1, 3)
  
  color_counts = {}
  for colour in image_data:
    if str(colour) not in color_counts:
        color_counts[str(colour)]=1
    else:
        color_counts[str(colour)]+=1
  #color_counts = collections.Counter(image_data)
  
  return color_counts

# Example usage
image_path = "test_captcha.png"
color_counts = count_pixel_colors(image_path)

# Print the color counts
for color, count in color_counts.items():
  print(f"Color: {color} - Count: {count}")
