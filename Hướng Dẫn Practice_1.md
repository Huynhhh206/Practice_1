# HƯỚNG DẪN CẤU TRÚC THƯ MỤC – PRACTICE 1
## PyTorch FashionMNIST Classification


# TIMELINE TRIỂN KHAI PROJECT

**Thời gian:** 03/11/2026 – 11/11/2026  



##  Bảng phân công

| TV | Vai trò | File / thư mục phụ trách |
|---|---|---|
| **Mai** | Quản lý và tích hợp | `README.md`, `requirements.txt`, `CHANGELOG.md`, `LICENSE`, `.gitignore`; `src/config.py`; các file `__init__.py`; `docs/01_project_management/` (4 file); `docs/02_requirements/` (2 file); `notebooks/03_practice1_full.ipynb` |
| **Nguyễn Chi** | Dữ liệu và kiến thức nền | `src/preprocessing/transforms.py`, `dataset.py`; `tests/test_transforms.py`, `test_dataset.py`; `notebooks/01_pytorch_basics.ipynb`; `docs/03_research/pytorch_basics.md`, `data_preprocessing.md` |
| **My** | Mô hình | `src/models/neural_network.py`, `model_io.py`; `experiments/compare_models.py`; `tests/test_model.py`, `test_model_io.py`; lưu checkpoint vào `data/output/checkpoints/` |
| **Huynh** | Huấn luyện và đánh giá | `src/training/trainer.py`; `src/evaluation/metrics.py`; `tests/test_trainer.py`, `test_metrics.py`; `notebooks/02_fashionmnist_training.ipynb`; `docs/03_research/evaluation_methods.md`; `docs/06_results/evaluation_results.md`; log vào `data/output/tensorboard/` |
| **Đức** | Thử nghiệm và trực quan hóa | `experiments/tune_hyperparams.py`; `src/visualization/plot_loss.py`, `show_predictions.py`; `docs/03_research/hyperparameters.md`; `docs/06_results/experiment_results.md`; đầu ra vào `results/figures/`, `results/tables/`, `data/output/predictions/` |
| **Trúc Chi** | Thiết kế, kiểm thử và báo cáo | `tests/conftest.py`; `docs/04_design/` (2 file); `docs/05_testing/` (3 file); `docs/06_results/conclusion.md`; `results/reports/` (báo cáo cuối) |



## Kế hoạch thực hiện chi tiết

