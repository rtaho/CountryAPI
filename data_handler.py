import json
import os

# Function to read JSON data from a file
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    except json.JSONDecodeError as e:
        print(f"An error occurred while decoding JSON: {e}")
    return None

# Function to write JSON data to a file
def write_json(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been written to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# Function to get a parameter from JSON data
def get_parameter(data, key):
    return data.get(key, None)

# Function to set a parameter in JSON data
def set_parameter(data, key, value):
    data[key] = value

# Function to delete a parameter from JSON data
def delete_parameter(data, key):
    if key in data:
        del data[key]

# Main function to demonstrate usage
def main():
    # Configurable parameter for the JSON file
    json_filename = 'Data.json'

    # Check if the file exists
    if not os.path.exists(json_filename):
        print(f"{json_filename} does not exist. Creating a new file.")
        data = {}
        write_json(json_filename, data)

    # Read JSON data from the file
    data = read_json(json_filename)
    if data is None:
        return

    # Demonstrate getting a parameter
    key_to_get = 'example_key'
    value = get_parameter(data, key_to_get)
    print(f"Value for '{key_to_get}': {value}")

    # Demonstrate setting a parameter
    key_to_set = 'example_key'
    value_to_set = 'example_value'
    set_parameter(data, key_to_set, value_to_set)
    print(f"Set '{key_to_set}' to '{value_to_set}'")

    # Write the updated data back to the file
    write_json(json_filename, data)

if __name__ == "__main__":
    main()