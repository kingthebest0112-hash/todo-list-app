# Danh sách để lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới dạng dictionary."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Hiển thị trạng thái [x] hoặc [ ] của từng công việc."""
    print("\n--- Danh sách công việc ---")
    if not tasks:
        print("Danh sách trống.")
        return
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành dựa trên chỉ số index (bắt đầu từ 1)."""
    actual_index = task_index - 1
    if 0 <= actual_index < len(tasks):
        tasks[actual_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[actual_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách dựa trên chỉ số index (bắt đầu từ 1)."""
    actual_index = task_index - 1
    if 0 <= actual_index < len(tasks):
        removed_task = tasks.pop(actual_index)
        print(f"Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ để xóa!")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()

    print("\nĐánh dấu hoàn thành công việc số 1:")
    complete_task(1)
    list_tasks()

    print("\nXóa công việc số 2:")
    delete_task(2)
    list_tasks()