| Ngày | TV phụ trách | Công việc cần hoàn thành |
|---|---|---|
| **03/11 (T3)** | Mai | Tạo `src/config.py`, các `__init__.py`, `requirements.txt`, `.gitignore`; chốt cấu trúc project. |
| | Mai | Hoàn thành `lab_requirements.md`. |
| | Đức | Hoàn thành `hyperparameters.md`. |
| | Trúc Chi | Chốt chữ ký hàm mục 15.3 để Trúc Chi viết `conftest.py`. |
| **04/11 (T4)** | Nguyễn Chi | Hoàn thành `transforms.py`. |
| | My | Hoàn thành `neural_network.py`. |
| | Huynh | Hoàn thành `metrics.py`. |
| | Trúc Chi | Hoàn thành `tests/conftest.py`. |
| **05/11 (T5)** | Nguyễn Chi | Hoàn thành `dataset.py`. |
| | My | Hoàn thành `test_model.py`, bắt đầu `model_io.py`. |
| | Huynh | Viết khung `trainer.py`, chạy thử bằng dữ liệu giả. |
| | Đức | Hoàn thành `plot_loss.py` bằng history giả. |
| | Trúc Chi | Hoàn thành `test_plan.md`, `test_cases.md`. |
| | Mai | Hoàn thành 4 file trong `docs/01_project_management/` và `experiment_requirements.md`. |
| **06/11 (T6)** | Nguyễn Chi | Hoàn thành `test_transforms.py`, `test_dataset.py`. |
| | My | Hoàn thành `model_io.py`, `test_model_io.py`. |
| | Huynh | Hoàn chỉnh `trainer.py`, bắt đầu `test_metrics.py`, `test_trainer.py`. |
| | Đức | Viết khung `show_predictions.py`. |
| **07/11 (T7)** | Huynh | Chạy notebook `02_fashionmnist_training.ipynb`, sinh history và checkpoint thật. |
| | Nguyễn Chi | Hoàn thành notebook `01_pytorch_basics.ipynb`. |
| | My | Hỗ trợ kiểm tra tích hợp model và model_io. |
| | Trúc Chi | Kiểm tra các module và test đã hoàn thành. |
| **08/11 (CN)** | Đức | Hoàn thành `tune_hyperparams.py`; chạy `show_predictions.py`, `plot_loss.py` trên dữ liệu thật. |
| | My | Hoàn thành `compare_models.py`. |
| | Huynh | Kiểm tra và xác nhận kết quả huấn luyện. |
| | Trúc Chi | Hoàn thiện `processing_pipeline.md`, `system_architecture.md`. |
| **09/11 (T2)** | Huynh | Hoàn thành `evaluation_results.md`. |
| | Đức | Hoàn thành `experiment_results.md`. |
| | Trúc Chi | Chạy `pytest -q`, sửa lỗi và viết `test_report.md`. |
| | Mai | Hoàn thành notebook `03_practice1_full.ipynb`. |
| **10/11 (T3)** | Trúc Chi | Hoàn thành `conclusion.md` dựa trên kết quả đánh giá và thực nghiệm. |
| | Mai | Cập nhật `README.md`, `CHANGELOG.md`. |
| | Nguyễn Chi, My, Huynh, Đức | Hỗ trợ sửa lỗi, kiểm tra kết quả và tích hợp toàn bộ module. |
| **11/11 (T4)** | Trúc Chi | Hoàn thiện báo cáo cuối trong `results/reports/`, bổ sung biểu đồ và bảng kết quả. |
| | Mai, Nguyễn Chi, My, Huynh, Đức, Trúc Chi | Kiểm tra toàn bộ project, cấu trúc thư mục, code, notebook và kết quả. |
| | Mai, Nguyễn Chi, My, Huynh, Đức, Trúc Chi | Chạy kiểm tra cuối cùng, xử lý lỗi còn lại, xác nhận các file đã được cập nhật lên GitHub và bàn giao project. |
## 2. Các mốc hoàn thành quan trọng

| Mốc | Thời hạn | Kết quả cần đạt |
|---|---|---|
| Mốc 1 | 03/11 | Hoàn thành cấu hình và thống nhất cấu trúc |
| Mốc 2 | 04/11 | Hoàn thành các module nền tảng |
| Mốc 3 | 06/11 | Hoàn thành các module chính và bộ test cơ bản |
| Mốc 4 | 07/11 | Chạy được mô hình huấn luyện |
| Mốc 5 | 08/11 | Có checkpoint, history và kết quả thực nghiệm |
| Mốc 6 | 09/11 | Có kết quả đánh giá và báo cáo test |
| Mốc 7 | 10/11 | Hoàn thành notebook tổng hợp và kết luận |
| Mốc 8 | 11/11 | Hoàn thành báo cáo và tài liệu dự án |
| Mốc 9 | 11/11 | Kiểm tra, nghiệm thu và bàn giao |


---

# 1. Tổng quan bài thực hành

**Tên bài:** PyTorch FashionMNIST Classification

**Mục tiêu:** Xây dựng một mô hình học sâu phân loại ảnh thời trang FashionMNIST thành 10 lớp bằng PyTorch.

Bài thực hành bám theo slide **Practice 1** gồm 4 nhóm yêu cầu: **Learn** (tìm hiểu), **Implement** (cài đặt), **Tasks** (nhiệm vụ) và **Deliver** (sản phẩm nộp). Cụ thể cần hoàn thành:

1. Tìm hiểu Tensor, Dataset, DataLoader, Transforms, Model, Autograd và Optimization.
2. Tải và tiền xử lý dữ liệu FashionMNIST.
3. Xây dựng mạng nơ-ron.
4. Huấn luyện mô hình theo quy trình Forward → Loss → Backward → Optimize.
5. Đánh giá độ chính xác của mô hình.
6. Thử nghiệm kiến trúc mạng và hyperparameters.
7. Trực quan hóa Loss và kết quả dự đoán.
8. Lưu mô hình và tải lại để sử dụng.
9. Viết báo cáo ngắn và chuẩn bị các sản phẩm cần nộp: mã Python, báo cáo ngắn, biểu đồ Loss, ảnh hiển thị dự đoán.
10. Tham khảo tài liệu/tutorial chính thức của PyTorch (yêu cầu *Use: PyTorch docs/tutorials*) và ghi lại nguồn đã dùng.

