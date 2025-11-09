# deploy.py
import sys
from pathlib import Path

def main():
    print("=== Deploy step (simulated) ===")
    # pretend to deploy app.py or any artifact
    if not Path("app.py").exists():
        print("app.py not found; nothing to deploy.")
        return 0
    print("Deploy OK ")
    return 0

if __name__ == "__main__":
    sys.exit(main())
