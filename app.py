
import streamlit as st
from datetime import date
from database import create_table
from task_manager import add_task, view_tasks, complete_task, delete_task

create_table()

st.title("Student Task Manager")
st.write("Manage your academic tasks easily.")

st.subheader("Add New Task")

task_name = st.text_input("Task Name")
due_date = st.date_input("Due Date", value=date.today())

if st.button("Add Task"):
    try:
        add_task(task_name, due_date)
        st.success("Task added successfully!")
    except ValueError as error:
        st.error(str(error))

st.subheader("My Tasks")

tasks = view_tasks()

if not tasks:
    st.info("No tasks available.")

for task in tasks:
    task_id, name, deadline, completed = task

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        status = "Completed" if completed else "Pending"
        st.write(f"{name} | Due: {deadline} | {status}")

    with col2:
        if not completed:
            if st.button("Complete", key=f"complete_{task_id}"):
                complete_task(task_id)
                st.rerun()

    with col3:
        if st.button("Delete", key=f"delete_{task_id}"):
            delete_task(task_id)
            st.rerun()
