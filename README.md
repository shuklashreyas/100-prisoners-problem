# FinanceAI: Prisoner Box Simulation

This project simulates a well-known probability problem often referred to as the "Prisoner's Box Problem." The goal is to evaluate how often a group of prisoners successfully find their numbers within a set number of box openings. The problem is based on a cyclical search where each prisoner is allowed to open up to half of the boxes to find their number.

## How It Works

The setup involves **N prisoners** and **N boxes**, each box containing a random number between 0 and N-1. Each prisoner begins by opening a box that corresponds to their prisoner number. They continue opening boxes based on the number found inside the previous box, hoping to find their own number within **N/2** attempts.

If all prisoners successfully find their number within the limit, the scenario is marked as a success. Otherwise, it is a failure.

## Execution

To run the simulation, execute the following command:

```bash
python3 main.py

Success rate after 1000 trials for 100 prisoners: 29.40%
Success rate after 1000 trials for 100 prisoners: 32.80%
Success rate after 1000 trials for 100 prisoners: 33.40%
Success rate after 1000 trials for 100 prisoners: 30.20%
...

