# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Duyệt qua danh sách tasks và in ra tất cả công việc có đánh số thứ tự."""
    print("\n--- Danh sách công việc ---")
    if not tasks:
        print("Danh sách trống.")
        return
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()