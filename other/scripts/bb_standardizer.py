import os
import re
from io import StringIO
import logging

template_data = []

def building_block_rewrite():
    template_file_path = "other/utils/BB_Template.md"
    global template_data
    template_data = extract_headings_and_content(template_file_path, is_template_file=True)

    directory = os.path.join(os.getcwd(), os.pardir)
    excluded_dirs = [".github", ".venv", "other", "UseCases"]
    keyword = "BB"
    markdown_files = find_markdown_files(directory, excluded_dirs, keyword)

    for file in markdown_files:
        extract_headings_and_content(file)

def extract_headings_and_content(file_path, is_template_file = False):
    """
    Extract headings and their content from a markdown file.

    Args:
        file_path (str): Path to the markdown file.
        is_template_file: Specifies when the template file is initially loaded.
    Returns:
        dict: Dictionary with headings as keys and their content as values.
    """
    name_pattern = re.compile(r"# ([a-zA-Z0-9, +\-\ \/(\)]*)\s*## BB Tag")
    heading_pattern = re.compile(r"## ([a-zA-Z +\-\/\(\)]*)")

    missing_headings = []

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    #content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    headings = heading_pattern.findall(content)
    names = name_pattern.findall(content)

    if not names:
        raise ValueError(f"No BB Name found in {file_path}")

    implementation_status = 'implementation exists'
    if "WorkInProgress" in file_path:
        implementation_status = 'suggested'

    heading_contents = {"BB Name": names[0], "Implementation Status":implementation_status}

    for i, heading in enumerate(headings):
        if heading not in template_data and not is_template_file:
            logging.warning(f"Wrong template in {file_path}, contains unspecified heading: {heading}.")
            continue
        start = content.find(heading) + len(heading)
        end = content.find(headings[i + 1]) if i + \
            1 < len(headings) else len(content)
        heading_content = content[start: end - 3].replace("\n", " ").strip()
        if heading_content.startswith(("-", "+", "=")):
            heading_content = "'" + heading_content
        heading_contents[heading] = heading_content
    if len(heading_contents) < len(template_data) and not is_template_file:
        template_diff = list(set(template_data).difference(heading_contents))
        logging.warning(f"Missing heading(s) specified in template in file {file_path}. Missing headings: {template_diff}")
        missing_headings.append(template_diff)
        missing_headings = missing_headings[0]

    if len(missing_headings) > 0:
        heading_contents = fix_markdown_file(file_path, heading_contents, missing_headings)
    
    return heading_contents

def find_markdown_files(directory, excluded_dirs, keyword):
    """
    Traverse the directory to find markdown files that include a specific keyword.

    Args:
        directory (str): The root directory to start the search.
        excluded_dirs (list): List of directories to exclude from the search.
        keyword (str): Keyword to filter markdown files.

    Returns:
        list: List of markdown file paths that match the criteria.
    """
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            if file.endswith(".md") and keyword in file:
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def fix_markdown_file(file, content, missing_headings):
    for misssing_heading in missing_headings:
        position = list(template_data.keys()).index(misssing_heading)
        items = list(content.items())
        items.insert(position, (misssing_heading, template_data[misssing_heading]))
        content = dict(items)

    file_content = StringIO()

    for heading, data in content.items():
        file_content.write(heading + "\n")
        file_content.write(data + "\n")

        with open(file, "w", encoding="utf-8") as f:
            f.write(file_content.getvalue())


if __name__ == "__main__":
    building_block_rewrite()