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

        Raises:
            ValueError: If name is empty, age is negative, or animal_type is empty
        """
        if not name or not name.strip():
            raise ValueError("Pet name cannot be empty")
        if age < 0:
            raise ValueError("Pet age cannot be negative")
        if not animal_type or not animal_type.strip():
            raise ValueError("Pet animal type cannot be empty")

        self._name = name.strip()
        self._age = age
        self._animal_type = animal_type.strip().lower()

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
        """Set the pet's age

        Raises:
            ValueError: If age is negative
        """
        if age < 0:
            raise ValueError("Pet age cannot be negative")
        self._age = age

    def set_animal_type(self, animal_type: str) -> None:
        """Set the pet's animal type"""
        self._animal_type = animal_type

    def __repr__(self) -> str:
        """String representation of the Pet"""
        return f"Pet(name='{self._name}', age={self._age}, type='{self._animal_type}')"


class Owner:
    """Represents a pet owner who can have multiple pets"""

    def __init__(self, name: str, email: str, phone: Optional[str] = None):
        """
        Initialize an Owner instance

        Args:
            name: Owner's name
            email: Owner's email address
            phone: Owner's phone number (optional)

        Raises:
            ValueError: If name or email is empty, or email is invalid format
        """
        if not name or not name.strip():
            raise ValueError("Owner name cannot be empty")
        if not email or not email.strip():
            raise ValueError("Owner email cannot be empty")
        if '@' not in email:
            raise ValueError("Owner email must be a valid email address")

        self._owner_id = str(uuid.uuid4())
        self._name = name.strip()
        self._email = email.strip()
        self._phone = phone.strip() if phone else None
        self._pets: List[Pet] = []

    def get_owner_id(self) -> str:
        """Get the owner's unique ID"""
        return self._owner_id

    def get_name(self) -> str:
        """Get the owner's name"""
        return self._name

    def get_email(self) -> str:
        """Get the owner's email"""
        return self._email

    def get_phone(self) -> Optional[str]:
        """Get the owner's phone number"""
        return self._phone

    def get_pets(self) -> List[Pet]:
        """Get all pets owned by this owner"""
        return self._pets

    def set_name(self, name: str) -> None:
        """Set the owner's name"""
        self._name = name

    def set_email(self, email: str) -> None:
        """Set the owner's email"""
        self._email = email

    def set_phone(self, phone: str) -> None:
        """Set the owner's phone number"""
        self._phone = phone

    def add_pet(self, pet: Pet) -> None:
        """
        Add a pet to the owner's pet list

        Args:
            pet: Pet object to add
        """
        if pet not in self._pets:
            self._pets.append(pet)

    def remove_pet(self, pet_name: str) -> bool:
        """
        Remove a pet by name

        Args:
            pet_name: Name of the pet to remove

        Returns:
            True if pet was removed, False if not found
        """
        for pet in self._pets:
            if pet.get_name() == pet_name:
                self._pets.remove(pet)
                return True
        return False

    def get_pet_by_name(self, pet_name: str) -> Optional[Pet]:
        """
        Find a pet by name

        Args:
            pet_name: Name of the pet to find

        Returns:
            Pet object if found, None otherwise
        """
        for pet in self._pets:
            if pet.get_name() == pet_name:
                return pet
        return None

    def get_pet_count(self) -> int:
        """
        Get the total number of pets

        Returns:
            Number of pets owned
        """
        return len(self._pets)

    def get_pets_by_type(self, animal_type: str) -> List[Pet]:
        """
        Get all pets of a specific type

        Args:
            animal_type: Type of animal to filter by

        Returns:
            List of pets matching the type
        """
        return [pet for pet in self._pets if pet.get_animal_type() == animal_type.lower()]

    def list_pet_names(self) -> List[str]:
        """
        Get a list of all pet names

        Returns:
            List of pet names
        """
        return [pet.get_name() for pet in self._pets]

    def __repr__(self) -> str:
        """String representation of the Owner"""
        return f"Owner(name='{self._name}', email='{self._email}', pets={len(self._pets)})"


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

        Raises:
            ValueError: If parameters are invalid
        """
        if not task_name or not task_name.strip():
            raise ValueError("Task name cannot be empty")
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        if priority < 0:
            raise ValueError("Task priority cannot be negative")
        if duration <= 0:
            raise ValueError("Task duration must be positive")
        if not task_type or not task_type.strip():
            raise ValueError("Task type cannot be empty")

        self._task_id = str(uuid.uuid4())
        self._task_name = task_name.strip()
        self._description = description.strip()
        self._time = time.strip()
        self._priority = priority
        self._duration = duration
        self._task_type = task_type.strip().lower()

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
        self._time = time.strip()

    def set_priority(self, priority: int) -> None:
        """Set the task priority

        Raises:
            ValueError: If priority is negative
        """
        if priority < 0:
            raise ValueError("Task priority cannot be negative")
        self._priority = priority

    def set_duration(self, duration: int) -> None:
        """Set the task duration

        Raises:
            ValueError: If duration is not positive
        """
        if duration <= 0:
            raise ValueError("Task duration must be positive")
        self._duration = duration

    def __repr__(self) -> str:
        """String representation of the Task"""
        return (f"Task(name='{self._task_name}', type='{self._task_type}', "
                f"time='{self._time}', priority={self._priority}, duration={self._duration}min)")


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

    def get_tasks_by_type(self, task_type: str) -> List[Task]:
        """
        Get all tasks of a specific type

        Args:
            task_type: Type of task to filter by

        Returns:
            List of tasks matching the type
        """
        return [task for task in self._tasks if task.get_task_type() == task_type.lower()]

    def get_tasks_by_priority(self, min_priority: int) -> List[Task]:
        """
        Get all tasks with priority >= min_priority

        Args:
            min_priority: Minimum priority level

        Returns:
            List of tasks with sufficient priority
        """
        return [task for task in self._tasks if task.get_priority() >= min_priority]

    def get_total_duration(self) -> int:
        """
        Calculate total duration of all tasks

        Returns:
            Total duration in minutes
        """
        return sum(task.get_duration() for task in self._tasks)


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
        self._last_plan: List[Task] = []
        self._excluded_tasks: List[Task] = []

    def set_available_time(self, time: int) -> None:
        """
        Set the available time for pet care

        Args:
            time: Available time in minutes

        Raises:
            ValueError: If time is negative
        """
        if time < 0:
            raise ValueError("Available time cannot be negative")
        self._available_time = time

    def set_preferences(self, preferences: Dict[str, Any]) -> None:
        """
        Set owner preferences for scheduling

        Args:
            preferences: Dictionary of preferences (e.g., preferred_task_types, avoid_times)
        """
        self._preferences = preferences

    def generate_plan(self) -> List[Task]:
        """
        Generate an optimized daily care plan based on available tasks,
        time constraints, and preferences

        Returns:
            List of scheduled tasks in optimal order

        Raises:
            ValueError: If available_time is not set
        """
        if self._available_time is None:
            raise ValueError("Available time must be set before generating a plan")

        # Get all tasks and optimize them
        optimized_tasks = self.optimize_schedule()

        # Store the plan for explanation
        self._last_plan = optimized_tasks

        return optimized_tasks

    def optimize_schedule(self) -> List[Task]:
        """
        Optimize the schedule based on constraints and priorities.
        Uses a greedy algorithm considering:
        - Task priority (higher first)
        - Available time budget
        - User preferences for task types
        - Task duration fitting

        Returns:
            Optimized list of tasks that fit within time constraints
        """
        all_tasks = self._task_manager.get_all_tasks()

        if not all_tasks:
            self._excluded_tasks = []
            return []

        # Get preference settings
        preferred_types = self._preferences.get('preferred_task_types', [])
        avoided_types = self._preferences.get('avoided_task_types', [])

        # Score each task based on priority and preferences
        scored_tasks = []
        for task in all_tasks:
            score = task.get_priority()

            # Boost score for preferred task types
            if preferred_types and task.get_task_type() in preferred_types:
                score += 10

            # Penalize avoided task types
            if avoided_types and task.get_task_type() in avoided_types:
                score -= 5

            scored_tasks.append((score, task))

        # Sort by score (descending) - higher scores first
        scored_tasks.sort(key=lambda x: x[0], reverse=True)

        # Select tasks that fit within available time using greedy approach
        selected_tasks = []
        total_time = 0
        self._excluded_tasks = []

        for score, task in scored_tasks:
            if self._available_time is not None and total_time + task.get_duration() <= self._available_time:
                selected_tasks.append(task)
                total_time += task.get_duration()
            else:
                self._excluded_tasks.append(task)

        # Sort selected tasks by time if specified, otherwise keep priority order
        if self._preferences.get('sort_by_time', False):
            selected_tasks.sort(key=lambda t: t.get_time())

        return selected_tasks

    def explain_plan(self) -> str:
        """
        Explain the reasoning behind the generated plan with details
        about task selection, priorities, and time management

        Returns:
            Detailed explanation string
        """
        if not self._last_plan and not self._excluded_tasks:
            return "No plan has been generated yet. Call generate_plan() first."

        explanation_parts = []

        # Header with pet info
        explanation_parts.append(f"=== Daily Care Plan for {self._pet.get_name()} ===")
        explanation_parts.append(f"Pet: {self._pet.get_name()} ({self._pet.get_animal_type()}, {self._pet.get_age()} years old)")
        explanation_parts.append(f"Available Time: {self._available_time} minutes\n")

        # Calculate total scheduled time
        total_scheduled = sum(task.get_duration() for task in self._last_plan)

        explanation_parts.append(f"Total Tasks Scheduled: {len(self._last_plan)}")
        explanation_parts.append(f"Total Time Used: {total_scheduled} minutes")
        explanation_parts.append(f"Remaining Time: {self._available_time - total_scheduled if self._available_time else 0} minutes\n")

        # Explain selected tasks
        if self._last_plan:
            explanation_parts.append("Selected Tasks (in priority order):")
            for i, task in enumerate(self._last_plan, 1):
                explanation_parts.append(
                    f"  {i}. {task.get_task_name()} "
                    f"[{task.get_task_type()}] - "
                    f"{task.get_duration()} min, "
                    f"Priority: {task.get_priority()}, "
                    f"Time: {task.get_time()}"
                )
        else:
            explanation_parts.append("No tasks could be scheduled within the available time.")

        # Explain preferences applied
        if self._preferences:
            explanation_parts.append("\nPreferences Applied:")
            if 'preferred_task_types' in self._preferences:
                explanation_parts.append(f"  - Preferred task types: {', '.join(self._preferences['preferred_task_types'])}")
            if 'avoided_task_types' in self._preferences:
                explanation_parts.append(f"  - Avoided task types: {', '.join(self._preferences['avoided_task_types'])}")
            if self._preferences.get('sort_by_time'):
                explanation_parts.append("  - Tasks sorted by scheduled time")

        # Explain excluded tasks
        if self._excluded_tasks:
            explanation_parts.append(f"\nTasks Not Scheduled ({len(self._excluded_tasks)}):")
            explanation_parts.append("  (Excluded due to time constraints or low priority)")
            for task in self._excluded_tasks[:5]:  # Show first 5
                explanation_parts.append(
                    f"  - {task.get_task_name()} "
                    f"({task.get_duration()} min, Priority: {task.get_priority()})"
                )
            if len(self._excluded_tasks) > 5:
                explanation_parts.append(f"  ... and {len(self._excluded_tasks) - 5} more")

        # Optimization strategy explanation
        explanation_parts.append("\n=== Optimization Strategy ===")
        explanation_parts.append("This plan was optimized using a priority-based greedy algorithm:")
        explanation_parts.append("1. Tasks scored by priority level")
        explanation_parts.append("2. Preferred task types received bonus points")
        explanation_parts.append("3. Tasks selected in order until time budget exhausted")
        explanation_parts.append("4. High-priority tasks scheduled first to ensure completion")

        return "\n".join(explanation_parts)

    def get_plan_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current plan as a dictionary

        Returns:
            Dictionary with plan statistics
        """
        if not self._last_plan:
            return {
                'total_tasks': 0,
                'total_time': 0,
                'remaining_time': self._available_time or 0,
                'tasks_excluded': len(self._excluded_tasks)
            }

        total_time = sum(task.get_duration() for task in self._last_plan)
        task_types = {}
        for task in self._last_plan:
            task_type = task.get_task_type()
            task_types[task_type] = task_types.get(task_type, 0) + 1

        return {
            'pet_name': self._pet.get_name(),
            'total_tasks': len(self._last_plan),
            'total_time': total_time,
            'remaining_time': (self._available_time - total_time) if self._available_time else 0,
            'tasks_excluded': len(self._excluded_tasks),
            'task_types': task_types,
            'time_utilization': (total_time / self._available_time * 100) if self._available_time else 0
        }

    def get_last_plan(self) -> List[Task]:
        """
        Get the most recently generated plan

        Returns:
            List of tasks in the last generated plan
        """
        return self._last_plan.copy()

    def clear_plan(self) -> None:
        """Clear the current plan and excluded tasks"""
        self._last_plan = []
        self._excluded_tasks = []
