# Nộp bài Day04 — K4, Level 3B

**Hình thức: làm nhóm. Mỗi cá nhân phải tự nộp bài trên tài khoản VLearn của mình.** Nhóm dùng một repo chung, đặt tên theo họ tên và MSSV của người đại diện. Mọi thành viên nộp cùng URL đó, kê khai đầy đủ trong [TEAM.md](TEAM.md).

## 1. Tên repository

Repo đề bài: **K4-L3B-Day04-Prompt-Engineering-Tool-Calling-Labs**.

Repo bài nộp:

```text
K4-L3-DAY04-HoVaTen-MSSV-PromptEngineeringToolCalling
```

- `HoVaTen` và `MSSV`: thông tin của người đại diện nhóm.
- Họ tên viết không dấu, không khoảng trắng. Các phần phân cách bằng dấu `-`.
- Ngày dùng hai chữ số: `DAY04`. Tên bài nộp dùng `L3`, không dùng `L3B`.
- Nếu Keycoach cho phép làm cá nhân, dùng họ tên và MSSV của chính mình, ghi rõ hình thức trong README bài nộp và vẫn tự nộp trên VLearn.

Ví dụ minh họa, không dùng nguyên thông tin này để nộp:

```text
K4-L3-DAY04-NguyenVanAn-2A20260001-PromptEngineeringToolCalling
```

## 2. Tạo repo chung

