from pawpal_system import Pet, Owner, TaskManager, DailyPlanner

# Constants
SEPARATOR = "=" * 60

# Create Owner and Pets
owner = Owner("Sarah Johnson", "sarah@email.com")
pet1 = Pet("Max", 3, "dog")
pet2 = Pet("Luna", 2, "cat")
owner.add_pet(pet1)
owner.add_pet(pet2)

# Create TaskManager
task_manager = TaskManager()

print(SEPARATOR)
print("🐾 PawPal+ Sorting & Filtering Demo")
print(SEPARATOR)

# Add tasks OUT OF ORDER for Max (dog)
print("\n📝 Creating tasks in random order...")
task_manager.create_task("Dinner", "Evening meal", "18:00", 9, 10, "feed", recurrence="daily", pet_id=pet1.get_name())
task_manager.create_task("Playtime", "Fetch and play", "12:00", 7, 45, "playtime", pet_id=pet1.get_name())
task_manager.create_task("Morning Walk", "Walk in the park", "07:00", 10, 30, "walk", recurrence="daily", pet_id=pet1.get_name())
task_manager.create_task("Afternoon Walk", "Short walk", "15:00", 8, 20, "walk", recurrence="daily", pet_id=pet1.get_name())
task_manager.create_task("Breakfast", "Feed dry food", "08:00", 9, 10, "feed", recurrence="daily", pet_id=pet1.get_name())

# Add tasks for Luna (cat)
task_manager.create_task("Luna Breakfast", "Feed wet food", "08:30", 9, 5, "feed", recurrence="daily", pet_id=pet2.get_name())
task_manager.create_task("Luna Dinner", "Evening meal", "18:30", 9, 5, "feed", recurrence="daily", pet_id=pet2.get_name())
task_manager.create_task("Luna Playtime", "Laser pointer", "14:00", 6, 20, "playtime", pet_id=pet2.get_name())

# Conflicting tasks
task_manager.create_task("Vet Visit", "Annual checkup", "07:15", 10, 20, "medical", pet_id=pet1.get_name())
task_manager.create_task("Luna Brushing", "Brush her fur", "12:15", 6, 15, "grooming", pet_id=pet2.get_name())

print(f"✓ Created {len(task_manager.get_all_tasks())} tasks")

# SORTING: Sort all tasks by time
print("\n" + SEPARATOR)
print("⏰ ALL TASKS SORTED BY TIME")
print(SEPARATOR)
sorted_tasks = task_manager.get_tasks_sorted_by_time()
for task in sorted_tasks:
    pet_name = task.get_pet_id() or "No pet"
    print(f"{task.get_time()} - {task.get_task_name()} ({pet_name})")

# FILTERING: By Pet
print("\n" + SEPARATOR)
print(f"🐕 TASKS FOR {pet1.get_name().upper()} ONLY")
print(SEPARATOR)
max_tasks = task_manager.get_tasks_by_pet(pet1.get_name())
max_tasks_sorted = sorted(max_tasks, key=lambda t: t.get_time_obj())
for task in max_tasks_sorted:
    recur = " (daily)" if task.get_recurrence() else ""
    print(f"{task.get_time()} - {task.get_task_name()}{recur}")

print("\n" + SEPARATOR)
print(f"🐈 TASKS FOR {pet2.get_name().upper()} ONLY")
print(SEPARATOR)
luna_tasks = task_manager.get_tasks_by_pet(pet2.get_name())
luna_tasks_sorted = sorted(luna_tasks, key=lambda t: t.get_time_obj())
for task in luna_tasks_sorted:
    recur = " (daily)" if task.get_recurrence() else ""
    print(f"{task.get_time()} - {task.get_task_name()}{recur}")

# Mark some tasks as completed
sorted_tasks[0].mark_completed()
sorted_tasks[2].mark_completed()

# FILTERING: By Status
print("\n" + SEPARATOR)
print("✅ COMPLETED TASKS")
print(SEPARATOR)
completed = task_manager.get_completed_tasks()
for task in completed:
    print(f"✓ {task.get_time()} - {task.get_task_name()}")

print("\n" + SEPARATOR)
print("⏳ PENDING TASKS")
print(SEPARATOR)
pending = task_manager.get_pending_tasks()
pending_sorted = sorted(pending, key=lambda t: t.get_time_obj())
for task in pending_sorted:
    print(f"☐ {task.get_time()} - {task.get_task_name()}")

# FILTERING: Recurring tasks
print("\n" + SEPARATOR)
print("🔄 RECURRING TASKS ONLY")
print(SEPARATOR)
recurring = task_manager.get_recurring_tasks()
recurring_sorted = sorted(recurring, key=lambda t: t.get_time_obj())
for task in recurring_sorted:
    pet_name = task.get_pet_id() or "No pet"
    print(f"{task.get_time()} - {task.get_task_name()} ({pet_name})")

# Summary
print("\n" + SEPARATOR)
print("📊 SUMMARY")
print(SEPARATOR)
print(f"Total tasks: {len(task_manager.get_all_tasks())}")
print(f"Max's tasks: {len(max_tasks)}")
print(f"Luna's tasks: {len(luna_tasks)}")
print(f"Completed: {len(completed)}")
print(f"Pending: {len(pending)}")
print(f"Recurring: {len(recurring)}")
print(SEPARATOR)

# CONFLICT DETECTION
print("\n" + SEPARATOR)
print("⚠️  CONFLICT DETECTION")
print(SEPARATOR)

all_conflicts = task_manager.get_all_conflicts()
if all_conflicts:
    print(f"Found {len(all_conflicts)} scheduling conflict(s):\n")
    for task1, task2, reason in all_conflicts:
        print(f"  {reason}")
        print(f"    • {task1.get_task_name()} ({task1.get_pet_id()}) at {task1.get_time()}")
        print(f"    • {task2.get_task_name()} ({task2.get_pet_id()}) at {task2.get_time()}")
        print()
else:
    print("✅ No conflicts")

print(SEPARATOR)
