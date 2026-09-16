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
| Nguyễn Hoàng Cường |2A202602473 | 5cuong | Experiment & Prompt Lead,Cài provider; chạy v0; phân tích lỗi baseline; thực hiện v1 trên system prompt, Run v0/v1, thay đổi `system_prompt.md`, metric và version log  | `2b6fa00`, `1a4dfd9`, `405f068`, `ff2bdf5` |
| Tống Trần Tiến Dũng |2A202602791 | Tiendung3tzz | Rà soát tool registry; cải thiện `tools.yaml`; thực hiện v2; xây bonus tool nếu có Tool declaration, tool implementation/smoke test, run v2 và bonus evidence  | `9f150e6`, `fc6f977`, `13747b4`, `dfc98a4`, `ae562fd`, `647663d`, `5ab5b13`, `bf4806a`, `69a76b1`, `e239980` |
| Vũ Đức Thiện |2A202602437 | vuthien3002-sys | Viết đúng 10 case nhóm gốc (`data/eval_group.json`: 5 một lượt + 5 nhiều lượt) bao phủ ý định mơ hồ, đính chính mã thiết bị/đổi quyết định, hủy hành động và policy+ticket sau xác nhận; chạy run group/adversarial hợp lệ (`provider_error_cases=0`) làm evidence cho ranh giới confirmation/cancel/privacy ở v3 | `ce5f1ec`, `025eb0f`, `a2b4a24`, `654db19` |
| Vũ Quốc Huy |2A202602929 | VuQuocHuy89 | Tích hợp UI web, transcript demo; hoàn thiện v2/v3 prompt/tool contract và evidence eval | `3d3a773`, `3ce2d67`, `4c39b81`, `3aa8b19`, `3f88f3c`, `c3ec3a7` |

> Danh sách trên tập trung vào các commit có trong lịch sử `main`. Commit UI `c5239aa` là bản gốc trên nhánh `Huy`, đã được tích hợp vào `main` bằng `4c39b81`; `13747b4` là merge PR #1 đưa phần v0/v1 của Cường vào repo nhóm.

## Nhận xét chung

- Kết quả và bằng chứng: v3 base `30/30`, group `10/10`, adversarial `12/12`, extension `10/10`, tool bonus check_warranty 6/6; xem các run trong `starter_v0/runs/` và `starter_v0/artifacts/REPORT.md`.
- Thay đổi hiệu quả nhất: ràng buộc required arguments, latest-turn routing, fresh confirmation và privacy boundary.
- Giới hạn còn lại: UI/transcript và evidence đã có; mục INDIVIDUAL của cả bốn thành viên đã được điền kèm commit tương ứng.
- Cách phân công và tích hợp: Cường phụ trách v0/v1; Dũng phụ trách tool registry/bonus warranty; Thiện phụ trách group/safety cases; Huy phụ trách UI, v2/v3 và tích hợp evidence.

## INDIVIDUAL

### Vũ Quốc Huy — 2A202602929

- Phần việc và file/commit/PR: `3d3a773` bổ sung thông tin thành viên trong `TEAM.md`; `3ce2d67` triển khai prompt và tool contract cho v2/v3 cùng các run thử nghiệm; `4c39b81` thêm `starter_v0/ui.py` và tài liệu UI; `3aa8b19` tích hợp REPORT, snapshot prompt/tool, các run eval và transcript; `3f88f3c` ghi nhận commit chốt; `c3ec3a7` cập nhật thời điểm nộp VLearn. Commit `c5239aa` là bản gốc UI trên nhánh `Huy`, được tích hợp tương ứng bằng `4c39b81`.
- Quyết định, khó khăn và cách xử lý: siết schema tool, thêm snapshot v0/v2 để hash reproducible, bổ sung quy tắc chống stale confirmation/prompt injection và kiểm thử lại bằng OpenRouter.
- Điều đã học: phân biệt lỗi routing, argument và boundary; kết quả chỉ hợp lệ khi không có provider error và phải kiểm tra tool result/filesystem.
- AI/công cụ đã dùng và cách kiểm tra: Codex, OpenRouter `openai/gpt-4o-mini`; kiểm tra bằng run base/group/adversarial/extension, smoke tests và UI HTTP requests.
- Thời điểm đã tự nộp URL repo chung trên VLearn: [21:45:00 15/9/2026]

### Nguyễn Hoàng Cường — 2A202602473

