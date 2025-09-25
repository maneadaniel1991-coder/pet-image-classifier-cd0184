def print_results(results_dic, results_stats, model, print_misclassified=False):
    print("\n*** Results Summary for CNN Model:", model.upper(), "***")
    print(f"Images: {results_stats['n_images']} | Dogs: {results_stats['n_dogs_img']} | Not-dogs: {results_stats['n_notdogs_img']}")
    print(f"Pct match: {results_stats['pct_match']:.1f}%")
    print(f"Pct correct dogs: {results_stats['pct_correct_dogs']:.1f}% | "
          f"Pct correct breed: {results_stats['pct_correct_breed']:.1f}% | "
          f"Pct correct not-dogs: {results_stats['pct_correct_notdogs']:.1f}%")
    if print_misclassified:
        print("\n-- Misclassified Dogs --")
        for fname, v in results_dic.items():
            pet_label, clabel, match, isdog_pet, isdog_cls = v
            if isdog_pet != isdog_cls:
                print(f"[{fname}] pet='{pet_label}'  classifier='{clabel}'")
        print("\n-- Misclassified Breeds --")
        for fname, v in results_dic.items():
            pet_label, clabel, match, isdog_pet, isdog_cls = v
            if isdog_pet == 1 and isdog_cls == 1 and match == 0:
                print(f"[{fname}] pet='{pet_label}'  classifier='{clabel}'")
