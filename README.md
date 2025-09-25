# Pet Image Classifier (cd0184)
## Run
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt --print_misclassified
## Args
--dir, --arch [vgg|alexnet|resnet], --dogfile, --print_misclassified
## Files
check_images.py, get_input_args.py, get_pet_labels.py, classifier.py, classify_images.py,
adjust_results4_isadog.py, calculates_results_stats.py, print_results.py, dognames.txt
## Rubric Mapping
1 Timing 2 CLI 3 Labels 4 Classify 5 Dogs 6 Stats 7 Print
