# Proposed-BuildingBlocks

Landing page for all proposed building blocks; use the README to navigate through all the Building Blocks.

## Implementation of new BBs / Change of README

When Implementing a new BB please follow these [implementation guidelines](/other/utils/BB_Implementation_guideline.md).

When wanting to make changes to the [README](/README.md), please make the changes to the [README_base](/other/utils/README_base.md) so that they can be accessed by the [README Generator](/other/scripts/readme_generator.py). After adding the changes, run the [README Generator](/other/scripts/readme_generator.py) locally and push the changes.

## BB Tags


First tag of BB defines its location in git repo

|Tag|Description|
|----|----|
|FC|Functional Cluster – Logical group of technically similar BBs|
|BB-SC|Building Block Stack Component (In-Vehicle / On-Board)|
|BB-CSC|Building Block Cloud Stack Component (Cloud / Off-Board)|
|BB-MU|Building Block Mockup Unit (In-Vehicle / On-Board Component)|
|BB-CMU|Building Block Cloud Mockup Unit (Cloud / Off-Board Component)|
|BB-EST|Building Block Engineering & Support Tools (for In-Vehicle / On-Board Components)|
|BB-CEST|Building Block Cloud Engineering & Support Tools (for Cloud / Off-Board Components)|
|BB-SC-TC|Building Block Stack Component ToolChain (contains compatible set of Engineering & Support Tools and Mockup Units for In-Vehicle dev)|
|BB-CSC-TC|Building Block Cloud Stack Component ToolChain ToolChain (contains compatible set of Engineering & Support Tools and Mockup Units for Cloud dev)|
|S-BB|Supporting Building Blocks (Standards, API & Interface Definitions, standardized Data Model)|
|BB-WE|Whatever Tag / Whitecard|

## Process description

BBs get collected in the [WorkInProgress folder](/WorkInProgress/). As soon as they have a name, a description, a state and a specified known implementation, they are moved up to the root. The BBs that were moved up, get deleted in the WorkInProgress folder.

![Process description](/other/figures/Process_description.PNG)



## Navigation

***

## Navigation for Work In Progress BBs

***
generated using [README Generator](/other/scripts/readme_generator.py)