import math

# Define the QWERTY keyboard layout as a dictionary
keyboard_layout = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
}

def distance_between_keys(key1, key2):
    if key1 in keyboard_layout and key2 in keyboard_layout:
        row1, col1 = keyboard_layout[key1]
        row2, col2 = keyboard_layout[key2]
        # Calculate Euclidean distance between two keys
        distance = math.sqrt((row2 - row1)**2 + (col2 - col1)**2)
        return distance
    else:
        return None

def check_keyboard_smash(key_sequence):
    max_segment_distance = 4  # Adjust as needed based on sensitivity
    segment_length = 4  # Adjust as needed based on the segment length to check
    tot = 0
    
    for i in range(len(key_sequence) - segment_length + 1):
        segment = key_sequence[i:i + segment_length]
        segment_distances = []
        
        # Calculate distances between consecutive keys in the segment
        for j in range(len(segment) - 1):
            key1 = segment[j]
            key2 = segment[j + 1]
            distance = distance_between_keys(key1, key2)
            if distance is not None:
                segment_distances.append(distance)
        
        # Check if all distances in the segment are within max_segment_distance
        if all(distance <= max_segment_distance for distance in segment_distances):
            tot += 1
    
    return tot > 3

while True:
    print(check_keyboard_smash(input()))
