branch_coverage = {}

def calculate_coverage(branch_coverage):
    total_branches = len(branch_coverage)
    hit_branches = sum(branch_coverage.values())
    coverage_percentage = (hit_branches / total_branches) * 100
    return coverage_percentage

def write_coverage_to_file(branch_coverage, file_name):
    with open(file_name, 'w') as f:
        for branch, hit in branch_coverage.items():
            f.write(f"{branch} was {'hit' if hit else 'not hit'}\n")
        coverage_percentage = calculate_coverage(branch_coverage)
        f.write(f"\nCoverage Percentage: {coverage_percentage:.2f}%\n")

import atexit

def register_coverage_tracker(branch_coverage, file_name):
    atexit.register(write_coverage_to_file, branch_coverage, file_name)
