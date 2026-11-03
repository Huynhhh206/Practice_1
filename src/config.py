
"""Cấu hình dùng chung cho Practice 1 – PyTorch FashionMNIST Classification.
 
Mọi module (preprocessing, models, training, evaluation, visualization,
experiments) nên lấy đường dẫn và hyperparameters mặc định từ file này thay vì
tự khai báo lại. Khi thử nghiệm, đổi giá trị tại đây hoặc truyền giá trị khác
vào hàm; không sửa rải rác nhiều file.
 
Dùng:
    from src.config import BATCH_SIZE, CHECKPOINT_DIR, get_device
"""
 
from pathlib import Path
 
# ----------------------------------------------------------------------------
# Đường dẫn (tính từ thư mục gốc dự án, không phụ thuộc nơi chạy lệnh)
# ----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
 
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"                    # FashionMNIST tải về (torchvision)
OUTPUT_DIR = DATA_DIR / "output"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"       # trọng số mô hình (.pth)
PREDICTIONS_DIR = OUTPUT_DIR / "predictions"      # ảnh/bảng dự đoán, ca dự đoán sai
TENSORBOARD_DIR = OUTPUT_DIR / "tensorboard"      # log huấn luyện
 
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"             # loss curve, ảnh dự đoán
TABLES_DIR = RESULTS_DIR / "tables"               # history, bảng so sánh (CSV)
REPORTS_DIR = RESULTS_DIR / "reports"             # báo cáo cuối
 
# ----------------------------------------------------------------------------
# Dữ liệu FashionMNIST
# ----------------------------------------------------------------------------
IMAGE_SIZE = 28            # ảnh 28 x 28
NUM_CHANNELS = 1           # grayscale
NUM_CLASSES = 10           # 10 nhãn
 
CLASS_NAMES = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]
 
# Chuẩn hóa pixel: dùng chung cho train và test
NORMALIZE_MEAN = (0.5,)
NORMALIZE_STD = (0.5,)
 
# ----------------------------------------------------------------------------
# Hyperparameters mặc định (giá trị khởi đầu, sẽ được thử nghiệm thay đổi)
# ----------------------------------------------------------------------------
BATCH_SIZE = 64            # số ảnh trong một batch
LEARNING_RATE = 1e-3       # tốc độ học
EPOCHS = 10                # số lượt duyệt qua tập train
NUM_WORKERS = 0            # số tiến trình nạp dữ liệu (0 = an toàn trên mọi hệ điều hành)
 
# ----------------------------------------------------------------------------
# Tái lập kết quả và lưu mô hình
# ----------------------------------------------------------------------------
RANDOM_SEED = 42
DEFAULT_CHECKPOINT_NAME = "fashion_mnist_model.pth"
 
 
# ----------------------------------------------------------------------------
# Hàm tiện ích (import torch bên trong hàm để config nhẹ và import nhanh)
# ----------------------------------------------------------------------------
def ensure_dirs():
    """Tạo các thư mục đầu ra nếu chưa tồn tại."""
    for path in (
        INPUT_DIR,
        CHECKPOINT_DIR,
        PREDICTIONS_DIR,
        TENSORBOARD_DIR,
        FIGURES_DIR,
        TABLES_DIR,
        REPORTS_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)
 
 
def set_seed(seed=RANDOM_SEED):
    """Đặt seed cho random, numpy và torch để hỗ trợ tái lập kết quả."""
    import random
 
    import numpy as np
    import torch
 
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
 
 
def get_device():
    """Trả về thiết bị tính toán: cuda, mps (Mac Apple Silicon) hoặc cpu."""
    import torch
 
    if torch.cuda.is_available():
        return torch.device("cuda")
    if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")
