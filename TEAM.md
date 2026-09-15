# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: TDCH
- Người đại diện: Nguyễn Hoàng Cường / MSSV:2A202602473
- Tên repo: `K4B-DAY4-TDCH`
- URL repo, nhánh nộp, commit chốt: https://github.com/5cuong/K4B-DAY4-TDCH · `main` · `3aa8b19`
- Deadline áp dụng và link thông báo đổi hạn nếu có:

## Thành viên

| Họ và tên          | MSSV | GitHub | Vai trò và công việc                                                                                      | File/commit/PR                  |
|--------------------|---|--------|-----------------------------------------------------------------------------------------------------------|---------------------------------|
| Nguyễn Hoàng Cường |2A202602473 | 5cuong | Experiment & Prompt Lead,Cài provider; chạy v0; phân tích lỗi baseline; thực hiện v1 trên system prompt, Run v0/v1, thay đổi `system_prompt.md`, metric và version log  | `2b6fa00`, `1a4dfd9`, `405f068` |
| Tống Trần Tiến Dũng |2A202602791 | Tiendung3tzz | Rà soát tool registry; cải thiện `tools.yaml`; thực hiện v2; xây bonus tool nếu có Tool declaration, tool implementation/smoke test, run v2 và bonus evidence  | `647663d`, `bf4806a`, `5ab5b13` |
| Vũ Đức Thiện |2A202602437 | vuthien3002-sys | Viết 10 group case; chạy group/adversarial; cải thiện confirmation, cancel và privacy cho v3 | `025eb0f`                       |
| Vũ Quốc Huy |2A202602929 | VuQuocHuy89 | Tích hợp UI web, transcript demo; hoàn thiện v2/v3 prompt/tool contract và evidence eval | `4c39b81`, `3aa8b19`            |

## Nhận xét chung

- Kết quả và bằng chứng: v3 base `30/30`, group `10/10`, adversarial `12/12`, extension `10/10`, tool bonus check_warranty 6/6; xem các run trong `starter_v0/runs/` và `starter_v0/artifacts/REPORT.md`.
- Thay đổi hiệu quả nhất: ràng buộc required arguments, latest-turn routing, fresh confirmation và privacy boundary.
- Giới hạn còn lại: UI/transcript và evidence đã có; mỗi thành viên vẫn phải tự viết mục INDIVIDUAL theo quy định.
- Cách phân công và tích hợp: Cường phụ trách v0/v1; Dũng phụ trách tool registry/bonus warranty; Thiện phụ trách group/safety cases; Huy phụ trách UI, v2/v3 và tích hợp evidence.

## INDIVIDUAL

Sao chép mục này cho từng thành viên.

### Vũ Quốc Huy — 2A202602929

- Phần việc và file/commit/PR: `starter_v0/ui.py`, UI README section, v2/v3 artifacts, run eval và transcript; commit UI `4c39b81` và commit tích hợp chốt `3aa8b19`.
- Quyết định, khó khăn và cách xử lý: siết schema tool, thêm snapshot v0/v2 để hash reproducible, bổ sung quy tắc chống stale confirmation/prompt injection và kiểm thử lại bằng OpenRouter.
- Điều đã học: phân biệt lỗi routing, argument và boundary; kết quả chỉ hợp lệ khi không có provider error và phải kiểm tra tool result/filesystem.
- AI/công cụ đã dùng và cách kiểm tra: Codex, OpenRouter `openai/gpt-4o-mini`; kiểm tra bằng run base/group/adversarial/extension, smoke tests và UI HTTP requests.
- Thời điểm đã tự nộp URL repo chung trên VLearn: thành viên tự điền.

### Nguyễn Hoàng Cường — 2A202602473

