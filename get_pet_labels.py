import os, re
def get_pet_labels(image_dir: str):
    results = {}
    for fname in os.listdir(image_dir):
        if fname.startswith('.'): continue
        path = os.path.join(image_dir, fname)
        if os.path.isfile(path):
            stem = os.path.splitext(fname)[0]
            words = re.findall(r'[A-Za-z]+', stem)
            label = " ".join(w.lower() for w in words).strip()
            results[fname] = [label]
    return results
