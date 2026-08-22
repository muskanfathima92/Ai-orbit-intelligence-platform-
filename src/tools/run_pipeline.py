import subprocess
import sys


STEPS = [
    [
        sys.executable,
        "src/tools/batch_scraper.py"
    ],
    [
        sys.executable,
        "src/tools/quality_check.py"
    ],
    [
        sys.executable,
        "src/tools/format_ai_orbit.py"
    ],
    [
        sys.executable,
        "src/tools/deduplicate.py"
    ],
    [
        sys.executable,
        "src/tools/validate_schema.py"
    ],
    [
        sys.executable,
        "src/tools/load_postgres.py"
    ],
]


for index, command in enumerate(STEPS, start=1):

    print()
    print("=" * 60)
    print(f"STEP {index}/{len(STEPS)}")
    print("=" * 60)

    result = subprocess.run(command)

    if result.returncode != 0:

        print(
            f"\nPipeline stopped at step {index}."
        )

        raise SystemExit(
            result.returncode
        )


print()
print("=" * 60)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)