# 2. Cấu trúc tổng thể

```text
Practice_1/
│
├── README.md
├── requirements.txt
├── CHANGELOG.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── input/
│   └── output/
│       ├── checkpoints/
│       ├── predictions/
│       └── tensorboard/
│
├── notebooks/
│   ├── 01_pytorch_basics.ipynb
│   ├── 02_fashionmnist_training.ipynb
│   └── 03_practice1_full.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── transforms.py
│   │   └── dataset.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── neural_network.py
│   │   └── model_io.py
│   ├── training/
│   │   ├── __init__.py
│   │   └── trainer.py
│   ├── evaluation/
│   │   ├── __init__.py
│   │   └── metrics.py
│   └── visualization/
│       ├── __init__.py
│       ├── plot_loss.py
│       └── show_predictions.py
│
├── experiments/
│   ├── __init__.py
│   ├── compare_models.py
│   └── tune_hyperparams.py
│
├── tests/
│   ├── conftest.py
│   ├── test_dataset.py
│   ├── test_transforms.py
│   ├── test_model.py
│   ├── test_model_io.py
│   ├── test_trainer.py
│   └── test_metrics.py
│
├── docs/
│   ├── 01_project_management/
│   │   ├── project_plan.md
│   │   ├── task_list.md
│   │   ├── task_guide.md
│   │   └── timeline.md
│   ├── 02_requirements/
│   │   ├── lab_requirements.md
│   │   └── experiment_requirements.md
│   ├── 03_research/
│   │   ├── pytorch_basics.md
│   │   ├── data_preprocessing.md
│   │   ├── hyperparameters.md
│   │   └── evaluation_methods.md
│   ├── 04_design/
│   │   ├── processing_pipeline.md
│   │   └── system_architecture.md
│   ├── 05_testing/
│   │   ├── test_plan.md
│   │   ├── test_cases.md
│   │   └── test_report.md
│   └── 06_results/
│       ├── experiment_results.md
│       ├── evaluation_results.md
│       └── conclusion.md
│
└── results/
    ├── figures/
    ├── tables/
    └── reports/
```

Các file `.gitkeep` nằm trong những thư mục rỗng (`data/`, `results/`) chỉ để Git giữ lại thư mục; có thể xóa khi thư mục đã có nội dung.

# 3. [Mai] Giải thích các tệp ở cấp gốc

| TV | Tên | Ý nghĩa | Công việc cần làm |
|---|---|---|---|
| Mai | `README.md` | Trang giới thiệu dự án | Ghi mục tiêu, cách cài đặt, cách chạy và sản phẩm cần nộp. Cập nhật khi quy trình chạy thay đổi. |
| Mai | `requirements.txt` | Danh sách thư viện Python | Cập nhật các thư viện cần thiết; cài bằng `pip install -r requirements.txt`. |
| Mai | `CHANGELOG.md` | Nhật ký thay đổi | Ghi lại các phiên bản, thay đổi quan trọng trong mã nguồn và cấu trúc dự án. |
| Mai | `LICENSE` | Giấy phép sử dụng mã nguồn | Giữ nguyên giấy phép đã chọn cho repo. |
| Mai | `.gitignore` | Danh sách tệp Git không theo dõi | Không đưa môi trường ảo, cache, dữ liệu tải về, checkpoint và file kết quả sinh tự động lên Git. |

## 3.1. [Mai] `README.md`

Nên có:
- Tên và mục tiêu bài thực hành.
- Mô tả dữ liệu FashionMNIST.
- Cấu trúc thư mục.
- Hướng dẫn cài đặt môi trường.
- Cách chạy (mở notebook hoặc chạy script trong `experiments/`).
- Danh sách sản phẩm cần nộp.

## 3.2. [Mai] `requirements.txt`

