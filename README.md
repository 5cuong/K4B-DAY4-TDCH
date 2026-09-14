# Day04 — Prompt Engineering & Tool Calling

**Làm nhóm.** Mỗi thành viên tự nộp cùng URL repo nhóm trên VLearn. Repo bài nộp dùng tên và MSSV người đại diện theo mẫu `K4-L3-DAY04-HoVaTen-MSSV-PromptEngineeringToolCalling`; khai báo thành viên và đóng góp trong [TEAM.md](TEAM.md).

## Mục tiêu

- Cải thiện cách trợ lý Helpdesk chọn công cụ và điền thông tin đầu vào.
- So sánh v0, v1, v2, v3 bằng kết quả chạy thật.
- Xử lý hội thoại nhiều lượt, xác nhận hành động và dữ liệu nội bộ an toàn.
- Làm việc nhóm có bằng chứng đóng góp rõ ràng.

## Đọc trước khi làm

| File | Dùng khi |
|---|---|
| [SUBMISSION.md](SUBMISSION.md) | Đặt tên repo, chuẩn bị file và nộp VLearn |
| [RUBRIC.md](RUBRIC.md) | Biết cách chấm và bằng chứng cần có |
| [CHECKPOINTS.md](CHECKPOINTS.md) | Theo mốc thời gian của buổi học |
| [RULES.md](RULES.md) | Dùng AI, làm nhóm, deadline và bảo mật |
| [TEAM.md](TEAM.md) | Ghi thành viên, phần việc và INDIVIDUAL |

## Chuẩn bị và bắt đầu

Cần Python 3.10+, Git/GitHub và API key của một provider hỗ trợ tool calling. Chỉ cần `TAVILY_API_KEY` nếu nhóm dùng tìm kiếm thiết bị trên web.

```powershell
cd starter_v0
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Điền **một** key provider vào `.env`, sau đó chạy bản gốc trước khi sửa hai artifact:

```powershell
python scripts/preflight_provider.py --provider openrouter
python run_eval.py --provider openrouter --version v0 --suite base --eval-cases data/eval_base.json
```

Thay `openrouter` bằng `openai`, `anthropic` hoặc `gemini` khi dùng provider khác. Không commit `.env`.

## Nhiệm vụ nhóm

1. Đọc lỗi từ run v0.
2. Cải thiện `starter_v0/artifacts/system_prompt.md` và `starter_v0/artifacts/tools.yaml`.
3. Chạy v1, v2, v3 trên cùng bộ base và ghi `version_log.csv`.
4. Tự viết đúng 10 tình huống mới trong `data/eval_group.json`: 5 một lượt, 5 nhiều lượt.
5. Chạy bộ an toàn, lưu transcript và làm UI chat hiển thị tool call, đầu vào, kết quả/lỗi và phiên bản.
6. Hoàn thiện `REPORT.md` và `TEAM.md` bằng run, file và commit thật.

Giữ nguyên các bộ câu có sẵn: base 30, adversarial 12 và extension 10. `eval_group.json` để trống có chủ đích để nhóm thực hiện.

## Thời gian và đầu ra

Buổi học: **17:30–21:00**. 17:30–17:40 giới thiệu, 17:40–17:50 Kahoot, 17:50–20:25 làm nhóm, 20:25–21:00 demo. Mốc kiểm tra bản tại lớp là 20:25; xem [CHECKPOINTS.md](CHECKPOINTS.md).

Bài hoàn thành có: prompt và khai báo công cụ cuối, v0–v3, bộ 10 tình huống nhóm, run an toàn, transcript, UI, report và TEAM/INDIVIDUAL. `provider_error_cases` phải bằng 0 và `measured_cases` phải bằng `total_cases` khi dùng một run làm bằng chứng.

Không nộp API key, dữ liệu thật, `.venv`, cache hoặc ticket phát sinh. Hạn mặc định là **23:59 ngày học, Asia/Ho_Chi_Minh (UTC+07:00)**; xem [SUBMISSION.md](SUBMISSION.md) và [RULES.md](RULES.md).
