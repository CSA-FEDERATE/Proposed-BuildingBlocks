import os
import re
from io import StringIO
import logging

template_data = []

def building_block_rewrite():
    template_file_path = "other/utils/BB_Template.md"
    global template_data, template_descriptions
    template_data, template_descriptions = extract_template_headings_content_description(template_file_path)

    directory = os.path.join(os.getcwd(), os.pardir)
    excluded_dirs = [".github", ".venv", "other", "UseCases"]
    keyword = "BB"
    markdown_files = find_markdown_files(directory, excluded_dirs, keyword)

    for file in markdown_files:
        scan_bb_file(file)

def extract_template_headings_content_description(file_path):
    """
    Extract headings and their content from a the BB template file.

    Args:
        file_path (str): Path to the markdown file.
    Returns:
        dict(str, str): Dictionary with headings as keys and their content as values.
        list(str): List containing heading descriptions of template file.
    """
    name_pattern = re.compile(r"# ([a-zA-Z0-9, +\-\ \/(\)]*)\s*## BB Tag")
    heading_pattern = re.compile(r"## ([a-zA-Z +\-\/\(\)]*)")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    headings = heading_pattern.findall(content)
    names = name_pattern.findall(content)

    if not names:
        raise ValueError(f"No BB Name found in {file_path}")


    heading_contents = {"BB Name": names[0]}
    template_descriptions = list()

    for i, heading in enumerate(headings):
        start = content.find(heading) + len(heading)
        end = content.find(headings[i + 1]) if i + \
            1 < len(headings) else len(content)
        
        heading_content = content[start:end].strip("\r\n# ")
        heading_contents[heading] = heading_content

        # extract heading descriptions, i.e comments under heading <!--...-->
        template_descriptions.append(heading_content)

    return heading_contents, template_descriptions

def scan_bb_file(file_path):
    """
    Checks BB file for missing headings, unspecified headings and mismatched heading descriptions with template file as a reference.
    If any headings are missing, the file contains unspecified headings, or the heading descriptions are mismatched, the fix_markdown_file function is called.

    Args:
        file_path (str): Path to the markdown file.
    """
    name_pattern = re.compile(r"# ([a-zA-Z0-9, +\-\ \/(\)]*)\s*## BB Tag")
    heading_pattern = re.compile(r"## ([a-zA-Z +\-\/\(\)]*)")

    missing_headings = []
    # if there are any headings in the file not specified in the template, the file will be rewritten without the unsepcified heading
    contains_unspecified_headings = False

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    headings = heading_pattern.findall(content)
    names = name_pattern.findall(content)

    if not names:
        raise ValueError(f"No BB Name found in {file_path}")


    heading_contents = {"BB Name": names[0]}

    end = 0

    # check for missing headings
    for i, heading in enumerate(headings):
        if heading not in template_data:
            logging.warning(f"Wrong template in {file_path}, contains unspecified heading: {heading}.")
            contains_unspecified_headings = True
            continue
        start = end + content[end:].find(heading) + len(heading)
        end = start + content[start:].find(headings[i + 1]) if i + \
            1 < len(headings) else len(content)
        
        heading_content = content[start:end].strip("\r\n# ")
        heading_contents[heading] = heading_content

        heading_contents[heading] = heading_content

    # check for mismatched descriptions
    descriptions = list()
    for i, heading in enumerate(headings):
        start = content.find(heading) + len(heading)
        end = content.find(headings[i + 1]) if i + \
            1 < len(headings) else len(content)
        
        heading_content = content[start:end].strip("\r\n# ")
        heading_contents[heading] = heading_content

        # extract heading descriptions, i.e comments under heading <!--...-->
        descriptions.append(heading_content) if heading_content.startswith("<!--") else descriptions.append("")
    
    if len(heading_contents) < len(template_data):
        template_diff = list(set(template_data).difference(heading_contents))
        logging.warning(f"Missing heading(s) specified in template in file {file_path}. Missing headings: {template_diff}")
        missing_headings.append(template_diff)
        missing_headings = missing_headings[0]

    if len(missing_headings) > 0 or contains_unspecified_headings:
        heading_contents = fix_markdown_file(file_path, heading_contents, missing_headings)
    
def find_markdown_files(directory, excluded_dirs, keyword):
    """
    Traverse the directory to find markdown files that include a specific keyword.

    Args:
        directory (str): The root directory to start the search.
        excluded_dirs (list(str)): List of directories to exclude from the search.
        keyword (str): Keyword to filter markdown files.

    Returns:
        list(str): List of markdown file paths that match the criteria.
    """
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            if file.endswith(".md") and keyword in file:
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def fix_markdown_file(file, content, missing_headings):
    """
    Add missing headings to file at the appropriate position. 
    Rewrite the file with the new headings and invalid headings removed.

    Args:
        file (str): Path to building block file to be rewritten.
        content (dict(str, str)): Contents of the file. Key: Heading, Value: Content of the heading.
        missing_headings (list(str)): List containing missing headings in the file according to the template.
    """
    for misssing_heading in missing_headings:
        position = list(template_data.keys()).index(misssing_heading)
        items = list(content.items())
        items.insert(position, (misssing_heading, template_data[misssing_heading]))
        content = dict(items)

    file_content = StringIO()
    file_content.write("# " + content["BB Name"] + "\n")
    content.pop("BB Name")

    i = 0
    for heading, data in content.items():
        # special logic for API Type, if nothing is written, then the text 'None' is added
        if heading == "Type of API":
            comment_pattern = re.compile(r"<!--.*-->")
            comment = comment_pattern.findall(data)[0]
            data_no_comment = data.replace(comment,"")
            if not data_no_comment:
                data = data + "\nNone"
        file_content.write("## " + heading + "\n")
        file_content.write(data)
        if i+1 < len(content):
            if len(data) > 0:
                file_content.write("\n\n")
            else:
                file_content.write("\n")
        i = i + 1

    with open(file, "w", encoding="utf-8") as f:
        f.write(file_content.getvalue())


if __name__ == "__main__":
    building_block_rewrite()