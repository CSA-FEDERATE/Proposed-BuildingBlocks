import os
import re
from io import StringIO


def generate():
    directory_to_traverse = "."
    output_file = "other/utils/structure.md"

    # Call the function to start traversing and saving to a markdown file
    traverse_directory_and_save_to_md(directory_to_traverse, output_file)
    # Merge the structure.md file with the README_base.md file, add content after the "## Navigation" flag, and save to README.md

    traverse_wip_directory("WorkInProgress", "other/utils/structure_wip.md")
    insert_md_content(
        "other/utils/structure.md",
        "other/utils/structure_wip.md",
        "other/utils/README_base.md",
        "## Navigation",
        "## Navigation for Work In Progress BBs",
        "README.md",
    )
    print("README created!")


def traverse_directory_and_save_to_md(path, output_file):
    output = StringIO()
    pattern = re.compile(r"(^\s*- [a-zA-Z-:0-9]*\n)(^\s*- \[[a-zA-Z-0-9]*\])(.*)", re.MULTILINE)
    for root, dirs, files in os.walk(path):
        # Only process if the root directory contains "Library"

        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "other" and d != "WorkInProgress"]
        # Compute the directory level for indentation
        level = root.replace(path, "").count(os.sep) - 1
        indent = "    " * level
        output.write(f"{indent}- {os.path.basename(root)}\n")

        sub_indent = "    " * (level + 1)

        # Iteration to create the General Structure and links to READMEs

        for file_name in files:
            # Skip hidden files and git-related files
            if file_name.startswith(".") or file_name == "LICENSE.txt":
                continue
            file_path = os.path.join(root, file_name)
            file_link = file_path.replace(" ", "%20").replace("\\", "/")
            file_link = file_link[1:]
            # Remove the file extension from the file name
            file_base_name = os.path.splitext(file_name)[0]
            file_clean_name = file_base_name.lstrip("0123456789_")
            # when the file is a README, link it to the corresponding folder, skip the base README
            if file_clean_name == "README" or file_clean_name == os.path.basename(root):
                if os.path.basename(root) == ".":
                    continue
                output.write(f"{indent}- [{os.path.basename(root)}]({file_link})\n")

        # Another iteration for the BBs

        for file_name in files:
            # Skip hidden files and git-related files
            if file_name.startswith(".") or file_name == "LICENSE.txt":
                continue
            file_path = os.path.join(root, file_name)
            file_link = file_path.replace(" ", "%20").replace("\\", "/")
            file_link = file_link[1:]
            # Remove the file extension from the file name
            file_base_name = os.path.splitext(file_name)[0]
            file_clean_name = file_base_name.lstrip("0123456789_")
            # when the file is a README, link it to the corresponding folder, skip the base README
            if file_clean_name == "README" or file_clean_name == os.path.basename(root):
                if os.path.basename(root) == ".":
                    continue
                continue
            else:
                output.write(f"{sub_indent}- [{file_clean_name}]({file_link})\n")

    output_string = output.getvalue()
    output_lines = output_string.split("\n")[1:]  # Remove the first line
    output_string = "\n".join(output_lines)
    # Delete the pattern from the output
    matches = pattern.findall(output_string)
    if matches:
        print("Pattern found!")
        for match in matches:
            output_string = output_string.replace(match[0], "")
    else:
        print("Pattern not found!")

    # Write the contents of the StringIO object to the file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_string)

    print("Created Structure")


def insert_md_content(source_file, wip_source_file, target_file, flag, wip_flag, output_file):
    with open(source_file, "r", encoding="utf-8") as f:
        source_content = f.readlines()

    with open(wip_source_file, "r", encoding="utf-8") as f:
        wip_source_content = f.readlines()

    with open(target_file, "r", encoding="utf-8") as f:
        target_content = f.readlines()

    # Find the flag in the target file
    flag_index = next((i for i, line in enumerate(target_content) if line.strip() == flag), None)

    # If the flag is not found, append at the end
    if flag_index is None:
        flag_index = len(target_content)
    else:
        flag_index += 1  # Insert after the flag
        print("Flag found!")
        print(flag_index)

    target_content[flag_index:flag_index] = source_content

    wip_flag_index = next((i for i, line in enumerate(target_content) if line.strip() == wip_flag), None)

    if wip_flag_index is None:
        wip_flag_index = len(target_content)
    else:
        wip_flag_index += 1
        print("WIP Flag found!")
        print(wip_flag_index)

    # Insert the source content into the target content

    target_content[wip_flag_index:wip_flag_index] = wip_source_content

    # Write the new content to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(target_content)

    print("Merge successful!")


def traverse_wip_directory(path, output_file):
    output = StringIO()
    pattern = re.compile(r"(^\s*- [a-zA-Z-:0-9]*\n)(^\s*- \[[a-zA-Z-0-9]*\])(.*)", re.MULTILINE)
    for root, dirs, files in os.walk(path):
        # Only process if the root directory contains "Library"

        dirs[:] = [d for d in dirs]
        # Compute the directory level for indentation
        level = root.replace(path, "").count(os.sep) - 1
        indent = "    " * level
        output.write(f"{indent}- {os.path.basename(root)}\n")

        sub_indent = "    " * (level + 1)

        # Iteration to create the General Structure and links to READMEs

        for file_name in files:
            # Skip hidden files and git-related files
            if file_name.startswith("."):
                continue
            file_path = os.path.join(root, file_name)
            file_link = file_path.replace(" ", "%20").replace("\\", "/")
            file_link = file_link.replace("WorkInProgress/", "/WorkInProgress/")
            # Remove the file extension from the file name
            file_base_name = os.path.splitext(file_name)[0]
            file_clean_name = file_base_name.lstrip("0123456789_")
            # when the file is a README, link it to the corresponding folder, skip the base README
            if file_clean_name == "README" or file_clean_name == os.path.basename(root):
                if os.path.basename(root) == ".":
                    continue
                output.write(f"{indent}- [{os.path.basename(root)}]({file_link})\n")

        # Another iteration for the BBs

        for file_name in files:
            # Skip hidden files and git-related files
            if file_name.startswith("."):
                continue
            file_path = os.path.join(root, file_name)
            file_link = file_path.replace(" ", "%20").replace("\\", "/")
            file_link = file_link.replace("WorkInProgress/", "/WorkInProgress/")
            # Remove the file extension from the file name
            file_base_name = os.path.splitext(file_name)[0]
            file_clean_name = file_base_name.lstrip("0123456789_")
            # when the file is a README, link it to the corresponding folder, skip the base README
            if file_clean_name == "README" or file_clean_name == os.path.basename(root):
                if os.path.basename(root) == ".":
                    continue
                continue
            else:
                output.write(f"{sub_indent}- [{file_clean_name}]({file_link})\n")

    output_string = output.getvalue()
    output_lines = output_string.split("\n")[1:]  # Remove the first line
    output_string = "\n".join(output_lines)
    # Delete the pattern from the output
    matches = pattern.findall(output_string)
    if matches:
        print("Pattern found!")
        for match in matches:
            output_string = output_string.replace(match[0], "")
    else:
        print("Pattern not found!")

    # Write the contents of the StringIO object to the file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_string)

    print("Created Structure")


if __name__ == "__main__":
    generate()
