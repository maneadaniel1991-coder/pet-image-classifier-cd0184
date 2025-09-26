@echo off
setlocal
set PYTHON_EXE=.\.venv\Scripts\python.exe
if not exist %PYTHON_EXE% set PYTHON_EXE=python
%PYTHON_EXE% check_images.py --dir uploaded_images\ --arch resnet  --dogfile data\dognames.txt > resnet_uploaded-images.txt
%PYTHON_EXE% check_images.py --dir uploaded_images\ --arch alexnet --dogfile data\dognames.txt > alexnet_uploaded-images.txt
%PYTHON_EXE% check_images.py --dir uploaded_images\ --arch vgg     --dogfile data\dognames.txt > vgg_uploaded-images.txt
echo Done.
endlocal

