<<<<<<< HEAD
# Guido's Gorgeous Lasagna

This project contains Python code for calculating lasagna preparation and baking times, based on the specifications from the Exercism Python track.

## Description

This module provides functions to:

* Calculate the remaining bake time.
* Calculate the preparation time based on the number of layers.
* Calculate the total elapsed time for preparing and baking the lasagna.

## Files

* `lasagna.py`: Contains the Python code for the lasagna time calculations.
* `test_lasagna.py`: Contains the unit tests for the `lasagna.py` functions.
* `README.md`: This file, providing project documentation.

## Functions

* `bake_time_remaining(elapsed_bake_time)`: Calculates the remaining bake time.
* `preparation_time_in_minutes(number_of_layers)`: Calculates the preparation time in minutes.
* `elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)`: Calculates the total elapsed time.

## Usage

To use these functions, simply import them from the `lasagna` module:

```python
from lasagna import bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes

remaining_time = bake_time_remaining(30)
print(f"Remaining bake time: {remaining_time} minutes")

preparation_time = preparation_time_in_minutes(3)
print(f"Preparation time: {preparation_time} minutes")

total_time = elapsed_time_in_minutes(3, 30)
print(f"Total elapsed time: {total_time} minutes")
=======
# Exercism Tasks

This repository contains my solutions to various exercises from [Exercism](https://exercism.org/).

## About Exercism

Exercism is a platform that helps you improve your coding skills through practice and mentorship. It provides exercises in many different programming languages, and you can get feedback on your solutions from experienced mentors.

## Repository Structure

Each exercise is typically contained within its own directory. The directory name often corresponds to the exercise's slug on Exercism.
>>>>>>> origin/lasagna-task
