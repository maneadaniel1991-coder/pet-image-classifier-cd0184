@echo off
setlocal
set PYTHON_EXE=.\.venv\Scripts\python.exe
if not exist %PYTHON_EXE% set PYTHON_EXE=python
%PYTHON_EXE% check_images.py --dir data\pet_images\ --arch resnet  --dogfile data\dognames.txt > resnet_pet-images.txt
%PYTHON_EXE% check_images.py --dir data\pet_images\ --arch alexnet --dogfile data\dognames.txt > alexnet_pet-images.txt
%PYTHON_EXE% check_images.py --dir data\pet_images\ --arch vgg     --dogfile data\dognames.txt > vgg_pet-images.txt
echo Done.
endlocal

