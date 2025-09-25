import argparse
def get_input_args():
    p = argparse.ArgumentParser(description="Classify pet images with pretrained CNNs")
    p.add_argument('--dir', type=str, default='pet_images/', help='path to images')
    p.add_argument('--arch', type=str, default='vgg', choices=['vgg','alexnet','resnet'])
    p.add_argument('--dogfile', type=str, default='dognames.txt')
    p.add_argument('--print_misclassified', action='store_true')
    return p.parse_args()
