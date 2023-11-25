# Student Planner App

## Overview

AcademIEx is a Python application (run on console) designed to help IE students track their performance and improve upon it by recommending courses to follow before facing the final exams, depending on their academic goals. Besides showing plain recommendations, it also provides a recommended schedule based on the number of available hours the student has for each day of a week.

## Features

### 1. Course and Student Classes

The app includes two main classes:

- **Student:** A student class with attributes name, age, degree, year, marks and goals. Marks and goals are inputted by the student and can be updated at any time. This class works as a "create a profile" initial task.
- **Course:** A course class with attributes name, subject, weeks, and hours (weeks — weeks it takes to complete, hours — hours per day we recommend to take it for)

### 2. Schedule Class

The **Schedule** class is the one behind the design a schedule option, allowing users to add courses for specific days and hours.

### 3. Recommendation Engine

The recommendation feature of AcademIEx works taking into account the student's academic performance (which in turn compares students' latest updated grades and their goals) and how far away the final exams are. It prioritizes subjects that the student is failing and then goes on to explore those the student hasn't reached its goals for, and then outputs several courses the student might want to look out for and make space for in their constrained schedule. To do so, the app uses a Selection Sort algorithm.

### 4. Study Schedule Generation

StudentIEx implements a schedule generator, which takes into consideration the recommended courses and outputs a weekly schedule based on the student's daily time constraints. The app employs a simple greedy algorithm to distribute courses across days, considering the available hours.

### 5. User Interaction

The app features an interactive menu that allows users to:

- View course recommendations.
- Generate a study schedule.
- Display their academic profile.
- Change marks and goals for specific subjects.
- Exit the program.

## How to Use

1. Make sure you have a Python interpreter installed.
2. Run the Python script (`academIEx.py`).
3. Input your student data — name, age, degree and year.
4. Input your latest updated mark and your goal for each subject.
5. Input the number of weeks remaining until the final exams — this will help the recommendations tab work properly.
6. Explore the interactive menu and enjoy AcademIEx!

## Sample Data

The app currently includes sample courses to partake on and currently only works for BBABDBA sophomore students due to its limited reach.

## Dependencies

The app does not require any external dependencies beyond a Python interpreter (3.x).

## Notes

- When asked for a digit (age, marks, goals), please input the nearest integer to the correct value — the system is not acquainted with decimals and will throw an exception.
- The app uses a basic priority scoring system to recommend courses, and the study schedule generation follows a simple greedy approach.
- Expected formats are assumed to be followed. Error handling for unexpected inputs is not implemented — exceptions are not accounted for.

## Future improvements

This app is still on a very early development stage. Future developments upon them are very welcome, and could include:
- A seminar recommendation system taking into account specific interests
- Difficulty levels for the courses
- An increase in the number of courses (and a more proficient and perhaps topic-based selection)
- An account creation function that stores data to avoid inputing all data every time the code is run
- Visual / aesthetic improvements.

## Authors

Gonzalo Domínguez, Sarah Coste, Eli Homsi, Sergio García, Felipe Gómez
