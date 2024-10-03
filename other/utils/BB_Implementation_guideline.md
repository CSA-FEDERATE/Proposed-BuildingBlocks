# Implementation of a new BB

When implementing a new BB one has to follow the described guidelines.

## Use Cases and Scenarios

While building blocks are useful as a starting point for specific software component design and implementation considerations, it is always desireable to be able to put building blocks into a larger context, asking the question: what actual use cases and scenarios should a system be able to cover? Such [use case scenarios are collected and maintained in a dedicated structure](/UseCases/Scenarios/).


## BB Contents
- New BBs should be implemented using the [BB_Template](/other/utils/BB_Template.md). 
- Abbreviations used in the BB have to be added to the [abbreviation list](/other/utils/Abbreviations.md). 


## Folder Structure
The position of the BB has to comply to the folowing folder structure:

```

└── 📁BB-SC  # primary tag
    └── 00_BB-SC.md  
    └── 📁AppLayer  # layer (AppLayer, MWLayer, OSLayer, HWLayer)
        └── 00_AppLayer.md  
        └── 📁Communication  # functional cluster name
            └── BB_AOSP_Push_Notification_Service.md  # BB - if it is in >1 FC or tag, put symlink there
            └── 📁BB_OTA_Manager  # folder if more than a .md file exists for BB
                └── BB_OTA_Manager.md # BB if it is in >1 FC or tag, put symlink there
                └── BB_OTA_Manager.xml 
    └── 📁MWLayer  # layer
        └── .gitkeep
```

#### Structure Guidelines
- If you create a folder without content, put a .gitkeep into the folder.  
- Every layer or tag folder has to include a readme file. Use the following pattern to name these files:
```
                00_insert-Layer-or-Tag-name.md

                eg. "00_AppLayer.md
```
The 00_readme.md files to the corresponding folder (eg. folder AppLayer: 00_AppLayer) always have to start with "00_"  

## Naming Convention

- Whitespaces in Folders: "-" (Dash)  
- Whitespaces in Files: "_" (Underscore)  
x
### BBs
Use the following pattern to name BBs:
```
                BB_insert_BB_name.md

                eg. "BB_OTA_Master.md"
```

### Folders
Use the following pattern to name folders:
```
                Insert-folder-name
                
                eg. "AppLayer"
```
            

## Update Readme

When a new BB or folder is added to the libary, the structure in the README has to be updated using 
the [README Generator](/other/scripts/readme_generator.py). To adjust contents of the README other than 
the Navigation, change them in the [README_base file](/other/utils/README_base.md). The Navigation will 
be inserted at the "## Navigation" flag in the [README_base file](/other/utils/README_base.md).

> [!CAUTION]
> If you don't follow this guideline correctly the automatic structure generation will not work!


### Automatic README generation

> [!Warning]
> AUTOMATED README GENERATION VIA ACTIONS DOES NOT WORK YET! HAS TO BE DONE MANUALLY!

Run the [README Generator](/other/scripts/readme_generator.py) script to update the README file.