Lưu tên các thư viện bên ngoài mà dự án sử dụng:
- `torch`: xây dựng và huấn luyện mô hình.
- `torchvision`: dataset FashionMNIST và transforms ảnh.
- `matplotlib`: vẽ biểu đồ và hiển thị ảnh.
- `numpy`, `pandas`: hỗ trợ xử lý dữ liệu và bảng kết quả.
- `tensorboard`: ghi log huấn luyện vào `data/output/tensorboard/` (nếu dùng).
- `scikit-learn`: có thể dùng thêm confusion matrix và classification report.
- `pytest`: chạy kiểm thử.
- `jupyter`: làm việc với notebook.

Lưu ý: Phiên bản PyTorch phù hợp phụ thuộc hệ điều hành và phần cứng. Nếu cần tái lập môi trường chính xác, nên cố định phiên bản sau khi kiểm tra môi trường đã cài.

# 4. [Nguyễn Chi, My, Huynh, Đức] Thư mục `data/` – Dữ liệu

## 4.1. [Nguyễn Chi] `data/input/`

**Ý nghĩa:** Nơi lưu bộ dữ liệu gốc FashionMNIST do `torchvision.datasets.FashionMNIST` tải về.

**Công việc:**
- Tải bộ dữ liệu train và test.
- Giữ nguyên dữ liệu gốc, không chỉnh sửa thủ công.
- Không đưa dữ liệu tải về lên Git.

FashionMNIST có 60.000 ảnh train, 10.000 ảnh test; ảnh grayscale kích thước 28 × 28 và có 10 nhãn.

## 4.2. [My, Huynh, Đức] `data/output/`

**Ý nghĩa:** Chứa các tệp phát sinh sau khi chạy chương trình.

### [My] `data/output/checkpoints/`
Lưu trọng số hoặc checkpoint của mô hình, ví dụ `fashion_mnist_model.pth`.

Công việc:
- Lưu `model.state_dict()` sau huấn luyện (thực hiện bằng hàm trong `src/models/model_io.py`).
- Khi cần dùng lại, khởi tạo đúng kiến trúc rồi nạp trọng số.
- Có thể lưu thêm optimizer state và epoch nếu muốn tiếp tục huấn luyện.

### [Đức] `data/output/predictions/`
Lưu kết quả dự đoán được xuất ra:
- Ảnh minh họa dự đoán.
- Bảng nhãn thật và nhãn dự đoán.
- Các trường hợp mô hình dự đoán sai để phân tích.

### [Huynh] `data/output/tensorboard/`
Lưu log huấn luyện cho TensorBoard (nếu dùng `SummaryWriter`): loss và accuracy theo epoch, thông tin cấu hình. Xem bằng lệnh `tensorboard --logdir data/output/tensorboard`.

Không nên nhầm thư mục này với `results/tables/`: `tensorboard/` ghi lại quá trình chạy; `tables/` là bảng kết quả đã tổng hợp để đưa vào báo cáo.

# 5. [Mai, Nguyễn Chi, Huynh] Thư mục `notebooks/` – Thực hành theo từng bước

Notebook là nơi thử nghiệm, quan sát dữ liệu, chạy từng đoạn lệnh và ghi chú. Vì repo không có file chạy chính (như `train.py`), **notebook là nơi ghép các module trong `src/` thành quy trình hoàn chỉnh**. Hiện các notebook là khung trống.

## 5.1. [Nguyễn Chi] `01_pytorch_basics.ipynb`

**Mục đích:** Làm quen PyTorch và khám phá dữ liệu trước khi xây dựng mô hình (phần *Learn* của slide).

Nội dung nên có:
1. Tensor: tạo, thao tác, chuyển đổi.
2. Autograd: ví dụ `requires_grad` và `backward()`.
3. Tải FashionMNIST, kiểm tra số lượng ảnh train/test, kích thước và kiểu dữ liệu.
4. Hiển thị ảnh mẫu, tên 10 lớp và phân bố nhãn.
5. Thử Transforms và DataLoader.
6. Nhận xét dữ liệu.

**Đầu ra mong đợi:** Hiểu các khái niệm PyTorch cơ bản và hiểu dữ liệu gồm những gì.

## 5.2. [Huynh] `02_fashionmnist_training.ipynb`

**Mục đích:** Xây dựng và thử nghiệm pipeline huấn luyện.

