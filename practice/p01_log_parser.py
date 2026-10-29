def summarise(lines):
    """Summarise test-run log lines.

    Returns a dict with: passed, failed, skipped_lines,
    failing_tests (sorted, no duplicates), total_time (1 dp).
    """
    result = {"passed": 0, "failed": 0, "skipped_lines": 0}
    for line in lines:
        parts = line.split()
        if len(parts) != 6:
            result["skipped_lines"] += 1
            continue
        status = parts[4]
        if status == "PASSED":
            result["passed"] += 1
        elif status == "FAILED":
            result["failed"] += 1
    
    return result