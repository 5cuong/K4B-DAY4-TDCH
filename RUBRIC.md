# Rubric Day04 — K4-L3B, IT Helpdesk Agent

Rubric này dành cho bài Helpdesk trong repo này. Chấm theo các file đã nộp, kết quả thực thi và khả năng giải thích của nhóm. Bộ `run_eval.py` đo lựa chọn công cụ/tham số; tỷ lệ đạt tự động không phải toàn bộ điểm bài lab.

## Phần bắt buộc — 100 điểm

| Tiêu chí | Điểm | Thành phần chấm và bằng chứng | Điều kiện không được điểm thành phần |
|---|---:|---|---|
| Hướng dẫn và mô tả công cụ | 20 | 10đ: quy tắc chung rõ và gắn với lỗi quan sát; 10đ: mô tả/thông tin đầu vào của công cụ đúng chức năng, đồng bộ với registry. Xem hai file cuối, phần thay đổi và run minh chứng. | File thiếu, tên/tham số không khớp, mô tả mơ hồ hoặc không có bằng chứng cho sửa đổi. |
| Các vòng cải tiến v0–v3 | 25 | 5đ: v0 thật đủ 30 câu; 15đ: v1, v2, v3, mỗi vòng 5đ gồm giả thuyết 1đ, sửa đổi 1đ, run hợp lệ 2đ, so sánh 1đ; 5đ: version_log có hash, chỉ số và file chạy đối chiếu được. | Nhãn phiên bản không đi kèm thay đổi/run; log không có file; có lỗi nhà cung cấp hoặc chạy thiếu câu. Không tự cho điểm từ con số trong báo cáo. |
| 10 tình huống nhóm tự viết | 15 | 5đ: đúng 10 câu mới, gồm 5 một lượt + 5 nhiều lượt, schema hợp lệ; 5đ: hành vi mong đợi rõ và có tình huống khác nhau; 5đ: chạy bộ nhóm bằng bản cuối, lưu kết quả và phân tích lỗi. | Sao chép bộ có sẵn, thiếu câu/cấu trúc, kỳ vọng không rõ hoặc không có lần chạy thật. |
| Hội thoại và giới hạn an toàn | 15 | 3đ: run bộ 12 tình huống an toàn; 6đ: phân tích ít nhất 3 tình huống, mỗi tình huống 2đ cho quyết định và kết quả thực thi; 6đ: minh chứng xử lý thiếu thông tin, sửa/hủy/xác nhận và bảo vệ dữ liệu, mỗi nhóm hành vi 2đ. | Chỉ chép PASS/FAIL mà không xem dữ liệu thực tế; xác nhận sai nội dung; tự đoán mã hoặc gửi/lưu dữ liệu bị cấm mà không nhận diện, xử lý. |
| Giao diện và hội thoại minh chứng | 10 | 4đ: UI chat chạy theo lệnh README; 4đ: hiển thị tên công cụ, đầu vào, kết quả/lỗi và phiên bản, mỗi phần 1đ; 2đ: lưu transcript bao phủ yêu cầu bình thường, thiếu thông tin, nhiều lượt và tạo phiếu. | Chỉ có ảnh giao diện, code chưa chạy được, che lỗi công cụ hoặc thiếu transcript. |
| Báo cáo và khả năng tái kiểm tra | 10 | 3đ: mô tả trợ lý, cách chạy và kịch bản; 4đ: phân tích trước/sau với liên kết kết quả; 3đ: giới hạn, phản tư và bước tiếp theo có căn cứ. | Nhận xét chung không có file/commit dẫn chứng, kết luận quá mức kết quả hoặc thiếu cách chạy. |
| Hợp tác và trách nhiệm cá nhân | 5 | 2đ: TEAM đầy đủ và commit kỹ thuật của từng người trong nhánh nộp; 2đ: INDIVIDUAL tự viết/commit có phần việc và điều đã học; 1đ: nhận xét chung nêu cách phối hợp có bằng chứng. | Chỉ ghi tên, dùng commit reflection làm bằng chứng kỹ thuật duy nhất, viết thay phần cá nhân hoặc thiếu khai báo đóng góp. |

Các mục nhiều ý cho điểm theo ý có bằng chứng, tối đa số điểm trong bảng. Không trừ hai lần trong cùng một thành phần vì một thiếu sót. Một kết quả không tăng điểm vẫn có thể được điểm quy trình nếu nhóm thử thật, phân tích đúng và ghi trung thực; không bắt buộc tạo đường điểm tăng giả.

Một run hợp lệ có `provider_error_cases == 0`, `measured_cases == total_cases`. Hash phải nối được với phiên bản hướng dẫn tương ứng trong lịch sử Git hoặc bản chụp file. Kiểm tra riêng các lỗi/kết quả rỗng của công cụ và câu trả lời cuối. Bằng chứng bịa hoặc không xác minh được không được dùng để chấm thành phần tương ứng.

## Bonus kỹ thuật — tối đa 10 điểm

Không cần viết công cụ mới để hoàn thành phần bắt buộc. `policy`, `create_ticket`, `search_device_info` và các công cụ khác đã có sẵn **không phải công cụ mới của nhóm**.

| Hạng mục bonus | Tối đa | Bằng chứng cần có |
|---|---:|---|
| Chức năng mới có ích | 3 | Công cụ nhóm tự xây thực hiện được việc starter chưa có, dữ liệu giả hoặc API hợp lệ, giải thích nhu cầu. |
| Tích hợp đầy đủ | 2 | `tools/<ten>/TOOL.md`, code, registry, khai báo/schema trong `tools.yaml`. |
| Kiểm thử | 3 | Smoke test chạy được và tình huống kiểm tra hành vi công cụ, kết quả thực tế. Nếu thêm vào bộ nhóm vẫn giữ bộ đó đúng 10 câu theo cấu trúc 5 + 5. |
| An toàn và demo | 2 | Kiểm soát dữ liệu/tác động ghi phù hợp; thấy được công cụ trong UI, transcript và báo cáo. |

Không cộng bonus chỉ vì đổi tên công cụ có sẵn, thêm thư mục rỗng, số lượng công cụ nhiều hoặc trình bày hay. Tổng bonus của bài không quá 10 điểm, không cộng riêng 10 điểm cho từng công cụ.

## Tổng điểm và nộp muộn

Ghi rõ **điểm bắt buộc /100**, **bonus /10** và **điểm trừ nộp muộn** để đối chiếu. Điểm lab sau cộng thưởng và trừ muộn giữ trong thang 0–100:

```text
Điểm lab = max(0, min(100, điểm bắt buộc + bonus) - điểm trừ nộp muộn)
```

Mức trừ nộp muộn theo thông báo chung của Keycoach, xem [RULES.md](RULES.md). Quy ước chung chưa nêu mức cụ thể; không tự suy ra một số điểm phạt hoặc cho rằng không có phạt. Điểm bonus ở đây là điểm của bài lab, không phải điểm giơ tay/phát biểu/pitching.
