# Learning Path — The Waiting List

Colin's learning plan, built into **one portfolio project** on Irish public hospital waiting list data (NTPF). Each step is a real change to this repo, so the learning and the portfolio grow together.

**Updated 2026-11-13: SQL first.** The plan from 2026-10-29 put eight weeks of Python first and SQL under "Later". Since then Colin decided to tailor his learning towards **SQL** (it keeps coming up in the roles he's looking at), with **Python for loading, cleaning and tests**. AWS is on hold. This file now follows that order.

**Why:** getting a job is the priority, on two paths. The data analyst path needs SQL and Power BI; the QA path needs Python, pytest, Playwright and CI. This one project shows both on real public-sector data.

**back_in_bounds** is paused. Nothing there is deleted.

## Formal courses alongside the project

| When | Course | Feeds into |
|---|---|---|
| Now → 4 Dec 2026 | eCollege *Introduction to Power BI* (access ends 8 Dec) | B1–B2 below |
| After Power BI | ICT Skillnet *Data Analytics Essentials* (SQL) | S-steps below |
| From 7 Dec 2026 | PCAP Python (eCollege) | Python track below |

## How the time is used

- **At Colin's own pace. No fixed timetable, no deadlines** apart from the courses above.
- **Main focus until 4 Dec: the Power BI course.** The waiting list is the side project: short sessions on the next S-step when there's energy. Skipping a day is fine.
- Finish one thing before opening another: close out P1 (log parser) first.
- **Progress checklist:** the Learning path panel of Colin's *Daily Board* mirrors this file. Step IDs match it.

## How to help (for Claude in VS Code)

- **Colin writes his own code.** Give hints, questions and the problem statement, not solutions. Afterwards, review it like an interviewer would: correctness, edge cases, naming, tests, and how he'd explain it out loud. Suggest a better version only after he's had his go.
- **Project steps:** teach, don't just do. Explain the concept, let Colin write the code or query, then review it.
- Start by checking `NOTES.md`, `practice/`, `sql/` and the notebooks to see where he's up to.
- Keep explanations plain and concrete. Keep changes small and committed per step.
- Encourage a line in `NOTES.md` for each finding, cleaning decision or practice problem.
- Raw CSVs stay out of git (`data/raw/` is ignored); the README says where each file came from.

---

## Now · Finish Problem 1

- [ ] **P1** Test-log parser (`practice/p01_log_parser.py`): round `total_time` once after the loop, remove the debugging `print`, fix the expected values in the other two tests, add an edge-case test for a valid `SKIPPED` line (decide first: should it count in `skipped_lines`?). Run `pytest -v`, commit, then get an interviewer-style review.

## Next · SQL on the waiting list data (side project until 4 Dec)

Python loads the data; the questions are answered in SQL. Save each good query as a `.sql` file in `sql/` with a comment saying what it answers.

- [x] **PS0** First look in `notebooks/01_explore.ipynb`: commas in numbers fixed (`thousands=","`), `ArchiveDate` converted, latest month filtered. (Its open questions move to S2–S4.)
- [ ] **S1** Load the outpatient-by-specialty CSV into SQLite (`data/waiting.db`, ignored by git) with a short Python script. Check the row count matches the CSV.
- [ ] **S2** Investigate the duplicate Adult rows found on 11 Nov (e.g. Breast Surgery 994 and 4,511 in January) with `GROUP BY … HAVING COUNT(*) > 1`. Find out why before summing anything. Note the answer in `NOTES.md`.
- [ ] **S3** Which specialty waits longest? Most people in the 18+ months band in the latest month. Decide: combine adult + child, or keep separate.
- [ ] **S4** Is the list up or down over the year? Total per month, then month-on-month change with `LAG()`.
- [ ] **S5** Download the by-hospital file (`OpenData_OPNational01_2026.csv`), load it, and answer: how many are waiting at Cork hospitals?
- [ ] **S6** `RANK()` specialties by long waits each month; a CTE that combines S3 and S4.

## Then · Power BI on the same data (after the course)

- [ ] **B1** Load the cleaned data (or the S-step query results) into Power BI Desktop on the Windows laptop, using Transform Data (Power Query) for the cleaning.
- [ ] **B2** A one-page dashboard: waits by time band per specialty, trend over the year, Cork hospitals. Screenshot for the README.

## Python track (alongside PCAP from 7 Dec)

Focus: strings, lists, dicts, comprehensions, functions, error handling, then classes and pytest.

- [ ] **D1** Plain Python, no pandas: read the specialty CSV with the `csv` module and return the total waiting per specialty for one month, as a dict. Watch out for the commas in the numbers.
- [ ] **D2** Same answer in pandas, plus a pytest test that checks plain Python, pandas and the S-step SQL answers all match.
- [ ] **D4** A `Snapshot` class for one month's data (load, total, by specialty, by time band), with tests.
- [ ] **D5** Data-quality tests with pytest: time bands add up to `Total`, no negative counts, no missing specialties, one snapshot per month. Small test CSVs in `tests/data/` with known answers, loaded by a fixture in `conftest.py`.
- [ ] **D6** Parametrize the data-quality tests over every monthly snapshot. Write each real problem found in `NOTES.md`.

## Later · Test automation, the app and CI (when the above is done, or a job ad asks for it)

- [ ] **A1** NTPF downloader with `requests`, saving to `data/raw/`.
- [ ] **A2** Retry wrapper, tested with a mocked response so tests never hit the real site.
- [ ] **A3** Small Dash app, "How long will I wait?": pick a specialty to see the time bands and the trend.
- [ ] **A4** Run pytest from a script with `subprocess` and parse its output into a summary (builds on P1).
- [ ] **A5** Playwright tests for the app: page loads, picking a specialty updates the numbers, the chart renders. `get_by_role` / `get_by_test_id` locators and `expect()`.
- [ ] **A6** GitHub Actions: install, run unit and data-quality tests, start the app, run Playwright, upload a trace on failure. Status badge in the README.
- [ ] **A7** README: what it does, screenshot, key findings, how the tests are organised, what was learned.
- [ ] **M1** Mock interviews: timed problems, thinking out loud, Claude as interviewer.

## Other ideas

- **pandas course:** https://www.kaggle.com/learn/pandas, to fill gaps.
- **More data:** inpatient/day case and GI endoscopy lists; CSO population figures for waits per head.
- **Tableau Public**, if a data analyst job ad asks for it.

---

## The data

- Source: NTPF Open Data page — https://www.ntpf.ie/waiting-list-data/open-data/
- Lists: Outpatient (OP), Inpatient/Day Case (IPDC), GI Endoscopy. Each has a "by hospital" and a "by specialty" file per year.
- Each file holds **monthly snapshots** of how many people are waiting, in time bands (0–6, 6–12, 12–18, 18+ months). It is not activity data: no numbers treated or removed.
- Privacy adjustments: cells under 5 are replaced with an average of the small values, and specialty/hospital combinations under 20 people are grouped as "Small Volume". Subtotals may not reconcile exactly.
- Format changed in April 2021 (separate adult and child reports). Older files (2014–Mar 2021) are on data.gov.ie.
- Context data: CSO population figures (data.cso.ie, PxStat) for waits per head of population.
