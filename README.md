# Proposed-BuildingBlocks

Landing page for all proposed building blocks; use the README to navigate through all the Building Blocks.

## Implementation of new BBs

- New BB should be implemented using the [BB_Template](/utils/BB_Template.md).  
- If you create a folder without content, put a .gitkeep into the folder.  
- Whitespaces in Folders: "-" (Dash)  
- Whitespaces in Files: "_" (Underscore)  

Abbreviations have to be added to the [abbreviation list](/utils/Abbreviations.md).

### Folder Structure

When implementing a new BB one has to comply to the following folder structure:

```
└── 📁BB-SC  # primary tag
        └── readme.md  
        └── 📁AppLayer  # layer (AppLayer, MWLayer, OSLayer, HWLayer)
            └── readme.md  
            └── 📁Communication  # functional cluster name
                └── BB_AOSP_Push_Notification_Service.md  # BB - if it is in >1 FC or tag, put symlink there
                └── 📁BB_OTA_Manager  # folder if more than a .md file exists for BB
                    └── BB_AOSP_Push_Notification_Service.md # BB if it is in >1 FC or tag, put symlink there
                    └── BB_AOSP_Push_Notification_Service.xml 

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

### Cloud

- #### [BB-CSC](/BB-CSC/BB-CSC.md)

- #### [BB-CEST](/BB-CEST/BB-CEST.md)

- ##### Cross-Layer  

  - _Not_Clustered
    - [Car Simulator](/BB-CEST/_Not_Clustered/BB_Car_Simulator.md)

- #### [BB-CSC-TC](/BB-CSC-TC/BB-CSC-TC.md)

- #### [BB-CMU](/BB-CMU/BB-CMU.md)

***

### In-Vehicle

- #### [BB-SC](/BB-SC/BB-SC.md)

- ##### [AppLayer](/BB-SC/AppLayer/Applayer.md)

  - Communication
    - [AOSP Push Notification Server](/BB-SC/MWLayer/Communication/BB_Communication_Server_S2S.md)

- ##### [MWLayer](/BB-SC/MWLayer/MWLayer.md)

  - Communication
    - [Communication Service S2S](/BB-SC/MWLayer/Communication/BB_Communication_Service_S2S.md)
    - [Constraint DDS embeddedRTPS](/BB-SC/MWLayer/Communication/BB_Constraint_DDS_embeddedRTPS.md)
    - [Gateway Mirroring](/BB-SC/MWLayer/Communication/BB_Gateway_Mirroring.md)
    - [Network Management](/BB-SC/MWLayer/Communication/BB_Network_Management.md)
    - [SecOS](/BB-SC/MWLayer/Communication/BB_SecOS.md)
    - [Smart Charging Communication](/BB-SC/MWLayer/Communication/BB_Smart_Charging_Communication.md)
    - [Standard Android VHAL](/BB-SC/MWLayer/Communication/BB_Standard_Android_VHAL.md)
  - Configuration
    - [Local Update Manager](/BB-SC/MWLayer/Configuration/BB_Local_Update_Manager.md)
    - [OTA Master](/BB-SC/MWLayer/Configuration/BB_OTA_Master.md)
  - Diagnostics
    - [Policy Manager](/BB-SC/MWLayer/Diagnostics/BB_Policy_Manager.md)
  - Platform Health Management
    - [Distributed Health Management](/BB-SC/MWLayer/Platform-Health-Management/BB_Distributed_Health_Management.md)
    - [Watchdog](/BB-SC/MWLayer/Platform-Health-Management/BB_Watchdog.md)
  - Power Management
    - [Power Management Coordination](/BB-SC/MWLayer/Power-Management/BB_Power_Management_Coordination.md)
  - Runtime
    - [State Management](/BB-SC/MWLayer/Runtime/BB_State_Management.md)
    - [Diagnostic Services Applications](/BB-SC/MWLayer/Runtime/BB_State_Management.md)
  - Security
    - [Crypto Service Manager](/BB-SC/MWLayer/Security/BB_Crypto_Service_Manager.md)
    - [Internet Protocol Security](/BB-SC/MWLayer/Security/BB_Internet_Protocol_Security.md)
    - [Intrusion Detection](/BB-SC/MWLayer/Security/BB_Intrusion_Detection.md)
    - [Secure Onboard Communication](/BB-SC/MWLayer/Security/BB_Secure_Onboard_Communication.md)
    - [Security Event Manager](/BB-SC/MWLayer/Security/BB_Security_Event_Manager.md)
    - [Security Transport Layer](/BB-SC/MWLayer/Security/BB_Security_Transport_Layer.md)
  - Storage
    - [Vehicle Data Collector](/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Collector.md)
    - [Vehicle Data Persistency](/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Persistency.md)
    - [Vehicle Logging and Recording](/BB-SC/MWLayer/Storage/BB_Vehicle_Logging_and_Recording.md)
  - Time
    - [Time Service](/BB-SC/MWLayer/Time/BB_Time_Service.md)
  - Tools and Methods
    - [Key Management System](/BB-SC/MWLayer/Tools-and-Methods/BB_Key_Management_System.md)

- ##### [OSLayer](/BB-SC/OSLayer/OSLayer.md)

  - Time
    - [Automotive Edge Runtime](/BB-SC/OSLayer/Time/BB_Automotive_Edge_Runtime.md)

- ##### HWLayer

- #### [BB-EST](/BB-EST/BB-EST.md)

- #### [BB-SC-TC](/BB-SC-TC/BB-SC-TC.md)

  - Testing
    - [Shadowing](/BB-SC-TC/Testing/BB_Shadowing.md)
  - Virtualization
    - [Digital Twin](/BB-SC-TC/Virtualization/BB_Digital_Twin.md)

- #### [BB-MU](/BB-MU/BB-MU.md)

***

### Other

- #### [S-BB](/S-BB/S-BB.md)

- ##### [AppLayer](/S-BB/AppLayer/AppLayer.md)

  - [Standardization of Vehicle API](/S-BB/AppLayer/BB_Standardization_of_Vehicle_API.md)
  - [Standardized Architectural Patterns for Cross Platform Data Service Infrastructure](/S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure.md)
  - [Standardized Description of Data from Related Domains](/S-BB/AppLayer/BB_Standardized_Description_of_Data_from_Related_Domains.md)
  - [Standardized Procedure and Tooling for Combining Data from Different Domains](/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains.md)
  - [Standardized Procedure and Tooling for Modelling Data from Different Domains](/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains.md)

- ##### [MWLayer](/S-BB/MWLayer/MWLayer.md)

  - [SOA](/S-BB/MWLayer/BB_SOA.md)

  - [sSOA](/S-BB/MWLayer/BB_sSOA.md)

  - [Standardized Data Conversion Tools for Info-Knowledge Layers](/S-BB/MWLayer/BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers.md)
  - [Standardized Data Description for Vehicle Sensors, Attributes, and Actuators](/S-BB/MWLayer/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators.md)
  - [Standardized way for Reasoning on Data Streams](/S-BB/MWLayer/BB_Standardized_way_for_Reasoning_on_Data_Streams.md)
  
- ##### OSLayer

***

## Use Cases and Scenarios

While building blocks are useful as a starting point for specific software component design and implementation considerations, it is always desireable to be able to put building blocks into a larger context, asking the question: what actual use cases and scenarios should a system be able to cover? Such [use case scenarios are collected and maintained in a dedicated structure](/UseCases/Scenarios/).
