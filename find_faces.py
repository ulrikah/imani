#!/usr/bin/env python3
from PIL import Image
import face_recognition
import argparse

# from face_recognition examples: https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("assets/klst/klst2.jpg")
size = (100, 100)

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
face_locations = face_recognition.face_locations(image)

print("Found {} face(s) in this photograph.".format(len(face_locations)))

i = 0
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image = pil_image.resize(size)
    pil_image = pil_image.convert('1') # convert to bw
    pil_image.save(f"assets/klst/faces_bw/face{i}.png")
    # pil_image.show()
    i += 1