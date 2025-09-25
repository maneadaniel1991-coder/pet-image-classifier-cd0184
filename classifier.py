from PIL import Image
import torch
from torchvision import models, transforms
def _get_model(arch: str):
    arch = arch.lower()
    if arch == "vgg":
        m = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
    elif arch == "alexnet":
        m = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)
    elif arch == "resnet":
        m = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    else:
        raise ValueError(f"Unsupported arch: {arch}")
    m.eval(); return m
def classifier(image_path: str, arch: str) -> str:
    m = _get_model(arch)
    preprocess = transforms.Compose([
        transforms.Resize(256), transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225]),
    ])
    img = Image.open(image_path).convert("RGB")
    x = preprocess(img).unsqueeze(0)
    import torch
    with torch.no_grad():
        idx = int(m(x).argmax(1))
    meta = getattr(m, "weights", None)
    cats = getattr(meta, "meta", {}).get("categories", []) if meta else []
    label = cats[idx] if cats and 0 <= idx < len(cats) else str(idx)
    return label.lower().replace("_"," ").strip()
