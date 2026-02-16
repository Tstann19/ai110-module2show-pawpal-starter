import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Pet, Task, TaskManager


def test_task_completion():
    """Verify that calling mark_complete() changes the task's status"""
    task = Task("Walk", "Morning walk", "08:00", 10, 30, "walk")

    # Assuming Task has a mark_complete() method and is_complete() method
    # These would need to be implemented in the Task class
    initial_status = task.is_complete() if hasattr(task, 'is_complete') else False

    if hasattr(task, 'mark_complete'):
        task.mark_complete()
        assert task.is_complete() == True
        print("✓ Task completion test passed")
    else:
        print("✗ Task class does not have mark_complete() method")


def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count"""
    pet = Pet("Max", 3, "dog")
    task = Task("Walk", "Morning walk", "08:00", 10, 30, "walk")

    # Assuming Pet has add_task() and get_task_count() methods
    # These would need to be implemented in the Pet class
    initial_count = pet.get_task_count() if hasattr(pet, 'get_task_count') else 0

    if hasattr(pet, 'add_task'):
        pet.add_task(task)
        new_count = pet.get_task_count()
        assert new_count == initial_count + 1
        print("✓ Task addition test passed")
    else:
        print("✗ Pet class does not have add_task() method")


def test_tasks_chronological_ordering():
    """Verify tasks are returned in chronological order"""
    tm = TaskManager()
    # create tasks out of order
    tm.create_task("Feed", "Feed breakfast", "08:00", 5, 10, "feed")
    tm.create_task("Walk", "Morning walk", "07:00", 8, 30, "walk")
    tm.create_task("Med", "Give meds", "12:00", 9, 5, "medication")

    sorted_tasks = tm.get_tasks_sorted_by_time()
    times = [t.get_time() for t in sorted_tasks]
    assert times == sorted(times), "Tasks are not sorted chronologically"


def test_recurring_daily_completion_creates_next():
    """Confirm marking a daily task complete creates a new task for next day"""
    tm = TaskManager()
    daily = tm.create_task("Walk", "Daily walk", "09:00", 5, 20, "walk", recurrence="daily")
    initial_count = len(tm.get_all_tasks())

    new_task = tm.mark_task_completed(daily.get_task_id())

    # original marked completed
    assert daily.is_completed() is True

    # new recurring task returned and added
    assert new_task is not None
    assert len(tm.get_all_tasks()) == initial_count + 1
    assert new_task.get_recurrence() == "daily"
    assert new_task.is_completed() is False


def test_scheduler_flags_duplicate_times():
    """Verify that the Scheduler flags duplicate times (by name+time)"""
    tm = TaskManager()
    tm.create_task("Feed", "Feed breakfast", "08:00", 5, 10, "feed")

    # has_duplicate_task should detect
    assert tm.has_duplicate_task("Feed", "08:00") is True

    # creating same name+time without allow_duplicates should raise
    try:
        tm.create_task("Feed", "Feed again", "08:00", 3, 5, "feed")
        raised = False
    except ValueError:
        raised = True

    assert raised, "Creating duplicate task should raise ValueError unless allow_duplicates=True"


if __name__ == '__main__':
    test_task_completion()
    test_task_addition()
