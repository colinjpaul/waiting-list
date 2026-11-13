# The Waiting List

Colin's main project and learning plan (from 2026-10-29): interview-ready Python at senior SDET level, built into a "How long will I wait?" app on Irish public hospital waiting list data (NTPF open data). It uses Python, pandas, pytest data-quality tests, Dash, Playwright and GitHub Actions, so it shows both QA and data skills. Getting a job is the priority. `back_in_bounds` is paused.

## Learning plan

Read **LEARNING.md** at the start of a session and follow its "How to help" section. Step IDs (PS0, D1, A1, M1…) match the Learning path checklist on Colin's Daily Board.

How to help, in short:
- Each day has two optional parts (see the 2026-11-02 note below): a QA or data Python puzzle in the morning (9:30–10:30), then a project step or job search in the afternoon (2:30–3:30). Skipping either is fine.
- Daily problem: Colin writes it **without AI**. Give the problem statement and examples only, then review his solution like an interviewer.
- Project steps: teach, don't just do. Explain the concept, let Colin write the code, then review it.
- Ask where he's up to and check `NOTES.md`, `practice/` and the notebooks first.
- Keep explanations plain and concrete; he's rebuilding Python fluency and learning pandas from the basics.
- Encourage a line in `NOTES.md` for each finding, cleaning decision or practice problem.

## Where things live

Colin works in three places. Keep them separate:

- **VS Code (here): the learning.** Morning block 9:30–10:30: the daily no-AI problem. Afternoon block 2:30–3:30: one project step. When Colin says "start today's session" in the morning, read `LEARNING.md`, `NOTES.md` and `practice/`, tell him where he's up to, and give today's problem. In the afternoon, pick up the next project step.
- **The repo: the single record of progress.** Plan in `LEARNING.md`, findings and practice results in `NOTES.md`, code in `practice/` and `notebooks/`. If it isn't in the repo, it didn't happen.
- **The "New Job" project in the Claude desktop app: the job search.** Until January this is reactive: a quick look at alerts over coffee at 8:30, and applications only when something strong turns up (see the 2026-11-02 note). LinkedIn, CVs, cover letters, applications, company-specific interview prep, and bigger decisions about focus. Decisions there that change the learning plan land here as handoff notes below.

## Handoff notes (from Colin's planning chat in the Claude desktop app)

Colin also plans with Claude in the desktop app. That chat can't talk to this one, so notes land here.

- **2026-10-28 · PS0 started**
  - Repo set up: `data/raw/`, `notebooks/01_explore.ipynb`, `NOTES.md`, `requirements.txt`, `.venv` kernel.
  - Loaded `data/raw/OpenData_OPNational02_2026.csv` (outpatient by specialty, Jan–Sep 2026; NTPF publishes each month the following month).
  - All columns first loaded as text because the counts contain commas. Fixed with `pd.read_csv(..., thousands=",")`; counts are now `int64`. No missing values found so far (worth rechecking now types are numeric).
  - Covered so far: `head()`, `info()`, dtypes, `repr`, `unique()` / `nunique()` / `value_counts()`, why `np.int64(...)` appears.
  - Colin is keeping Data Wrangler for checking his work only, not for generating code.
  - **Next (PS0 continued):**
    1. Convert `ArchiveDate` with `pd.to_datetime(..., dayfirst=True)` and confirm 9 monthly snapshots.
    2. Which specialty waits longest? (e.g. most people in the 18+ months band in the latest month.)
    3. Cork hospitals needs the **by hospital** file, which isn't downloaded yet: `OpenData_OPNational01_2026.csv` from https://www.ntpf.ie/waiting-list-data/open-data/ (load it with `thousands=","` too).
    4. Is the list up or down over the year? (Total per month.)
- **2026-10-29 · housekeeping done**
  - `data/raw/` and `.DS_Store` are now in `.gitignore`; the raw CSV is no longer tracked. The README says where to download the data. Raw files live only on Colin's Mac.