Nội dung nên có:
1. Tạo transforms và DataLoader.
2. Xây dựng mô hình.
3. Khai báo loss function và optimizer.
4. Huấn luyện một số epoch.
5. Đánh giá trên tập test.
6. Vẽ Loss và theo dõi Accuracy.
7. Lưu checkpoint.

**Đầu ra mong đợi:** Có mô hình chạy được và hiểu được các bước huấn luyện.

## 5.3. [Mai] `03_practice1_full.ipynb`

**Mục đích:** Notebook tổng hợp toàn bộ bài thực hành theo trình tự hoàn chỉnh.

Nội dung nên có:
1. Giới thiệu bài toán và dataset.
2. Tiền xử lý dữ liệu.
3. Xây dựng mô hình.
4. Huấn luyện và đánh giá.
5. Thử nghiệm các cấu hình.
6. Trực quan hóa Loss.
7. Hiển thị ảnh dự đoán so với nhãn thật.
8. Lưu và tải mô hình.
9. Kết luận.

**Lưu ý:** Không nhất thiết viết lại mọi thứ ở cả ba notebook. Notebook 01 dùng học và khám phá, notebook 02 dùng phát triển pipeline, notebook 03 dùng tổng hợp kết quả cuối. Nên import hàm từ `src/` thay vì chép lại mã.

# 6. [Mai, Nguyễn Chi, My, Huynh, Đức] Thư mục `src/` – Mã nguồn chính

Phần chương trình Python chính thức, tách theo module để dễ đọc, sửa lỗi và tái sử dụng. Các file `__init__.py` đánh dấu thư mục là Python package và có thể để trống.

## 6.1. [Mai] `src/config.py`

**Ý nghĩa:** Tập trung các cấu hình dùng chung. Nên định nghĩa:
- Đường dẫn dữ liệu, checkpoint và kết quả.
- `BATCH_SIZE`: số ảnh trong một batch.
- `LEARNING_RATE`: tốc độ học.
- `EPOCHS`: số lượt duyệt qua tập train.
- `NUM_CLASSES`: số lớp, bằng 10.
- `RANDOM_SEED`: seed để hỗ trợ tái lập kết quả.

Khi thử nghiệm, nên thay đổi cấu hình tại đây hoặc truyền cấu hình vào hàm, tránh sửa nhiều file cùng lúc.

## 6.2. [Nguyễn Chi] `src/preprocessing/` – Dữ liệu và tiền xử lý

### [Nguyễn Chi] `transforms.py`
**Ý nghĩa:** Định nghĩa các phép biến đổi ảnh. Nên bắt đầu với:
- `ToTensor()`: chuyển ảnh thành Tensor.
- `Normalize((0.5,), (0.5,))`: chuẩn hóa giá trị pixel.

Có thể mở rộng:
- Thử augmentation nếu phù hợp.
- Dùng cùng quy trình chuẩn hóa nhất quán khi train và test.
- Không áp dụng biến đổi ngẫu nhiên lên tập test.

### [Nguyễn Chi] `dataset.py`
**Ý nghĩa:** Tải dataset và tạo DataLoader.

Công việc:
- Tải FashionMNIST train và test vào `data/input/`.
- Gắn transform cho dataset.
- Tạo DataLoader theo batch size.
- Shuffle tập train; thông thường không shuffle tập test.
- Nếu cần tuning nghiêm túc: tách validation set từ tập train.

**Đầu ra:** `train_loader` và `test_loader` (và `val_loader` nếu có), cung cấp từng batch gồm ảnh và nhãn cho mô hình.

## 6.3. [My] `src/models/` – Mô hình và lưu/tải

### [My] `neural_network.py`
**Ý nghĩa:** Định nghĩa kiến trúc mạng nơ-ron phân loại ảnh (slide: *Build a neural network*). Có thể chứa nhiều lớp mô hình để phục vụ so sánh, ví dụ MLP và CNN.

Thành phần CNN gợi ý:
- Convolution: trích xuất đặc trưng ảnh.
- ReLU: thêm tính phi tuyến.
- MaxPooling: giảm kích thước feature map.
- Flatten: chuyển feature map thành vector.
- Fully Connected: phân loại thành 10 lớp.
- Dropout: giảm nguy cơ overfitting.

Hàm `forward()` mô tả đường đi của dữ liệu qua các lớp.

