# Hướng dẫn thực hiện công việc – Practice 1


## 1. Quy tắc làm việc chung

1. **Mỗi người chỉ sửa file mình phụ trách** (xem bảng phân công trong `Hướng Dẫn Practice_1.md`). Cần sửa file người khác thì báo họ.
2. **Chạy lệnh từ thư mục gốc** `Practice_1/` để import `src.…` hoạt động.
3. **Dùng chung cấu hình** từ `src/config.py`; không tự khai báo lại đường dẫn hay hyperparameters.
4. **Git:** `git pull` trước khi làm, commit nhỏ và thường xuyên, `git push` ngay khi xong một file.
   ```bash
   git pull
   git add <file mình sửa>
   git commit -m "Tên: mô tả ngắn"
   git push
   ```
5. **Không đưa lên Git:** dataset, checkpoint (`.pth`), môi trường ảo. `.gitignore` đã xử lý.
6. **Kết quả trong báo cáo phải lấy từ lần chạy thực tế.**

## 2. Chuẩn bị môi trường (mỗi người làm một lần)

```bash
git clone https://github.com/maintx1770-sudo/Practice_1.git
cd Practice_1
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

## 3. Thứ tự thực hiện

| Bước | Việc | Ai | Phải chờ |
|---:|---|---|---|
| 1 | Chốt cấu trúc, `config.py`, `requirements.txt`, `.gitignore` | Mai | – |
| 2 | Đọc `lab_requirements.md` để nắm yêu cầu và sản phẩm nộp | Cả nhóm | Bước 1 |
| 3 | Viết ghi chú kiến thức nền (`docs/03_research/`) | Nguyễn Chi, Huynh, Đức | – |
| 4 | `transforms.py`, `neural_network.py`, `metrics.py`, `conftest.py` | Nguyễn Chi, My, Huynh, Trúc Chi | Bước 1 |
| 5 | `dataset.py`, khung `trainer.py`, `plot_loss.py` (dữ liệu giả) | Nguyễn Chi, Huynh, Đức | Bước 4 |
| 6 | `model_io.py`, hoàn chỉnh `trainer.py`, khung `show_predictions.py`, các test | My, Huynh, Đức, Nguyễn Chi | Bước 5 |
| 7 | Chạy huấn luyện thật, sinh history và checkpoint | Huynh | Bước 6 |
| 8 | Thử nghiệm `compare_models`, `tune_hyperparams`; vẽ biểu đồ trên dữ liệu thật | My, Đức | Bước 7 |
| 9 | Đánh giá, `pytest -q`, viết `evaluation_results`, `experiment_results`, `test_report` | Huynh, Đức, Trúc Chi | Bước 8 |
| 10 | Notebook tổng hợp, `conclusion.md`, README, CHANGELOG | Mai, Trúc Chi | Bước 9 |
| 11 | Báo cáo cuối, kiểm tra toàn bộ, bàn giao | Cả nhóm | Bước 10 |



## 3. Kiểm tra trước khi coi là "xong" một file

- [ ] Chạy được từ thư mục gốc, không lỗi import.
- [ ] Có test tương ứng (nếu thuộc `src/`) và `pytest -q` qua.
- [ ] Đã push lên GitHub.
- [ ] Đã tích `[x]` trong `task_list.md`.
