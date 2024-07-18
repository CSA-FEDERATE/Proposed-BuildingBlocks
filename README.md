# Proposed-BuildingBlocks

Landing page for all proposed building blocks; use the README to navigate through all the Building Blocks.

## Implementation of new BBs

- New BB should be implemented using the [BB_Template](/utils/BB_Template.md).  
- If you create a folder without content, put a .gitkeep into the folder.  
- Whitespaces in Folders: "-" (Dash)  
- Whitespaces in Files: "_" (Underscore)  

Abbreviations have to be added to the [abbreviation list](/utils/Abbreviations.md).

When a new BB or folder is added to the libary, the structure in the README can be updated using 
the [README Generator](/scripts/readme_generator.py). To adjust contents of the README other than 
the Navigation, change them in the [README_base file](/utils/README_base.md). The Navigation will 
be inserted at the "## Navigation" flag in the [README_base file](/utils/README_base.md).

> [!CAUTION]
> If you don't follow the structure correctly the automatic structure generation will not work!

### Automatic README generation

> [!Warning]
> AUTOMATED README GENERATION VIA ACTIONS DOES NOT WORK YET! HAS TO BE DONE MANUALLY!

Run the [README Generator](/scripts/readme_generator.py) script to update the README file


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
- library
    - Cloud
        - [BB-CEST](/library/Cloud/BB-CEST/BB-CEST.md)
            - _Not_Clustered
                - [BB_Car_Simulator](/library/Cloud/BB-CEST/_Not_Clustered/BB_Car_Simulator.md)
        - [BB-CMU](/library/Cloud/BB-CMU/BB-CMU.md)
        - [BB-CSC](/library/Cloud/BB-CSC/BB-CSC.md)
        - [BB-CSC-TC](/library/Cloud/BB-CSC-TC/BB-CSC-TC.md)
    - In-Vehicle
        - [BB-EST](/library/In-Vehicle/BB-EST/BB-EST.md)
        - [BB-MU](/library/In-Vehicle/BB-MU/BB-MU.md)
        - [BB-SC](/library/In-Vehicle/BB-SC/BB-SC.md)
            - [AppLayer](/library/In-Vehicle/BB-SC/AppLayer/AppLayer.md)
                - Communication
                    - [BB_AOSP_Push_Notification_Service](/library/In-Vehicle/BB-SC/AppLayer/Communication/BB_AOSP_Push_Notification_Service.md)
            - HWLayer
            - [MWLayer](/library/In-Vehicle/BB-SC/MWLayer/MWLayer.md)
                - Communication
                    - [BB_Communication_Server_S2S](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_Communication_Server_S2S.md)
                    - [BB_Gateway_Mirroring](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_Gateway_Mirroring.md)
                    - [BB_Network_Management](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_Network_Management.md)
                    - [BB_SecOS](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_SecOS.md)
                    - [BB_Smart_Charging_Communication](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_Smart_Charging_Communication.md)
                    - [BB_Standard_Android_VHAL](/library/In-Vehicle/BB-SC/MWLayer/Communication/BB_Standard_Android_VHAL.md)
                - Configuration
                    - [BB_Local_Update_Manager](/library/In-Vehicle/BB-SC/MWLayer/Configuration/BB_Local_Update_Manager.md)
                    - [BB_OTA_Master](/library/In-Vehicle/BB-SC/MWLayer/Configuration/BB_OTA_Master.md)
                - Diagnostics
                    - [BB_Policy_Manager](/library/In-Vehicle/BB-SC/MWLayer/Diagnostics/BB_Policy_Manager.md)
                - Platform-Health-Management
                    - [BB_Distributed_Health_Management](/library/In-Vehicle/BB-SC/MWLayer/Platform-Health-Management/BB_Distributed_Health_Management.md)
                    - [BB_Watchdog](/library/In-Vehicle/BB-SC/MWLayer/Platform-Health-Management/BB_Watchdog.md)
                - Power-Management
                    - [BB_Power_Management_Coordination](/library/In-Vehicle/BB-SC/MWLayer/Power-Management/BB_Power_Management_Coordination.md)
                - Runtime
                    - [BB_Diagnostic_Services_Applications](/library/In-Vehicle/BB-SC/MWLayer/Runtime/BB_Diagnostic_Services_Applications.md)
                    - [BB_State_Management](/library/In-Vehicle/BB-SC/MWLayer/Runtime/BB_State_Management.md)
                - Security
                    - [BB_Crypto_Service_Manager](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Crypto_Service_Manager.md)
                    - [BB_Internet_Protocol_Security](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Internet_Protocol_Security.md)
                    - [BB_Intrusion_Detection](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Intrusion_Detection.md)
                    - [BB_Secure_Onboard_Communication](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Secure_Onboard_Communication.md)
                    - [BB_Security_Event_Manager](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Security_Event_Manager.md)
                    - [BB_Security_Transport_Layer](/library/In-Vehicle/BB-SC/MWLayer/Security/BB_Security_Transport_Layer.md)
                - Storage
                    - [BB_Vehicle_Data_Collector](/library/In-Vehicle/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Collector.md)
                    - [BB_Vehicle_Data_Persistency](/library/In-Vehicle/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Persistency.md)
                    - [BB_Vehicle_Logging_and_Recording](/library/In-Vehicle/BB-SC/MWLayer/Storage/BB_Vehicle_Logging_and_Recording.md)
                - Time
                    - [BB_Time_Service](/library/In-Vehicle/BB-SC/MWLayer/Time/BB_Time_Service.md)
                - Tools-and-Methods
                    - [BB_Key_Management_System](/library/In-Vehicle/BB-SC/MWLayer/Tools-and-Methods/BB_Key_Management_System.md)
            - [OSLayer](/library/In-Vehicle/BB-SC/OSLayer/OSLayer.md)
                - Time
                    - [BB_Automotive_Edge_Runtime](/library/In-Vehicle/BB-SC/OSLayer/Time/BB_Automotive_Edge_Runtime.md)
        - [BB-SC-TC](/library/In-Vehicle/BB-SC-TC/BB-SC-TC.md)
            - Testing
                - [BB_Shadowing](/library/In-Vehicle/BB-SC-TC/Testing/BB_Shadowing.md)
            - Virtualization
                - [BB_Digital_Twin](/library/In-Vehicle/BB-SC-TC/Virtualization/BB_Digital_Twin.md)
    - [S-BB](/library/S-BB/S-BB.md)
        - [AppLayer](/library/S-BB/AppLayer/AppLayer.md)
            - [BB_Standardization_of_Vehicle_API](/library/S-BB/AppLayer/BB_Standardization_of_Vehicle_API.md)
            - [BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure](/library/S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure.md)
            - [BB_Standardized_Description_of_Data_from_Related_Domains](/library/S-BB/AppLayer/BB_Standardized_Description_of_Data_from_Related_Domains.md)
            - [BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains](/library/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains.md)
            - [BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains](/library/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains.md)
        - HWLayer
        - [MWLayer](/library/S-BB/MWLayer/MWLayer.md)
            - No_cluster
                - [BB_SOA](/library/S-BB/MWLayer/No_cluster/BB_SOA.md)
                - [BB_sSOA](/library/S-BB/MWLayer/No_cluster/BB_sSOA.md)
                - [BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers](/library/S-BB/MWLayer/No_cluster/BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers.md)
                - [BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators](/library/S-BB/MWLayer/No_cluster/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators.md)
                - [BB_Standardized_way_for_Reasoning_on_Data_Streams](/library/S-BB/MWLayer/No_cluster/BB_Standardized_way_for_Reasoning_on_Data_Streams.md)
        - OSLayer
    - unsorted_BB
        - Daniel
            - [BB_Template_filled_FleetData_WP3](/library/unsorted_BB/Daniel/BB_Template_filled_FleetData_WP3.md)
            - [BB_Template_filled_RemoteVehicleInteraction_WP3](/library/unsorted_BB/Daniel/BB_Template_filled_RemoteVehicleInteraction_WP3.md)
            - [BB_Template_filled_ServiceMesh_WP3](/library/unsorted_BB/Daniel/BB_Template_filled_ServiceMesh_WP3.md)
***
generated using [README Generator](/scripts/readme_generator.py)