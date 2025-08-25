def reverse_file_with_stack(input_filename, output_filename):
    """
    Reverses the content of a file line by line using a stack.

    Args:
        input_filename (str): The name of the file to be reversed.
        output_filename (str): The name of the file to save the reversed content.
    """
    stack = []

    try:
        # Step 1: Read the file and push each line onto the stack
        with open(input_filename, 'r') as file:
            for line in file:
                stack.append(line)
        
        # Step 2: Pop each line from the stack and write to the output file
        with open(output_filename, 'w') as file:
            while stack:
                file.write(stack.pop())

        print(f"Successfully reversed the content of '{input_filename}' and saved it to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---

# 1. Create a dummy file to test with
with open("original.txt", "w") as f:
    f.write("Line 1: This is the first line.\n")
    f.write("Line 2: Followed by the second.\n")
    f.write("Line 3: And then the third.\n")
    f.write("Line 4: Finally, the last line.\n")

# 2. Call the function to reverse the file
reverse_file_with_stack("original.txt", "reversed.txt")

# 3. (Optional) Print the content of the new file to verify
print("\nContent of the reversed file:")
with open("reversed.txt", "r") as f:
    print(f.read())