- Phần việc và file/commit/PR: `2b6fa00` khởi tạo thông tin nhóm; `1a4dfd9` chuẩn bị provider, lưu baseline tại `starter_v0/artifacts/system_prompt.v0.md`, xây prompt v1, ghi giả thuyết trong `starter_v0/artifacts/EXPERIMENT_MEMBER1.md` và theo dõi metric ở `starter_v0/artifacts/version_log.csv`; `405f068` ghi vai trò/evidence vào `TEAM.md`; `ff2bdf5` hoàn thiện metadata nhóm. Evidence hợp lệ là `starter_v0/runs/v0_B_base_openrouter_20260915T215253369415.json` và `starter_v0/runs/v1_B_base_openrouter_20260915T215355736879.json`; PR #1 (`13747b4`) đã được merge vào repo nhóm.
- Quyết định, khó khăn và cách xử lý: giữ nguyên bộ 30 case và bản prompt gốc để so sánh đúng điều kiện. Các lần chạy Gemini gặp `429 RESOURCE_EXHAUSTED` (29/30 và 30/30 provider error), nên chỉ lưu chúng làm chẩn đoán, không dùng làm baseline. Chuyển sang OpenRouter để đo đủ 30 case; trace v0 cho thấy agent gọi thêm tool khi tra nhân viên, đoán asset/employee ID khi thiếu thông tin, tạo ticket trước xác nhận và truyền thiếu tham số `check`. V1 bổ sung quy tắc routing, hỏi lại, ưu tiên sửa/hủy ở lượt mới và xác nhận ticket; case accuracy tăng từ 21/30 (0,70) lên 24/30 (0,80). V1 vẫn còn lỗi, chẳng hạn chọn sai category của KB và sai `response_type` khi cần hỏi xác nhận.
- Điều đã học: lỗi API/quota khác lỗi của agent; chỉ so sánh run khi `provider_error_cases = 0` và `measured_cases = total_cases`. Cần đọc cả tool call, arguments và tool result; tỷ lệ PASS một mình không chứng minh hành động ghi dữ liệu đã đúng. Prompt giúp định hướng hành vi, còn schema và mô tả tool cần được siết ở vòng sau để sửa lỗi input còn lại.
- AI/công cụ đã dùng và cách kiểm tra: Codex, Python, Git, Gemini để preflight/chẩn đoán quota và OpenRouter `openai/gpt-4o-mini` cho run v0/v1 hợp lệ. Kiểm tra bằng `scripts/preflight_provider.py`, `run_eval.py`, summary 30/30 không có provider error, đối chiếu các case FAIL và `tool_results` trong run JSON, hash của prompt/tool trong version log.
- Thời điểm đã tự nộp URL repo chung trên VLearn: 20:00:01 15/9/2026


### Tống Trần Tiến Dũng — 2A202602791

- Phần việc và file/commit/PR: `9f150e6` bổ sung vai trò Dũng vào `TEAM.md`; `fc6f977` cập nhật/giải quyết danh sách vai trò; `13747b4` merge PR #1 trên GitHub để tích hợp phần v0/v1 vào repo nhóm; `dfc98a4` chạy eval v1; `ae562fd` thêm `test_tools_smoke.py`; `647663d` tạo tool bonus `check_warranty`, dữ liệu, declaration và test; `5ab5b13` merge phần tool/prompt và giải quyết xung đột `tools.yaml`; `bf4806a` chạy eval v2-bonus và lưu evidence; `69a76b1` viết mục INDIVIDUAL; `e239980` cập nhật đóng góp trong bảng thành viên.
    
- Quyết định, khó khăn và cách xử lý: Dùng kết quả eval v1 để xác định lỗi chọn tool và tham số trước khi đề xuất cải tiến. Với bonus, tái sử dụng warranty_until trong inventory, bổ sung dữ liệu phạm vi bảo hành riêng để tránh trùng lặp ngày hết hạn. Tính trạng thái theo ngày snapshot giúp kết quả kiểm thử ổn định. Xử lý riêng mã sai, thiết bị không tồn tại, thiếu ngày bảo hành và lỗi dữ liệu; không suy đoán phạm vi khi chưa có thông tin. Khi PowerShell hiển thị NativeCommandError dù test báo OK, xác định nguyên nhân là unittest ghi kết quả ra stderr và điều chỉnh cách xuất log.

- Điều đã học: cách tạo 1 tool mới, Phân biệt smoke test kiểm tra implementation với eval kiểm tra khả năng AI chọn tool và điền tham số. Hiểu rằng tên tool, schema và chữ ký hàm phải thống nhất; routing đúng chưa bảo đảm thực thi thành công. Việc kiểm tra ngày hết hạn, input không hợp lệ và dữ liệu thiếu giúp tool xử lý được nhiều tình huống hơn ngoài trường hợp thông thường.

