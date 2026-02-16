# PawPal+ Class Diagram

```mermaid
classDiagram
    class Pet {
        -string name
        -int age
        -string animal_type
        +__init__(name, age, animal_type)
        +get_name()
        +get_age()
        +get_animal_type()
        +set_name(name)
        +set_age(age)
        +set_animal_type(animal_type)
    }

    class Task {
        -string task_id
        -string task_name
        -string description
        -string time
        -int priority
        -int duration
        -string task_type
        +__init__(task_name, description, time, priority, duration, task_type)
        +get_task_id()
        +get_task_name()
        +get_description()
        +get_time()
        +get_priority()
        +get_duration()
        +get_task_type()
        +set_time(time)
        +set_priority(priority)
        +set_duration(duration)
    }

    class TaskManager {
        -list~Task~ tasks
        +__init__()
        +create_task(task_name, description, time, priority, duration, task_type)
        +edit_task(task_id, **kwargs)
        +delete_task(task_id)
        +get_all_tasks()
        +get_task_by_id(task_id)
    }

    class DailyPlanner {
        -Pet pet
        -TaskManager task_manager
        -int available_time
        -dict preferences
        +__init__(pet, task_manager)
        +set_available_time(time)
        +set_preferences(preferences)
        +generate_plan()
        +optimize_schedule()
        +explain_plan()
    }

    DailyPlanner --> Pet : uses
    DailyPlanner --> TaskManager : uses
    TaskManager --> Task : manages
```

## Class Descriptions

### Pet
Stores information about the pet including name, age, and animal type (dog, cat, bunny, fish, etc.).

### Task
Represents a care task with details like name, description, scheduled time, priority, duration, and type (walk, feed, medication, grooming, playtime, etc.).

### TaskManager
Handles creating, editing, and deleting tasks. Maintains a collection of all tasks for the pet.

### DailyPlanner
Generates an optimized daily care plan using AI. Takes into account the pet information, available tasks, time constraints, and owner preferences to create a schedule.
