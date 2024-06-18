import os

def traverse_directory_and_save_to_md(path, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(path):
            # Filter out hidden directories and git directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '.git']
            
            # Compute the directory level for indentation
            level = root.replace(path, '').count(os.sep)
            indent = '    ' * level
            f.write(f"{indent}- {os.path.basename(root)}:\n")
            
            sub_indent = '    ' * (level + 1)
            for file_name in files:
                # Skip hidden files and git-related files
                if file_name.startswith('.') or file_name == '.git':
                    continue
                
                file_path = os.path.join(root, file_name)
                file_link = file_path.replace(" ", "%20")
                f.write(f"{sub_indent}- [{file_name}]({file_link})\n")

# Specify the directory you want to traverse
directory_to_traverse = "."
output_file = "directory_structure.md"

# Call the function to start traversing and saving to a markdown file
traverse_directory_and_save_to_md(directory_to_traverse, output_file)

print("Done!")
