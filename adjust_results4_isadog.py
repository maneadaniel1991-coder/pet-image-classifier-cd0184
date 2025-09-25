def adjust_results4_isadog(results_dic, dogfile):
    dognames = set()
    with open(dogfile, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip().lower()
            if name:
                dognames.add(name)
    for _, values in results_dic.items():
        pet_label = values[0]
        classifier_label = values[1] if len(values) > 1 else ""
        isdog_pet = 1 if pet_label in dognames else 0
        isdog_classifier = 1 if any(part.strip() in dognames for part in classifier_label.split(",")) else 0
        values.extend([isdog_pet, isdog_classifier])