**Đầu vào:** Batch ảnh có dạng `(batch_size, 1, 28, 28)`.
**Đầu ra:** Logits có dạng `(batch_size, 10)`.

Lưu ý: Logits chưa phải xác suất. Khi dùng `CrossEntropyLoss`, không cần thêm Softmax trước loss.

### [My] `model_io.py`
**Ý nghĩa:** Lưu và tải mô hình (slide: *Save and load the model*).

Công việc:
- Hàm lưu: ghi `model.state_dict()` vào `data/output/checkpoints/`.
- Hàm tải: khởi tạo đúng kiến trúc trước, rồi nạp `state_dict`.
- Kiểm tra: tải lại model, đánh giá lại và xác nhận accuracy khớp với trước khi lưu.

## 6.4. [Huynh] `src/training/trainer.py` – Huấn luyện

**Ý nghĩa:** Chứa hàm thực hiện huấn luyện (slide: *Training loop*, Autograd, Optimization).

Các bước một epoch:
1. `model.train()`: đặt mô hình ở chế độ huấn luyện.
2. Lấy batch ảnh và nhãn, đưa lên device.
3. `optimizer.zero_grad()`: xóa gradient cũ.
4. `model(images)`: Forward.
5. Tính loss.
6. `loss.backward()`: Backward, tính gradient.
7. `optimizer.step()`: cập nhật trọng số.
8. Tổng hợp loss và accuracy.

**Đầu ra:** Train loss và train accuracy của epoch; nên trả về lịch sử (history) qua các epoch để vẽ biểu đồ và lưu bảng.

## 6.5. [Huynh] `src/evaluation/metrics.py` – Đánh giá

**Ý nghĩa:** Đánh giá mô hình trên dữ liệu không dùng để cập nhật trọng số.

Công việc:
- Gọi `model.eval()` và dùng `torch.no_grad()`.
- Dự đoán nhãn.
- Tính loss và accuracy.

Lưu ý: Tập test chỉ nên dùng để đánh giá cuối cùng. Nếu cần chọn hyperparameters, tách validation set từ tập train.

## 6.6. [Đức] `src/visualization/` – Trực quan hóa

### [Đức] `plot_loss.py`
**Ý nghĩa:** Vẽ biểu đồ quá trình học (slide: *Visualize loss*).

Nên thể hiện:
- Train Loss theo epoch; Validation/Test Loss nếu có.
- Accuracy theo epoch nếu có.
- Tên trục, tiêu đề và chú giải.
- Lưu ảnh vào `results/figures/`.

Mục tiêu: Quan sát loss giảm hay không, phát hiện dấu hiệu học chưa tốt hoặc overfitting.

### [Đức] `show_predictions.py`
**Ý nghĩa:** Hiển thị ảnh dự đoán so với nhãn thật (slide: *Display predicted vs actual images*).

Nên thể hiện:
- Lưới ảnh test (ví dụ 4 × 4 hoặc 5 × 5), mỗi ảnh ghi nhãn dự đoán và nhãn thật.
- Tô màu tiêu đề để phân biệt đúng (ví dụ xanh) và sai (ví dụ đỏ).
- Lưu ảnh vào `results/figures/`; có thể lưu thêm các ca dự đoán sai vào `data/output/predictions/`.

## 6.7. [Huynh, Đức] Lưu lịch sử huấn luyện

Repo không có file riêng để xuất CSV. Lịch sử huấn luyện (`epoch`, `train_loss`, `train_accuracy`, `test_loss`, `test_accuracy`) có thể được lưu bằng `pandas` từ notebook hoặc từ các script trong `experiments/` vào `results/tables/`. File CSV giúp tạo bảng so sánh, vẽ biểu đồ và đưa số liệu vào báo cáo.

## 6.8. [Mai] Cách chạy

Repo **không có** file chạy chính. Quy trình được ghép trong `notebooks/` (mục 5) và các script thử nghiệm trong `experiments/`. Chạy script từ thư mục gốc dự án, ví dụ:

```bash
python -m experiments.tune_hyperparams
python -m experiments.compare_models
```

# 7. [My, Đức] Thư mục `experiments/` – Thử nghiệm

Dùng cho yêu cầu đề bài: “Experiment with network/hyperparameters”. `__init__.py` đánh dấu package.

