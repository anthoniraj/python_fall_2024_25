def read_file(filename):
    """
    Reads data from a CSV file and converts it into a list of lists.

    Parameters:
    filename (str): The name of the CSV file to read.

    Returns:
    list: A list where each item is a list containing the registration number,
          name, and mark of each student.
    """
    # Open the file in read mode
    f = open(filename, 'r')
    
    # Read all lines from the file
    lines = f.readlines()
    
    # Close the file after reading to free up resources
    f.close()
    
    data = []  # Initialize an empty list to store the processed data
    
    # Skip the header line (lines[1:]) and process each remaining line
    for line in lines[1:]:
        # Split the line by commas to separate regno, name, and mark
        parts = line.strip().split(',')
        
        # Convert the mark (at index 2) from string to integer
        parts[2] = int(parts[2])
        
        # Append the processed list (regno, name, mark) to data
        data.append(parts)
    
    return data  # Return the list of data


def find_max(data):
    """
    Finds the maximum mark in the list of student data.

    Parameters:
    data (list): A list of student records, where each record is a list
                 containing regno, name, and mark.

    Returns:
    int: The maximum mark found in the data.
    """
    max_mark = 0  # Initialize max_mark to the lowest possible value
    
    # Iterate over each student record
    for line in data:
        # Check if the student's mark is greater than the current max_mark
        if line[2] > max_mark:
            max_mark = line[2]  # Update max_mark if a higher mark is found
    
    return max_mark  # Return the highest mark


def find_min(data):
    """
    Finds the minimum mark in the list of student data.

    Parameters:
    data (list): A list of student records, where each record is a list
                 containing regno, name, and mark.

    Returns:
    int: The minimum mark found in the data.
    """
    min_mark = 20  # Initialize min_mark with the maximum possible mark in this dataset
    
    # Iterate over each student record
    for line in data:
        # Check if the student's mark is less than the current min_mark
        if line[2] < min_mark:
            min_mark = line[2]  # Update min_mark if a lower mark is found
    
    return min_mark  # Return the lowest mark


def top_performers(data):
    """
    Sorts the list of student data in descending order by marks and retrieves
    the top performers.

    Parameters:
    data (list): A list of student records, where each record is a list
                 containing regno, name, and mark.

    Returns:
    list: A list of the top 15 performers based on marks.
    """
    # Sort the data by mark in descending order
    top = sorted(data, key=lambda x: x[2], reverse=True)
    
    # Return the top 15 performers
    return top[:15]


if __name__ == '__main__':
    # Read data from the CSV file
    content = read_file('mid_term_marks.csv')
    
    # Print the maximum mark
    print(f"The maximum mark is {find_max(content)}")
    
    # Print the minimum mark
    print(f"The minimum mark is {find_min(content)}")
    
    # Display the top performers
    print(f"The top performers are:")
    for line in top_performers(content):
        print(f"{line[0]}-{line[1]}: {line[2]}")
