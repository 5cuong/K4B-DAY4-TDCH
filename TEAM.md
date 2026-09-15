# TEAM — Day04, K4-L3B

**Làm nhóm.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: TDCH
- Người đại diện / MSSV:2A202602473
- Tên repo: `K4B-DAY4-TDCH`
- URL repo, nhánh nộp, commit chốt: https://github.com/5cuong/K4B-DAY4-TDCH · `main` · `3aa8b19`
- Deadline áp dụng và link thông báo đổi hạn nếu có:

## Thành viên

| Họ và tên          | MSSV | GitHub | Vai trò và công việc                                                                                      | File/commit/PR |
|--------------------|---|--------|-----------------------------------------------------------------------------------------------------------|---|
| Nguyễn Hoàng Cường |2A202602473 | 5cuong | Experiment & Prompt Lead,Cài provider; chạy v0; phân tích lỗi baseline; thực hiện v1 trên system prompt, Run v0/v1, thay đổi `system_prompt.md`, metric và version log  | `1a4dfd9`, `405f068` |
| Tống Trần Tiến Dũng |2A202602791 | Tiendung3tzz | Rà soát tool registry; cải thiện `tools.yaml`; thực hiện v2; xây bonus tool nếu có Tool declaration, tool implementation/smoke test, run v2 và bonus evidence  | `647663d`, `bf4806a`, `5ab5b13` |
| Vũ Đức Thiện |2A202602437 | vuthien3002-sys | Viết 10 group case; chạy group/adversarial; cải thiện confirmation, cancel và privacy cho v3 | `025eb0f` |
| Vũ Quốc Huy |2A202602929 | VuQuocHuy89 | Tích hợp UI web, transcript demo; hoàn thiện v2/v3 prompt/tool contract và evidence eval | `4c39b81`, `3aa8b19` |

## Nhận xét chung

- Kết quả và bằng chứng: v3 base `30/30`, group `10/10`, adversarial `12/12`, extension `10/10`; xem các run trong `starter_v0/runs/` và `starter_v0/artifacts/REPORT.md`.
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

- Phần việc và file/commit/PR:
- Quyết định, khó khăn và cách xử lý:
- Điều đã học:
- AI/công cụ đã dùng và cách kiểm tra:
- Thời điểm đã tự nộp URL repo chung trên VLearn:

> Thành viên tự viết và commit nội dung INDIVIDUAL của mình theo quy định lab.

### Tống Trần Tiến Dũng — 2A202602791

- Phần việc và file/commit/PR: thành viên tự điền.
- Quyết định, khó khăn và cách xử lý: thành viên tự điền.
- Điều đã học: thành viên tự điền.
- AI/công cụ đã dùng và cách kiểm tra: thành viên tự điền.
- Thời điểm đã tự nộp URL repo chung trên VLearn: thành viên tự điền.

### Vũ Đức Thiện — 2A202602437

- Phần việc và file/commit/PR: thành viên tự điền.
- Quyết định, khó khăn và cách xử lý: thành viên tự điền.
- Điều đã học: thành viên tự điền.
- AI/công cụ đã dùng và cách kiểm tra: thành viên tự điền.
- Thời điểm đã tự nộp URL repo chung trên VLearn: thành viên tự điền.
