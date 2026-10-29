# Learning Path — The Waiting List

Colin's single learning plan from 2026-10-29: **interview-ready Python at senior SDET level**, built into **one portfolio project** on Irish public hospital waiting list data (NTPF). Each step is a real change to this repo, so the learning and the portfolio grow together.

**Why:** getting a job is the priority. The Python part of the Qualcomm interview (22 Oct) showed live coding needs work, so this follows Stage 2 of `qualcomm_prep_plan.xlsx` (Google Drive): about 8 weeks to "comfortable live-coding at senior SDET level". The waiting list app is where those skills get used, and it shows QA skills (pytest, Playwright, CI) and data skills (pandas, SQL) in one place.

**back_in_bounds** is paused. Nothing there is deleted.
**Study time:** at Colin's own pace: **9:30–10:30** Mon–Fri for the daily problem, **2:30–3:30** Mon–Thu for the project step (Friday afternoon is family time). These match the focus blocks in *My day* on the Daily Board. The week numbers are a guide, not deadlines.
**Progress checklist:** the Learning path panel of Colin's *Daily Board* mirrors this file. Step IDs (PS0, D1, A1…) match it.

## How to help (for Claude in VS Code)

- Each day has two parts: **the daily problem in the morning block (9:30–10:30), then one project step in the afternoon block (2:30–3:30).**
- **Daily problem: no AI while Colin writes it.** When asked, give the problem statement and example input/output only: no hints, no code. Afterwards, review his solution like an interviewer would: correctness, edge cases, naming, tests, and how he'd explain it out loud. Suggest a better version only after he's had his go.
- **Project steps:** teach, don't just do. Explain the concept, let Colin write the code, then review it.
- Start by checking `NOTES.md`, the `practice/` folder and the notebooks to see where he's up to.
- Keep explanations plain and concrete. Keep changes small and committed per step.
- Encourage a line in `NOTES.md` for each finding, cleaning decision or practice problem.
- Raw CSVs stay out of git (`data/raw/` is ignored); the README says where each file came from.

## The daily problem (morning block, 30–45 min)

1. Ask Claude for today's problem, matched to the current week's focus below.
2. Set a timer (aim for 20 minutes by week 2). Talk through it **out loud** as if in an interview.
3. Write the simplest version first, then add a pytest test or two.
4. Ask Claude for a review. Note the problem, time taken and one lesson in `NOTES.md`.

Files go in `practice/`: `practice/p01_log_parser.py` with `practice/test_p01_log_parser.py`. Sample input files go in `practice/data/` and should end in `.txt`, because `*.log` files are ignored by git.

Problems are a mix: interview-style (test logs, tool output, strings) and ones using the NTPF CSVs.

**First:** find Problem 1 from the prep plan (test-log parser + 2 pytest tests, started 15 Oct) and get it reviewed. The review sets the starting level for week 1.

---

## Weeks 1–2 · Core Python

Focus: strings, lists, dicts, sets, comprehensions, functions, error handling.
**Ready when:** you can solve a log/CSV problem in 20 minutes without looking things up.

- [ ] **PS0** Finish the first look in `notebooks/01_explore.ipynb`: which specialty waits longest (decide: combine adult + child, or keep separate), and is the list up or down over the year (total per month). Write the findings in `NOTES.md`.
- [ ] **D1** Plain Python, no pandas: read the specialty CSV with the `csv` module and write a function that returns the total waiting per specialty for one month, as a dict. Watch out for the commas in the numbers.
- [ ] **D2** Write the same answer in pandas and add a pytest test that checks the plain Python and pandas answers match.
- [ ] **D3** Download the by-hospital file (`OpenData_OPNational01_2026.csv`) and answer the Cork question both ways: how many are waiting at Cork hospitals?

## Weeks 3–4 · Classes, files and pytest

Focus: classes, file I/O, json/csv, `re`, pytest fixtures and parametrize.
**Ready when:** you can write a small class and its tests from scratch.

- [ ] **D4** A `Snapshot` class for one month's data (load, total, by specialty, by time band), with tests.
- [ ] **D5** Data-quality tests with pytest: time bands add up to `Total`, no negative counts, no missing specialties, one snapshot per month. Use small test CSVs in `tests/data/` with known answers, loaded by a fixture in `conftest.py`.
- [ ] **D6** Parametrize the data-quality tests to run over every monthly snapshot. Write each real problem you find in `NOTES.md`.

## Weeks 5–6 · Test-automation tasks

Focus: a `requests` API client, mocking, retry wrappers, parsing tool output, `subprocess`.
**Ready when:** you can talk through and build a small framework piece live.

- [ ] **A1** NTPF downloader: a function that fetches a given file with `requests` and saves it to `data/raw/`.
- [ ] **A2** Add a retry wrapper (e.g. 3 attempts with a wait), and test it with a mocked response so the tests never hit the real site.
- [ ] **A3** The app: a small Dash app, "How long will I wait?". Pick a specialty to see the numbers in each time band and the trend over the year.
- [ ] **A4** Run pytest from a script with `subprocess` and parse its output into a short summary (passed / failed / time).

## Weeks 7–8 · Mock interviews, end-to-end tests and CI

Focus: timed mock interviews with Claude as interviewer; finishing the portfolio.
**Ready when:** you stay calm and structured even when stuck.

- [ ] **M1** Mock interviews: timed problems, thinking out loud, Claude as interviewer. Two or three a week.
- [ ] **A5** Playwright tests for the app: the page loads, picking a specialty updates the numbers, the chart renders. Use `get_by_role` / `get_by_test_id` locators and `expect()`.
- [ ] **A6** GitHub Actions: install, run the unit and data-quality tests, start the app, run the Playwright tests, and upload a trace on failure. Add the status badge to the README.
- [ ] **A7** README: what the app does, a screenshot, key findings, how the tests are organised, and what you learned.

## Later (after the 8 weeks, or when a job ad asks for it)

- **SQL:** load the data into SQLite (`waiting.db`), then `GROUP BY`, `JOIN`, CTEs, window functions (`LAG()`, `RANK()`). Save good queries in `sql/`.
- **pandas course:** https://www.kaggle.com/learn/pandas, to fill gaps.
- **More data:** inpatient/day case and GI endoscopy lists; CSO population figures for waits per head.
- **Power BI / Tableau Public** for data analyst roles. Power BI doesn't run on a Mac.

---

## The data

- Source: NTPF Open Data page — https://www.ntpf.ie/waiting-list-data/open-data/
- Lists: Outpatient (OP), Inpatient/Day Case (IPDC), GI Endoscopy. Each has a "by hospital" and a "by specialty" file per year.
- Each file holds **monthly snapshots** of how many people are waiting, in time bands (0–6, 6–12, 12–18, 18+ months). It is not activity data: no numbers treated or removed.
- Privacy adjustments: cells under 5 are replaced with an average of the small values, and specialty/hospital combinations under 20 people are grouped as "Small Volume". Subtotals may not reconcile exactly.
- Format changed in April 2021 (separate adult and child reports). Older files (2014–Mar 2021) are on data.gov.ie.
- Context data: CSO population figures (data.cso.ie, PxStat) for waits per head of population.
