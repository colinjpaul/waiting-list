# Learning Path — The Waiting List (data track)

Colin's data learning plan, worked through **on this repo**: SQL, pandas and Python for SQL, using Irish public hospital waiting list data from the NTPF. Each step is a real change to the project, so the learning and the portfolio grow together.

**Why this project:** real Irish health data, relevant to public sector data analyst roles (HSE, CSO, civil service), with Colin's QA background built in through data-quality tests. SQL and pandas count for both the QA and data paths.

**QA track** (Playwright, Python for QA) lives in [back_in_bounds](https://github.com/colinjpaul/back_in_bounds).
**Study time:** weekday mornings, at Colin's own pace (no deadlines). Mon/Wed/Fri mornings are the waiting list days.
**Progress checklist:** the Learning path panel of Colin's *Daily Board* is the master list. Step IDs here (PS0, S1, KP1, PB1…) match it exactly. Update the `[ ]` boxes here as well if useful.

## How to help (for Claude in VS Code)

- Teach, don't just do. Explain the concept, then let Colin write the code; review it and suggest improvements.
- One step per session. Start by asking which step Colin is on, and check what already exists in the repo first.
- Keep changes small and committed per step, with a clear commit message.
- Raw CSVs stay out of git (`data/raw/` is ignored); note in the README where each file came from.

## The data

- Source: NTPF Open Data page — https://www.ntpf.ie/waiting-list-data/open-data/
- Lists: Outpatient (OP), Inpatient/Day Case (IPDC), GI Endoscopy. Each has a "by hospital" and a "by specialty" file per year.
- Each file holds **monthly snapshots** of how many people are waiting, in time bands (0–6, 6–12, 12–18, 18+ months). It is not activity data: no numbers treated or removed.
- Privacy adjustments: cells under 5 are replaced with an average of the small values, and specialty/hospital combinations under 20 people are grouped as "Small Volume". Subtotals may not reconcile exactly.
- Format changed in April 2021 (separate adult and child reports). Older files (2014–Mar 2021) are on data.gov.ie.
- Context data: CSO population figures (data.cso.ie, PxStat) for waits per head of population.

---

## Start here

- [ ] **PS0** Kick-off: new repo, download one outpatient CSV, load it in pandas. Answer: how many are waiting at Cork hospitals, which specialty waits longest, and is it up or down over the year?
  - Setup: folders `data/raw/`, `notebooks/`, `sql/`, `tests/`; a virtual environment; `requirements.txt` (pandas, jupyter, pytest); `data/raw/` and `.venv/` in `.gitignore`.
  - Write three or four lines in `NOTES.md` on what you found and what confused you.

## 1 · SQL — `waiting.db` (SQLite)

Practise in DB Browser for SQLite, the VS Code SQLite extension, or the `sqlite3` CLI. Save good queries in `sql/`.

- [ ] **S1** Load the NTPF outpatient CSV into SQLite (`waiting.db`); `SELECT` / `WHERE` / `ORDER BY`: Cork hospitals.
- [ ] **S2** `GROUP BY`: total waiting by hospital and by specialty.
- [ ] **S3** Add an inpatient/day case table and `JOIN` on hospital.
- [ ] **S4** Subqueries and CTEs: share waiting over 12 months by specialty.
- [ ] **S5** Window functions: month-on-month change (`LAG()`) and `RANK()` of longest waits.
- [ ] **S6** Data-quality SQL wired into pytest: NULLs, negative counts, unknown hospitals, time bands that don't add up to `Total`.
- [ ] **S7** Monthly refresh: `INSERT` the new month inside a transaction.

## 2 · pandas — Kaggle course, then each lesson on the waiting list data

Course: https://www.kaggle.com/learn/pandas. Do a lesson, then try it on the NTPF data the same day.

- [ ] **KP1** Creating, reading and writing
- [ ] **KP2** Indexing, selecting and assigning
- [ ] **KP3** Summary functions and maps
- [ ] **KP4** Grouping and sorting
- [ ] **KP5** Data types and missing values
- [ ] **KP6** Renaming and combining

## 3 · Python for SQL — pandas + SQL with tests

- [ ] **PS1** `sqlite3` with parameterised queries (pick hospital/specialty); never string-format SQL.
- [ ] **PS2** Load script: CSV → SQLite with `read_csv` / `to_sql`, safe to run twice.
- [ ] **PS3** Clean and combine several months into one tidy table.
- [ ] **PS4** pandas `groupby` / `merge` vs SQL, checked in a test.
- [ ] **PS5** SQLAlchemy engine (SQLite → PostgreSQL ready).
- [ ] **PS6** pytest fixtures with a temporary test database.

## Portfolio milestones

- [ ] **F2** SQLite + SQL queries + data tests.
- [ ] **F3** README: CI badge, findings and what I learned.

## Power BI · low priority, for the data path

Power BI Desktop doesn't run on a Mac: use a Windows laptop or VM, or Tableau Public instead.

- [ ] **PB1** Microsoft Learn: Get started with Power BI (free modules).
- [ ] **PB2** Load the waiting list data into Power BI and clean it in Power Query.
- [ ] **PB3** One-page report: waiting trend, Cork hospitals, longest-wait specialties.
- [ ] **PB4** DAX basics: measures for total waiting and % over 12 months.
- [ ] **PB5** Publish the report and add a screenshot and link to the README.

## Later: pandas and data science

Reshaping (`pivot_table`, `melt`), time series (`resample`, `rolling`), seaborn charts, NumPy, a first scikit-learn model (e.g. forecast next month's waiting list), CSO population data for waits per head, and maths at your own pace.
