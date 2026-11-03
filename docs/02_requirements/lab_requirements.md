# Yêu cầu bài thực hành – Practice 1
## Exercise: PyTorch FashionMNIST Classification



---

## 1. Learn – Tìm hiểu kiến thức

Study PyTorch Tensors, Datasets/Loaders, Transforms, Model Building, Autograd, Optimization, and Model Saving/Loading.

| # | Nội dung cần tìm hiểu | Nơi ghi nhận | Phụ trách |
|---|---|---|---|
| L1 | Tensors: tạo, thao tác, chuyển đổi | `notebooks/01_pytorch_basics.ipynb`, `docs/03_research/pytorch_basics.md` | Nguyễn Chi |
| L2 | Datasets / DataLoaders | `docs/03_research/data_preprocessing.md` | Nguyễn Chi |
| L3 | Transforms | `docs/03_research/data_preprocessing.md` | Nguyễn Chi |
| L4 | Model Building (`nn.Module`) | `docs/03_research/pytorch_basics.md` | Nguyễn Chi |
| L5 | Autograd | `notebooks/01_pytorch_basics.ipynb` | Nguyễn Chi |
| L6 | Optimization (loss, optimizer, hyperparameters) | `docs/03_research/hyperparameters.md` | Đức |
| L7 | Model Saving / Loading | `docs/03_research/pytorch_basics.md` | Nguyễn Chi |

## 2. Implement – Cài đặt

| # | Yêu cầu | Vị trí thực hiện | Phụ trách |
|---|---|---|---|
| I1 | Load FashionMNIST dataset | `src/preprocessing/dataset.py` | Nguyễn Chi |
| I2 | Apply transforms | `src/preprocessing/transforms.py` | Nguyễn Chi |
| I3 | Build a neural network | `src/models/neural_network.py` | My |
| I4 | Create a training loop (forward, loss, backward, optimize) | `src/training/trainer.py` | Huynh |
| I5 | Evaluate model accuracy | `src/evaluation/metrics.py` | Huynh |
| I6 | Save and load the model | `src/models/model_io.py`, `data/output/checkpoints/` | My |

## 3. Tasks – Nhiệm vụ

| # | Yêu cầu | Vị trí thực hiện | Phụ trách |
|---|---|---|---|
| T1 | Experiment with network/hyperparameters | `experiments/compare_models.py`, `experiments/tune_hyperparams.py` | My, Đức |
| T2 | Visualize loss | `src/visualization/plot_loss.py`, `results/figures/` | Đức |
| T3 | Display predicted vs actual images | `src/visualization/show_predictions.py`, `results/figures/` | Đức |

## 4. Deliver – Sản phẩm cần nộp

| # | Sản phẩm | Vị trí | Phụ trách |
|---|---|---|---|
| D1 | Python code | `src/`, `experiments/`, `notebooks/` | Cả nhóm |
| D2 | Brief report (báo cáo ngắn) | `results/reports/` | Trúc Chi |
| D3 | Loss graphs (biểu đồ loss) | `results/figures/` | Đức |
| D4 | Image displays (ảnh dự đoán so với nhãn thật) | `results/figures/`, `data/output/predictions/` | Đức |

## 5. Use – Tài liệu tham khảo

Use: PyTorch docs/tutorials.

- Tham khảo tài liệu và tutorial chính thức của PyTorch (https://pytorch.org/tutorials/, https://pytorch.org/docs/).
- Ghi lại nguồn đã dùng ở cuối mỗi file trong `docs/03_research/`.

## 6. Tiêu chí hoàn thành chung

- [ ] Tải được FashionMNIST (60.000 ảnh train, 10.000 ảnh test, 10 lớp, ảnh 28 × 28) bằng code.
- [ ] Mô hình huấn luyện được, loss giảm qua các epoch.
- [ ] Có accuracy trên tập test từ lần chạy thực tế.
- [ ] Lưu checkpoint và tải lại được; accuracy sau khi tải khớp với trước khi lưu.
- [ ] Có ít nhất một thử nghiệm thay đổi kiến trúc hoặc hyperparameters, kết quả ghi trong `results/tables/`.
- [ ] Có biểu đồ loss và ảnh dự đoán so với nhãn thật trong `results/figures/`.
- [ ] `pytest -q` chạy qua không lỗi.
- [ ] Có báo cáo ngắn trong `results/reports/`.
- [ ] Mọi file đã được cập nhật lên GitHub.
