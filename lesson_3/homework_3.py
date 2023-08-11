from pathlib import Path
ROOT_DIR = Path(__file__).absolute().parent.parent

file =open(ROOT_DIR / "rockyou.txt")
lines: list[str]= file.readlines()
result = []

for line in lines:
    if "user" in line:
        choice= input(f"Do you want to add file to the results? (y,n,stop): {line.strip()}").lower() 
        if choice == "y":
            result.append(line.strip())
        elif choice == "stop":
            break 

file.close()

print("\nResults:")
for result in result:
    print(result)
print(f"\nThe amount of added lines:{len(result)}")