# Proposed-BuildingBlocks

Landing page for all proposed building blocks; use the README to navigate through all the Building Blocks.

## Implementation of new BBs

New BB should be implemented using the [BB_Template](/utils/BB_Template.md).

Abbreviations have to be added to the [abbreviation list](/utils/Abbreviations.md).

Whitespaces in Folders: "-" (Dash)  
Whitespaces in Files: "_" (Underscore)  

When a new BB or folder is added to the libary, the structure in the README can be updated using the [README Generator](/scripts/readme_generator.py). To adjust contents of the README other than the Navigation, change them in the [README_base file](/utils/README_base.md). The Navigation will be inserted at the "## Navigation" flag in the [README_base file](/utils/README_base.md).

If you create a folder without content, put a .gitkeep into the folder.

### Folder Structure

When implementing a new BB one has to comply to the following folder structure:

```
📁library
    └──📁In-Vehicle
        └── 📁BB-SC  # primary tag
            └── readme.md  
            └── 📁AppLayer  # layer (AppLayer, MWLayer, OSLayer, HWLayer)
                └── readme.md  
                └── 📁Communication  # functional cluster name
                    └── BB_AOSP_Push_Notification_Service.md  # BB - if it is in >1 FC or tag, put symlink there
                    └── 📁BB_OTA_Manager  # folder if more than a .md file exists for BB
                        └── BB_OTA_Manager.md # BB if it is in >1 FC or tag, put symlink there
                        └── BB_OTA_Manager.xml 

```

## BB Tags

First tag of BB defines its location in git repo

|Tag|Description|
|----|----|
|BB-SC|Building Block Stack Component (In-Vehicle / On-Board)|
|BB-CSC|Building Block Cloud Stack Component (Cloud / Off-Board)|
|BB-MU|Building Block Mockup Unit (In-Vehicle / On-Board Component)|
|BB-CMU|Block Cloud Mockup Unit (Cloud / Off-Board Component)|
|BB-EST|Building Block Engineering & Support Tools (for In-Vehicle / On-Board Components)|
|BB-CEST|Building Block Cloud Engineering & Support Tools (for Cloud / Off-Board Components)|
|S-BB|Supporting Building Blocks (Standards, API & Interface Definitions, standardized Data Model)|
|FC|Functional Cluster – Logical group of technically similar BBs|
|BB-SC-TC|Building Block Stack Component ToolChain (contains compatible set of Engineering & Support Tools and Mockup Units for In-Vehicle dev)|
|BB-CSC-TC|Building Block Cloud Stack Component ToolChain ToolChain (contains compatible set of Engineering & Support Tools and Mockup Units for Cloud dev)|
|BB-WE|Whatever Tag / Whitecard|

## Navigation

