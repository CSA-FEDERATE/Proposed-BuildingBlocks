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

BBs get collected in the [WorkInProgress folder](/WorkInProgress/). As soon as they have a name, a description, a state and a specified known implementation, they are moved up, to the root. The BBs that were moved up, get deleted in the WorkInProgress folder.

![Process description](/other/figures/Process_description.PNG)



## Navigation
- [BB-CEST](/BB-CEST/README.md)
    - Diagnostics
- [BB-CMU](/BB-CMU/README.md)
- [BB-CSC](/BB-CSC/README.md)
- [BB-CSC-TC](/BB-CSC-TC/README.md)
- [BB-EST](/BB-EST/README.md)
    - Build-and-Implementation
    - Deployment
    - Design
    - Implementation
    - Lifecycle-Management
    - Monitoring-and-Diagnostics
    - Requirements
    - Testing
- [BB-MU](/BB-MU/README.md)
- [BB-SC](/BB-SC/README.md)
    - [AppLayer](/BB-SC/AppLayer/README.md)
        - Communication
    - [HWLayer](/BB-SC/HWLayer/README.md)
    - [MWLayer](/BB-SC/MWLayer/README.md)
        - Communication
            - [RTPS-Types](/BB-SC/MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - cycloneDDS
                - embeddedRTPS
                - FastDDS
                - OpenDDS
        - Configuration
        - Diagnostics
        - Platform-Health-Management
        - Power-Management
        - Security
        - Storage
        - Time
        - Tools-and-Methods
    - [OSLayer](/BB-SC/OSLayer/README.md)
        - Time
- [BB-SC-TC](/BB-SC-TC/README.md)
    - Testing
- [S-BB](/S-BB/README.md)
    - [AppLayer](/S-BB/AppLayer/README.md)
    - [HWLayer](/S-BB/HWLayer/README.md)
    - [MWLayer](/S-BB/MWLayer/README.md)
    - [OSLayer](/S-BB/OSLayer/README.md)
- UseCases
    - Scenarios

***

## Navigation for Work In Progress BBs
- [BB-CEST](/WorkInProgress/BB-CEST/README.md)
    - [BB_Car_Simulator](/WorkInProgress/BB-CEST/BB_Car_Simulator.md)
    - Diagnostics
        - [BB_RemotiveCloud](/WorkInProgress/BB-CEST/Diagnostics/BB_RemotiveCloud.md)
- [BB-CMU](/WorkInProgress/BB-CMU/README.md)
    - [BB_Digital_Twin_proxy_in_cloud](/WorkInProgress/BB-CMU/BB_Digital_Twin_proxy_in_cloud.md)
- [BB-CSC](/WorkInProgress/BB-CSC/README.md)
    - [BB_Active_diagnostics_and_repair_services](/WorkInProgress/BB-CSC/BB_Active_diagnostics_and_repair_services.md)
    - [BB_App_and_services_store](/WorkInProgress/BB-CSC/BB_App_and_services_store.md)
    - [BB_Cloud_container_and_OS](/WorkInProgress/BB-CSC/BB_Cloud_container_and_OS.md)
    - [BB_Config_and_settngs_collector](/WorkInProgress/BB-CSC/BB_Config_and_settngs_collector.md)
    - [BB_Data_manager_ensuring_compliance_with_regulation](/WorkInProgress/BB-CSC/BB_Data_manager_ensuring_compliance_with_regulation.md)
    - [BB_Data_spaces](/WorkInProgress/BB-CSC/BB_Data_spaces.md)
    - [BB_Driver_authentication](/WorkInProgress/BB-CSC/BB_Driver_authentication.md)
    - [BB_Driver_monitor](/WorkInProgress/BB-CSC/BB_Driver_monitor.md)
    - [BB_End_to_end_security_for_C2X](/WorkInProgress/BB-CSC/BB_End_to_end_security_for_C2X.md)
    - [BB_Extended_accident_data_recorder](/WorkInProgress/BB-CSC/BB_Extended_accident_data_recorder.md)
    - [BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle](/WorkInProgress/BB-CSC/BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle.md)
    - [BB_Orchestration_support_for_energy_and_mobility_providers](/WorkInProgress/BB-CSC/BB_Orchestration_support_for_energy_and_mobility_providers.md)
    - [BB_Secure_and_privacy_aware_voice_assistant](/WorkInProgress/BB-CSC/BB_Secure_and_privacy_aware_voice_assistant.md)
    - [BB_Vehicle_data_streaming](/WorkInProgress/BB-CSC/BB_Vehicle_data_streaming.md)
    - [BB_Vehicle_monitor](/WorkInProgress/BB-CSC/BB_Vehicle_monitor.md)
- [BB-CSC-TC](/WorkInProgress/BB-CSC-TC/README.md)
- [BB-EST](/WorkInProgress/BB-EST/README.md)
    - Build-and-Implementation
    - Deployment
    - Design
    - Implementation
    - Lifecycle-Management
    - Monitoring-and-Diagnostics
    - Requirements
        - [BB_DocAsCode](/WorkInProgress/BB-EST/Requirements/BB_DocAsCode.md)
    - Testing
        - [BB_OpenDUT](/WorkInProgress/BB-EST/Testing/BB_OpenDUT.md)
- [BB-MU](/WorkInProgress/BB-MU/README.md)
- [BB-SC](/WorkInProgress/BB-SC/README.md)
    - [AppLayer](/WorkInProgress/BB-SC/AppLayer/README.md)
        - Communication
            - [BB_AOSP_Push_Notification_Service](/WorkInProgress/BB-SC/AppLayer/Communication/BB_AOSP_Push_Notification_Service.md)
    - [HWLayer](/WorkInProgress/BB-SC/HWLayer/README.md)
    - [MWLayer](/WorkInProgress/BB-SC/MWLayer/README.md)
        - Communication
            - [BB_Communication_Server_S2S](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Communication_Server_S2S.md)
            - [BB_Gateway_Mirroring](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Gateway_Mirroring.md)
            - [BB_Network_Management](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Network_Management.md)
            - [BB_SecOS](/WorkInProgress/BB-SC/MWLayer/Communication/BB_SecOS.md)
            - [BB_Smart_Charging_Communication](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Smart_Charging_Communication.md)
            - [BB_SomeIP](/WorkInProgress/BB-SC/MWLayer/Communication/BB_SomeIP.md)
            - [BB_Standard_Android_VHAL](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Standard_Android_VHAL.md)
            - [RTPS-Types](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - cycloneDDS
                    - [BB_cycloneDDS](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/cycloneDDS/BB_cycloneDDS.md)
                - embeddedRTPS
                    - [BB_Constraint_DDS_embeddedRTPS](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/embeddedRTPS/BB_Constraint_DDS_embeddedRTPS.md)
                - FastDDS
                    - [BB_FastDDS](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/FastDDS/BB_FastDDS.md)
                - OpenDDS
                    - [BB_OpenDDS](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/OpenDDS/BB_OpenDDS.md)
        - Configuration
            - [BB_Local_Update_Manager](/WorkInProgress/BB-SC/MWLayer/Configuration/BB_Local_Update_Manager.md)
            - [BB_OTA_Master](/WorkInProgress/BB-SC/MWLayer/Configuration/BB_OTA_Master.md)
        - Diagnostics
            - [BB_Policy_Manager](/WorkInProgress/BB-SC/MWLayer/Diagnostics/BB_Policy_Manager.md)
        - Platform-Health-Management
            - [BB_Distributed_Health_Management](/WorkInProgress/BB-SC/MWLayer/Platform-Health-Management/BB_Distributed_Health_Management.md)
            - [BB_Watchdog](/WorkInProgress/BB-SC/MWLayer/Platform-Health-Management/BB_Watchdog.md)
        - Power-Management
            - [BB_Power_Management_Coordination](/WorkInProgress/BB-SC/MWLayer/Power-Management/BB_Power_Management_Coordination.md)
        - Runtime
            - [BB_Diagnostic_Services_Applications](/WorkInProgress/BB-SC/MWLayer/Runtime/BB_Diagnostic_Services_Applications.md)
            - [BB_State_Management](/WorkInProgress/BB-SC/MWLayer/Runtime/BB_State_Management.md)
        - Security
            - [BB_Crypto_Service_Manager](/WorkInProgress/BB-SC/MWLayer/Security/BB_Crypto_Service_Manager.md)
            - [BB_Internet_Protocol_Security](/WorkInProgress/BB-SC/MWLayer/Security/BB_Internet_Protocol_Security.md)
            - [BB_Intrusion_Detection](/WorkInProgress/BB-SC/MWLayer/Security/BB_Intrusion_Detection.md)
            - [BB_Secure_Onboard_Communication](/WorkInProgress/BB-SC/MWLayer/Security/BB_Secure_Onboard_Communication.md)
            - [BB_Security_Event_Manager](/WorkInProgress/BB-SC/MWLayer/Security/BB_Security_Event_Manager.md)
            - [BB_Security_Transport_Layer](/WorkInProgress/BB-SC/MWLayer/Security/BB_Security_Transport_Layer.md)
        - Storage
            - [BB_Vehicle_Data_Collector](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Collector.md)
            - [BB_Vehicle_Data_Persistency](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Persistency.md)
            - [BB_Vehicle_Logging_and_Recording](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Logging_and_Recording.md)
        - Time
            - [BB_Time_Service](/WorkInProgress/BB-SC/MWLayer/Time/BB_Time_Service.md)
        - Tools-and-Methods
            - [BB_Key_Management_System](/WorkInProgress/BB-SC/MWLayer/Tools-and-Methods/BB_Key_Management_System.md)
    - [OSLayer](/WorkInProgress/BB-SC/OSLayer/README.md)
        - Time
            - [BB_Automotive_Edge_Runtime](/WorkInProgress/BB-SC/OSLayer/Time/BB_Automotive_Edge_Runtime.md)
- [BB-SC-TC](/WorkInProgress/BB-SC-TC/README.md)
    - Testing
        - [BB_Shadowing](/WorkInProgress/BB-SC-TC/Testing/BB_Shadowing.md)
- [S-BB](/WorkInProgress/S-BB/README.md)
    - [AppLayer](/WorkInProgress/S-BB/AppLayer/README.md)
        - [BB_Standardization_of_Vehicle_API](/WorkInProgress/S-BB/AppLayer/BB_Standardization_of_Vehicle_API.md)
        - [BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure.md)
        - [BB_Standardized_Description_of_Data_from_Related_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Description_of_Data_from_Related_Domains.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains.md)
    - [HWLayer](/WorkInProgress/S-BB/HWLayer/README.md)
    - [MWLayer](/WorkInProgress/S-BB/MWLayer/README.md)
        - [BB_Legally_binding_formats_for_data_exchange](/WorkInProgress/S-BB/MWLayer/BB_Legally_binding_formats_for_data_exchange.md)
        - [BB_SOA](/WorkInProgress/S-BB/MWLayer/BB_SOA.md)
        - [BB_sSOA](/WorkInProgress/S-BB/MWLayer/BB_sSOA.md)
        - [BB_Standardized_authentication_of_vehicle_users](/WorkInProgress/S-BB/MWLayer/BB_Standardized_authentication_of_vehicle_users.md)
        - [BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles](/WorkInProgress/S-BB/MWLayer/BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles.md)
        - [BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers](/WorkInProgress/S-BB/MWLayer/BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers.md)
        - [BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators](/WorkInProgress/S-BB/MWLayer/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators.md)
        - [BB_Standardized_data_formats_for_digital_twins](/WorkInProgress/S-BB/MWLayer/BB_Standardized_data_formats_for_digital_twins.md)
        - [BB_Standardized_HD_maps_formats](/WorkInProgress/S-BB/MWLayer/BB_Standardized_HD_maps_formats.md)
        - [BB_Standardized_way_for_Reasoning_on_Data_Streams](/WorkInProgress/S-BB/MWLayer/BB_Standardized_way_for_Reasoning_on_Data_Streams.md)
    - [OSLayer](/WorkInProgress/S-BB/OSLayer/README.md)
- UseCases
    - Scenarios
        - [BB_Central_database_of_vehicle_failures_and_incidents](/WorkInProgress/UseCases/Scenarios/BB_Central_database_of_vehicle_failures_and_incidents.md)
        - [BB_Central_traffic_manager](/WorkInProgress/UseCases/Scenarios/BB_Central_traffic_manager.md)
        - [BB_Collect_street_data](/WorkInProgress/UseCases/Scenarios/BB_Collect_street_data.md)
        - [BB_Location_based_services](/WorkInProgress/UseCases/Scenarios/BB_Location_based_services.md)
        - [BB_Offloading_tasks_to_cloud_resources](/WorkInProgress/UseCases/Scenarios/BB_Offloading_tasks_to_cloud_resources.md)
        - [BB_Remote_driving](/WorkInProgress/UseCases/Scenarios/BB_Remote_driving.md)
        - [BB_Remote_Vehicle_Interaction](/WorkInProgress/UseCases/Scenarios/BB_Remote_Vehicle_Interaction.md)
        - [BB_Universal_Service_Mesh](/WorkInProgress/UseCases/Scenarios/BB_Universal_Service_Mesh.md)
        - [BB_Vehicle_FleetData](/WorkInProgress/UseCases/Scenarios/BB_Vehicle_FleetData.md)

***
generated using [README Generator](/other/scripts/readme_generator.py)