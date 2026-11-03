# Kế hoạch dự án – Practice 1

## 1. Thông tin chung

| Mục | Nội dung |
|---|---|
| Tên dự án | Practice 1 – PyTorch FashionMNIST Classification |
| Thời gian | 03/11/2026 – 11/11/2026 |
| Quản lý và tích hợp | Mai |
| Repo | https://github.com/maintx1770-sudo/Practice_1 |

## 2. Mục tiêu

Xây dựng mô hình học sâu bằng PyTorch để phân loại ảnh FashionMNIST (10 lớp), thực hiện đầy đủ các yêu cầu Practice 1: Learn, Implement, Tasks và Deliver (chi tiết xem `docs/02_requirements/lab_requirements.md`).

## 3. Phạm vi

**Trong phạm vi:**
- Tải và tiền xử lý FashionMNIST.
- Xây dựng, huấn luyện, đánh giá mạng nơ-ron.
- Thử nghiệm kiến trúc và hyperparameters.
- Vẽ biểu đồ loss, hiển thị ảnh dự đoán so với nhãn thật.
- Lưu và tải lại mô hình.
- Kiểm thử, viết tài liệu và báo cáo ngắn.

**Ngoài phạm vi:**
- Dùng mô hình pretrained hoặc transfer learning.
- Triển khai thành ứng dụng/dịch vụ.
- Dùng bộ dữ liệu khác ngoài FashionMNIST.

## 4. Phương pháp

1. Tìm hiểu kiến thức nền từ PyTorch docs/tutorials.
2. Chia module theo thành viên (`src/`), thống nhất cấu hình qua `src/config.py`.
3. Huấn luyện theo quy trình Forward → Loss → Backward → Optimize.
4. So sánh kiến trúc (MLP, CNN) và hyperparameters, giữ các điều kiện khác giống nhau.
5. Kiểm thử bằng `pytest`; tích hợp toàn bộ trong notebook tổng hợp.

## 5. Phân công

| Thành viên | Vai trò | Phụ trách chính |
|---|---|---|
| Mai | Quản lý và tích hợp | File cấp gốc, `config.py`, `docs/01`, `docs/02`, notebook 03 |
| Nguyễn Chi | Dữ liệu và kiến thức nền | `transforms.py`, `dataset.py`, notebook 01, `pytorch_basics.md`, `data_preprocessing.md` |
| My | Mô hình | `neural_network.py`, `model_io.py`, `compare_models.py`, checkpoint |
| Huynh | Huấn luyện và đánh giá | `trainer.py`, `metrics.py`, notebook 02, `evaluation_methods.md`, `evaluation_results.md` |
| Đức | Thử nghiệm và trực quan hóa | `tune_hyperparams.py`, `plot_loss.py`, `show_predictions.py`, `hyperparameters.md`, `experiment_results.md` |
| Trúc Chi | Thiết kế, kiểm thử, báo cáo | `conftest.py`, `docs/04`, `docs/05`, `conclusion.md`, `results/reports/` |

## 6. Sản phẩm đầu ra

- Mã Python (`src/`, `experiments/`, `notebooks/`).
- Báo cáo ngắn (`results/reports/`).
- Biểu đồ loss và ảnh dự đoán (`results/figures/`).
- Bảng kết quả thử nghiệm (`results/tables/`).
- Tài liệu dự án (`docs/`).

## 7. Mốc quan trọng

| Mốc | Hạn | Kết quả |
|---|---|---|
| 1 | 03/11 | Hoàn thành cấu hình, thống nhất cấu trúc |
| 2 | 04/11 | Hoàn thành module nền tảng |
| 3 | 06/11 | Hoàn thành module chính và test cơ bản |
| 4 | 07/11 | Chạy được huấn luyện |
| 5 | 08/11 | Có checkpoint, history và kết quả thực nghiệm |
| 6 | 09/11 | Có kết quả đánh giá và báo cáo test |
| 7 | 10/11 | Hoàn thành notebook tổng hợp và kết luận |
| 8 | 11/11 | Hoàn thành báo cáo và tài liệu |
| 9 | 11/11 | Kiểm tra, nghiệm thu, bàn giao |

Lịch chi tiết xem `timeline.md`.

## 8. Rủi ro và cách xử lý

| Rủi ro | Cách xử lý |
|---|---|
| Module phụ thuộc nhau, một người chậm làm kẹt người sau | Thống nhất chữ ký hàm sớm; dùng dữ liệu/history giả để làm song song |
| Xung đột khi nhiều người cùng push | Mỗi người sửa file của mình; `git pull` trước khi push; commit nhỏ, thường xuyên |
| Máy không có GPU, huấn luyện chậm | FashionMNIST nhỏ nên chạy CPU được; giảm số epoch khi thử nghiệm; có thể dùng Google Colab |
| Lỗi môi trường (khác phiên bản thư viện) | Dùng chung `requirements.txt` và môi trường ảo |
| Kết quả không tái lập được | Cố định seed bằng `set_seed()` trong `src/config.py` |
| Trễ hạn | Mai theo dõi `task_list.md` hằng ngày, báo sớm khi có nguy cơ trễ |
