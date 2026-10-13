
import csv
from pathlib import Path


def normalize(text):
    """Chuẩn hóa câu trả lời để so sánh."""
    return " ".join(text.strip().casefold().split())


def main():
    # Xác định đường dẫn dựa trên vị trí của file run.py
    project_root = Path(__file__).resolve().parent.parent
    cases_file = project_root / "eval" / "cases.csv"

    if not cases_file.exists():
        print(f"Không tìm thấy file: {cases_file}")
        return

    with cases_file.open("r", encoding="utf-8-sig", newline="") as file:
        cases = list(csv.DictReader(file))

    if not cases:
        print("Benchmark chưa có câu hỏi.")
        return

    correct = 0

    for index, case in enumerate(cases, start=1):
        question = case["question"].strip()
        expected = case["expected_answer"].strip()

        # Tạm thời dùng đáp án mẫu để kiểm tra cách tính.
        # Sau đó thay bằng lời gọi đến trợ lý AI của dự án.
        actual = expected

        is_correct = normalize(actual) == normalize(expected)
        correct += int(is_correct)

        print(f"Câu {index}: {question}")
        print(f"  Mong đợi: {expected}")
        print(f"  Thực tế:  {actual}")
        print(f"  Kết quả:  {'ĐÚNG' if is_correct else 'SAI'}")

    accuracy = correct / len(cases) * 100

    print("\n===== BENCHMARK SUMMARY =====")
    print(f"Total questions: {len(cases)}")
    print(f"Correct answers: {correct}")
    print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    main()