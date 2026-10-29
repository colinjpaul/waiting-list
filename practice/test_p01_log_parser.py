from p01_log_parser import summarise

LINES = [
    "2026-10-15 08:01:12 INFO  test_login PASSED 1.2s",
    "2026-10-15 08:01:14 ERROR test_upload FAILED 3.4s",
    "2026-10-15 08:01:15 INFO  test_logout PASSED 0.8s",
    "garbage line",
    "2026-10-15 08:01:19 ERROR test_upload FAILED 2.9s",   
]

def test_example_from_the_problem():
    assert summarise([LINES[0]])== {"passed": 1, "failed": 0, "skipped_lines": 0}

def test_counts_a_failed_line():
    assert summarise(LINES[0:2]) == {"passed": 1, "failed": 1, "skipped_lines": 0}

def test_skips_a_garbage_line():
    assert summarise(LINES[0:4]) == {"passed": 2, "failed": 1, "skipped_lines": 1} 

def test_my_edge_case():
    # TODO:  pick one:  empty list, all garbage, a SKIPPED status, ...
    pass 