## 7.1. [My] `compare_models.py`
**Mục đích:** So sánh các kiến trúc mạng.

Có thể triển khai:
- MLP.
- CNN cơ bản.
- CNN có nhiều lớp convolution hơn.

Cần ghi lại cấu trúc, số tham số (tổng và có thể huấn luyện), kích thước tensor qua các layer, thời gian huấn luyện, loss và accuracy. Giữ các điều kiện khác giống nhau để so sánh công bằng.

## 7.2. [Đức] `tune_hyperparams.py`
**Mục đích:** Thử nghiệm các siêu tham số.

Có thể thay đổi:
- Learning rate.
- Batch size.
- Số epoch.
- Optimizer.
- Dropout rate.

Mỗi lần chạy cần ghi cấu hình và kết quả. Không thay đổi quá nhiều yếu tố cùng lúc vì khó xác định yếu tố nào tạo ra khác biệt.

# 8. [Nguyễn Chi, My, Huynh, Trúc Chi] Thư mục `tests/` – Kiểm thử mã nguồn

Dùng để kiểm tra các thành phần hoạt động đúng, tránh lỗi khi ghép pipeline.

| TV | File | Kiểm tra |
|---|---|---|
| Trúc Chi | `conftest.py` | Cấu hình dùng chung cho pytest; định nghĩa fixture như model mẫu, tensor mẫu, dữ liệu giả. |
| Nguyễn Chi | `test_dataset.py` | DataLoader trả về batch đúng kích thước; ảnh `(1, 28, 28)`; nhãn trong khoảng 0–9. |
| Nguyễn Chi | `test_transforms.py` | Transform gọi được, chuyển ảnh thành Tensor, kích thước và kiểu dữ liệu phù hợp. |
| My | `test_model.py` | Mô hình nhận input đúng kích thước, forward không lỗi, output có 10 logits cho mỗi ảnh. |
| My | `test_model_io.py` | Lưu rồi tải lại model cho kết quả dự đoán giống nhau. |
| Huynh | `test_trainer.py` | Một bước/epoch huấn luyện chạy không lỗi; loss là số hợp lệ; trọng số được cập nhật. |
| Huynh | `test_metrics.py` | Hàm đánh giá trả về loss và accuracy hợp lệ (accuracy trong [0, 1]). |

Chạy toàn bộ test từ thư mục gốc:

```bash
pytest -q
```

# 9. [Mai, Nguyễn Chi, Huynh, Đức, Trúc Chi] Thư mục `docs/` – Tài liệu dự án

Nơi lưu tài liệu mô tả kế hoạch, yêu cầu, kiến thức nền, thiết kế, kiểm thử và kết quả.

## 9.1. [Mai] `docs/01_project_management/` – Quản lý công việc
- [Mai] `project_plan.md`: mục tiêu, phạm vi, phương pháp và sản phẩm đầu ra.
- [Mai] `task_list.md`: checklist các công việc cần hoàn thành; đánh dấu khi xong.
- [Mai] `task_guide.md`: thứ tự thực hiện các công việc, nên bắt đầu từ đâu và chuyển sang bước nào tiếp theo.
- [Mai] `timeline.md`: lịch trình theo giai đoạn, công việc và đầu ra dự kiến (có thể thêm ngày bắt đầu, hạn hoàn thành, người phụ trách).

## 9.2. [Mai] `docs/02_requirements/` – Yêu cầu bài tập
- [Mai] `lab_requirements.md`: chuyển yêu cầu trên slide Practice 1 thành danh sách cụ thể: Learn, Implement, Tasks và Deliver.
- [Mai] `experiment_requirements.md`: thông tin cần ghi nhận cho từng thử nghiệm: kiến trúc, hyperparameters, loss, accuracy và nhận xét.

## 9.3. [Nguyễn Chi, Huynh, Đức] `docs/03_research/` – Nghiên cứu kiến thức
- [Nguyễn Chi] `pytorch_basics.md`: ghi chú Tensor, Dataset, DataLoader, `nn.Module`, Autograd, Optimizer, train/eval mode, training loop (Forward, Loss, Backward, Optimize), lưu/tải model và mô tả dataset FashionMNIST (số ảnh, kích thước, số lớp, ý nghĩa từng nhãn). Ghi nguồn PyTorch docs/tutorials đã dùng.
- [Nguyễn Chi] `data_preprocessing.md`: cách tải dữ liệu, chuyển Tensor, chuẩn hóa, chia batch và các bước tiền xử lý.
- [Đức] `hyperparameters.md`: giải thích learning rate, batch size, epoch, optimizer, dropout và ảnh hưởng của chúng; cách thử nghiệm kiến trúc MLP/CNN.
- [Huynh] `evaluation_methods.md`: Accuracy, Loss và các phương pháp bổ sung như Confusion Matrix, Precision, Recall, F1-score.

