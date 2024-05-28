# Proposed-BuildingBlocks

Landing page for all proposed building blocks; use the README to navigate through all the Building Blocks.

New BB should be implemented using the [BB_Template](/utils/BB_Template.md).

## BB Tags

OLD TAGS ARE USED HERE WHICH DO NOT COMPLY TO THE FOLDER STRUCTURE!!!  

- First tag of BB defines its location in git repo

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

### Cloud

- #### [BB-CSC (work in progress)](/BB-CSC/BB-CSC.md)

- #### BB-CEST

- #### BB-CSC-TC

- #### BB-CMU

***

### In-Vehicle

- #### [BB-SC (work in progress)](/BB-SC/BB-SC.md)

  - AppLayer
    - IVI
    - Powertrain_Chassis

  - Layer2a - HW Abstraction Virtualization OS

  - Layer2b - MW and API
    - Communication
    - Runtime
      - [Power Management]
    - Time
      - [Time Service]
    - LogTrace
    - Persistency
    - PlatformHealthManagement
    - Security

- #### [BB-EST](/BB-EST/BB-EST.md)

- #### [BB-SC-TC (work in progress)](/BB-SC-TC/BB-SC-TC.md)

- #### BB-MU

***

### Other

- #### S-BB
