# Student Task Manager

**Course:** SE 513 – Software Testing  
**Track:** B – Testing a Newly-Developed System  
**Team Members:** Mohith Chinni and Venkata Teja Talasila

## Project Description

Student Task Manager is a simple Python application that helps students organize academic tasks. Users can add tasks with due dates, view tasks, mark tasks as completed, and delete tasks.

## Technologies Used

Python, Streamlit, SQLite, pytest, and pytest-cov.

## Installation

Install the required dependencies:

`python -m pip install -r requirements.txt`

## Run the Application

`python -m streamlit run app.py`

## Run Automated Tests

`python -m pytest tests/ -v`

## Generate Coverage Report

`python -m pytest tests/ --cov=task_manager --cov=database --cov-report=term-missing -v`

## Current Testing Results

Six automated tests passed successfully, with 100% statement coverage across `database.py` and `task_manager.py` in the latest local test run.

## Project Status

The basic application and initial unit and integration tests are complete. Additional testing, continuous integration, and final documentation are planned for later project milestones.