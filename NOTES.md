## 28 Oct 2026: first look (PS0)
- File: OpenData_OPNational02_2026.csv (OP by specialty), Jan–Sep 2026
- All columns loaded as text. Cause: numbers have commas (e.g. 1,234).
  Fix: read_csv(..., thousands=","). Counts now int64.
- No missing values found (recheck after converting types).
- ArchiveDate needs pd.to_datetime(dayfirst=True).
- Confused by: unique() vs nunique(), np.int64 in repr output.

## 29 Oct 2026: working with dataframes (PS0)
- Latest month (Sep 2026): 74 rows = 55 specialties, split by Adult_Child (41 Adult, 33 Child). One row per specialty per adult/child group.
- Approach 1: add up adult and child per speciality using groupby
- Approach 2:  filter by one group using true/false (as before with latest)

## 30 Oct 2026: log parser (P1)
- A trailing comma after {...} turned my dict into a tuple - "tuple indices must be integers".
- Stopped before failing_tests / total_time.

