import sys
import platform
from pathlib import Path


def check_python_version():
    version = sys.version_info

    print("=== Python Environment Check ===")
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major == 3 and version.minor >= 10:
        print("[OK] Python version is supported.")
        return True

    print("[ERROR] Python 3.10 or newer is required.")
    return False


def check_project_structure():
    project_root = Path(__file__).resolve().parent.parent

    required_paths = [
        project_root / "src",
        project_root / "scripts",
        project_root / "requirements.txt",
        project_root / "pyproject.toml",
    ]

    print("\n=== Project Structure Check ===")

    all_exist = True

    for path in required_paths:
        if path.exists():
            print(f"[OK] {path.relative_to(project_root)}")
        else:
            print(f"[MISSING] {path.relative_to(project_root)}")
            all_exist = False

    return all_exist


def show_system_info():
    print("\n=== System Information ===")
    print(f"Operating system: {platform.system()}")
    print(f"OS version: {platform.release()}")
    print(f"Machine: {platform.machine()}")


def main():
    python_ok = check_python_version()
    structure_ok = check_project_structure()
    show_system_info()

    print("\n=== Result ===")

    if python_ok and structure_ok:
        print("[SUCCESS] Environment is ready.")
        return 0

    print("[WARNING] Some environment checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())