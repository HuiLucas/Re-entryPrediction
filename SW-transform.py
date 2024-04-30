SW_NEW = open('SW-NEW.txt', 'w')
kp_indeces = open('SW-kp-indeces.txt', 'r')
SW_F10_predicted = open('SW-F10-predicted.txt', 'r')




# Open the file for reading and writing
with open('SW-NEW.txt', 'r+') as file:
    # Read the contents of the file
    lines = file.readlines()

    # Iterate over each line
    for i, line in enumerate(lines):
        # Check if the line has at least 46 characters
        if len(line) >= 46:
            # Modify the text of columns 18 to 46
            line = line[:17] + 'modified text' + line[46:]

            # Update the line in the list of lines
            lines[i] = line

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Write the modified lines back to the file
    file.writelines(lines)

# Close the file
file.close()




# Close files
SW_NEW.close()
kp_indeces.close()
SW_F10_predicted.close()
