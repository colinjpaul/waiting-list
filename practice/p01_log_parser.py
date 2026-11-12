def summarise(lines):
    """Summarise test-run log lines.

    Returns a dict with: passed, failed, skipped_lines,
    failing_tests (sorted, no duplicates), total_time (1 dp).
    """
    result = {"passed": 0, "failed": 0, "skipped_lines": 0, "failing_tests": [], "total_time": 0.0}
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
            result["failing_tests"].append(parts[3])  # Add the test name to failing_tests
            print(f"Failed test: {parts[3]}")  # Debugging line to print the failing test name
        elif status == "SKIPPED":
            result["skipped_lines"] += 1
        total_time = float(parts[5][:-1])  # Remove the 's' at the end and convert to float
        result["total_time"] += total_time
    
    result["failing_tests"].sort()
    result["failing_tests"] = list(dict.fromkeys(result["failing_tests"]))  # Remove duplicates
    return result