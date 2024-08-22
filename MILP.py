# Define the data
requests = [
    {'id': 1, 'start': 1, 'end': 4},
    {'id': 2, 'start': 2, 'end': 5},
    {'id': 3, 'start': 3, 'end': 9},
    {'id': 4, 'start': 5, 'end': 7},
    {'id': 5, 'start': 6, 'end': 8},
    {'id': 6, 'start': 7, 'end': 13},
    {'id': 7, 'start': 8, 'end': 10},
    {'id': 8, 'start': 9, 'end': 11},
    {'id': 9, 'start': 10, 'end': 12},
    {'id': 10, 'start': 11, 'end': 13}
]
num_slots = 2  # Number of available parking slots

def initialize_variables(num_requests, num_slots):
    # Create a binary matrix for decision variables
    x = [[0] * num_slots for _ in range(num_requests)]
    return x

def is_non_conflicting(req1, req2):
    # Check if two requests conflict with each other
    return req1['end'] <= req2['start'] or req2['end'] <= req1['start']

def apply_constraints_and_objective(requests, num_slots):
    num_requests = len(requests)
    x = initialize_variables(num_requests, num_slots)

    # Sort requests by end time to maximize the number of scheduled requests
    sorted_requests = sorted(requests, key=lambda r: r['end'])

    # Assign tasks to slots
    for req in sorted_requests:
        for j in range(num_slots):
            conflict = False
            for k in range(num_requests):
                if x[k][j] == 1 and not is_non_conflicting(req, requests[k]):
                    conflict = True
                    break
            if not conflict:
                index = requests.index(req)
                x[index][j] = 1
                break

    # Output the result
    for j in range(num_slots):
        print(f"Slot {j + 1} assignments:")
        for i in range(num_requests):
            if x[i][j] == 1:
                print(f"  Request {requests[i]['id']} from {requests[i]['start']} to {requests[i]['end']}")

# Execute the scheduling
apply_constraints_and_objective(requests, num_slots)
