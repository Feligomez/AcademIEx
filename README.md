# Student Planner App

## Overview

The Student Planner App is a Python console application designed to help students manage their courses, track their performance, and receive personalized recommendations based on their academic goals. The app allows users to input information about their courses, marks, and goals, and it provides features such as generating a study schedule and offering course recommendations.

## Features

### 1. Course and Student Classes

The app includes two main classes:

- **Course:** Represents a course with attributes such as name, subject, duration in weeks, and hours per day.
- **Student:** Represents a student with details like name, age, degree, and year. Students can also input their marks and goals for each subject.

### 2. Schedule Class

The **Schedule** class manages the study schedule, allowing users to add courses for specific days and hours.

### 3. Recommendation Engine

The app provides a recommendation engine that suggests courses based on a student's academic performance and goals. It considers factors like the difference between marks and goals, subject priority, and the number of weeks remaining until final exams.

### 4. Study Schedule Generation

Users can generate a study schedule based on the recommended courses and their availability. The app employs a simple greedy algorithm to distribute courses across days, considering the available hours.

### 5. User Interaction

The app features an interactive menu that allows users to:

- View course recommendations.
- Generate a study schedule.
- Display their academic profile.
- Change marks and goals for specific subjects.
- Exit the program.

## How to Use

1. Run the Python script (`student_planner.py`).
2. Follow the interactive menu to input your details, marks, goals, and the number of weeks remaining until final exams.
3. Explore course recommendations, generate a study schedule, view your academic profile, or update marks and goals.

## Sample Data

The app includes sample courses and a sample student (`student1`). Users can modify the courses or create additional students by updating the `courses` list and using the `get_student_details` function.

## Dependencies

The app does not require any external dependencies beyond a Python interpreter (3.x).

## Notes

- The app uses a basic priority scoring system to recommend courses, and the study schedule generation follows a simple greedy approach.
- User input is assumed to be valid within the expected format. Error handling for unexpected inputs is not extensively implemented in this version.

## Author

[Your Name]
