"""programmers/ 디렉토리를 스캔하여 README.md의 문제 풀이 목록을 자동 업데이트합니다."""

import os
from pathlib import Path


def get_problems():
    problems = []
    programmers_dir = Path("programmers")

    if not programmers_dir.exists():
        return problems

    for problem_dir in sorted(programmers_dir.iterdir()):
        if not problem_dir.is_dir():
            continue

        readme_path = problem_dir / "README.md"
        category = ""
        level = ""

        if readme_path.exists():
            with open(readme_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("- 유형:"):
                        category = line.split(":", 1)[1].strip()
                    elif line.startswith("- 난이도:"):
                        level = line.split(":", 1)[1].strip()

        name = problem_dir.name
        solution_link = f"[풀이]({problem_dir}/solution.py)"
        problems.append((name, category, level, solution_link))

    return problems


def update_readme(problems):
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")

    table_header = "| 문제 | 유형 | 난이도 | 풀이 |\n|------|------|--------|------|\n"
    rows = "\n".join(
        f"| {name} | {cat} | {level} | {link} |"
        for name, cat, level, link in problems
    )

    marker = "## 문제 풀이 목록"
    idx = content.find(marker)
    if idx == -1:
        return

    new_content = content[: idx + len(marker)] + "\n\n" + table_header + rows + "\n"
    readme_path.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    problems = get_problems()
    update_readme(problems)
    print(f"Updated README with {len(problems)} problems.")
