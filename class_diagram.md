# PawPal+ Class Diagram
```mermaid
classDiagram
    class Owner {
        -string owner_id
        -string name
        -string email
        -string phone
        -list~Pet~ _pets
        +__init__(name, email, phone=None)
        +add_pet(pet)
        +get_pets()
        +get_pet_count()
    }

    class Pet {
        -string name
        -int age
        -string animal_type
        +__init__(name, age, animal_type)
        +get_name()
        +get_age()
        +get_animal_type()
    }

    class Task {
        -string task_id
        -string task_name
        -string description
        -string time
        -time time_obj
        -int priority
        -int duration
        -string task_type
        -string? recurrence
        -string? pet_id
        -bool completed
        -datetime? completed_time
        +__init__(task_name, description, time, priority, duration, task_type, recurrence=None, pet_id=None)
        +get_task_id()
        +get_task_name()
        +get_time()
        +get_time_obj()
        +get_recurrence()
        +is_completed() / get_completed_time()
        +mark_completed()
    }

    class TaskManager {
        -Dict~string, Task~ _tasks
        -int? _total_duration_cache
        +__init__()
        +create_task(..., allow_duplicates=False, warn_conflicts=False)
        +has_duplicate_task(task_name, time)
        +get_all_tasks()
        +get_task_by_id(task_id)
        +get_tasks_sorted_by_time()
        +check_task_conflicts(task)
        +get_all_conflicts()
        +mark_task_completed(task_id)
    }

    class DailyPlanner {
        -Pet pet
        -TaskManager task_manager
        -int available_time
        -dict preferences
        -list~Task~ _last_plan
        +__init__(pet, task_manager)
        +set_available_time(time)
        +set_preferences(preferences)
        +generate_plan()
        +optimize_schedule()
        +explain_plan()
        +get_plan_summary()
    }

    class App_UI {
        <<client>>
        +interacts_with(TaskManager, DailyPlanner)
    }

    %% Relationships and multiplicities
    Owner "1" o-- "*" Pet : owns
    TaskManager "1" o-- "*" Task : manages
    Task "0..1" -- "1" Pet : assigned_to (via pet_id)
    DailyPlanner --> TaskManager : uses
    DailyPlanner --> Pet : uses
    App_UI ..> TaskManager : calls
    App_UI ..> DailyPlanner : calls

    %% Notes about behavior
    note right of TaskManager
        - _tasks: Dict[task_id, Task]
        - create_task prevents duplicates unless allow_duplicates=True
        - check_task_conflicts / get_all_conflicts return warnings (do not block)
    end note

    note right of Task
        - mark_completed() sets completed and completed_time
        - if recurrence in ["daily","weekly"], mark_task_completed() creates next occurrence
    end note
```