## 9.4. [Trúc Chi] `docs/04_design/` – Thiết kế giải pháp
- [Trúc Chi] `processing_pipeline.md`: luồng xử lý từ ảnh đầu vào đến dự đoán, tính loss, cập nhật trọng số và lưu kết quả.
- [Trúc Chi] `system_architecture.md`: vai trò từng module trong `src/` và cách các module gọi nhau.

## 9.5. [Trúc Chi] `docs/05_testing/` – Kiểm thử
- [Trúc Chi] `test_plan.md`: mục tiêu, phạm vi, phương pháp và môi trường kiểm thử.
- [Trúc Chi] `test_cases.md`: từng trường hợp kiểm thử, dữ liệu đầu vào và kết quả mong đợi.
- [Trúc Chi] `test_report.md`: kết quả chạy thực tế: số test thành công, thất bại, lỗi phát hiện và kết luận.

## 9.6. [Huynh, Đức, Trúc Chi] `docs/06_results/` – Tổng hợp kết quả
- [Đức] `experiment_results.md`: bảng so sánh các lần thử nghiệm kiến trúc và hyperparameters.
- [Huynh] `evaluation_results.md`: kết quả đánh giá mô hình cuối cùng, các metric và nhận xét.
- [Trúc Chi] `conclusion.md`: mô hình tốt nhất, cấu hình phù hợp, hạn chế và hướng cải thiện.

# 10. [Đức, Trúc Chi] Thư mục `results/` – Sản phẩm đầu ra

Khác với `docs/`, thư mục `results/` lưu các file kết quả thực tế sinh ra từ chương trình.

- [Đức] `results/figures/`: Loss curve, Accuracy curve, ảnh so sánh nhãn thật và nhãn dự đoán, confusion matrix nếu có.
- [Đức] `results/tables/`: training history, bảng so sánh kiến trúc, bảng so sánh hyperparameters, bảng metric (CSV hoặc định dạng khác).
- [Trúc Chi] `results/reports/`: báo cáo cuối cùng dạng PDF, DOCX hoặc Markdown.

Báo cáo nên có:
1. Giới thiệu bài toán.
2. Mô tả FashionMNIST.
3. Phương pháp và kiến trúc mô hình.
4. Quy trình huấn luyện.
5. Thiết lập thực nghiệm.
6. Kết quả và biểu đồ.
7. Phân tích dự đoán đúng/sai.
8. Kết luận.

# 11. Mối liên hệ giữa các thành phần

```text
        notebooks/  và  experiments/   (điểm chạy)
                         |
          +--------------+--------------+
          |              |              |
    preprocessing/    models/        config.py
  (transforms, dataset) (neural_network,
          |              model_io)
          +---- DataLoader ----+
                         |
                    training/
                         |
              Forward / Loss / Backward / Update
                         |
                    evaluation/
                         |
                  Loss / Accuracy
                         |
                  visualization/
              (plot_loss, show_predictions)
                         |
            +------------+-------------+
            |                          |
        results/                  data/output/
  Figures / Tables / Reports  Checkpoints / Predictions / TensorBoard
            |
          docs/
   Phân tích và kết luận
```




---

**Nguyên tắc dễ nhớ:**
- `docs/`: ghi chép, kế hoạch, yêu cầu, thiết kế và phân tích.
- `notebooks/`: học, khám phá, thử nghiệm và ghép pipeline.
- `src/`: mã nguồn chính của chương trình.
- `experiments/`: các lần thử nghiệm có kiểm soát.
- `tests/`: kiểm tra mã nguồn có hoạt động đúng.
- `data/`: dữ liệu đầu vào và file phát sinh.
- `results/`: sản phẩm thực tế dùng để phân tích và nộp bài.
