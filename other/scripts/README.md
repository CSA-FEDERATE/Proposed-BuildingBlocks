# Output File Generator

This script traverses a directory to find markdown files, extracts specific headings and their content, and generates an output file the format of which can be specified via the *'file_format'* argument. Available choices are:
- xlsx
- csv

The default choice for the export is the xlsx format. 

## Setup

### Create a Virtual Environment

In the project directory, create a virtual environment:

```sh
python3 -m venv .venv
```

### Activate the Virtual Environment

On macOS and Linux:

```sh
source .venv/bin/activate
```

On Windows:

```sh
.\.venv\Scripts\activate
```

### Install Dependencies

With the virtual environment activated, install the required dependencies:

```sh
pip3 install pandas
pip3 install openpyxl
```

## Usage

```sh
output_file_generator.py [-h] [-o OUTPUT] [--exclude [EXCLUDE ...]] [--keyword KEYWORD] [--file_format FORMAT] directory

positional arguments:
  directory             Directory to traverse

options:
  -h, --help            show this help message and exit
  -o, --output OUTPUT   Output file path, default is 'output'
  --exclude [EXCLUDE ...]
                        Directories to exclude, default is '.github', '.venv', 'other', 'UseCases'
  --keyword KEYWORD     Keyword to filter markdown files, default is 'BB'
  --file_format FORMAT  Format of the output file, default is 'xlsx'. Available choices are xlsx, csv.
```

### Example

```sh
python csv_generator.py /path/to/markdown/files -o my_output --exclude .github other --keyword BB
```

This command will:

- Traverse the directory `/path/to/markdown/files`
- Exclude directories `.github` and `other`
- Look for markdown files containing the keyword `BB`
- Generate an Excel file named `my_output.xlsx`


## Github workflow
This script is called when a release is published on the repo and generates an Excel output file in the root folder of the repo. It is assumed that a commit on the main branch is tagged for the release and as such the output file is added to the main branch. When a release is published the workflow *excel_release_workflow* is triggered and first removes the old version of the *output.xlsx* file from the root of the repo if it exists before running the script and pushing the newly generated output file to the main branch.

The workflow executes the script with the following parameters:

python other/scripts/output_file_generator.py ${{ github.workspace }}/ -o ${{ github.workspace }}\output

The *github.workspace* variable specifies the working directory for the runner executing the workflow. In practice it can look like this:

D:\a\Proposed-BuildingBlocks\Proposed-BuildingBlocks/
