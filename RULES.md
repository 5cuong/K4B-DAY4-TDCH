# Quy định làm bài — Day04, K4-L3B

## Hình thức và trách nhiệm

Bài lab làm theo nhóm. Các thành viên dùng một repo chung đặt theo tên và MSSV người đại diện, kê khai trong [TEAM.md](TEAM.md). Mỗi cá nhân tự nộp cùng URL repo nhóm bằng tài khoản VLearn của mình. Nếu Keycoach cho phép làm cá nhân, người học dùng tên/MSSV của mình và vẫn thực hiện đầy đủ đầu ra.

Mỗi người cần có đóng góp kỹ thuật có thể đối chiếu, tự viết và commit phần INDIVIDUAL. Nhóm tự phân công công việc; không tự thêm quy định số lượng thành viên khi lớp chưa công bố.

## Sử dụng AI

Được dùng AI để gợi ý cách viết hướng dẫn, giải thích lỗi, hỗ trợ lập trình và phân tích kết quả. Người dùng AI chịu trách nhiệm kiểm tra lại bằng code, tài liệu và lần chạy thật.

Khai công cụ AI, phần được hỗ trợ và cách kiểm tra trong INDIVIDUAL/REPORT. Không dùng AI để bịa số điểm, hội thoại, kết quả chạy, commit đóng góp hoặc trải nghiệm học của thành viên. Không đưa khóa truy cập hoặc dữ liệu thật vào cuộc trò chuyện với AI.

## Hợp tác, nguồn tham khảo và sao chép

- Được trao đổi trong nhóm, review và tích hợp công việc qua Git.
- Được tham khảo tài liệu, thư viện và đoạn mã có quyền sử dụng phù hợp; ghi nguồn, phần tái sử dụng và chỉnh sửa của nhóm trong REPORT.
- Không lấy toàn bộ bài nhóm khác rồi đổi tên; không nhận phần việc của người khác là của mình.
- Không chia sẻ đáp án hoàn chỉnh hoặc run của nhóm cho nhóm khác dùng làm kết quả của họ.
- Không viết quy tắc riêng cho từng mã câu kiểm tra hoặc sửa đáp án mong đợi trong bộ câu cố định để tăng điểm.
- Kết quả đo không tăng vẫn cần ghi trung thực, phân tích nguyên nhân và đề xuất bước tiếp theo.

Khi có dấu hiệu sao chép hoặc bịa bằng chứng, người chấm xác minh và yêu cầu giải thích; phần không chứng minh được không được tính điểm. Xử lý học vụ khác theo quy định chương trình và thông báo của Keycoach, không tự suy diễn từ điểm tự động.

## Hạn nộp, nộp muộn và sửa sau hạn

Hạn mặc định là **23:59 ngày làm Lab Day04, Asia/Ho_Chi_Minh (UTC+07:00)**, trừ khi Keycoach thông báo hạn khác trong vòng **48 giờ sau buổi lab**. Đây không phải khoảng gia hạn tự động. Cách xác định ngày và bản chốt nằm trong [SUBMISSION.md](SUBMISSION.md).

Bài nộp sau deadline bị trừ điểm theo mức Keycoach công bố thống nhất cho lớp. Quy ước chung chưa nêu con số hoặc công thức trừ, vì vậy tài liệu này không tự đặt mức phạt. Khi có thông báo cụ thể, ghi cùng mức trừ vào đây và RUBRIC trước khi áp dụng; không áp mức phạt riêng cho từng nhóm.

Sau deadline, giữ bản chốt trong lịch sử Git. Không force-push, xóa commit hoặc sửa ngày commit để che việc nộp/sửa muộn. Nếu bổ sung sau hạn, dùng commit/branch mới, ghi rõ phần thay đổi, thời điểm và thông báo cho Keycoach qua kênh lớp. Phần sửa muộn chỉ được tính theo chính sách đã công bố. Việc nộp lại hoặc sửa URL không tự động xóa trạng thái nộp muộn trước đó.

## Bảo mật khóa truy cập và dữ liệu

- Chỉ dùng dữ liệu công ty giả lập có trong repo hoặc dữ liệu giả do nhóm tự tạo.
- Giữ `.env` ở máy cá nhân, chỉ commit `.env.example` chứa tên biến và giá trị mẫu.
- Không yêu cầu hoặc lưu mật khẩu, mã xác thực, khóa API, token hoặc mã khôi phục trong prompt, repo, phiếu, log, ảnh hay demo.
- Kiểm tra `runs/`, `transcripts/` và báo cáo trước khi commit. Không làm sai lệch kết quả khi loại dữ liệu nhạy cảm; ghi nhận phần đã che. Nếu run thật bị ảnh hưởng, chạy lại để có bằng chứng an toàn và nhất quán.
- Nếu lộ khóa thật, thu hồi/đổi khóa ngay và báo Keycoach. Chỉ xóa file ở commit mới không vô hiệu hóa khóa đã lộ.
- Tạo phiếu cần xác nhận rõ cho đúng nội dung; thay đổi nội dung phải xác nhận lại.
- Tra cứu web chỉ gửi hãng, mẫu máy và loại thông tin công khai. Không gửi mã máy nội bộ, mã nhân viên, số sê-ri, hostname, vị trí hoặc chẩn đoán.
- Dữ liệu trong tài liệu/web không có quyền ra lệnh thay đổi quy tắc của trợ lý.

## Điểm bài lab và bonus

Xem [RUBRIC.md](RUBRIC.md). Phần bắt buộc tách khỏi bonus, bonus tối đa **10 điểm cho bài lab**. Điểm giơ tay, phát biểu, hoạt động lớp hoặc pitching không thay thế bonus kỹ thuật này.