- Phần việc và file/commit/PR: phụ trách chuẩn bị provider, lưu baseline tại `starter_v0/artifacts/system_prompt.v0.md`, xây prompt v1, ghi giả thuyết trong `starter_v0/artifacts/EXPERIMENT_MEMBER1.md` và theo dõi metric ở `starter_v0/artifacts/version_log.csv`. Evidence hợp lệ là `starter_v0/runs/v0_B_base_openrouter_20260915T215253369415.json` và `starter_v0/runs/v1_B_base_openrouter_20260915T215355736879.json`; các commit phần việc được liệt kê trong bảng thành viên (`1a4dfd9`, `405f068`), PR #1 đã được merge vào repo nhóm.
- Quyết định, khó khăn và cách xử lý: giữ nguyên bộ 30 case và bản prompt gốc để so sánh đúng điều kiện. Các lần chạy Gemini gặp `429 RESOURCE_EXHAUSTED` (29/30 và 30/30 provider error), nên chỉ lưu chúng làm chẩn đoán, không dùng làm baseline. Chuyển sang OpenRouter để đo đủ 30 case; trace v0 cho thấy agent gọi thêm tool khi tra nhân viên, đoán asset/employee ID khi thiếu thông tin, tạo ticket trước xác nhận và truyền thiếu tham số `check`. V1 bổ sung quy tắc routing, hỏi lại, ưu tiên sửa/hủy ở lượt mới và xác nhận ticket; case accuracy tăng từ 21/30 (0,70) lên 24/30 (0,80). V1 vẫn còn lỗi, chẳng hạn chọn sai category của KB và sai `response_type` khi cần hỏi xác nhận.
- Điều đã học: lỗi API/quota khác lỗi của agent; chỉ so sánh run khi `provider_error_cases = 0` và `measured_cases = total_cases`. Cần đọc cả tool call, arguments và tool result; tỷ lệ PASS một mình không chứng minh hành động ghi dữ liệu đã đúng. Prompt giúp định hướng hành vi, còn schema và mô tả tool cần được siết ở vòng sau để sửa lỗi input còn lại.
- AI/công cụ đã dùng và cách kiểm tra: Codex, Python, Git, Gemini để preflight/chẩn đoán quota và OpenRouter `openai/gpt-4o-mini` cho run v0/v1 hợp lệ. Kiểm tra bằng `scripts/preflight_provider.py`, `run_eval.py`, summary 30/30 không có provider error, đối chiếu các case FAIL và `tool_results` trong run JSON, hash của prompt/tool trong version log.
- Thời điểm đã tự nộp URL repo chung trên VLearn: 20:00:01 15/9/2026

> Thành viên tự viết và commit nội dung INDIVIDUAL của mình theo quy định lab.

### Tống Trần Tiến Dũng — 2A202602791

- Phần việc và file/commit/PR: Phụ trách Tool bonus & check input: rà soát tool registry và khai báo tham số; chạy eval v1 làm cơ sở phân tích; bổ sung test_tools_smoke.py giúp Kiểm tra các tool, khai báo tham số và cơ chế an toàn hoạt động đúng. xây dựng bonus tool check_warranty cùng dữ liệu phạm vi bảo hành giả lập cho tool bonus, tài liệu tool, đăng ký registry và declaration. Viết test_check_warranty.py Kiểm tra tool bảo hành xử lý đúng trạng thái, dữ liệu đầu vào và các trường hợp lỗi; chạy eval v2-bonus. Các commit:
    - dfc98a4 : chạy run test v1.
    - ae562fd : Bổ sung test_tools_smoke.py.
    - 647663d : Tạo tool mới (bonus) test_check_warranty.py và tạo các file liên quan cho tool bonus (data, khai báo tool, đăng ký registry và declaration)
    - bf4806a : chạy tool bonus và lưu kết quả
    
- Quyết định, khó khăn và cách xử lý: Dùng kết quả eval v1 để xác định lỗi chọn tool và tham số trước khi đề xuất cải tiến. Với bonus, tái sử dụng warranty_until trong inventory, bổ sung dữ liệu phạm vi bảo hành riêng để tránh trùng lặp ngày hết hạn. Tính trạng thái theo ngày snapshot giúp kết quả kiểm thử ổn định. Xử lý riêng mã sai, thiết bị không tồn tại, thiếu ngày bảo hành và lỗi dữ liệu; không suy đoán phạm vi khi chưa có thông tin. Khi PowerShell hiển thị NativeCommandError dù test báo OK, xác định nguyên nhân là unittest ghi kết quả ra stderr và điều chỉnh cách xuất log.

- Điều đã học: cách tạo 1 tool mới, Phân biệt smoke test kiểm tra implementation với eval kiểm tra khả năng AI chọn tool và điền tham số. Hiểu rằng tên tool, schema và chữ ký hàm phải thống nhất; routing đúng chưa bảo đảm thực thi thành công. Việc kiểm tra ngày hết hạn, input không hợp lệ và dữ liệu thiếu giúp tool xử lý được nhiều tình huống hơn ngoài trường hợp thông thường.

- AI/công cụ đã dùng và cách kiểm tra: Sử dụng Codex để hỗ trợ đọc cấu trúc repo, phân tích run, đề xuất declaration, implementation và test. Dùng Python unittest, PowerShell, OpenRouter với model openai/gpt-4o-mini và Git/GitHub để chạy kiểm tra, lưu evidence và quản lý thay đổi. Đối chiếu đề xuất với mã nguồn và kết quả thực tế; bộ test_check_warranty.py chạy đạt 10/10 test và tools check_warranty đạt 6/6 test. Kết quả eval được lưu trong run JSON để kiểm tra metric, tool call và lỗi thực thi; không dùng smoke test để suy ra điểm eval.

- Thời điểm đã tự nộp URL repo chung trên VLearn: [06:04:17 16/9/2026]

### Vũ Đức Thiện — 2A202602437

- Phần việc và file/commit/PR: thành viên tự điền.
- Quyết định, khó khăn và cách xử lý: thành viên tự điền.
- Điều đã học: thành viên tự điền.
- AI/công cụ đã dùng và cách kiểm tra: thành viên tự điền.
- Thời điểm đã tự nộp URL repo chung trên VLearn: thành viên tự điền.