Nguồn: [repo đề bài K4-L3B](https://github.com/VinUni-AI20k/K4-L3B-Day04-Prompt-Engineering-Tool-Calling-Labs).

Khi repo nguồn công khai và cho phép Fork, nhóm trưởng chọn **Fork**, đặt tên theo mục 1 rồi cấp quyền cộng tác cho các thành viên.

Nếu nguồn vẫn riêng tư hoặc không có nút Fork, nhóm trưởng tạo một repo GitHub rỗng, không khởi tạo README/license/.gitignore. Sau đó dùng cách sau. Các giá trị trong dấu `<...>` là chỗ phải thay, không chạy nguyên văn:

```powershell
git clone https://github.com/VinUni-AI20k/K4-L3B-Day04-Prompt-Engineering-Tool-Calling-Labs.git <TEN_REPO_DUNG_QUY_TAC>
cd <TEN_REPO_DUNG_QUY_TAC>
git remote rename origin upstream
git remote add origin <URL_REPO_NHOM>
git push -u origin main
```

Giữ riêng tư khi sao chép một nguồn còn riêng tư. Repo bài nộp phải cho giảng viên/tài khoản chấm bài truy cập được. Nếu dùng repo riêng tư, cấp quyền theo hướng dẫn lớp và kiểm tra trước hạn nộp.

Nhóm trưởng điền bảng thành viên trong `TEAM.md`. Mỗi người tự tạo branch, làm phần việc, commit dưới Git identity của mình và đưa vào nhánh nộp cuối cùng. Giữ các commit thể hiện đóng góp khi tích hợp. Chỉ có tên trong bảng thành viên hoặc commit phần tự đánh giá chưa đủ chứng minh công việc kỹ thuật.

## 3. Các file phải nộp

Cấu trúc dưới đây là **bài nộp đã hoàn thành**, không phải tất cả những file có sẵn trong starter:

```text
K4-L3-DAY04-HoVaTen-MSSV-PromptEngineeringToolCalling/
├── README.md                         # Hình thức, cách chạy UI, provider/model, link demo nếu có
├── TEAM.md                           # Thành viên + INDIVIDUAL của từng người
└── starter_v0/
    ├── artifacts/
    │   ├── system_prompt.md          # Hướng dẫn cuối cùng
    │   ├── tools.yaml                # Mô tả công cụ cuối cùng
    │   ├── version_log.csv           # v0, v1, v2, v3 và đường dẫn kết quả
    │   └── REPORT.md                 # Báo cáo và tự kiểm tra
    ├── data/
    │   ├── eval_base.json            # Giữ nguyên 30 tình huống có sẵn
    │   ├── eval_adversarial.json     # Giữ nguyên 12 tình huống thử an toàn
    │   ├── eval_helpdesk_extension.json # Giữ nguyên bộ mở rộng có sẵn
    │   └── eval_group.json           # Đúng 10 tình huống mới: 5 một lượt + 5 nhiều lượt
    ├── runs/                        # JSON thật: base v0–v3, group cuối, adversarial cuối
    ├── transcripts/                 # Hội thoại bình thường, thiếu thông tin, nhiều lượt, tạo phiếu
    ├── app.py hoặc mã nguồn UI/     # Nhóm tự xây, README chỉ rõ cách chạy
    ├── requirements.txt             # Có thêm thư viện mà UI/nhóm sử dụng
    └── ...                          # Giữ mã và dữ liệu starter cần thiết để chạy
```

`app.py` là ví dụ vị trí, không bắt buộc dùng Streamlit hoặc tên file này. Nếu đặt UI ở thư mục khác, README và REPORT phải trỏ đúng vị trí và lệnh chạy. Bản đề chưa cung cấp UI hoàn chỉnh; `eval_group.json` và mẫu báo cáo để trống có chủ đích cho học viên thực hiện.

Mỗi phiên bản lưu hướng dẫn tương ứng bằng commit hoặc bản chụp file. Trong báo cáo, nối phiên bản đó với run JSON và hash để kiểm tra lại. Không chỉ đổi nhãn `v1`, `v2`, `v3` trên cùng kết quả.

Điều kiện dùng một lần chạy làm bằng chứng: `provider_error_cases == 0` và `measured_cases == total_cases`. Xem cả lỗi công cụ, kết quả rỗng và câu trả lời cuối. Không dùng dữ liệu minh họa trong `samples/` thay cho kết quả của nhóm.

Các thư mục `runs/`, `transcripts/` và kết quả phân tích được phép commit sau khi kiểm tra nội dung. Không nộp `.env`, khóa truy cập, dữ liệu thật, `.venv`, cache hoặc file phiếu trong `tickets/`. Lưu bằng chứng kiểm tra việc tạo phiếu trong transcript/báo cáo, không nộp phiếu phát sinh.

## 4. Deadline và bản chốt

**Hạn nộp mặc định: 23:59 ngày diễn ra buổi Lab Day04 của lớp L3B, múi giờ Asia/Ho_Chi_Minh (UTC+07:00).** Lấy ngày học từ lịch lớp/VLearn, không lấy ngày trong dữ liệu giả lập của starter.

Nếu Keycoach thông báo một hạn khác trong vòng **48 giờ sau buổi lab**, áp dụng hạn đã thông báo. Khoảng 48 giờ là thời gian có thể công bố điều chỉnh, **không tự động gia hạn bài thêm 48 giờ**. Khi chưa có thông báo khác, nộp theo hạn 23:59 mặc định.

Mốc `T+155 phút` lúc 20:25 trong [CHECKPOINTS.md](CHECKPOINTS.md) là mốc kiểm tra bản làm tại lớp và chuẩn bị demo. Mốc này không thay thế hạn nộp cuối ngày.

Ghi commit chốt và thời điểm đẩy mã lên GitHub trong bài nộp VLearn nếu có ô ghi chú. Nếu hệ thống chỉ nhận URL, lưu commit chốt trong mục thông tin bài nộp của `TEAM.md` bằng một commit ghi nhận sau commit kỹ thuật cuối. Người chấm đối chiếu lịch sử GitHub và thời điểm VLearn ghi nhận, không chỉ dựa vào ngày tác giả tự đặt trong Git.

Sau deadline, không ghi đè hoặc sửa lịch sử bản đã nộp. Mọi sửa đổi sau hạn giữ ở commit/branch mới và khai rõ theo [RULES.md](RULES.md). Bài nộp muộn áp dụng quy định trừ điểm Keycoach công bố cho lớp.

## 5. Từng cá nhân tự nộp trên VLearn

1. Kiểm tra repo đã đặt đúng tên người đại diện và có đủ `TEAM.md`.
2. Mỗi người đăng nhập VLearn bằng tài khoản của mình, mở đúng **K4 — Level 3B — Day04**.
3. Nộp URL trang gốc của repo nhóm, ví dụ `https://github.com/<CHU_REPO>/<TEN_REPO>`.
4. Mở lại bài nộp để xác nhận URL đã lưu và người chấm mở được repo.
5. Cả nhóm đối chiếu: mỗi thành viên có một bài nộp trên VLearn, cùng URL repo chung.

Không dùng URL repo đề bài, pull request, commit riêng, thư mục con hoặc ảnh chụp thay cho URL repo bài nộp.

## 6. Kiểm tra trước khi nộp

- [ ] README ghi ngay đầu: làm nhóm, K4-L3B, Day04; có cách chạy UI.
- [ ] Tên repo đúng `K4-L3-DAY04-HoVaTen-MSSV-PromptEngineeringToolCalling`.
- [ ] `TEAM.md` đủ thành viên và mục INDIVIDUAL do từng người tự viết/commit.
- [ ] Nhánh nộp có commit đóng góp kỹ thuật của từng người.
- [ ] Có đủ file trong mục 3, kết quả thật và liên kết mở được.
- [ ] Bộ câu nhóm đúng 5 một lượt + 5 nhiều lượt; không sửa bộ câu cố định.
- [ ] Báo cáo phân tích ít nhất 3 tình huống an toàn; ghi rõ lỗi còn lại.
- [ ] Không có khóa truy cập, dữ liệu thật, cache hoặc phiếu phát sinh.
- [ ] Repo cho người chấm truy cập; ghi nhận bản chốt.
- [ ] Từng cá nhân đã tự nộp và kiểm tra lại URL trên VLearn trước deadline.
