from pawpal_system import Pet, Owner, TaskManager, DailyPlanner

# Create Owner
owner = Owner("Sarah Johnson", "sarah@email.com")

# Create Pets
pet1 = Pet("Max", 3, "dog")
pet2 = Pet("Luna", 2, "cat")

owner.add_pet(pet1)
owner.add_pet(pet2)

# Create Tasks
task_manager = TaskManager()
task_manager.create_task("Morning Walk", "Walk in the park", "07:00", 10, 30, "walk")
task_manager.create_task("Breakfast", "Feed dry food", "08:00", 9, 10, "feed")
task_manager.create_task("Playtime", "Fetch and play", "12:00", 7, 45, "playtime")
task_manager.create_task("Afternoon Walk", "Short walk", "15:00", 8, 20, "walk")
task_manager.create_task("Dinner", "Evening meal", "18:00", 9, 10, "feed")

# Generate Daily Plan
planner = DailyPlanner(pet1, task_manager)
planner.set_available_time(90)
planner.set_preferences({'sort_by_time': True})
schedule = planner.generate_plan()

# Print Today's Schedule
print("TODAY'S SCHEDULE")
print("=" * 50)
print(f"Pet: {pet1.get_name()}")
print(f"Owner: {owner.get_name()}")
print("=" * 50)

for task in schedule:
    print(f"{task.get_time()} - {task.get_task_name()} ({task.get_duration()} min)")

print("=" * 50)
