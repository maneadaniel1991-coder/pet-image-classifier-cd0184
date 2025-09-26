from PIL import Image
import torch
from torchvision import models, transforms

def _get_model_and_meta(arch: str):
    arch = arch.lower()
    if arch == "vgg":
        weights = models.VGG16_Weights.DEFAULT
        model = models.vgg16(weights=weights)
    elif arch == "alexnet":
        weights = models.AlexNet_Weights.DEFAULT
        model = models.alexnet(weights=weights)
    elif arch == "resnet":
        weights = models.ResNet18_Weights.DEFAULT
        model = models.resnet18(weights=weights)
    else:
        raise ValueError(f"Unsupported arch: {arch}")

    categories = weights.meta.get("categories", [])
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225]),
    ])
    model.eval()
    return model, preprocess, categories

def classifier(image_path: str, arch: str) -> str:
    model, preprocess, categories = _get_model_and_meta(arch)
    img = Image.open(image_path).convert("RGB")
    x = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        logits = model(x)
        idx = int(logits.argmax(1))
    label = categories[idx] if categories and 0 <= idx < len(categories) else str(idx)
    return label.lower().replace("_", " ").strip()
