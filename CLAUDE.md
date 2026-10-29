# The Waiting List

Colin's main project and learning plan (from 2026-10-29): interview-ready Python at senior SDET level, built into a "How long will I wait?" app on Irish public hospital waiting list data (NTPF open data). It uses Python, pandas, pytest data-quality tests, Dash, Playwright and GitHub Actions, so it shows both QA and data skills. Getting a job is the priority. `back_in_bounds` is paused.

## Learning plan

Read **LEARNING.md** at the start of a session and follow its "How to help" section. Step IDs (PS0, D1, A1, M1…) match the Learning path checklist on Colin's Daily Board.

How to help, in short:
- Each session has two parts: the daily Python problem first, then one project step.
- Daily problem: Colin writes it **without AI**. Give the problem statement and examples only, then review his solution like an interviewer.
- Project steps: teach, don't just do. Explain the concept, let Colin write the code, then review it.
- Ask where he's up to and check `NOTES.md`, `practice/` and the notebooks first.
- Keep explanations plain and concrete; he's rebuilding Python fluency and learning pandas from the basics.
- Encourage a line in `NOTES.md` for each finding, cleaning decision or practice problem.

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
