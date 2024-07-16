# import os
# from io import StringIO


# def traverse_directory_and_save_to_md(path, output_file):
#     output = StringIO()
#     for root, dirs, files in os.walk(path):
#         # Only process if the root directory contains "Library"
#         if "Library" in root:
#             dirs[:] = [d for d in dirs if not d.startswith(".") and d != ".git"]

#             # Compute the directory level for indentation
#             level = root.replace(path, "").count(os.sep) - 1
#             indent = "    " * level
#             output.write(f"{indent}- {os.path.basename(root)}\n")

#             sub_indent = "    " * (level + 1)
#             for file_name in files:
#                 # Skip hidden files and git-related files
#                 if file_name.startswith(".") or file_name == ".git":
#                     continue

#                 file_path = os.path.join(root, file_name)
#                 file_link = file_path.replace(" ", "%20")
#                 # Remove the file extension from the file name
#                 file_name_without_extension = os.path.splitext(file_name)[0]

#                 # Check if the file name without extension is similar to the folder name
#                 if file_name_without_extension == os.path.basename(root):
#                     output.write(f"{indent}- [{os.path.basename(root)}]({file_link})\n")
#                 else:
#                     output.write(f"{sub_indent}- [{file_name_without_extension}]({file_link})\n")

#     print(output.getvalue())
#     # Write the contents of the StringIO object to the file
#     with open(output_file, "w") as f:
#         f.write(output.getvalue())

#     print("Done!")


# # Specify the directory you want to traverse
# directory_to_traverse = "."
# output_file = "directory_structure.md"

# # Call the function to start traversing and saving to a markdown file
# traverse_directory_and_save_to_md(directory_to_traverse, output_file)


import os
import re
from io import StringIO


def traverse_directory_and_save_to_md(path, output_file):
    output = StringIO()
    pattern = re.compile(r"(^\s*- ([a-zA-Z]*)\n)^\s*- \[([a-zA-Z]*)\]\((...*)\)", re.MULTILINE)
    for root, dirs, files in os.walk(path):
        # Only process if the root directory contains "Library"
        if "library" in root:
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != ".git"]

            # Compute the directory level for indentation
            level = root.replace(path, "").count(os.sep) - 1
            indent = "    " * level
            output.write(f"{indent}- {os.path.basename(root)}\n")

            sub_indent = "    " * (level + 1)
            for file_name in files:
                # Skip hidden files and git-related files
                if file_name.startswith(".") or file_name == ".git":
                    continue

                file_path = os.path.join(root, file_name)
                file_link = file_path.replace(" ", "%20").replace("\\", "/")
                file_link = file_link[1:]
                # Remove the file extension from the file name
                file_name_without_extension = os.path.splitext(file_name)[0]

                # Check if the file name without extension is similar to the folder name
                if file_name_without_extension == os.path.basename(root):
                    output.write(f"{indent}- [{os.path.basename(root)}]({file_link})\n")
                else:
                    output.write(f"{sub_indent}- [{file_name_without_extension}]({file_link})\n")

    output_string = output.getvalue()

    # Delete the pattern from the output
    matches = pattern.findall(output_string)
    if matches:
        print("Pattern found!")
        for match in matches:
            output_string = output_string.replace(match[0], "")
    else:
        print("Pattern not found!")

    # Write the contents of the StringIO object to the file
    with open(output_file, "w") as f:
        f.write(output_string)

    print("Done!")


# Specify the directory you want to traverse
directory_to_traverse = "."
output_file = "directory_structure.md"

# Call the function to start traversing and saving to a markdown file
traverse_directory_and_save_to_md(directory_to_traverse, output_file)
