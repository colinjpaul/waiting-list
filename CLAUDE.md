# The Waiting List

Colin's data analysis project on Irish public hospital waiting lists (NTPF open data), using Python, pandas, SQL and pytest data-quality tests. It's his main portfolio project for public sector data analyst roles and the data side of QA.

## Learning plan

Read **LEARNING.md** at the start of a session and follow its "How to help" section. Step IDs (PS0, S1, KP1…) match the Learning path checklist on Colin's Daily Board. The QA track (Playwright, Python for QA) lives in the separate `back_in_bounds` repo.

How to help, in short:
- Teach, don't just do. Explain the concept, let Colin write the code, then review it.
- One step per session. Ask where he's up to and check `NOTES.md` and the notebooks first.
- Keep explanations plain and concrete; he's rebuilding Python and learning pandas from the basics.
- Encourage a line in `NOTES.md` for each cleaning decision or finding.

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
  - Housekeeping to suggest, not do unasked: the raw CSV is currently committed (LEARNING.md planned to keep `data/raw/` out of git; it's small public CC-BY data, so Colin can decide), and `.DS_Store` isn't in `.gitignore` yet.
