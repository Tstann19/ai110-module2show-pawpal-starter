import streamlit as st
from pawpal_system import Pet, Owner, TaskManager, DailyPlanner

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# Initialize session state objects
if "owner" not in st.session_state:
    st.session_state.owner = None
if "pet" not in st.session_state:
    st.session_state.pet = None
if "task_manager" not in st.session_state:
    st.session_state.task_manager = TaskManager()
if "planner" not in st.session_state:
    st.session_state.planner = None

st.subheader("Step 1: Setup Owner & Pet")
owner_name = st.text_input("Owner name", value="Jordan")
owner_email = st.text_input("Owner email", value="jordan@email.com")
pet_name = st.text_input("Pet name", value="Mochi")
pet_age = st.number_input("Pet age", min_value=0, max_value=30, value=3)
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Create Owner & Pet"):
    try:
        # Create Owner object using imported Owner class
        st.session_state.owner = Owner(owner_name, owner_email)

        # Create Pet object using imported Pet class
        st.session_state.pet = Pet(pet_name, pet_age, species)

        # Add pet to owner
        st.session_state.owner.add_pet(st.session_state.pet)

        # Initialize DailyPlanner with pet and task_manager
        st.session_state.planner = DailyPlanner(st.session_state.pet, st.session_state.task_manager)

        st.success(f"✅ Created owner {owner_name} with pet {pet_name} ({species})")
    except ValueError as e:
        st.error(f"Error: {e}")

if st.session_state.pet:
    st.info(f"Current pet: {st.session_state.pet.get_name()} - {st.session_state.pet.get_animal_type()}, {st.session_state.pet.get_age()} years old")

st.markdown("### Step 2: Add Tasks")
st.caption("Add tasks using the TaskManager class. Each task will be managed by the task_manager object.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    task_desc = st.text_input("Description", value="Walk around the block")
with col3:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col4:
    priority = st.number_input("Priority", min_value=0, max_value=10, value=5)

col5, col6 = st.columns(2)
with col5:
    task_time = st.text_input("Time", value="08:00 AM")
with col6:
    task_type = st.selectbox("Task type", ["walk", "feed", "medication", "grooming", "playtime", "training"])

if st.button("Add Task"):
    try:
        # Use TaskManager.create_task() method to add the task
        new_task = st.session_state.task_manager.create_task(
            task_name=task_title,
            description=task_desc,
            time=task_time,
            priority=priority,
            duration=duration,
            task_type=task_type
        )
        st.success(f"✅ Added task: {new_task.get_task_name()}")
    except ValueError as e:
        st.error(f"Error adding task: {e}")

# Display all tasks from TaskManager
all_tasks = st.session_state.task_manager.get_all_tasks()
if all_tasks:
    st.write("Current tasks in TaskManager:")
    task_data = [
        {
            "Task": task.get_task_name(),
            "Type": task.get_task_type(),
            "Duration (min)": task.get_duration(),
            "Priority": task.get_priority(),
            "Time": task.get_time()
        }
        for task in all_tasks
    ]
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Step 3: Generate Daily Schedule")
st.caption("Use the DailyPlanner to create an optimized schedule based on available time and preferences.")

# Settings for planner
col1, col2 = st.columns(2)
with col1:
    available_time = st.number_input("Available time (minutes)", min_value=0, max_value=1440, value=120)
with col2:
    sort_by_time = st.checkbox("Sort tasks by scheduled time", value=False)

# Preferences
with st.expander("Set Preferences (Optional)"):
    preferred_types = st.multiselect(
        "Preferred task types (will be prioritized)",
        ["walk", "feed", "medication", "grooming", "playtime", "training"]
    )
    avoided_types = st.multiselect(
        "Avoided task types (will be de-prioritized)",
        ["walk", "feed", "medication", "grooming", "playtime", "training"]
    )

if st.button("Generate Schedule"):
    if not st.session_state.planner:
        st.error("⚠️ Please create an owner and pet first (Step 1)")
    elif not st.session_state.task_manager.get_all_tasks():
        st.error("⚠️ Please add at least one task first (Step 2)")
    else:
        try:
            # Set available time using DailyPlanner.set_available_time()
            st.session_state.planner.set_available_time(available_time)

            # Set preferences using DailyPlanner.set_preferences()
            preferences = {
                'preferred_task_types': preferred_types,
                'avoided_task_types': avoided_types,
                'sort_by_time': sort_by_time
            }
            st.session_state.planner.set_preferences(preferences)

            # Generate the plan using DailyPlanner.generate_plan()
            plan = st.session_state.planner.generate_plan()

            # Display the results
            st.success(f"✅ Schedule generated! {len(plan)} tasks scheduled.")

            # Show the plan
            if plan:
                st.markdown("### 📅 Your Daily Schedule")
                for i, task in enumerate(plan, 1):
                    st.markdown(
                        f"**{i}. {task.get_task_name()}** ({task.get_task_type()}) "
                        f"- {task.get_duration()} min at {task.get_time()} "
                        f"[Priority: {task.get_priority()}]"
                    )

                # Display plan summary using DailyPlanner.get_plan_summary()
                summary = st.session_state.planner.get_plan_summary()
                st.markdown("### 📊 Schedule Summary")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Tasks", summary['total_tasks'])
                with col2:
                    st.metric("Time Used", f"{summary['total_time']} min")
                with col3:
                    st.metric("Time Remaining", f"{summary['remaining_time']} min")

                # Show detailed explanation using DailyPlanner.explain_plan()
                with st.expander("📝 View Detailed Explanation"):
                    explanation = st.session_state.planner.explain_plan()
                    st.text(explanation)

        except ValueError as e:
            st.error(f"Error generating schedule: {e}")
