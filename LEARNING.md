# Learning Path — The Waiting List (data track)

Colin's data learning plan, worked through **on this repo**: SQL, Python for SQL and pandas, using Irish public hospital waiting list data from the NTPF. Each step is a real change to the project, so the learning and the portfolio grow together.

**Why this project:** real Irish health data, relevant to public sector data analyst roles (HSE, CSO, civil service), with Colin's QA background built in through data-quality tests.

**QA track** (Playwright, Python for QA) lives in [back_in_bounds](https://github.com/colinjpaul/back_in_bounds).
**Study time:** weekday mornings, at Colin's own pace (no deadlines). Mon/Wed/Fri mornings are the waiting list days.
**Progress checklist:** ticked off on the Learning path panel of Colin's *Daily Board*. Step IDs (D, S, PS, P) match that checklist.

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

---

## 0 · Setup and first look

- [ ] **D1** Project setup: folders `data/raw/`, `notebooks/`, `sql/`, `tests/`; a virtual environment; `requirements.txt` (pandas, jupyter, pytest); `data/raw/` in `.gitignore`.
- [ ] **D2** First look: download the 2026 OP by specialty CSV; in `notebooks/01_explore.ipynb` run `read_csv`, `.head()`, `.shape`, `.info()`, `.columns`. Which months does it cover? Which columns load as text instead of numbers, and why?
- [ ] **D3** First question: total people waiting in each month. Write three or four lines in `NOTES.md` on what you found and what confused you.

## 1 · SQL — `data/waiting_list.db` (SQLite)

Load the CSVs into SQLite (a short Python script is fine at first; PS2 makes it clean). Practise in DB Browser for SQLite, the VS Code SQLite extension, or the `sqlite3` CLI. Save good queries in `sql/`.

- [ ] **S1** `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`: the 10 specialties with the most people waiting 18+ months in the latest month.
- [ ] **S2** Aggregates: totals per month with `GROUP BY`; specialties with over 10,000 waiting using `HAVING`; adult vs child totals.
- [ ] **S3** JOINs: join the by-hospital and by-specialty tables, or add a small `hospitals` lookup table (hospital → group/region, e.g. South/Southwest for Cork); use a `LEFT JOIN` to find hospitals with no lookup entry.
- [ ] **S4** Subqueries and CTEs: specialties above the national average wait; a CTE comparing Cork hospitals with the national picture.
- [ ] **S5** Window functions: month-on-month change with `LAG()`; `RANK()` specialties by 18+ month waits; rolling 3-month average.
- [ ] **S6** Data-quality checks: SQL that finds duplicate rows, NULLs, negative counts, time bands that don't add up to `Total`, and hospitals that disappear between months. Wire these into pytest as data tests.
- [ ] **S7** Writes: `INSERT` a new month's data, `UPDATE` a correction, wrap it in a transaction and roll back.

## 2 · Python for SQL

- [ ] **PS1** `sqlite3` in Python: connect, run parameterised queries (never string-format SQL).
- [ ] **PS2** pandas `read_sql` and `to_sql`: a `load_data.py` script that loads every CSV in `data/raw/` into SQLite cleanly and idempotently (safe to run twice).
- [ ] **PS3** pandas cleaning: fix column types, tidy column names, combine monthly snapshots from several years into one table.
- [ ] **PS4** pandas `groupby` / `merge` next to the equivalent SQL from S2/S3; confirm both give the same numbers in a test.
- [ ] **PS5** SQLAlchemy: create an engine so the project could switch from SQLite to PostgreSQL by changing one URL.
- [ ] **PS6** Test the data layer: pytest fixtures that build a temporary SQLite DB, load sample rows, and test your queries.

## 3 · pandas analysis and storytelling

- [ ] **P1** Reshaping: `melt` the time-band columns into long format; `pivot_table` specialty × month.
- [ ] **P2** Time series: build your own history from several years of files; `resample` and `rolling` to show trends.
- [ ] **P3** Charts: seaborn/matplotlib charts of the biggest movers, Cork vs national, adult vs child.
- [ ] **P4** Second source: add CSO population figures to estimate waits per head of population by region.
- [ ] **P5** Write-up: a short findings notebook or README section, written for a non-technical reader.

## Portfolio milestones

- [ ] **F2** Data loaded into SQLite with analysis queries in `sql/` and data-quality tests passing (S6, PS6).
- [ ] **F4** Data-quality tests running in GitHub Actions with a status badge.
- [ ] **F5** README with the question, the data source, key findings, charts and a short "what I learned" section.

## Later

NumPy, a first scikit-learn model (e.g. forecast next month's waiting list), and possibly a small dashboard.
