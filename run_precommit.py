import subprocess
import sys


def main():
    commands = [
        ["poetry", "run", "black", "--check", "src/"],
        ["poetry", "run", "ruff", "check", "src/"],
        ["poetry", "run", "mypy", "src/"],
    ]

    for cmd in commands:
        print(f"\nRunning: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd)
        except FileNotFoundError:
            print(f"❌ Command not found: {' '.join(cmd)}")
            sys.exit(1)

        if result.returncode != 0:
            print(f"❌ Command {' '.join(cmd)} failed.")
            sys.exit(result.returncode)

    print("\n✅ All checks passed!")

if __name__ == "__main__":
    main()
