seen = set()            # empty set (NOT {} - that's an empty dict)
seen.add("test_upload") # add an item; duplicates are ignored
sorted(seen)            # -> a sorted list

parts = line.split()    # split on whitespace -> list of strings
len(parts)              # how many pieces
float("1.2s"[:-1])      # strip the last character, convert -> 1.2
round(8.299999, 1)      # -> 8.3

counts = {"passed": 0}
counts["passed"] += 1  

float("3.4s".removesuffix("s"))  # strip a suffix and convert

counts = {"passed": 0, "failed": 0}
counts["passeed"] +=1.  # increment a dict value