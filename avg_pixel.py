#!/usr/bin/env python3
import imageio
import numpy as np
from pathlib import Path

faces = []

DATA_PATH = 'assets/faces/' # make sure all images have the same size (w x h)
NEW_FACE_URI = 'out.png'
SUFFIXES = ['.png', '.jpg']

try: 
    paths = [path for path in Path(DATA_PATH).iterdir() if path.suffix in SUFFIXES]
    n = len(paths)
    print(f"{n} faces is used to generate this output")
    
except FileNotFoundError:
    print(f"Could not find the directory {DATA_PATH}")

for posix_path in paths:
    path = str(posix_path)
    faces.append(imageio.imread(path))
    # print(f"Added {path} to output")

faces_sum = np.sum( [face for face in faces], axis=0, dtype=np.int32)
np.floor_divide(faces_sum, n)
imageio.imwrite(NEW_FACE_URI, faces_sum)

