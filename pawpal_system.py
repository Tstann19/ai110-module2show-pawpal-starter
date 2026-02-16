"""
PawPal+ System Classes
Pet care task scheduling system
"""

import uuid
from typing import List, Dict, Optional, Any


class Pet:
    """Stores information about a pet"""

    def __init__(self, name: str, age: int, animal_type: str):
        """
        Initialize a Pet instance

        Args:
            name: Pet's name
            age: Pet's age in years
            animal_type: Type of animal (dog, cat, bunny, fish, etc.)
        """
        self._name = name
        self._age = age
        self._animal_type = animal_type

    def get_name(self) -> str:
        """Get the pet's name"""
        return self._name

    def get_age(self) -> int:
        """Get the pet's age"""
        return self._age

    def get_animal_type(self) -> str:
        """Get the pet's animal type"""
        return self._animal_type

    def set_name(self, name: str) -> None:
        """Set the pet's name"""
        self._name = name

    def set_age(self, age: int) -> None:
        """Set the pet's age"""
        self._age = age

    def set_animal_type(self, animal_type: str) -> None:
        """Set the pet's animal type"""
        self._animal_type = animal_type


class Task:
    """Represents a pet care task"""

    def __init__(
        self,
        task_name: str,
        description: str,
        time: str,
        priority: int,
        duration: int,
        task_type: str
    ):
        """
        Initialize a Task instance

        Args:
            task_name: Name of the task
            description: Detailed description of the task
            time: Scheduled time for the task
            priority: Priority level (higher number = higher priority)
            duration: Duration in minutes
            task_type: Type of task (walk, feed, medication, grooming, playtime, etc.)
        """
        self._task_id = str(uuid.uuid4())
        self._task_name = task_name
        self._description = description
        self._time = time
        self._priority = priority
        self._duration = duration
        self._task_type = task_type

    def get_task_id(self) -> str:
        """Get the task's unique ID"""
        return self._task_id

    def get_task_name(self) -> str:
        """Get the task name"""
        return self._task_name

    def get_description(self) -> str:
        """Get the task description"""
        return self._description

    def get_time(self) -> str:
        """Get the scheduled time"""
        return self._time

    def get_priority(self) -> int:
        """Get the task priority"""
        return self._priority

    def get_duration(self) -> int:
        """Get the task duration in minutes"""
        return self._duration

    def get_task_type(self) -> str:
        """Get the task type"""
        return self._task_type

    def set_time(self, time: str) -> None:
        """Set the scheduled time"""
        self._time = time

    def set_priority(self, priority: int) -> None:
        """Set the task priority"""
        self._priority = priority

    def set_duration(self, duration: int) -> None:
        """Set the task duration"""
        self._duration = duration


class TaskManager:
    """Manages pet care tasks - creating, editing, and deleting"""

    def __init__(self):
        """Initialize TaskManager with an empty task list"""
        self._tasks: List[Task] = []

    def create_task(
        self,
        task_name: str,
        description: str,
        time: str,
        priority: int,
        duration: int,
        task_type: str
    ) -> Task:
        """
        Create a new task and add it to the task list

        Args:
            task_name: Name of the task
            description: Detailed description
            time: Scheduled time
            priority: Priority level
            duration: Duration in minutes
            task_type: Type of task

        Returns:
            The created Task object
        """
        task = Task(task_name, description, time, priority, duration, task_type)
        self._tasks.append(task)
        return task

    def edit_task(self, task_id: str, **kwargs) -> Optional[Task]:
        """
        Edit an existing task

        Args:
            task_id: ID of the task to edit
            **kwargs: Task attributes to update (time, priority, duration, etc.)

        Returns:
            The edited Task object, or None if task not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            if 'time' in kwargs:
                task.set_time(kwargs['time'])
            if 'priority' in kwargs:
                task.set_priority(kwargs['priority'])
            if 'duration' in kwargs:
                task.set_duration(kwargs['duration'])
        return task

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task from the task list

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self._tasks

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Get a specific task by ID

        Args:
            task_id: ID of the task to find

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.get_task_id() == task_id:
                return task
        return None


class DailyPlanner:
    """Generates optimized daily care plans using AI"""

    def __init__(self, pet: Pet, task_manager: TaskManager):
        """
        Initialize DailyPlanner

        Args:
            pet: The Pet object
            task_manager: The TaskManager containing all tasks
        """
        self._pet = pet
        self._task_manager = task_manager
        self._available_time: Optional[int] = None
        self._preferences: Dict[str, Any] = {}

    def set_available_time(self, time: int) -> None:
        """
        Set the available time for pet care

        Args:
            time: Available time in minutes
        """
        self._available_time = time

    def set_preferences(self, preferences: Dict[str, Any]) -> None:
        """
        Set owner preferences for scheduling

        Args:
            preferences: Dictionary of preferences
        """
        self._preferences = preferences

    def generate_plan(self) -> List[Task]:
        """
        Generate an optimized daily care plan

        Returns:
            List of scheduled tasks in order
        """
        # TODO: Implement scheduling logic
        pass

    def optimize_schedule(self) -> List[Task]:
        """
        Optimize the schedule based on constraints and priorities

        Returns:
            Optimized list of tasks
        """
        # TODO: Implement optimization logic
        pass

    def explain_plan(self) -> str:
        """
        Explain the reasoning behind the generated plan

        Returns:
            Explanation string
        """
        # TODO: Implement explanation logic
        pass
