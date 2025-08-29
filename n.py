import numpy as np
import matplotlib.pyplot as plt
 
# 1. Define a simple function to generate a random floor plan
def generate_floor_plan(width=10, height=10):
    # Randomly place rooms in a grid
    floor_plan = np.zeros((height, width))
    
    num_rooms = np.random.randint(3, 6)  # Random number of rooms
    for _ in range(num_rooms):
        room_width = np.random.randint(2, width // 2)
        room_height = np.random.randint(2, height // 2)
        
        x_pos = np.random.randint(0, width - room_width)
        y_pos = np.random.randint(0, height - room_height)
        
        # Place room in the grid
        floor_plan[y_pos:y_pos + room_height, x_pos:x_pos + room_width] = 1
    
    return floor_plan
 
# 2. Visualization function to plot the floor plan
def plot_floor_plan(floor_plan):
    plt.imshow(floor_plan, cmap='gray', origin='upper')
    plt.title("Generated Floor Plan")
    plt.axis('off')
    plt.show()
 
# 3. Generate and display a random floor plan
floor_plan = generate_floor_plan(width=10, height=10)
plot_floor_plan(floor_plan)
