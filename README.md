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
- [BB-CSC-TC](/BB-CSC-TC/README.md)
- [BB-SC-TC](/BB-SC-TC/README.md)
    - Testing
- UseCases
    - Scenarios
- [BB-CEST](/BB-CEST/README.md)
    - Diagnostics
- [BB-MU](/BB-MU/README.md)
- [BB-CMU](/BB-CMU/README.md)
- [BB-SC](/BB-SC/README.md)
    - [OSLayer](/BB-SC/OSLayer/README.md)
        - Virtualization
            - [BB_Ankaios](/BB-SC/OSLayer/Virtualization/BB_Ankaios.md)
        - Time
    - [AppLayer](/BB-SC/AppLayer/README.md)
        - Communication
    - [HWLayer](/BB-SC/HWLayer/README.md)
        - HardwareAbstraction
            - Type-1-Hypervisor
                - XENProject
                    - [BB_XENHypervisor](/BB-SC/HWLayer/HardwareAbstraction/Type-1-Hypervisor/XENProject/BB_XENHypervisor.md)
    - [MWLayer](/BB-SC/MWLayer/README.md)
        - Power-Management
        - Communication
            - [BB_uProtocol](/BB-SC/MWLayer/Communication/BB_uProtocol.md)
            - [BB_KUKSA](/BB-SC/MWLayer/Communication/BB_KUKSA.md)
            - [BB_uServices](/BB-SC/MWLayer/Communication/BB_uServices.md)
            - [BB_eCAL](/BB-SC/MWLayer/Communication/BB_eCAL.md)
            - [BB_VISSR](/BB-SC/MWLayer/Communication/BB_VISSR.md)
            - [RTPS-Types](/BB-SC/MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - embeddedRTPS
                    - [BB_Constraint_DDS_embeddedRTPS](/BB-SC/MWLayer/Communication/RTPS-Types/embeddedRTPS/BB_Constraint_DDS_embeddedRTPS.md)
                - FastDDS
                    - [BB_FastDDS](/BB-SC/MWLayer/Communication/RTPS-Types/FastDDS/BB_FastDDS.md)
                - vSomeIP
                    - [BB_vSomeIP](/BB-SC/MWLayer/Communication/RTPS-Types/vSomeIP/BB_vSomeIP.md)
                - OpenDDS
                    - [BB_OpenDDS](/BB-SC/MWLayer/Communication/RTPS-Types/OpenDDS/BB_OpenDDS.md)
                - cycloneDDS
                    - [BB_cycloneDDS](/BB-SC/MWLayer/Communication/RTPS-Types/cycloneDDS/BB_cycloneDDS.md)
        - Tools-and-Methods
        - Platform-Health-Management
        - Diagnostics
        - Configuration
        - Storage
- [S-BB](/S-BB/README.md)
    - [OSLayer](/S-BB/OSLayer/README.md)
    - [AppLayer](/S-BB/AppLayer/README.md)
    - Generator
        - [BB_Commercial_Vehicle_Information_Specifications](/S-BB/Generator/BB_Commercial_Vehicle_Information_Specifications.md)
    - [HWLayer](/S-BB/HWLayer/README.md)
    - [MWLayer](/S-BB/MWLayer/README.md)
        - [BB_Data_Architecture_Terminology](/S-BB/MWLayer/BB_Data_Architecture_Terminology.md)
        - [BB_In_Car_Wallet_Payments_and_Orchestration](/S-BB/MWLayer/BB_In_Car_Wallet_Payments_and_Orchestration.md)
        - [BB_Unified_Push_Notification](/S-BB/MWLayer/BB_Unified_Push_Notification.md)
        - [BB_Private_Cross_OEM_Joint_Compute_for_EV_Charging](/S-BB/MWLayer/BB_Private_Cross_OEM_Joint_Compute_for_EV_Charging.md)
        - [BB_EV_Charging_Event_Data_Aggregation](/S-BB/MWLayer/BB_EV_Charging_Event_Data_Aggregation.md)
        - [BB_Common_Vehicle_Capabilities](/S-BB/MWLayer/BB_Common_Vehicle_Capabilities.md)
        - [BB_HIM](/S-BB/MWLayer/BB_HIM.md)
        - [BB_VSS](/S-BB/MWLayer/BB_VSS.md)
        - Communication
            - [BB_VISS](/S-BB/MWLayer/Communication/BB_VISS.md)
- [BB-EST](/BB-EST/README.md)
    - Monitoring-and-Diagnostics
    - Requirements
    - Deployment
    - Testing
        - [BB_Central_Data_Service_Playground](/BB-EST/Testing/BB_Central_Data_Service_Playground.md)
        - [BB_OpenXilEnv](/BB-EST/Testing/BB_OpenXilEnv.md)
        - [BB_Autowrx](/BB-EST/Testing/BB_Autowrx.md)
    - Implementation
    - Generator
        - [BB_IFEX](/BB-EST/Generator/BB_IFEX.md)
    - Build-and-Implementation
        - [BB_VELOCITAS](/BB-EST/Build-and-Implementation/BB_VELOCITAS.md)
    - Lifecycle-Management
        - [BB_LEDA](/BB-EST/Lifecycle-Management/BB_LEDA.md)
    - Design
- [BB-CSC](/BB-CSC/README.md)

***

## Navigation for Work In Progress BBs
- [BB-CSC-TC](/WorkInProgress/BB-CSC-TC/README.md)
- [BB-SC-TC](/WorkInProgress/BB-SC-TC/README.md)
    - Testing
        - [BB_Shadowing](/WorkInProgress/BB-SC-TC/Testing/BB_Shadowing.md)
- UseCases
    - Scenarios
        - [BB_Remote_Vehicle_Interaction](/WorkInProgress/UseCases/Scenarios/BB_Remote_Vehicle_Interaction.md)
        - [BB_Remote_driving](/WorkInProgress/UseCases/Scenarios/BB_Remote_driving.md)
        - [BB_Central_traffic_manager](/WorkInProgress/UseCases/Scenarios/BB_Central_traffic_manager.md)
        - [BB_Vehicle_FleetData](/WorkInProgress/UseCases/Scenarios/BB_Vehicle_FleetData.md)
        - [BB_Location_based_services](/WorkInProgress/UseCases/Scenarios/BB_Location_based_services.md)
        - [BB_Offloading_tasks_to_cloud_resources](/WorkInProgress/UseCases/Scenarios/BB_Offloading_tasks_to_cloud_resources.md)
        - [BB_Central_database_of_vehicle_failures_and_incidents](/WorkInProgress/UseCases/Scenarios/BB_Central_database_of_vehicle_failures_and_incidents.md)
        - [BB_Universal_Service_Mesh](/WorkInProgress/UseCases/Scenarios/BB_Universal_Service_Mesh.md)
        - [BB_Collect_street_data](/WorkInProgress/UseCases/Scenarios/BB_Collect_street_data.md)
- [BB-CEST](/WorkInProgress/BB-CEST/README.md)
    - [BB_Car_Simulator](/WorkInProgress/BB-CEST/BB_Car_Simulator.md)
    - Diagnostics
        - [BB_RemotiveCloud](/WorkInProgress/BB-CEST/Diagnostics/BB_RemotiveCloud.md)
- [BB-MU](/WorkInProgress/BB-MU/README.md)
- [BB-CMU](/WorkInProgress/BB-CMU/README.md)
    - [BB_Digital_Twin_proxy_in_cloud](/WorkInProgress/BB-CMU/BB_Digital_Twin_proxy_in_cloud.md)
- [BB-SC](/WorkInProgress/BB-SC/README.md)
    - [OSLayer](/WorkInProgress/BB-SC/OSLayer/README.md)
        - Container
            - [BB_Container_Abstraction](/WorkInProgress/BB-SC/OSLayer/Container/BB_Container_Abstraction.md)
        - Virtualization
            - [BB_SR_VOSS](/WorkInProgress/BB-SC/OSLayer/Virtualization/BB_SR_VOSS.md)
        - Time
            - [BB_Automotive_Edge_Runtime](/WorkInProgress/BB-SC/OSLayer/Time/BB_Automotive_Edge_Runtime.md)
    - [AppLayer](/WorkInProgress/BB-SC/AppLayer/README.md)
        - API
            - [BB_Automotive_API_Framework](/WorkInProgress/BB-SC/AppLayer/API/BB_Automotive_API_Framework.md)
        - Communication
            - [BB_AOSP_Push_Notification_Service](/WorkInProgress/BB-SC/AppLayer/Communication/BB_AOSP_Push_Notification_Service.md)
        - Control
            - [BB_ADAAA](/WorkInProgress/BB-SC/AppLayer/Control/BB_ADAAA.md)
    - [HWLayer](/WorkInProgress/BB-SC/HWLayer/README.md)
    - [MWLayer](/WorkInProgress/BB-SC/MWLayer/README.md)
        - Power-Management
            - [BB_Power_Management_Coordination](/WorkInProgress/BB-SC/MWLayer/Power-Management/BB_Power_Management_Coordination.md)
        - Communication
            - [BB_Communication_Protocol_Abstraction](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Communication_Protocol_Abstraction.md)
            - [BB_TSN](/WorkInProgress/BB-SC/MWLayer/Communication/BB_TSN.md)
            - [BB_Network_Management](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Network_Management.md)
            - [BB_Smart_Charging_Communication](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Smart_Charging_Communication.md)
            - [BB_Communication_Server_S2S](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Communication_Server_S2S.md)
            - [BB_SecOS](/WorkInProgress/BB-SC/MWLayer/Communication/BB_SecOS.md)
            - [BB_Standard_Android_VHAL](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Standard_Android_VHAL.md)
            - [BB_Onboard_TSN_configuration](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Onboard_TSN_configuration.md)
            - [BB_Gateway_Mirroring](/WorkInProgress/BB-SC/MWLayer/Communication/BB_Gateway_Mirroring.md)
            - [RTPS-Types](/WorkInProgress/BB-SC/MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - embeddedRTPS
                - FastDDS
                - OpenDDS
                - cycloneDDS
        - Tools-and-Methods
            - [BB_Key_Management_System](/WorkInProgress/BB-SC/MWLayer/Tools-and-Methods/BB_Key_Management_System.md)
        - Platform-Health-Management
            - [BB_Watchdog](/WorkInProgress/BB-SC/MWLayer/Platform-Health-Management/BB_Watchdog.md)
            - [BB_Distributed_Health_Management](/WorkInProgress/BB-SC/MWLayer/Platform-Health-Management/BB_Distributed_Health_Management.md)
        - Diagnostics
            - [BB_SOVD_Reference_implementation](/WorkInProgress/BB-SC/MWLayer/Diagnostics/BB_SOVD_Reference_implementation.md)
            - [BB_Policy_Manager](/WorkInProgress/BB-SC/MWLayer/Diagnostics/BB_Policy_Manager.md)
        - Time
            - [BB_Time_Service](/WorkInProgress/BB-SC/MWLayer/Time/BB_Time_Service.md)
            - [BB_Onboard_TSN_scheduling_Tool](/WorkInProgress/BB-SC/MWLayer/Time/BB_Onboard_TSN_scheduling_Tool.md)
        - Security
            - [BB_Internet_Protocol_Security](/WorkInProgress/BB-SC/MWLayer/Security/BB_Internet_Protocol_Security.md)
            - [BB_Security_Event_Manager](/WorkInProgress/BB-SC/MWLayer/Security/BB_Security_Event_Manager.md)
            - [BB_Anomaly_Detection](/WorkInProgress/BB-SC/MWLayer/Security/BB_Anomaly_Detection.md)
            - [BB_Intrusion_Detection](/WorkInProgress/BB-SC/MWLayer/Security/BB_Intrusion_Detection.md)
            - [BB_Safety_Gateway](/WorkInProgress/BB-SC/MWLayer/Security/BB_Safety_Gateway.md)
            - [BB_Security_and_Safety_API](/WorkInProgress/BB-SC/MWLayer/Security/BB_Security_and_Safety_API.md)
            - [BB_Secure_Onboard_Communication](/WorkInProgress/BB-SC/MWLayer/Security/BB_Secure_Onboard_Communication.md)
            - [BB_Crypto_Service_Manager](/WorkInProgress/BB-SC/MWLayer/Security/BB_Crypto_Service_Manager.md)
            - [BB_Security_Transport_Layer](/WorkInProgress/BB-SC/MWLayer/Security/BB_Security_Transport_Layer.md)
        - Runtime
            - [BB_Diagnostic_Services_Applications](/WorkInProgress/BB-SC/MWLayer/Runtime/BB_Diagnostic_Services_Applications.md)
            - [BB_State_Management](/WorkInProgress/BB-SC/MWLayer/Runtime/BB_State_Management.md)
        - Configuration
            - [BB_Local_Update_Manager](/WorkInProgress/BB-SC/MWLayer/Configuration/BB_Local_Update_Manager.md)
            - [BB_OTA_Master](/WorkInProgress/BB-SC/MWLayer/Configuration/BB_OTA_Master.md)
        - Storage
            - [BB_Vehicle_Data_Collector](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Collector.md)
            - [BB_Vehicle_Logging_and_Recording](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Logging_and_Recording.md)
            - [BB_Vehicle_Data_Persistency](/WorkInProgress/BB-SC/MWLayer/Storage/BB_Vehicle_Data_Persistency.md)
- [S-BB](/WorkInProgress/S-BB/README.md)
    - [OSLayer](/WorkInProgress/S-BB/OSLayer/README.md)
    - [AppLayer](/WorkInProgress/S-BB/AppLayer/README.md)
        - [BB_Standardized_Description_of_Data_from_Related_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Description_of_Data_from_Related_Domains.md)
        - [BB_Standardization_of_Vehicle_API](/WorkInProgress/S-BB/AppLayer/BB_Standardization_of_Vehicle_API.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains.md)
        - [BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains](/WorkInProgress/S-BB/AppLayer/BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains.md)
        - [BB_Fleet_Management_System](/WorkInProgress/S-BB/AppLayer/BB_Fleet_Management_System.md)
        - API
            - [BB_VAPI_Stack_Demonstrator](/WorkInProgress/S-BB/AppLayer/API/BB_VAPI_Stack_Demonstrator.md)
    - [HWLayer](/WorkInProgress/S-BB/HWLayer/README.md)
    - [MWLayer](/WorkInProgress/S-BB/MWLayer/README.md)
        - [BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers](/WorkInProgress/S-BB/MWLayer/BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers.md)
        - [BB_Standardized_HD_maps_formats](/WorkInProgress/S-BB/MWLayer/BB_Standardized_HD_maps_formats.md)
        - [BB_Standardized_data_formats_for_digital_twins](/WorkInProgress/S-BB/MWLayer/BB_Standardized_data_formats_for_digital_twins.md)
        - [BB_Standardized_authentication_of_vehicle_users](/WorkInProgress/S-BB/MWLayer/BB_Standardized_authentication_of_vehicle_users.md)
        - [BB_SOA](/WorkInProgress/S-BB/MWLayer/BB_SOA.md)
        - [BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles](/WorkInProgress/S-BB/MWLayer/BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles.md)
        - [BB_Legally_binding_formats_for_data_exchange](/WorkInProgress/S-BB/MWLayer/BB_Legally_binding_formats_for_data_exchange.md)
        - [BB_sSOA](/WorkInProgress/S-BB/MWLayer/BB_sSOA.md)
        - [BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators](/WorkInProgress/S-BB/MWLayer/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators.md)
        - [BB_Standardized_way_for_Reasoning_on_Data_Streams](/WorkInProgress/S-BB/MWLayer/BB_Standardized_way_for_Reasoning_on_Data_Streams.md)
- [BB-EST](/WorkInProgress/BB-EST/README.md)
    - Monitoring-and-Diagnostics
    - Requirements
        - [BB_DocAsCode](/WorkInProgress/BB-EST/Requirements/BB_DocAsCode.md)
    - Deployment
    - Testing
        - [BB_OpenDUT](/WorkInProgress/BB-EST/Testing/BB_OpenDUT.md)
    - Implementation
    - Build-and-Implementation
    - Lifecycle-Management
    - Design
    - Configuration-and-Calibration
        - [BB_Offboard_Config_Tool_for_TSN](/WorkInProgress/BB-EST/Configuration-and-Calibration/BB_Offboard_Config_Tool_for_TSN.md)
- [BB-CSC](/WorkInProgress/BB-CSC/README.md)
    - [BB_Orchestration_support_for_energy_and_mobility_providers](/WorkInProgress/BB-CSC/BB_Orchestration_support_for_energy_and_mobility_providers.md)
    - [BB_Driver_monitor](/WorkInProgress/BB-CSC/BB_Driver_monitor.md)
    - [BB_Config_and_settngs_collector](/WorkInProgress/BB-CSC/BB_Config_and_settngs_collector.md)
    - [BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle](/WorkInProgress/BB-CSC/BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle.md)
    - [BB_End_to_end_security_for_C2X](/WorkInProgress/BB-CSC/BB_End_to_end_security_for_C2X.md)
    - [BB_Data_spaces](/WorkInProgress/BB-CSC/BB_Data_spaces.md)
    - [BB_Secure_and_privacy_aware_voice_assistant](/WorkInProgress/BB-CSC/BB_Secure_and_privacy_aware_voice_assistant.md)
    - [BB_Driver_authentication](/WorkInProgress/BB-CSC/BB_Driver_authentication.md)
    - [BB_Extended_accident_data_recorder](/WorkInProgress/BB-CSC/BB_Extended_accident_data_recorder.md)
    - [BB_App_and_services_store](/WorkInProgress/BB-CSC/BB_App_and_services_store.md)
    - [BB_Cloud_container_and_OS](/WorkInProgress/BB-CSC/BB_Cloud_container_and_OS.md)
    - [BB_Vehicle_monitor](/WorkInProgress/BB-CSC/BB_Vehicle_monitor.md)
    - [BB_Vehicle_data_streaming](/WorkInProgress/BB-CSC/BB_Vehicle_data_streaming.md)
    - [BB_Data_manager_ensuring_compliance_with_regulation](/WorkInProgress/BB-CSC/BB_Data_manager_ensuring_compliance_with_regulation.md)
    - [BB_Active_diagnostics_and_repair_services](/WorkInProgress/BB-CSC/BB_Active_diagnostics_and_repair_services.md)

***
generated using [README Generator](/other/scripts/readme_generator.py)