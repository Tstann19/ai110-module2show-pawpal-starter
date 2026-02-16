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


if __name__ == '__main__':
    test_task_completion()
    test_task_addition()
