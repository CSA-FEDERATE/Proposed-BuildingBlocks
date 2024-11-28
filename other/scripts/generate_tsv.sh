#!/bin/bash

# Ensure consistent sorting and text processing
export LC_ALL=C

# Default directory ignore list
IGNORE_DIRS=(".git" ".github" "other" "UseCases")

# BB Headings to include in output
HEADINGS=(
    "BB Tags(s)"
    "Functional Clusters"
    "Layer"
    "Known Implementation"
    "ID (unique name)"
    "Description"
    "Rationale"
    "Governance Applicable S-BB(s)"
    "Compose BB(s)"
    "What is needed to design and implement"
    "What is needed to build and run"
    "Non-Functional Requirements"
    "Dependencies to other clusters"
    "Vehicle API relevant"
    "Author/Company + Prio"
    "Related project(s)"
    "Availability of code"
    "Availability of API"
    "Reference to FEDERATE SDV repository - Open Toolchain(s)"
    "Potential obstacles"
    #    "Maturity Badges"
)

# Function to parse a single markdown file and extract relevant contents
parse_markdown_file() {
    local file="$1"
    local current_heading=""
    declare -a content
    content=() # Reset content array for this file

    while IFS= read -r line; do
        # Normalize special characters
        line=$(echo "$line" | sed 's/•/-/g; s/…/.../g; s/\t/ /g')

        # Match level 2 headings
        if [[ "$line" =~ ^##\ (.+) ]]; then
            current_heading="${BASH_REMATCH[1]}"

        # Handle bulleted lists or lines starting with "-"
        elif [[ "$line" =~ ^- ]]; then
            if [[ -n "$current_heading" ]]; then
                local heading_index=-1
                for i in "${!HEADINGS[@]}"; do
                    if [[ "${HEADINGS[$i]}" == "$current_heading" ]]; then
                        heading_index=$i
                        break
                    fi
                done
                if [[ $heading_index -ge 0 ]]; then
                    content[$heading_index]+="'${line//$'\t'/ } "
                fi
            fi
        fi
    done <"$file"

    # Output the parsed file's contents in TSV format
    local dirpath=$(dirname "$file")
    local headline=$(grep -m 1 '^# ' "$file" | sed 's/^# //')
    printf "%s\t%s" "$dirpath" "$headline"
    for i in "${!HEADINGS[@]}"; do
        printf "\t%s" "${content[$i]}"
    done
    printf "\n"
}

# Parse arguments for directories to ignore
while [[ "$1" == --ignore-dir=* ]]; do
    IGNORE_DIRS+=("${1#--ignore-dir=}")
    shift
done

# Remaining argument is the root directory
ROOT_DIR="$1"
if [[ -z "$ROOT_DIR" ]]; then
    echo "Usage: $0 [--ignore-dir=DIR]... ROOT_DIR"
    exit 1
fi

# Function to check if a directory is in the ignore list
is_ignored() {
    local dir="$1"
    for ignored in "${IGNORE_DIRS[@]}"; do
        # Check if the directory's basename or full path matches any ignored directory
        if [[ $dir == *"$ignored"* ]]; then
            return 0
        fi
    done
    return 1
}

# Output column headers
{
    # Print header line
    printf "Directory\tHeadline"
    for heading in "${HEADINGS[@]}"; do
        printf "\t%s" "$heading"
    done
    printf "\n"

    # Process Markdown files
    find "$ROOT_DIR" -maxdepth 5 -type f -name "*.md" ! -name "README.md" | sort | while read -r file; do
        if is_ignored "$file"; then
            continue
        fi
        parse_markdown_file "$file"
    done
}
