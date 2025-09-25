import os
from classifier import classifier
def classify_images(images_dir, results_dic, model):
    for filename, value in results_dic.items():
        image_path = os.path.join(images_dir, filename)
        clabel = classifier(image_path, model)
        pet_label = value[0]
        match = 1 if (pet_label in clabel or clabel in pet_label) else 0
        results_dic[filename].extend([clabel, match])
