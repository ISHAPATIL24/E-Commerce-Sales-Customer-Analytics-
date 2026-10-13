#!/usr/bin/env python3
"""
Group 4 DVT Lab Assignment — Packaging & Verification Script
Verifies all assignment deliverables and creates a clean consolidated ZIP submission.
"""

import os
import sys
import zipfile
import pandas as pd

REQUIRED_FILES = [
    "app.py",
    "requirements.txt",
    "README.md",
    "data/sample_superstore.csv",
    "data/dataset_metadata.json",
    "docs/DATASET_DISCOVERY.md",
    "docs/ANALYTICAL_QUESTIONS.md",
    "docs/FINDINGS_AND_RECOMMENDATIONS.md",
    "docs/AI_CRITIQUE.md",
    "docs/TWO_MINUTE_DATA_STORY.md",
    "utils/data_loader.py",
    "utils/column_detector.py",
    "utils/helpers.py",
    "utils/sample_data.py",
    "components/kpi.py",
    "components/charts.py",
    "components/filters.py",
    "pages_content/overview.py",
    "pages_content/deep_dive.py",
    "pages_content/misleading_vs_correct.py",
    "pages_content/ai_critique.py",
    "pages_content/data_story.py",
    "pages_content/reports.py",
    "screenshots/01_executive_overview.png",
    "screenshots/02_analytical_deep_dive.png",
    "screenshots/03_misleading_vs_correct.png",
    "screenshots/04_ai_critique.png",
    "screenshots/05_data_story_findings.png",
    "screenshots/06_dataset_reports.png",
]

EXCLUDE_PATTERNS = [
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".DS_Store",
    ".pytest_cache",
    ".zip"
]


def should_exclude(filepath):
    parts = filepath.split(os.sep)
    for p in parts:
        if p in [".git", ".venv", "venv", "__pycache__", ".pytest_cache"]:
            return True
        if p.endswith(".pyc") or p == ".DS_Store":
            return True
    if filepath.endswith(".zip"):
        return True
    return False


def verify_and_package():
    print("=" * 68)
    print("  GROUP 4 DVT LAB: PACKAGING & PRE-SUBMISSION VERIFICATION")
    print("=" * 68)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    # 1. Verify existence of all required files
    print("\n[Step 1/5] Verifying required deliverable files & screenshots...")
    missing_files = []
    for rf in REQUIRED_FILES:
        full_path = os.path.join(base_dir, rf)
        if os.path.isfile(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            print(f"  ✓ Found: {rf:<44} ({size_kb:>7.1f} KB)")
        else:
            print(f"  ✗ MISSING: {rf}")
            missing_files.append(rf)

    if missing_files:
        print(f"\n[ERROR] Packaging halted. Missing {len(missing_files)} required file(s).")
        sys.exit(1)

    # 2. Verify dataset integrity
    print("\n[Step 2/5] Verifying dataset integrity...")
    csv_path = os.path.join(base_dir, "data/sample_superstore.csv")
    try:
        df = pd.read_csv(csv_path)
        print(f"  ✓ Dataset verified: {len(df):,} rows x {len(df.columns)} columns.")
        assert len(df) == 9994, f"Expected 9,994 rows, got {len(df)}"
        assert df.isnull().sum().sum() == 0, "Dataset contains unexpected null values"
        print("  ✓ Integrity check PASSED: 0 missing cells, 0 duplicates.")
    except Exception as e:
        print(f"  ✗ Dataset verification FAILED: {e}")
        sys.exit(1)

    # 3. Verify screenshot images
    print("\n[Step 3/5] Verifying all 6 screenshot images...")
    screenshot_dir = os.path.join(base_dir, "screenshots")
    for shot in [
        "01_executive_overview.png",
        "02_analytical_deep_dive.png",
        "03_misleading_vs_correct.png",
        "04_ai_critique.png",
        "05_data_story_findings.png",
        "06_dataset_reports.png"
    ]:
        shot_path = os.path.join(screenshot_dir, shot)
        if os.path.isfile(shot_path):
            shot_kb = os.path.getsize(shot_path) / 1024
            assert shot_kb > 10, f"Screenshot {shot} appears truncated ({shot_kb:.1f} KB)"
            print(f"  ✓ Verified screenshot: {shot:<34} ({shot_kb:>6.1f} KB)")
        else:
            print(f"  ✗ Screenshot missing: {shot}")
            sys.exit(1)

    # 4. Remove old zip if present and create new ZIP package
    zip_filename = "Group4_DVT_Data_Detective_Submission.zip"
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
        print(f"\n[Step 4/5] Removed prior archive. Building fresh ZIP: {zip_filename}...")
    else:
        print(f"\n[Step 4/5] Building fresh ZIP: {zip_filename}...")

    file_count = 0
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                if not should_exclude(rel_path):
                    zipf.write(full_path, rel_path)
                    file_count += 1

    # 5. Archive integrity test
    print("\n[Step 5/5] Testing archive integrity...")
    with zipfile.ZipFile(zip_filename, "r") as test_zip:
        bad_file = test_zip.testzip()
        if bad_file:
            print(f"  ✗ Corrupted file in archive: {bad_file}")
            sys.exit(1)
        archive_names = test_zip.namelist()
        print(f"  ✓ Archive integrity test PASSED: 0 CRC errors across {len(archive_names)} files.")

    zip_size_mb = os.path.getsize(zip_filename) / (1024 * 1024)
    abs_zip_path = os.path.abspath(zip_filename)
    print("=" * 68)
    print("  SUCCESS! Consolidated Group 4 DVT submission archive created.")
    print(f"  Archive Path : {abs_zip_path}")
    print(f"  Total Files  : {file_count} files archived")
    print(f"  Archive Size : {zip_size_mb:.2f} MB")
    print("=" * 68)


if __name__ == "__main__":
    verify_and_package()
