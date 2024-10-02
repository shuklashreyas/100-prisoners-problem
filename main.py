import random

def initialize_boxes(n):
    """ Initializes the boxes with a random permutation of [0, N-1]. """
    boxes = list(range(n))
    random.shuffle(boxes)
    return boxes

def prisoner_finds_number(prisoner, boxes, max_attempts):
    """ Simulates a single prisoner trying to find their number. """
    attempts = 0
    current_box = prisoner
    
    while attempts < max_attempts:
        if boxes[current_box] == prisoner:
            return True
        else:
            current_box = boxes[current_box]  # Go to the next box based on the number found
            attempts += 1
    
    return False

def simulate_prisoner_boxes(n):
    """ Simulates the entire prisoner box problem. """
    boxes = initialize_boxes(n)
    max_attempts = n // 2 
  
    # Check if all prisoners find their number
    for prisoner in range(n):
        if not prisoner_finds_number(prisoner, boxes, max_attempts):
            return False  # If one prisoner fails, the whole attempt fails
    
    return True  # If all prisoners succeed

# Test the algorithm with a specific number of prisoners
def test_prisoner_box_scenario(n, trials=1000):
    """ Runs multiple trials to test the scenario with N prisoners. """
    success_count = 0
    for _ in range(trials):
        if simulate_prisoner_boxes(n):
            success_count += 1
    
    success_rate = (success_count / trials) * 100
    print(f"Success rate after {trials} trials for {n} prisoners: {success_rate:.2f}%")

# Example test scenario
test_prisoner_box_scenario(100, 1000)
