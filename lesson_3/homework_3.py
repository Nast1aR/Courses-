from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt")
lines = file.readlines()
result = []

for line in lines:
    if "user" in line:
        choice = input(f"Add to the results? (y/n/s): {line.strip()}").lower()
        if choice == "y":
            result.append(line.strip())
        elif choice == "stop":
            break

file.close()

print("\nResults:")
for res in result:
    print(res)

print(f"\nThe amount of added lines: {len(result)}")
