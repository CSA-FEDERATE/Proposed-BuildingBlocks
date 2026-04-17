# BuildingBlocks for Software Defined Vehicles

Landing page to navigate through the **repository of building block (BB) descriptions** for Software Defined Vehicles (SDV).
A BB can be a software component, an application, a digital asset or similar. Consistent with the [Vehicle of the Future Initiative](https://digital-strategy.ec.europa.eu/en/policies/vehicle-future-initiative) we focus on contributions available in Open Source.

This repository has been created and is maintained by project [FEDERATE](https://federate-sdv.eu/), funded by Chips Joint Undertaking (CHIPS JU), a public-private partnership in collaboration with the Horizon Europe (HORIZON) Framework Programme under Grant Agreement No. 101139749. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or European Commission. Neither the European Union nor the granting authority can be held responsible for them.

BB's are marked with **BB Tags** according to the list below. A BB can have one or more tags, with the first representing it's "main" tag.
In order to find your way through this repository, take the main tag as entry point to traverse the directory structure.
At the endpoint you will find the md file describing the BB including the link to its implementation/home repo. 

Important: you will find this directory structure *twice*: 
+ *primary*, directly starting at root, for **available** BBs  (both, "in work" and "released").
+ *secondary*, starting at "WorkInProgress", duplicates the primary structure, but holds BBs still in concept/ideation phase, waiting to be started. As soon as a BB implementation takes off, the according description will move into the primary structure.


## Releases
A GitHub workflow creates a new realease at the first of every month. This release contains an Excel file listing all the BBs in the repository as they exist in the main branch at that time. The release can be found in the [Releases](https://github.com/CSA-FEDERATE/Proposed-BuildingBlocks/releases) section of the repository.

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

Ideas and concepts for BBs get collected in the [WorkInProgress folder](/WorkInProgress/). As soon as they have a name, a description, a state and a specified known implementation, they are moved up to the root. The BBs that were moved up, get deleted in the WorkInProgress folder.


## Navigation

***

## Navigation for Work In Progress BBs

***


## Implementation of new BBs 

When Implementing a new BB description please follow these [implementation guidelines](/other/utils/BB_Implementation_guideline.md).

##  Change of README
If you uwant to update this [README](/README.md), please make the changes to the [README_base](/other/utils/README_base.md) so that they can be accessed by the [README Generator](/other/scripts/readme_generator.py). After adding the changes, run the [README Generator](/other/scripts/readme_generator.py) locally and push the changes.


generated using [README Generator](/other/scripts/readme_generator.py)
