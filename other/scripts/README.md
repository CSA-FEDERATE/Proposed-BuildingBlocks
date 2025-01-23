# CSV Generator

This script traverses a directory to find markdown files, extracts specific headings and their content, and generates a CSV file that can e.g. be imported into Excel.

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
```

## Usage

```sh
csv_generator.py [-h] [-o OUTPUT] [--exclude [EXCLUDE ...]] [--keyword KEYWORD] directory

positional arguments:
  directory             Directory to traverse

options:
  -h, --help            show this help message and exit
  -o, --output OUTPUT   Output CSV file path, default is 'output.csv'
  --exclude [EXCLUDE ...]
                        Directories to exclude, default is '.github', '.venv', 'other', 'UseCases'
  --keyword KEYWORD     Keyword to filter markdown files, default is 'BB'
```

### Example

```sh
python csv_generator.py /path/to/markdown/files -o my_output.csv -e .github other -k BB
```

This command will:

- Traverse the directory `/path/to/markdown/files`
- Exclude directories `.github` and `other`
- Look for markdown files containing the keyword `BB`
- Generate a CSV file named `my_output.csv`
