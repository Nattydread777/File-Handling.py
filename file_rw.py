# file_rw.py

# Open input.txt and read content
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (example: make it uppercase)
modified_content = content.upper()

# Write modified content to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been read and modified version written to output.txt")
