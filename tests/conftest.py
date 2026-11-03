from pathlib import Path
import pytest
import torch
from PIL import Image
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

@pytest.fixture
def device():
    """Chạy unit test trên CPU để không phụ thuộc máy có GPU hay không."""
    return torch.device("cpu")

@pytest.fixture
def sample_images():
    """8 ảnh giả FashionMNIST: (N, C, H, W) = (8, 1, 28, 28)."""
    generator = torch.Generator().manual_seed(42)
    return torch.rand((8, 1, 28, 28), generator=generator)

@pytest.fixture
def sample_labels():
    """8 nhãn hợp lệ của FashionMNIST, kiểu torch.long."""
    return torch.tensor([0, 1, 2, 3, 4, 5, 6, 9], dtype=torch.long)

@pytest.fixture
def sample_batch(sample_images, sample_labels):
    """Một batch gồm (images, labels), dùng cho forward/training/evaluation."""
    return sample_images, sample_labels

@pytest.fixture
def sample_dataset(sample_images, sample_labels):
    """Dataset giả không cần tải dữ liệu từ Internet."""
    return TensorDataset(sample_images, sample_labels)

@pytest.fixture
def sample_loader(sample_dataset):
    """DataLoader gồm 2 batch, mỗi batch 4 ảnh."""
    return DataLoader(sample_dataset, batch_size=4, shuffle=False, num_workers=0)

@pytest.fixture
def sample_pil_image():
    """Ảnh PIL grayscale 28x28 để kiểm tra transforms.ToTensor/Normalize."""
    return Image.new("L", (28, 28), color=128)

@pytest.fixture
def sample_model(device):
    """MLP nhỏ chỉ dùng để thử training, metrics và save/load.
    Đây không phải mô hình chính thức của nhóm.
    """
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 32),
        nn.ReLU(),
        nn.Linear(32, 10),
    )
    return model.to(device)

@pytest.fixture
def sample_criterion():
    """Hàm mất mát cho bài toán phân loại 10 lớp."""
    return nn.CrossEntropyLoss()

@pytest.fixture
def sample_optimizer(sample_model):
    """Optimizer mẫu cho sample_model."""
    return torch.optim.SGD(sample_model.parameters(), lr=0.01)

@pytest.fixture
def checkpoint_path(tmp_path: Path):
    """Đường dẫn lưu model tạm; pytest tự dọn sau khi test."""
    return tmp_path / "test_model.pth"
