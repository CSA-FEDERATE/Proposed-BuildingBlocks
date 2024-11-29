import os
import re
import pandas as pd


def find_markdown_files(directory, excluded_dirs, keyword):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            if file.endswith(".md") and keyword in file:
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def write_to_csv(df, output_csv):
    df.to_csv(output_csv, index=False)


def extract_headings_and_content(file_path):
    name_pattern = re.compile(r"# ([a-zA-Z0-9, +\-\ \/(\)]*)\s*## BB Tag")
    heading_pattern = re.compile(r"## ([a-zA-Z +\-\/\(\)]*)")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    headings = heading_pattern.findall(content)
    # headings = []
    names = name_pattern.findall(content)
    print(names)

    heading_contents = {"BB Name": names[0]}

    for i, heading in enumerate(headings):
        start = content.find(heading) + len(heading)
        end = content.find(headings[i + 1]) if i + 1 < len(headings) else len(content)
        heading_content = content[start : end - 3].replace("\n", " ").strip()
        heading_contents[heading] = heading_content
    return heading_contents


def create_df(markdown_files):
    file_contents = []

    for file in markdown_files:
        print(file)
        heading_content = extract_headings_and_content(file)
        file_contents.append(heading_content)

    df = pd.DataFrame.from_dict(file_contents)
    return df


def main():
    directory_to_traverse = "."
    keyword = "BB"
    output_csv = "./other/utils/bb_library.csv"

    # headings = [
    #     "BB Tags(s)",
    #     "Functional Clusters",
    #     "Layer",
    #     "Known Implementation",
    #     "ID (unique name)",
    #     "Description",
    #     "Rationale",
    #     "Governance Applicable S-BB(s)",
    #     "Compose BB(s)",
    #     "What is needed to design and implement",
    #     "What is needed to build and run",
    #     "Non-Functional Requirements",
    #     "Dependencies to other clusters",
    #     "Vehicle API relevant",
    #     "Author/Company + Prio",
    #     "Related project(s)",
    #     "Availability of code",
    #     "Availability of API",
    #     "Reference to FEDERATE SDV repository - Open Toolchain(s)",
    #     "Potential obstacles",
    #     "Maturity Badges",
    #     "State (+ date of last change)",
    #     "System Context",
    # ]

    excluded_dirs = [".github", "other", "scripts", "utils"]

    markdown_files = find_markdown_files(directory_to_traverse, excluded_dirs, keyword)
    # markdown_files = [markdown_files[0]]
    # print(markdown_file)
    df = create_df(markdown_files)

    # print(df)
    write_to_csv(df, output_csv)
    # print(f"CSV file '{output_csv}' created!")


if __name__ == "__main__":
    main()
