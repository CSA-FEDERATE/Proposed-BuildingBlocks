import os
import re
from io import StringIO


def generate():
    # Specify the directory you want to traverse
    directory_to_traverse = "."
    output_file = "utils/structure.md"

    # Call the function to start traversing and saving to a markdown file
    traverse_directory_and_save_to_md(directory_to_traverse, output_file)
    # Merge the structure.md file with the README_base.md file, add content after the "## Navigation" flag, and save to README.md
    insert_md_content("utils/structure.md", "utils/README_base.md", "## Navigation", "README.md")
    print("README created!")


def traverse_directory_and_save_to_md(path, output_file):
    output = StringIO()
    pattern = re.compile(r"(^\s*- [a-zA-Z-:]*\n)(^\s*- \[[a-zA-Z-]*\])(.*)", re.MULTILINE)
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
            # print(match[0])
            output_string = output_string.replace(match[0], "")
    else:
        print("Pattern not found!")

    # Write the contents of the StringIO object to the file
    with open(output_file, "w") as f:
        f.write(output_string)

    print("Created Structure")


def insert_md_content(source_file, target_file, flag, output_file):
    with open(source_file, "r", encoding="utf-8") as f:
        source_content = f.readlines()

    with open(target_file, "r", encoding="utf-8") as f:
        target_content = f.readlines()

    # Find the flag in the target file
    flag_index = next((i for i, line in enumerate(target_content) if line.strip() == flag), None)

    # If the flag is not found, append at the end
    if flag_index is None:
        flag_index = len(target_content)
    else:
        flag_index += 1  # Insert after the flag

    # Insert the source content into the target content
    target_content[flag_index:flag_index] = source_content

    # Write the new content to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(target_content)

    print("Merge successful!")


if __name__ == "__main__":
    generate()
