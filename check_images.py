from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    start = time()
    args = get_input_args()

    results = get_pet_labels(args.dir)
    classify_images(args.dir, results, args.arch)
    adjust_results4_isadog(results, args.dogfile)
    stats = calculates_results_stats(results)

    # Default behavior prints just the summary; pass flags to include misclassifications if requested
    print_results(results, stats, args.arch,
                  print_incorrect_dogs=args.print_misclassified,
                  print_incorrect_breed=args.print_misclassified)

    tot = time() - start
    print(f"\nTotal Elapsed Runtime: {tot/3600:.2f} hours, {(tot%3600)/60:.2f} minutes, {tot%60:.2f} seconds")

if __name__ == "__main__":
    main()
