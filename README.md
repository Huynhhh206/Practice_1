# Practice 1 – PyTorch FashionMNIST Classification

Bài thực hành xây dựng mô hình học sâu bằng PyTorch để phân loại ảnh thời trang FashionMNIST thành 10 lớp.

> **Trạng thái:** dự án đang trong giai đoạn triển khai (03/11/2026 – 11/11/2026). 

## 1. Mục tiêu

Theo Practice 1:
- **Learn:** PyTorch Tensors, Datasets/Loaders, Transforms, Model Building, Autograd, Optimization, Model Saving/Loading.
- **Implement:** tải FashionMNIST, áp dụng transforms, xây mạng nơ-ron, viết training loop (forward, loss, backward, optimize), đánh giá accuracy, lưu và tải model.
- **Tasks:** thử nghiệm kiến trúc/hyperparameters, vẽ biểu đồ loss, hiển thị ảnh dự đoán so với nhãn thật.
- **Deliver:** mã Python, báo cáo ngắn, biểu đồ loss, ảnh dự đoán.

## 2. Dữ liệu

FashionMNIST gồm 60.000 ảnh train và 10.000 ảnh test, ảnh grayscale 28 × 28, 10 lớp: T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot.

**Không cần tải thủ công.** Dataset được `torchvision.datasets.FashionMNIST` tự tải về `data/input/` ở lần chạy đầu tiên (cần Internet, khoảng 30 MB). Dữ liệu này không được đưa lên Git.

## 3. Cấu trúc thư mục

```text
Practice_1/
├── data/
│   ├── input/                 # FashionMNIST tải về
│   └── output/                # checkpoints/, predictions/, tensorboard/
├── notebooks/                 # 01_pytorch_basics, 02_fashionmnist_training, 03_practice1_full
├── src/
│   ├── config.py              # đường dẫn, hằng số, hyperparameters
│   ├── preprocessing/         # transforms.py, dataset.py
│   ├── models/                # neural_network.py, model_io.py
│   ├── training/              # trainer.py
│   ├── evaluation/            # metrics.py
│   └── visualization/         # plot_loss.py, show_predictions.py
├── experiments/               # compare_models.py, tune_hyperparams.py
├── tests/                     # kiểm thử với pytest
├── docs/                      # kế hoạch, yêu cầu, nghiên cứu, thiết kế, kiểm thử, kết quả
└── results/                   # figures/, tables/, reports/
```

Chi tiết từng thư mục và người phụ trách xem file `Hướng Dẫn Practice_1.md`.

## 4. Cài đặt

Yêu cầu Python 3.9 trở lên.

```bash
git clone https://github.com/maintx1770-sudo/Practice_1.git
cd Practice_1

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Phiên bản PyTorch phù hợp phụ thuộc hệ điều hành và phần cứng (CPU/GPU). Nếu cài lỗi, xem hướng dẫn tại https://pytorch.org/get-started/locally/.

## 5. Cách chạy

Chạy mọi lệnh từ thư mục gốc `Practice_1/`.

**Notebook** (cách dễ nhất):
```bash
jupyter notebook
```
Mở thư mục `notebooks/` và chạy theo thứ tự:
1. `01_pytorch_basics.ipynb`: làm quen PyTorch và khám phá dữ liệu.
2. `02_fashionmnist_training.ipynb`: huấn luyện và đánh giá mô hình.
3. `03_practice1_full.ipynb`: tổng hợp toàn bộ quy trình.

**Script thử nghiệm:**
```bash
python -m experiments.compare_models
python -m experiments.tune_hyperparams
```

**Kiểm thử:**
```bash
pytest -q
```

**Xem log huấn luyện (nếu có dùng TensorBoard):**
```bash
tensorboard --logdir data/output/tensorboard
```

## 6. Sản phẩm cần nộp

| Sản phẩm | Vị trí |
|---|---|
| Mã Python | `src/`, `experiments/`, `notebooks/` |
| Báo cáo ngắn | `results/reports/` |
| Biểu đồ loss | `results/figures/` |
| Ảnh dự đoán so với nhãn thật | `results/figures/`, `data/output/predictions/` |
| Bảng kết quả thử nghiệm | `results/tables/` |

## 7. Nhóm thực hiện

| Thành viên | Vai trò |
|---|---|
| Mai | Quản lý và tích hợp |
| Nguyễn Chi | Dữ liệu và kiến thức nền |
| My | Mô hình |
| Huynh | Huấn luyện và đánh giá |
| Đức | Thử nghiệm và trực quan hóa |
| Trúc Chi | Thiết kế, kiểm thử và báo cáo |

## 8. Tài liệu tham khảo

- PyTorch tutorials: https://pytorch.org/tutorials/
- PyTorch docs: https://pytorch.org/docs/
- FashionMNIST (torchvision): https://pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html

## 9. Giấy phép

MIT. Xem file `LICENSE`.
