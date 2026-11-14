import cv2
import csv
from itertools import combinations
from pathlib import Path
from zipfile import ZipFile
import numpy as np

input_file = "test-input.zip" if Path("test-input.zip").is_file() else "train-input.zip"
sift = cv2.SIFT_create(nfeatures=150)
matcher = cv2.BFMatcher()

images = {}
with ZipFile(input_file) as archive:
    for member in archive.namelist():
        if not member.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        image = cv2.imdecode(np.frombuffer(archive.read(member), np.uint8), cv2.IMREAD_GRAYSCALE)
        height, width = image.shape
        image = cv2.resize(image, (160, 160), interpolation=cv2.INTER_AREA)
        keypoints, descriptors = sift.detectAndCompute(image, None)
        images[Path(member).name] = (width, width / height, descriptors)

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["image_a", "image_b"])

    for name_a, name_b in combinations(sorted(images), 2):
        width_a, aspect_a, descriptors_a = images[name_a]
        width_b, aspect_b, descriptors_b = images[name_b]

        if width_a == width_b or abs(aspect_a / aspect_b - 1) > 0.015:
            continue

        # Count keypoints of A whose best match in B is clearly better than the second best
        matches = matcher.knnMatch(descriptors_a, descriptors_b, k=2)
        
        good = 0
        for best, second in matches:
            if best.distance < 0.75 * second.distance:
                good = good + 1

        if good >= 45:
            writer.writerow([name_a, name_b])
