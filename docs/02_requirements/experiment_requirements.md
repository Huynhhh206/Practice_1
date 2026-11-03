# Yêu cầu ghi nhận thử nghiệm – Practice 1

Áp dụng cho nhiệm vụ: **Experiment with network/hyperparameters**. Mỗi lần thử nghiệm cần ghi đủ thông tin dưới đây để so sánh được và đưa vào báo cáo.

## 1. Nguyên tắc

1. **Mỗi lần chỉ đổi một yếu tố chính** (kiến trúc *hoặc* một hyperparameter) để biết yếu tố nào tạo ra khác biệt.
2. **Giữ điều kiện khác giống nhau:** cùng dữ liệu, cùng transform, cùng seed (`set_seed()` trong `src/config.py`), cùng số epoch khi so sánh kiến trúc.
3. **Dùng validation set** (tách từ tập train) khi chọn hyperparameters; chỉ dùng tập test để đánh giá cuối.
4. **Số liệu phải lấy từ lần chạy thực tế**, không điền số minh họa.
5. Chạy lại cùng cấu hình với seed khác (nếu có thời gian) để biết kết quả có ổn định không.

## 2. Thông tin cần ghi cho mỗi thử nghiệm

| Nhóm | Thông tin |
|---|---|
| Định danh | Mã thử nghiệm (ví dụ `EXP-01`), ngày chạy, người chạy |
| Mục đích | Thử nghiệm này kiểm tra điều gì |
| Kiến trúc | Tên mô hình (MLP/CNN…), các lớp, số tham số (tổng và có thể huấn luyện), kích thước tensor qua các lớp |
| Hyperparameters | Learning rate, batch size, số epoch, optimizer, dropout, seed |
| Dữ liệu | Transform sử dụng, kích thước train/validation/test |
| Môi trường | CPU/GPU, thời gian huấn luyện |
| Kết quả | Train loss, validation/test loss, train accuracy, validation/test accuracy (giá trị cuối và giá trị tốt nhất) |
| Biểu đồ | Đường dẫn tới loss curve trong `results/figures/` |
| Nhận xét | Loss có giảm ổn định không, có dấu hiệu overfitting/underfitting không, so với thử nghiệm trước thế nào |

## 3. Mẫu bảng ghi nhận

| Mã | Kiến trúc | LR | Batch | Epoch | Optimizer | Dropout | Số tham số | Thời gian | Train loss | Test loss | Train acc | Test acc | Nhận xét |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EXP-01 | | | | | | | | | | | | | |
| EXP-02 | | | | | | | | | | | | | |

Bảng tổng hợp lưu dạng CSV trong `results/tables/` và tóm tắt trong `docs/06_results/experiment_results.md`.

## 4. Các thử nghiệm tối thiểu cần có

**So sánh kiến trúc** (`experiments/compare_models.py`):
- [ ] MLP.
- [ ] CNN cơ bản.
- [ ] CNN sâu hơn (nhiều lớp convolution hơn).

**Thử nghiệm hyperparameters** (`experiments/tune_hyperparams.py`):
- [ ] Learning rate (ít nhất 3 giá trị).
- [ ] Batch size (ít nhất 2–3 giá trị).
- [ ] Số epoch.
- [ ] Optimizer (ví dụ SGD và Adam).
- [ ] Dropout rate (nếu mô hình có dropout).

## 5. Lịch sử huấn luyện (history)

Mỗi lần huấn luyện nên lưu history theo epoch với các cột:

`epoch`, `train_loss`, `train_accuracy`, `val_loss` (hoặc `test_loss`), `val_accuracy` (hoặc `test_accuracy`)

Lưu CSV bằng `pandas` vào `results/tables/`; file này là đầu vào cho `plot_loss.py` và bảng so sánh.

## 6. Cách nhận xét kết quả

- **Loss giảm đều, train và test accuracy gần nhau:** học tốt.
- **Train accuracy cao nhưng test accuracy thấp hơn nhiều, test loss tăng:** dấu hiệu overfitting (thử dropout, giảm kích thước mô hình, giảm epoch).
- **Cả hai accuracy đều thấp, loss giảm chậm:** có thể underfitting (thử tăng learning rate, thêm lớp/nơ-ron, tăng epoch).
- **Loss dao động mạnh hoặc không giảm:** learning rate có thể quá lớn.

## 7. Sản phẩm của phần thử nghiệm

| Sản phẩm | Vị trí |
|---|---|
| Mã thử nghiệm | `experiments/` |
| Bảng kết quả (CSV) | `results/tables/` |
| Biểu đồ loss, accuracy | `results/figures/` |
| Tổng hợp và nhận xét | `docs/06_results/experiment_results.md` |
