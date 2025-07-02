import os
import sys
import subprocess

def main():
    # Read number of workers from env, default to 1
    num_workers = os.getenv("PYTEST_NUM_WORKERS", "1")
    pytest_args = ["pytest"]
    if num_workers and num_workers != "1":
        pytest_args += ["-n", num_workers]
    # Add any extra args passed to this script
    pytest_args += sys.argv[1:]
    print(f"Running: {' '.join(pytest_args)}")
    sys.exit(subprocess.call(pytest_args))

if __name__ == "__main__":
    main() 