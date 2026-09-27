from pathlib import Path

data_file = Path("/data/tasks.txt")

print("Study Task Saver")
task = input("Enter a study task: ").strip()

if task:
    data_file.parent.mkdir(parents=True, exist_ok=True)
    with data_file.open("a", encoding="utf-8") as file:
        file.write(task + "\n")
    print("Task saved!")
else:
    print("No task entered.")

print("\nSaved tasks:")
if data_file.exists():
    print(data_file.read_text(encoding="utf-8"))