def print_results(results_dic, results_stats, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary statistics and (optionally) lists misclassifications.
    results_dic: {filename: [pet_label, classifier_label, match, isdog_pet, isdog_classifier]}
    results_stats: keys include:
      n_images, n_dogs_img, n_notdogs_img, n_match,
      n_correct_dogs, n_correct_notdogs, n_correct_breed,
      pct_match, pct_correct_dogs, pct_correct_breed, pct_correct_notdogs
    """
    print("\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    print(f"{'Number of Images':>28}: {results_stats['n_images']}")
    print(f"{'Number of Dog Images':>28}: {results_stats['n_dogs_img']}")
    print(f"{'Number of Not-a-Dog Images':>28}: {results_stats['n_notdogs_img']}")

    # Print all percentage stats (keys that start with 'pct_')
    for k, v in results_stats.items():
        if k.startswith('pct_'):
            label = k.replace('pct_', 'Pct ').replace('_', ' ').title()
            print(f"{label:>28}: {v:.1f}%")

    # Misclassified Dog vs Not-Dog
    if print_incorrect_dogs and (results_stats['n_correct_dogs'] + results_stats['n_correct_notdogs'] != results_stats['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for fname, vals in results_dic.items():
            # Disagree on dog/not-dog => isdog_pet + isdog_classifier == 1
            if sum(vals[3:]) == 1:
                print(f"[{fname}] pet='{vals[0]}'  classifier='{vals[1]}'")

    # Misclassified Dog Breeds
    if print_incorrect_breed and (results_stats['n_correct_dogs'] != results_stats['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignments:")
        for fname, vals in results_dic.items():
            pet_label, clabel, match, isdog_pet, isdog_cls = vals
            # Both are dogs (2) but breed doesn't match (match == 0)
            if (isdog_pet + isdog_cls) == 2 and match == 0:
                print(f"[{fname}] pet='{pet_label}'  classifier='{clabel}'")
