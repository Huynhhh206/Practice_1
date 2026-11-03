# Yêu cầu bài thực hành – Practice 1

**Bài tập:** PyTorch FashionMNIST Classification
**Người phụ trách tài liệu:** Mai


---

## 1. Learn – Tìm hiểu

Nghiên cứu các chủ đề sau trong PyTorch và ghi chú lại (kèm nguồn PyTorch docs/tutorials đã dùng).

| # | Yêu cầu | Sản phẩm / vị trí | Phụ trách | Xong |
|---|---|---|---|---|
| L1 | Tensors | `docs/03_research/pytorch_basics.md`, `notebooks/01_pytorch_basics.ipynb` | Nguyễn Chi | [ ] |
| L2 | Datasets / DataLoaders | `docs/03_research/pytorch_basics.md`, `docs/03_research/data_preprocessing.md` | Nguyễn Chi | [ ] |
| L3 | Transforms | `docs/03_research/data_preprocessing.md` | Nguyễn Chi | [ ] |
| L4 | Model Building (`nn.Module`) | `docs/03_research/pytorch_basics.md` | Nguyễn Chi | [ ] |
| L5 | Autograd | `docs/03_research/pytorch_basics.md`, `notebooks/01_pytorch_basics.ipynb` | Nguyễn Chi | [ ] |
| L6 | Optimization (loss, optimizer, hyperparameters) | `docs/03_research/hyperparameters.md`, `docs/03_research/evaluation_methods.md` | Đức, Huynh | [ ] |
| L7 | Model Saving / Loading | `docs/03_research/pytorch_basics.md` | Nguyễn Chi | [ ] |

## 2. Implement – Cài đặt

| # | Yêu cầu | Sản phẩm / vị trí | Phụ trách | Xong |
|---|---|---|---|---|
| I1 | Load FashionMNIST dataset | `src/preprocessing/dataset.py` (dữ liệu tải vào `data/input/`) | Nguyễn Chi | [ ] |
| I2 | Apply transforms | `src/preprocessing/transforms.py` | Nguyễn Chi | [ ] |
| I3 | Build a neural network | `src/models/neural_network.py` | My | [ ] |
| I4 | Create a training loop (forward, loss, backward, optimize) | `src/training/trainer.py` | Huynh | [ ] |
| I5 | Evaluate model accuracy | `src/evaluation/metrics.py` | Huynh | [ ] |
| I6 | Save and load the model | `src/models/model_io.py` (checkpoint trong `data/output/checkpoints/`) | My | [ ] |

## 3. Tasks – Nhiệm vụ

| # | Yêu cầu | Sản phẩm / vị trí | Phụ trách | Xong |
|---|---|---|---|---|
| T1 | Experiment with network / hyperparameters | `experiments/compare_models.py`, `experiments/tune_hyperparams.py`; bảng trong `results/tables/` | My, Đức | [ ] |
| T2 | Visualize loss | `src/visualization/plot_loss.py`; ảnh trong `results/figures/` | Đức | [ ] |
| T3 | Display predicted vs actual images | `src/visualization/show_predictions.py`; ảnh trong `results/figures/` | Đức | [ ] |

## 4. Deliver – Sản phẩm nộp

| # | Yêu cầu | Sản phẩm / vị trí | Phụ trách | Xong |
|---|---|---|---|---|
| D1 | Python code | `src/`, `experiments/`, `tests/`, notebooks trong `notebooks/` | Cả nhóm | [ ] |
| D2 | Brief report | `results/reports/` (báo cáo cuối); tổng hợp trong `docs/06_results/` | Trúc Chi | [ ] |
| D3 | Loss graphs | `results/figures/` | Đức | [ ] |
| D4 | Image displays (dự đoán so với nhãn thật) | `results/figures/`, `data/output/predictions/` | Đức | [ ] |

Báo cáo ngắn (D2) nên có: giới thiệu bài toán; mô tả FashionMNIST; phương pháp và kiến trúc mô hình; quy trình huấn luyện; thiết lập thực nghiệm; kết quả và biểu đồ; phân tích dự đoán đúng/sai; kết luận.

## 5. Use – Tài liệu tham khảo

| # | Yêu cầu | Cách thực hiện | Xong |
|---|---|---|---|
| U1 | Sử dụng PyTorch docs / tutorials | Dùng tài liệu chính thức của PyTorch; ghi lại nguồn đã tham khảo (tên trang, đường dẫn) trong `docs/03_research/` và phần tài liệu tham khảo của báo cáo | [ ] |

---

## 6. Thông tin bài toán

- **Dữ liệu:** FashionMNIST, 60.000 ảnh train và 10.000 ảnh test.
- **Ảnh:** grayscale, kích thước 28 × 28.
- **Nhãn:** 10 lớp (T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot).
- **Đầu vào mô hình:** `(batch_size, 1, 28, 28)`; **đầu ra:** logits `(batch_size, 10)`.

## 7. Tiêu chí hoàn thành chung

1. Tất cả mục L, I, T, D, U ở trên được đánh dấu hoàn thành.
2. Mô hình huấn luyện được, có accuracy đo trên tập test.
3. Lưu rồi tải lại mô hình cho kết quả dự đoán giống nhau.
4. Số liệu trong báo cáo lấy từ lần chạy thực tế (có file trong `results/`).
5. `pytest -q` chạy qua từ thư mục gốc dự án.
