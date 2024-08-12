state = (1, 2, 3)  # Initial state as a tuple
state_list = list(state)  # Convert the tuple to a list
state_list.append((4, 5))  # Add a tuple to the list
state = tuple(state_list)  # Convert the list back to a tuple