- AI/công cụ đã dùng và cách kiểm tra: Sử dụng Codex để hỗ trợ đọc cấu trúc repo, phân tích run, đề xuất declaration, implementation và test. Dùng Python unittest, PowerShell, OpenRouter với model openai/gpt-4o-mini và Git/GitHub để chạy kiểm tra, lưu evidence và quản lý thay đổi. Đối chiếu đề xuất với mã nguồn và kết quả thực tế; bộ test_check_warranty.py chạy đạt 10/10 test và tools check_warranty đạt 6/6 test. Kết quả eval được lưu trong run JSON để kiểm tra metric, tool call và lỗi thực thi; không dùng smoke test để suy ra điểm eval.

- Thời điểm đã tự nộp URL repo chung trên VLearn: [06:04:17 16/9/2026]

### Vũ Đức Thiện — 2A202602437

- Phần việc và file/commit/PR: `ce5f1ec` bổ sung thông tin Thiện vào `TEAM.md`; `025eb0f` viết đúng 10 case nhóm gốc trong `starter_v0/data/eval_group.json` (5 một lượt G01–G05, 5 nhiều lượt G06–G10), tạo dữ liệu ví dụ và chạy eval group/adversarial; `a2b4a24` hoàn thiện mô tả case, evidence và kết quả; `654db19` cập nhật thời điểm nộp VLearn. Các case được thiết kế dựa trên phân tích lỗi thật ở `starter_v0/runs/v0_B_base_openrouter_20260915T194104245628.json` và đối chiếu asset/employee ID với `starter_v0/helpdesk_data/`. Bộ case bao phủ đúng 4 nhóm kịch bản được yêu cầu: ý định mơ hồ buộc hỏi lại (G03, G05), người dùng đính chính mã thiết bị/đổi quyết định ở lượt sau (G06, G07, G09), yêu cầu hủy hành động (G08), và tra cứu chính sách IT kết hợp tạo ticket sau khi xác nhận (G10). Evidence hợp lệ là run group `10/10` và adversarial `12/12` với `provider_error_cases=0`.
- Quyết định, khó khăn và cách xử lý: Chọn dùng ID có thật trong `users.json`/`assets.json` để case chạy được với dữ liệu giả lập, đồng thời tránh trùng câu hỏi với `eval_base.json`. Lần chạy đầu (20:42 15/9) thiếu cấu hình `OPENROUTER_API_KEY` trong `.env` nên toàn bộ 10 case nhóm và 12 case adversarial đều bị `provider_error_cases` (10/10 và 12/12), không dùng làm bằng chứng; sau khi điền lại `.env` đúng key và chạy lại, thu được run hợp lệ `provider_error_cases=0`: group `10/10` (`runs/v3_B_group_openrouter_20260915T221217368853.json`), adversarial `12/12` (`runs/v3_B_adversarial_openrouter_20260915T221251211267.json`).
- Điều đã học: Lỗi thiếu API key/quota (provider_error) khác hoàn toàn với lỗi hành vi agent (routing/argument/boundary sai); chỉ được tính run khi `provider_error_cases=0` và `measured_cases=total_cases`. Ranh giới xác nhận trước khi ghi dữ liệu (create_ticket) phải áp dụng ở mọi mức priority chứ không riêng high/critical, và một hành động hủy ở lượt sau phải thắng hoàn toàn yêu cầu ghi dữ liệu trước đó. Bộ adversarial cho thấy các kiểu tấn công (exfiltration prompt, giả role, forged tool result, stale confirmation, external identifier smuggling...) cần được chặn ở tầng ranh giới hành vi, không chỉ dựa vào câu trả lời text.
- AI/công cụ đã dùng và cách kiểm tra: Dùng Claude (Claude Code) để đọc run JSON của v0, đối chiếu `tools.yaml`/`helpdesk_data` và soạn 10 case đúng schema `expect`/`tool_calls`/`turns`. Tự kiểm tra bằng cách chạy thật `run_eval.py --provider openrouter --version v3 --suite group|adversarial --eval-cases ...` (model `openai/gpt-4o-mini`), đọc trực tiếp `summary` và từng `result`/`tool_results` trong run JSON để xác nhận `passed=10/10` và `12/12` thay vì chỉ tin vào log tool.
- Thời điểm đã tự nộp URL repo chung trên VLearn: [07:40:14 16/9/2026]
