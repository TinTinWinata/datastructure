import heapq

# Create an empty priority queue
priority_queue = []

# Function to push an item onto the queue
def push(queue, item, priority):
    heapq.heappush(queue, (priority, item))

# Function to pop the highest priority item from the queue
def pop(queue):
    return heapq.heappop(queue)

# Push some items with different priorities
push(priority_queue, 'task1', 2)
push(priority_queue, 'task2', 1)
push(priority_queue, 'task3', 3)

# Pop items from the priority queue
print(pop(priority_queue))  # Output: (1, 'task2')
print(pop(priority_queue))  # Output: (2, 'task1')
print(pop(priority_queue))  # Output: (3, 'task3')
