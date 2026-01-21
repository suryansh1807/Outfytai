# mltagging.py
import cv2
import numpy as np

def tag_clothing_image(image_path: str) -> dict:
    """
    Analyze clothing image and return basic tags.
    """

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found")

    img_resized = cv2.resize(img, (224, 224))

    avg_color = img_resized.mean(axis=(0, 1))
    brightness = np.mean(cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY))

    tags = {
        "dominant_color": f"RGB{tuple(avg_color.astype(int))}",
        "brightness": round(float(brightness), 2)
    }

    return tags
