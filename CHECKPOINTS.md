# Checkpoints — Day04, K4-L3B

**Hình thức: làm nhóm.** Buổi học diễn ra từ **17:30 đến 21:00**. Mở đầu và Kahoot dùng 20 phút đầu. `T+0` là **17:50**, khi các nhóm bắt đầu làm bài. Các nhóm có thể phân công UI, bộ câu và báo cáo song song.

Mốc kiểm tra bản tại lớp ở `T+155` là **20:25**, không phải deadline cuối cùng. Hạn mặc định là 23:59 ngày học, múi giờ Asia/Ho_Chi_Minh (UTC+07:00); xem [SUBMISSION.md](SUBMISSION.md).

| Mốc | Việc chính | Giờ lớp | Khoảng T+ | Thời lượng |
|---|---|---|---|---:|
| Mở đầu | Slide 1–2 | 17:30–17:40 | — | 10 phút |
| Kahoot | Quiz khởi động | 17:40–17:50 | — | 10 phút |
| CP0 | Môi trường, repo và phân công | 17:50–18:00 | T+0–T+10 | 10 phút |
| CP1 | Bản gốc v0 và đọc lỗi | 18:00–18:20 | T+10–T+30 | 20 phút |
| CP2 | Ba vòng cải tiến v1–v3 | 18:20–19:05 | T+30–T+75 | 45 phút |
| CP3 | Hội thoại và an toàn | 19:05–19:30 | T+75–T+100 | 25 phút |
| CP4 | Bộ câu riêng và UI | 19:30–20:10 | T+100–T+140 | 40 phút |
| FINAL | Kiểm tra bản tại lớp | 20:10–20:25 | T+140–T+155 | 15 phút |
| DEMO | Trình bày và trao đổi | 20:25–21:00 | T+155–T+190 | 35 phút |

Các lệnh Python dưới đây chạy trong `starter_v0/`. Thay `openrouter` bằng nhà cung cấp đã cấu hình. Kiểm tra kết nối AI cần khóa truy cập và có thể dùng quota.

## CP0 — Môi trường và repo nhóm

**Cần làm:** tạo repo đúng tên trong SUBMISSION; điền bảng TEAM; phân công. Theo TOOL-SETUP để cài Python 3.10+, môi trường ảo, thư viện và `.env`. Chạy kiểm tra cú pháp, công cụ local rồi kiểm tra nhà cung cấp AI.

**Sản phẩm:** repo chung mọi thành viên truy cập được, bảng phân công và môi trường chạy được.

**Cần hiểu:** phân biệt lỗi cài đặt/kết nối với lỗi trong hướng dẫn cho AI; kiểm tra nhà cung cấp không thay thế chấm chất lượng trợ lý.

**Tự kiểm tra:** các smoke command local trong TOOL-SETUP hoạt động; lệnh sau trả lời gọi công cụ có cấu trúc:

```powershell
python -m compileall -q .
python scripts/preflight_provider.py --provider openrouter
```

## CP1 — Bản gốc v0 và đọc lỗi

**Cần làm:** giữ nguyên hướng dẫn và khai báo công cụ, chạy bộ cơ bản. Đọc một lỗi đại diện: kỳ vọng, công cụ thực tế, đầu vào, kết quả/lỗi và nguyên nhân có thể có.

**Sản phẩm:** run JSON v0; dòng v0 trong `artifacts/version_log.csv`; ghi chú lỗi trong REPORT; commit hoặc bản chụp hai file v0.

**Cần hiểu:** chọn sai công cụ khác với truyền sai thông tin hoặc công cụ thực thi lỗi. Một điểm PASS tự động không chứng minh toàn bộ câu trả lời đúng.

**Tự kiểm tra:** `total_cases == 30`, `measured_cases == total_cases`, `provider_error_cases == 0`; mở được file dẫn trong version log.

```powershell
python run_eval.py --provider openrouter --version v0 --suite base --eval-cases data/eval_base.json
```

## CP2 — Ba vòng cải tiến v1, v2, v3

**Cần làm:** mỗi vòng chọn lỗi, đặt giả thuyết, sửa một điểm chính trong `system_prompt.md` hoặc `tools.yaml`, chạy lại cùng bộ, đọc cả tình huống từng đúng và ghi kết quả. Giữ cùng provider/model khi so sánh nếu không chủ đích thử tác động của mô hình.

**Sản phẩm:** ba phiên bản có thay đổi thật, ba run base hợp lệ, version log đủ v0–v3 và bảng trước/sau trong REPORT. Lưu phiên bản file tương ứng với hash của từng run.

**Cần hiểu:** sửa quy tắc chung khác với sửa mô tả một công cụ. Nếu đổi nhiều thứ cùng lúc sẽ khó giải thích nguyên nhân kết quả thay đổi. Kết quả kém hơn vẫn cần ghi trung thực.

**Tự kiểm tra:** mỗi dòng có giả thuyết, lý do, chỉ số, hash và đường dẫn run thật; các bộ câu cố định không thay đổi. Thực hiện lệnh sau **sau từng lần sửa riêng**, không chạy liền ba nhãn trên cùng file:

```powershell
python run_eval.py --provider openrouter --version v1 --suite base --eval-cases data/eval_base.json
```

Đổi thành `v2` và `v3` cho các vòng tiếp theo. Mô tả trong REPORT điều được cải thiện và lỗi còn tồn tại.

## CP3 — Hội thoại và giới hạn an toàn

**Cần làm:** thử thiếu mã máy, sửa mã ở lượt sau, nhắc lại “máy đó”, xác nhận, hủy và thay nội dung phiếu. Chạy đủ bộ 12 tình huống thử an toàn. Phân tích ít nhất 3 tình huống dựa trên lời gọi và kết quả công cụ.

**Sản phẩm:** run adversarial của bản cuối; transcript và phần B4/B4a/B6 của REPORT. Ghi việc tạo file/gửi dữ liệu có thực sự xảy ra hay không.

**Cần hiểu:** xác nhận gắn với đúng nội dung; lệnh trong tài liệu không có quyền thay quy tắc; dữ liệu nội bộ không được gửi ra web. Kiểm tra tên công cụ đúng chưa đủ chứng minh an toàn.

**Tự kiểm tra:** có minh chứng cho yêu cầu bình thường, thiếu thông tin, nhiều lượt và giới hạn hành động; không có khóa truy cập hoặc dữ liệu thật trong bản nộp.

```powershell
python chat.py --provider openrouter --version v3
python run_eval.py --provider openrouter --version v3 --suite adversarial --eval-cases data/eval_adversarial.json
```

`--suite` chỉ là nhãn lưu kết quả. Phải truyền đúng `--eval-cases` để chọn bộ dữ liệu.

## CP4 — Bộ câu riêng và giao diện chat

**Cần làm:** điền `data/eval_group.json` bằng đúng 10 tình huống mới, 5 một lượt dùng `query`, 5 nhiều lượt dùng `turns`; khai hành vi mong đợi. Tham khảo định dạng trong `samples/`, không dùng nguyên hai câu mẫu làm bài. Xây/tích hợp UI có cách chạy rõ trong README bài nộp.

**Sản phẩm:** bộ câu riêng hợp lệ và kết quả chạy; mã UI; thư viện cần cài; transcript thể hiện công cụ, thông tin đầu vào, kết quả/lỗi và phiên bản.

**Cần hiểu:** tình huống do nhóm thiết kế phải kiểm tra một quyết định có ý nghĩa. UI phải phản ánh hành vi thật và tái sử dụng vòng xử lý hội thoại đã có khi phù hợp.

**Tự kiểm tra:** đếm đủ cấu trúc 5 + 5; tên công cụ kỳ vọng có trong registry; chạy bộ nhóm với bản cuối; một thành viên khác làm theo README mở được UI.

```powershell
python run_eval.py --provider openrouter --version v3 --suite group --eval-cases data/eval_group.json
```

Nếu làm phần mở rộng, dùng thêm `data/eval_helpdesk_extension.json` với `--suite extension`. Bộ mở rộng không thay thế bộ nhóm hoặc bộ an toàn.

## FINAL — Kiểm tra bản tại lớp

**Cần làm:** tích hợp code, chạy và đối chiếu danh sách nộp. Hoàn thiện báo cáo, nhận xét nhóm, INDIVIDUAL và lịch sử đóng góp. Chuẩn bị bản demo và file kết quả dự phòng.

**Sản phẩm:** bản tại lớp có các đầu ra trong SUBMISSION, cùng danh sách phần còn thiếu nếu chưa hoàn tất. Có thể nộp sớm và kiểm tra lại link trước deadline.

**Cần hiểu:** mỗi người phải tự nộp trên VLearn dù bài làm chung. T+155 là mốc lớp lúc 20:25, còn deadline mặc định là 23:59 ngày học.

**Tự kiểm tra:** mở repo trên GitHub, đối chiếu file đã đẩy thật bằng `git status` và lịch sử commit; kiểm tra từng URL/run/transcript. Không chỉ kiểm tra bản trên máy. Mỗi người theo danh sách cuối SUBMISSION trước khi chốt bài.

## DEMO — Trình bày và trao đổi

**Cần làm:** chọn 3–5 kịch bản đã thử, trình bày lỗi trước sửa, giả thuyết, thay đổi, kết quả sau sửa và giới hạn. Keycoach phân bổ thời gian theo số nhóm thực tế.

**Sản phẩm:** phần trình bày dựa trên kết quả thật và ghi chú phản hồi để tiếp tục hoàn thiện trước hạn.

**Cần hiểu:** không suy ra chất lượng toàn bộ từ một ví dụ thành công. Điểm phát biểu/pitching không phải bonus kỹ thuật của lab.

**Tự kiểm tra:** mở ngay được file minh chứng cho từng kết luận; dùng kết quả dự phòng nếu kết nối AI lỗi; không trình bày ví dụ kỳ vọng như một lần chạy đã thành công. 35 phút là thời lượng chung của cả lớp.