- **2026-10-29 · new plan (decided in Claude Code)**
  - LEARNING.md rewritten as one plan following Stage 2 of `qualcomm_prep_plan.xlsx`: 8 weeks of a daily no-AI Python problem plus project steps towards the app. Old step IDs (S1, KP1, PS1…) are replaced; SQL and Power BI move to "Later".
  - PS0 progress: `ArchiveDate` converted; latest month filtered with a boolean mask. Sep 2026 has 74 rows but 55 specialties, because rows are split by `Adult_Child` (41 Adult, 33 Child). The column is spelled `Speciality`.
  - **Next:** find Problem 1 from the prep plan (test-log parser, 15 Oct) for review; finish PS0 (longest wait: combine adult + child or keep separate?).
- **2026-10-29 · Problem 1 moved**
  - The test-log parser is now in `practice/p01_log_parser.py` with `practice/test_p01_log_parser.py` (3 real tests plus an empty edge-case stub) and `practice/cheatsheet.py`. The old `~/code/interview_practice` folder is gone.
  - Still to do, by Colin without AI: `failing_tests` (sorted, no duplicates), `total_time` (1 dp) and the edge-case test. Then review it like an interviewer. Points already raised: docstring promises more than the code does; magic numbers (`6`, `parts[4]`); a well-formed `SKIPPED` line is counted nowhere; `LINES[4]` is unused; whole-dict asserts will break when keys are added.
  - Colin starts the new approach afresh on Fri 30 Oct 2026, beginning with finishing Problem 1.
- **2026-11-02 · routine reset until end of 2026 (decided in the Claude desktop planning chat; this note wins over anything above that conflicts)**
  - **No pressure, no deadlines.** Learning is for enjoyment until January. Don't frame the morning problem as "the daily problem" or something Colin has to do.
  - **9:30–10:30 is optional:** a Python puzzle with a QA or data flavour (parse a log, check a CSV, write a small test), Power BI on the Windows laptop, or Colin may tidy his space instead. Still no AI for writing his solution; review it like an interviewer if he does one.
  - **10:30–1:00 Mon/Wed is PS5 time** (free time on other days). PT twice a week at 11:30, days vary with the bookings (see the Golf calendar). Other weekdays are free time. Don't plan learning into these slots.
  - **2:30–3:30 is optional "project or job search time":** a small waiting-list step, an application if something good has turned up, or family time.
  - **Job search is reactive until January:** Monday job check plus at least one job action a week. Qualcomm rejected him on 30 Oct (gaps from that interview are in LEARNING.md / the board plan). NetApp via Danny is the main live lead.
  - **PL-300 / Power BI:** may start after the Intreo meeting on Tue 3 Nov. His old Windows laptop now works, so Power BI Desktop runs there. If he goes ahead, it can use either the 9:30 or the 2:30 slot and the waiting-list data (load one CSV in Power BI first). SQL and Power BI are no longer only "Later" if he chooses this.
  - **Pace:** Christmas prep and family take priority this year. Keep sessions short and encouraging; if Colin seems stretched, suggest stopping rather than pushing on.
  - **One place for planning:** Colin plans in the Claude desktop app (mornings and the Friday review) and codes here. If he starts re-planning mid-session, note it in NOTES.md and steer back to the code.
- **2026-11-13 · SQL first, own pace (decided in the Claude desktop planning chat; this note wins over anything above that conflicts)**
  - **LEARNING.md was rewritten today.** Follow it: finish P1 (log parser), then the SQL steps S1–S6 on the waiting-list data, then Power BI (B1–B2), with the Python track alongside PCAP from 7 Dec. SQL is no longer "Later".
  - **No fixed time slots.** The 9:30 and 2:30 blocks above are retired; Colin works at his own pace. The eCollege Power BI course is the main focus until 4 Dec; the waiting list is the side project.
  - **Hints only on code.** Colin writes his own code and queries; give hints and questions, then review like an interviewer.
  - **Next SQL step after P1:** S1 (load the specialty CSV into SQLite), then S2 (investigate the duplicate Adult rows found on 11 Nov before summing anything).
