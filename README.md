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
- [BB-EST](/BB-EST/README.md)
    - Implementation
    - Testing
        - [BB_Autowrx](/BB-EST/Testing/BB_Autowrx.md)
        - [BB_Central_Data_Service_Playground](/BB-EST/Testing/BB_Central_Data_Service_Playground.md)
        - [BB_OpenXilEnv](/BB-EST/Testing/BB_OpenXilEnv.md)
    - Generator
        - [BB_IFEX](/BB-EST/Generator/BB_IFEX.md)
    - Requirements
    - Deployment
    - Lifecycle-Management
        - [BB_LEDA](/BB-EST/Lifecycle-Management/BB_LEDA.md)
    - Build-and-Implementation
        - [BB_VELOCITAS](/BB-EST/Build-and-Implementation/BB_VELOCITAS.md)
        - Embedded-Linux
            - [BB_YoctoProject](/BB-EST/Build-and-Implementation/Embedded-Linux/BB_YoctoProject.md)
    - Design
        - [BB_SKyBT](/BB-EST/Design/BB_SKyBT.md)
    - Monitoring-and-Diagnostics
- [BB-CSC](/BB-CSC/README.md)
- [BB-MU](/BB-MU/README.md)
- [BB-SC-TC](/BB-SC-TC/README.md)
    - Testing
- UseCases
    - Scenarios
- [BB-SC](/BB-SC/README.md)
    - [2a-OSLayer](/BB-SC/2a-OSLayer/README.md)
        - Linux
            - [BB_AutomotiveGradeLinux](/BB-SC/2a-OSLayer/Linux/BB_AutomotiveGradeLinux.md)
        - Virtualization
            - [BB_Ankaios](/BB-SC/2a-OSLayer/Virtualization/BB_Ankaios.md)
        - Time
    - [1-HWLayer](/BB-SC/1-HWLayer/README.md)
        - HardwareAbstraction
            - Type-1-Hypervisor
                - XENProject
                    - [BB_XENHypervisor](/BB-SC/1-HWLayer/HardwareAbstraction/Type-1-Hypervisor/XENProject/BB_XENHypervisor.md)
    - [3-AppLayer](/BB-SC/3-AppLayer/README.md)
        - Communication
    - [2b-MWLayer](/BB-SC/2b-MWLayer/README.md)
        - Platform-Health-Management
        - Storage
        - Diagnostics
        - Power-Management
        - Tools-and-Methods
        - Configuration
        - Communication
            - [BB_KUKSA](/BB-SC/2b-MWLayer/Communication/BB_KUKSA.md)
            - [BB_uProtocol](/BB-SC/2b-MWLayer/Communication/BB_uProtocol.md)
            - [BB_uServices](/BB-SC/2b-MWLayer/Communication/BB_uServices.md)
            - [BB_VISSR](/BB-SC/2b-MWLayer/Communication/BB_VISSR.md)
            - [BB_eCAL](/BB-SC/2b-MWLayer/Communication/BB_eCAL.md)
            - [RTPS-Types](/BB-SC/2b-MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - cycloneDDS
                    - [BB_cycloneDDS](/BB-SC/2b-MWLayer/Communication/RTPS-Types/cycloneDDS/BB_cycloneDDS.md)
                - embeddedRTPS
                    - [BB_Constraint_DDS_embeddedRTPS](/BB-SC/2b-MWLayer/Communication/RTPS-Types/embeddedRTPS/BB_Constraint_DDS_embeddedRTPS.md)
                - OpenDDS
                    - [BB_OpenDDS](/BB-SC/2b-MWLayer/Communication/RTPS-Types/OpenDDS/BB_OpenDDS.md)
                - FastDDS
                    - [BB_FastDDS](/BB-SC/2b-MWLayer/Communication/RTPS-Types/FastDDS/BB_FastDDS.md)
                - vSomeIP
                    - [BB_vSomeIP](/BB-SC/2b-MWLayer/Communication/RTPS-Types/vSomeIP/BB_vSomeIP.md)
- [BB-CMU](/BB-CMU/README.md)
- [BB-CEST](/BB-CEST/README.md)
    - [Operations-and-Maintenance](/BB-CEST/Operations-and-Maintenance/README.md)
        - [Automation-and-Orchestration](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/README.md)
            - [Data-Driven-Integration-via-Observations](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Data-Driven-Integration-via-Observations/README.md)
            - [Workflow-Orchestration](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Workflow-Orchestration/README.md)
            - [Task-Automation](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Task-Automation/README.md)
            - [Automated-Testing-and-Validation](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Automated-Testing-and-Validation/README.md)
            - [Policy-and-Compliance-Automation](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Policy-and-Compliance-Automation/README.md)
            - [Configuration-as-Code](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Configuration-as-Code/README.md)
            - [Event-Driven-Automation](/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Event-Driven-Automation/README.md)
        - [Security-and-Compiance-in-Operation](/BB-CEST/Operations-and-Maintenance/Security-and-Compiance-in-Operation/README.md)
        - [Predictive-Maintenance](/BB-CEST/Operations-and-Maintenance/Predictive-Maintenance/README.md)
        - [Monitoring-and-Observability](/BB-CEST/Operations-and-Maintenance/Monitoring-and-Observability/README.md)
        - [Incident-Management](/BB-CEST/Operations-and-Maintenance/Incident-Management/README.md)
        - [Over-the-Air-Updates](/BB-CEST/Operations-and-Maintenance/Over-the-Air-Updates/README.md)
        - [Lifecycle-Management](/BB-CEST/Operations-and-Maintenance/Lifecycle-Management/README.md)
    - [Artificial-Intelligence-and-Machine-Learning](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/README.md)
        - [Data-Preparation-and-Management](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Preparation-and-Management/README.md)
        - [Monitoring-and-Feedback-Loop](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Monitoring-and-Feedback-Loop/README.md)
        - [Data-Centric-Validation-and-Testing](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Centric-Validation-and-Testing/README.md)
        - [Model-Deployment-and-Inference](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Model-Deployment-and-Inference/README.md)
        - [Model-Development-and-Training](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Model-Development-and-Training/README.md)
        - [Security-and-Governance-in-AI](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Security-and-Governance-in-AI/README.md)
        - [Data-Centric-AI-Development](/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Centric-AI-Development/README.md)
    - [Communication-and-Networking](/BB-CEST/Communication-and-Networking/README.md)
        - [Dependable-Communication](/BB-CEST/Communication-and-Networking/Dependable-Communication/README.md)
        - [Secure-Communication](/BB-CEST/Communication-and-Networking/Secure-Communication/README.md)
        - [Networking-Monitoring-and-Diagnostics](/BB-CEST/Communication-and-Networking/Networking-Monitoring-and-Diagnostics/README.md)
        - [Networking-Protocols](/BB-CEST/Communication-and-Networking/Networking-Protocols/README.md)
        - [Data-Routing-and-Load-Balancing](/BB-CEST/Communication-and-Networking/Data-Routing-and-Load-Balancing/README.md)
        - [Edge-to-Cloud-Connectivity](/BB-CEST/Communication-and-Networking/Edge-to-Cloud-Connectivity/README.md)
        - [Wireless-Connectivity](/BB-CEST/Communication-and-Networking/Wireless-Connectivity/README.md)
    - [User-and-Developer-Portals](/BB-CEST/User-and-Developer-Portals/README.md)
        - [User-Portals](/BB-CEST/User-and-Developer-Portals/User-Portals/README.md)
        - [Collaboration-Tools](/BB-CEST/User-and-Developer-Portals/Collaboration-Tools/README.md)
        - [Developer-Portals](/BB-CEST/User-and-Developer-Portals/Developer-Portals/README.md)
        - [Integration-with-SDV-EcoSystem](/BB-CEST/User-and-Developer-Portals/Integration-with-SDV-EcoSystem/README.md)
        - [Securtiy-and-Access-Control](/BB-CEST/User-and-Developer-Portals/Securtiy-and-Access-Control/README.md)
        - [Analytics-and-Insights](/BB-CEST/User-and-Developer-Portals/Analytics-and-Insights/README.md)
    - [Data-Processing-and-Management](/BB-CEST/Data-Processing-and-Management/README.md)
        - [Data-Tranformation-and-Integration](/BB-CEST/Data-Processing-and-Management/Data-Tranformation-and-Integration/README.md)
        - [Data-Storage-and-Retrieval](/BB-CEST/Data-Processing-and-Management/Data-Storage-and-Retrieval/README.md)
        - [Data-Governance-and-Security](/BB-CEST/Data-Processing-and-Management/Data-Governance-and-Security/README.md)
        - [Data-Streaming-and-Real-Time-Processing](/BB-CEST/Data-Processing-and-Management/Data-Streaming-and-Real-Time-Processing/README.md)
        - [Big-Data-Processing](/BB-CEST/Data-Processing-and-Management/Big-Data-Processing/README.md)
    - [Security-and-Compliance](/BB-CEST/Security-and-Compliance/README.md)
        - [Data-Security](/BB-CEST/Security-and-Compliance/Data-Security/README.md)
        - [Application-Security](/BB-CEST/Security-and-Compliance/Application-Security/README.md)
        - [Incident-Management-and-Recovery](/BB-CEST/Security-and-Compliance/Incident-Management-and-Recovery/README.md)
        - [Network-Security](/BB-CEST/Security-and-Compliance/Network-Security/README.md)
        - [Compliance-Management-with-Data-Governance](/BB-CEST/Security-and-Compliance/Compliance-Management-with-Data-Governance/README.md)
        - [Data-Centric-Access-and-Protection](/BB-CEST/Security-and-Compliance/Data-Centric-Access-and-Protection/README.md)
        - [Identity-and-Access-Management](/BB-CEST/Security-and-Compliance/Identity-and-Access-Management/README.md)
        - [Threat-Detection-and-Response](/BB-CEST/Security-and-Compliance/Threat-Detection-and-Response/README.md)
    - [Development-Testing-and-Simulation-Environments](/BB-CEST/Development-Testing-and-Simulation-Environments/README.md)
        - [Testing-Frameworks](/BB-CEST/Development-Testing-and-Simulation-Environments/Testing-Frameworks/README.md)
        - [Debugging-and-Monitoring](/BB-CEST/Development-Testing-and-Simulation-Environments/Debugging-and-Monitoring/README.md)
        - [Integrated-Development-Environments](/BB-CEST/Development-Testing-and-Simulation-Environments/Integrated-Development-Environments/README.md)
        - [Performance-and-Load-Testing](/BB-CEST/Development-Testing-and-Simulation-Environments/Performance-and-Load-Testing/README.md)
        - [Simulation-and-Emulation-Tools](/BB-CEST/Development-Testing-and-Simulation-Environments/Simulation-and-Emulation-Tools/README.md)
        - [Software-Development-Kits](/BB-CEST/Development-Testing-and-Simulation-Environments/Software-Development-Kits/README.md)
        - [Cloud-Based-Development-Environments](/BB-CEST/Development-Testing-and-Simulation-Environments/Cloud-Based-Development-Environments/README.md)
        - [Continuous-Integration-Continuous-Deployment](/BB-CEST/Development-Testing-and-Simulation-Environments/Continuous-Integration-Continuous-Deployment/README.md)
    - [Cloud-Infrastructure-and-Deployment](/BB-CEST/Cloud-Infrastructure-and-Deployment/README.MD)
        - [Edge-to-Cloud-Integration](/BB-CEST/Cloud-Infrastructure-and-Deployment/Edge-to-Cloud-Integration/README.md)
        - [Infrastructure-as-Code](/BB-CEST/Cloud-Infrastructure-and-Deployment/Infrastructure-as-Code/README.md)
        - [Containerization](/BB-CEST/Cloud-Infrastructure-and-Deployment/Containerization/README.md)
- [S-BB](/S-BB/README.md)
    - [2a-OSLayer](/S-BB/2a-OSLayer/README.md)
    - [1-HWLayer](/S-BB/1-HWLayer/README.md)
    - Generator
        - [BB_Commercial_Vehicle_Information_Specifications](/S-BB/Generator/BB_Commercial_Vehicle_Information_Specifications.md)
    - [3-AppLayer](/S-BB/3-AppLayer/README.md)
    - [2b-MWLayer](/S-BB/2b-MWLayer/README.md)
        - [BB_Unified_Push_Notification](/S-BB/2b-MWLayer/BB_Unified_Push_Notification.md)
        - [BB_VSS](/S-BB/2b-MWLayer/BB_VSS.md)
        - [BB_Data_Architecture_Terminology](/S-BB/2b-MWLayer/BB_Data_Architecture_Terminology.md)
        - [BB_HIM](/S-BB/2b-MWLayer/BB_HIM.md)
        - [BB_Private_Cross_OEM_Joint_Compute_for_EV_Charging](/S-BB/2b-MWLayer/BB_Private_Cross_OEM_Joint_Compute_for_EV_Charging.md)
        - [BB_EV_Charging_Event_Data_Aggregation](/S-BB/2b-MWLayer/BB_EV_Charging_Event_Data_Aggregation.md)
        - [BB_Common_Vehicle_Capabilities](/S-BB/2b-MWLayer/BB_Common_Vehicle_Capabilities.md)
        - [BB_In_Car_Wallet_Payments_and_Orchestration](/S-BB/2b-MWLayer/BB_In_Car_Wallet_Payments_and_Orchestration.md)
        - Communication
            - [BB_VISS](/S-BB/2b-MWLayer/Communication/BB_VISS.md)
- [BB-CSC-TC](/BB-CSC-TC/README.md)

***

## Navigation for Work In Progress BBs
- [BB-EST](/WorkInProgress/BB-EST/README.md)
    - Implementation
    - Configuration-and-Calibration
        - [BB_Offboard_Config_Tool_for_TSN](/WorkInProgress/BB-EST/Configuration-and-Calibration/BB_Offboard_Config_Tool_for_TSN.md)
    - Testing
        - [BB_OpenDUT](/WorkInProgress/BB-EST/Testing/BB_OpenDUT.md)
    - Requirements
        - [BB_DocAsCode](/WorkInProgress/BB-EST/Requirements/BB_DocAsCode.md)
    - Deployment
    - Lifecycle-Management
    - Build-and-Implementation
    - Design
    - Monitoring-and-Diagnostics
- [BB-CSC](/WorkInProgress/BB-CSC/README.md)
    - [BB_Cloud_container_and_OS](/WorkInProgress/BB-CSC/BB_Cloud_container_and_OS.md)
    - [BB_End_to_end_security_for_C2X](/WorkInProgress/BB-CSC/BB_End_to_end_security_for_C2X.md)
    - [BB_Vehicle_data_streaming](/WorkInProgress/BB-CSC/BB_Vehicle_data_streaming.md)
    - [BB_Orchestration_support_for_energy_and_mobility_providers](/WorkInProgress/BB-CSC/BB_Orchestration_support_for_energy_and_mobility_providers.md)
    - [BB_Driver_monitor](/WorkInProgress/BB-CSC/BB_Driver_monitor.md)
    - [BB_Data_spaces](/WorkInProgress/BB-CSC/BB_Data_spaces.md)
    - [BB_Vehicle_monitor](/WorkInProgress/BB-CSC/BB_Vehicle_monitor.md)
    - [BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle](/WorkInProgress/BB-CSC/BB_Monitoring_and_Tracing_of_specific_HW_in_vehicle.md)
    - [BB_Active_diagnostics_and_repair_services](/WorkInProgress/BB-CSC/BB_Active_diagnostics_and_repair_services.md)
    - [BB_Data_manager_ensuring_compliance_with_regulation](/WorkInProgress/BB-CSC/BB_Data_manager_ensuring_compliance_with_regulation.md)
    - [BB_App_and_services_store](/WorkInProgress/BB-CSC/BB_App_and_services_store.md)
    - [BB_Extended_accident_data_recorder](/WorkInProgress/BB-CSC/BB_Extended_accident_data_recorder.md)
    - [BB_Config_and_settngs_collector](/WorkInProgress/BB-CSC/BB_Config_and_settngs_collector.md)
    - [BB_Driver_authentication](/WorkInProgress/BB-CSC/BB_Driver_authentication.md)
    - [BB_Secure_and_privacy_aware_voice_assistant](/WorkInProgress/BB-CSC/BB_Secure_and_privacy_aware_voice_assistant.md)
- [BB-MU](/WorkInProgress/BB-MU/README.md)
- [BB-SC-TC](/WorkInProgress/BB-SC-TC/README.md)
    - Testing
        - [BB_Shadowing](/WorkInProgress/BB-SC-TC/Testing/BB_Shadowing.md)
- UseCases
    - Scenarios
        - [BB_Central_traffic_manager](/WorkInProgress/UseCases/Scenarios/BB_Central_traffic_manager.md)
        - [BB_Location_based_services](/WorkInProgress/UseCases/Scenarios/BB_Location_based_services.md)
        - [BB_Offloading_tasks_to_cloud_resources](/WorkInProgress/UseCases/Scenarios/BB_Offloading_tasks_to_cloud_resources.md)
        - [BB_Central_database_of_vehicle_failures_and_incidents](/WorkInProgress/UseCases/Scenarios/BB_Central_database_of_vehicle_failures_and_incidents.md)
        - [BB_Vehicle_FleetData](/WorkInProgress/UseCases/Scenarios/BB_Vehicle_FleetData.md)
        - [BB_Collect_street_data](/WorkInProgress/UseCases/Scenarios/BB_Collect_street_data.md)
        - [BB_Universal_Service_Mesh](/WorkInProgress/UseCases/Scenarios/BB_Universal_Service_Mesh.md)
        - [BB_Remote_driving](/WorkInProgress/UseCases/Scenarios/BB_Remote_driving.md)
        - [BB_Remote_Vehicle_Interaction](/WorkInProgress/UseCases/Scenarios/BB_Remote_Vehicle_Interaction.md)
- [BB-SC](/WorkInProgress/BB-SC/README.md)
    - [2a-OSLayer](/WorkInProgress/BB-SC/2a-OSLayer/README.md)
        - Container
            - [BB_Container_Abstraction](/WorkInProgress/BB-SC/2a-OSLayer/Container/BB_Container_Abstraction.md)
        - Virtualization
            - [BB_SR_VOSS](/WorkInProgress/BB-SC/2a-OSLayer/Virtualization/BB_SR_VOSS.md)
        - Time
            - [BB_Automotive_Edge_Runtime](/WorkInProgress/BB-SC/2a-OSLayer/Time/BB_Automotive_Edge_Runtime.md)
    - [1-HWLayer](/WorkInProgress/BB-SC/1-HWLayer/README.md)
    - [3-AppLayer](/WorkInProgress/BB-SC/3-AppLayer/README.md)
        - Control
            - [BB_ADAAA](/WorkInProgress/BB-SC/3-AppLayer/Control/BB_ADAAA.md)
        - API
            - [BB_Automotive_API_Framework](/WorkInProgress/BB-SC/3-AppLayer/API/BB_Automotive_API_Framework.md)
        - Communication
            - [BB_AOSP_Push_Notification_Service](/WorkInProgress/BB-SC/3-AppLayer/Communication/BB_AOSP_Push_Notification_Service.md)
    - [2b-MWLayer](/WorkInProgress/BB-SC/2b-MWLayer/README.md)
        - Platform-Health-Management
            - [BB_Watchdog](/WorkInProgress/BB-SC/2b-MWLayer/Platform-Health-Management/BB_Watchdog.md)
            - [BB_Distributed_Health_Management](/WorkInProgress/BB-SC/2b-MWLayer/Platform-Health-Management/BB_Distributed_Health_Management.md)
        - Storage
            - [BB_Vehicle_Data_Persistency](/WorkInProgress/BB-SC/2b-MWLayer/Storage/BB_Vehicle_Data_Persistency.md)
            - [BB_Vehicle_Logging_and_Recording](/WorkInProgress/BB-SC/2b-MWLayer/Storage/BB_Vehicle_Logging_and_Recording.md)
            - [BB_Vehicle_Data_Collector](/WorkInProgress/BB-SC/2b-MWLayer/Storage/BB_Vehicle_Data_Collector.md)
        - Diagnostics
            - [BB_Policy_Manager](/WorkInProgress/BB-SC/2b-MWLayer/Diagnostics/BB_Policy_Manager.md)
            - [BB_SOVD_Reference_implementation](/WorkInProgress/BB-SC/2b-MWLayer/Diagnostics/BB_SOVD_Reference_implementation.md)
        - Runtime
            - [BB_Diagnostic_Services_Applications](/WorkInProgress/BB-SC/2b-MWLayer/Runtime/BB_Diagnostic_Services_Applications.md)
            - [BB_State_Management](/WorkInProgress/BB-SC/2b-MWLayer/Runtime/BB_State_Management.md)
        - Power-Management
            - [BB_Power_Management_Coordination](/WorkInProgress/BB-SC/2b-MWLayer/Power-Management/BB_Power_Management_Coordination.md)
        - Security
            - [BB_Secure_Onboard_Communication](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Secure_Onboard_Communication.md)
            - [BB_Security_Transport_Layer](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Security_Transport_Layer.md)
            - [BB_Safety_Gateway](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Safety_Gateway.md)
            - [BB_Crypto_Service_Manager](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Crypto_Service_Manager.md)
            - [BB_Security_and_Safety_API](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Security_and_Safety_API.md)
            - [BB_Anomaly_Detection](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Anomaly_Detection.md)
            - [BB_Intrusion_Detection](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Intrusion_Detection.md)
            - [BB_Internet_Protocol_Security](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Internet_Protocol_Security.md)
            - [BB_Security_Event_Manager](/WorkInProgress/BB-SC/2b-MWLayer/Security/BB_Security_Event_Manager.md)
        - Tools-and-Methods
            - [BB_Key_Management_System](/WorkInProgress/BB-SC/2b-MWLayer/Tools-and-Methods/BB_Key_Management_System.md)
        - Configuration
            - [BB_Local_Update_Manager](/WorkInProgress/BB-SC/2b-MWLayer/Configuration/BB_Local_Update_Manager.md)
            - [BB_OTA_Master](/WorkInProgress/BB-SC/2b-MWLayer/Configuration/BB_OTA_Master.md)
        - Communication
            - [BB_TSN](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_TSN.md)
            - [BB_Smart_Charging_Communication](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Smart_Charging_Communication.md)
            - [BB_SecOS](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_SecOS.md)
            - [BB_Communication_Protocol_Abstraction](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Communication_Protocol_Abstraction.md)
            - [BB_Gateway_Mirroring](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Gateway_Mirroring.md)
            - [BB_Standard_Android_VHAL](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Standard_Android_VHAL.md)
            - [BB_Onboard_TSN_configuration](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Onboard_TSN_configuration.md)
            - [BB_Network_Management](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Network_Management.md)
            - [BB_Communication_Server_S2S](/WorkInProgress/BB-SC/2b-MWLayer/Communication/BB_Communication_Server_S2S.md)
            - [RTPS-Types](/WorkInProgress/BB-SC/2b-MWLayer/Communication/RTPS-Types/RTPS-Types.md)
                - cycloneDDS
                - embeddedRTPS
                - OpenDDS
                - FastDDS
        - Time
            - [BB_Time_Service](/WorkInProgress/BB-SC/2b-MWLayer/Time/BB_Time_Service.md)
            - [BB_Onboard_TSN_scheduling_Tool](/WorkInProgress/BB-SC/2b-MWLayer/Time/BB_Onboard_TSN_scheduling_Tool.md)
- [BB-CMU](/WorkInProgress/BB-CMU/README.md)
    - [BB_Digital_Twin_proxy_in_cloud](/WorkInProgress/BB-CMU/BB_Digital_Twin_proxy_in_cloud.md)
- [BB-CEST](/WorkInProgress/BB-CEST/README.md)
    - [Operations-and-Maintenance](/WorkInProgress/BB-CEST/Operations-and-Maintenance/README.md)
        - [Automation-and-Orchestration](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/README.md)
            - [Data-Driven-Integration-via-Observations](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Data-Driven-Integration-via-Observations/README.md)
            - [Workflow-Orchestration](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Workflow-Orchestration/README.md)
            - [Task-Automation](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Task-Automation/README.md)
            - [Automated-Testing-and-Validation](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Automated-Testing-and-Validation/README.md)
            - [Policy-and-Compliance-Automation](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Policy-and-Compliance-Automation/README.md)
            - [Configuration-as-Code](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Configuration-as-Code/README.md)
            - [Event-Driven-Automation](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Automation-and-Orchestration/Event-Driven-Automation/README.md)
        - [Security-and-Compiance-in-Operation](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Security-and-Compiance-in-Operation/README.md)
        - [Predictive-Maintenance](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Predictive-Maintenance/README.md)
        - [Monitoring-and-Observability](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Monitoring-and-Observability/README.md)
        - [Incident-Management](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Incident-Management/README.md)
        - [Over-the-Air-Updates](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Over-the-Air-Updates/README.md)
        - [Lifecycle-Management](/WorkInProgress/BB-CEST/Operations-and-Maintenance/Lifecycle-Management/README.md)
    - [Artificial-Intelligence-and-Machine-Learning](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/README.md)
        - [Data-Preparation-and-Management](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Preparation-and-Management/README.md)
        - [Monitoring-and-Feedback-Loop](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Monitoring-and-Feedback-Loop/README.md)
        - [Data-Centric-Validation-and-Testing](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Centric-Validation-and-Testing/README.md)
        - [Model-Deployment-and-Inference](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Model-Deployment-and-Inference/README.md)
        - [Model-Development-and-Training](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Model-Development-and-Training/README.md)
        - [Security-and-Governance-in-AI](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Security-and-Governance-in-AI/README.md)
        - [Data-Centric-AI-Development](/WorkInProgress/BB-CEST/Artificial-Intelligence-and-Machine-Learning/Data-Centric-AI-Development/README.md)
    - [Communication-and-Networking](/WorkInProgress/BB-CEST/Communication-and-Networking/README.md)
        - [Dependable-Communication](/WorkInProgress/BB-CEST/Communication-and-Networking/Dependable-Communication/README.md)
        - [Secure-Communication](/WorkInProgress/BB-CEST/Communication-and-Networking/Secure-Communication/README.md)
        - [Networking-Monitoring-and-Diagnostics](/WorkInProgress/BB-CEST/Communication-and-Networking/Networking-Monitoring-and-Diagnostics/README.md)
        - [Networking-Protocols](/WorkInProgress/BB-CEST/Communication-and-Networking/Networking-Protocols/README.md)
        - [Data-Routing-and-Load-Balancing](/WorkInProgress/BB-CEST/Communication-and-Networking/Data-Routing-and-Load-Balancing/README.md)
        - [Edge-to-Cloud-Connectivity](/WorkInProgress/BB-CEST/Communication-and-Networking/Edge-to-Cloud-Connectivity/README.md)
        - [Wireless-Connectivity](/WorkInProgress/BB-CEST/Communication-and-Networking/Wireless-Connectivity/README.md)
    - [User-and-Developer-Portals](/WorkInProgress/BB-CEST/User-and-Developer-Portals/README.md)
        - [User-Portals](/WorkInProgress/BB-CEST/User-and-Developer-Portals/User-Portals/README.md)
        - [Collaboration-Tools](/WorkInProgress/BB-CEST/User-and-Developer-Portals/Collaboration-Tools/README.md)
        - [Developer-Portals](/WorkInProgress/BB-CEST/User-and-Developer-Portals/Developer-Portals/README.md)
        - [Integration-with-SDV-EcoSystem](/WorkInProgress/BB-CEST/User-and-Developer-Portals/Integration-with-SDV-EcoSystem/README.md)
        - [Securtiy-and-Access-Control](/WorkInProgress/BB-CEST/User-and-Developer-Portals/Securtiy-and-Access-Control/README.md)
        - [Analytics-and-Insights](/WorkInProgress/BB-CEST/User-and-Developer-Portals/Analytics-and-Insights/README.md)
    - [Data-Processing-and-Management](/WorkInProgress/BB-CEST/Data-Processing-and-Management/README.md)
        - [Data-Tranformation-and-Integration](/WorkInProgress/BB-CEST/Data-Processing-and-Management/Data-Tranformation-and-Integration/README.md)
        - [Data-Storage-and-Retrieval](/WorkInProgress/BB-CEST/Data-Processing-and-Management/Data-Storage-and-Retrieval/README.md)
        - [Data-Governance-and-Security](/WorkInProgress/BB-CEST/Data-Processing-and-Management/Data-Governance-and-Security/README.md)
        - [Data-Streaming-and-Real-Time-Processing](/WorkInProgress/BB-CEST/Data-Processing-and-Management/Data-Streaming-and-Real-Time-Processing/README.md)
        - [Big-Data-Processing](/WorkInProgress/BB-CEST/Data-Processing-and-Management/Big-Data-Processing/README.md)
    - [Security-and-Compliance](/WorkInProgress/BB-CEST/Security-and-Compliance/README.md)
        - [Data-Security](/WorkInProgress/BB-CEST/Security-and-Compliance/Data-Security/README.md)
        - [Application-Security](/WorkInProgress/BB-CEST/Security-and-Compliance/Application-Security/README.md)
        - [Incident-Management-and-Recovery](/WorkInProgress/BB-CEST/Security-and-Compliance/Incident-Management-and-Recovery/README.md)
        - [Network-Security](/WorkInProgress/BB-CEST/Security-and-Compliance/Network-Security/README.md)
        - [Compliance-Management-with-Data-Governance](/WorkInProgress/BB-CEST/Security-and-Compliance/Compliance-Management-with-Data-Governance/README.md)
        - [Data-Centric-Access-and-Protection](/WorkInProgress/BB-CEST/Security-and-Compliance/Data-Centric-Access-and-Protection/README.md)
        - [Identity-and-Access-Management](/WorkInProgress/BB-CEST/Security-and-Compliance/Identity-and-Access-Management/README.md)
        - [Threat-Detection-and-Response](/WorkInProgress/BB-CEST/Security-and-Compliance/Threat-Detection-and-Response/README.md)
    - [Development-Testing-and-Simulation-Environments](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/README.md)
        - [Testing-Frameworks](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Testing-Frameworks/README.md)
        - [Debugging-and-Monitoring](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Debugging-and-Monitoring/README.md)
        - [Integrated-Development-Environments](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Integrated-Development-Environments/README.md)
        - [Performance-and-Load-Testing](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Performance-and-Load-Testing/README.md)
        - [Simulation-and-Emulation-Tools](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Simulation-and-Emulation-Tools/README.md)
            - [BB_RemotiveCloud](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Simulation-and-Emulation-Tools/BB_RemotiveCloud.md)
            - [BB_Car_Simulator](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Simulation-and-Emulation-Tools/BB_Car_Simulator.md)
        - [Software-Development-Kits](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Software-Development-Kits/README.md)
        - [Cloud-Based-Development-Environments](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Cloud-Based-Development-Environments/README.md)
        - [Continuous-Integration-Continuous-Deployment](/WorkInProgress/BB-CEST/Development-Testing-and-Simulation-Environments/Continuous-Integration-Continuous-Deployment/README.md)
    - [Cloud-Infrastructure-and-Deployment](/WorkInProgress/BB-CEST/Cloud-Infrastructure-and-Deployment/README.MD)
        - [Edge-to-Cloud-Integration](/WorkInProgress/BB-CEST/Cloud-Infrastructure-and-Deployment/Edge-to-Cloud-Integration/README.md)
        - [Infrastructure-as-Code](/WorkInProgress/BB-CEST/Cloud-Infrastructure-and-Deployment/Infrastructure-as-Code/README.md)
        - [Containerization](/WorkInProgress/BB-CEST/Cloud-Infrastructure-and-Deployment/Containerization/README.md)
- [S-BB](/WorkInProgress/S-BB/README.md)
    - [2a-OSLayer](/WorkInProgress/S-BB/2a-OSLayer/README.md)
    - [1-HWLayer](/WorkInProgress/S-BB/1-HWLayer/README.md)
    - [3-AppLayer](/WorkInProgress/S-BB/3-AppLayer/README.md)
        - [BB_Standardization_of_Vehicle_API](/WorkInProgress/S-BB/3-AppLayer/BB_Standardization_of_Vehicle_API.md)
        - [BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure](/WorkInProgress/S-BB/3-AppLayer/BB_Standardized_Architectural_Patterns_for_Cross_Platform_Data_Service_Infrastructure.md)
        - [BB_Standardized_Description_of_Data_from_Related_Domains](/WorkInProgress/S-BB/3-AppLayer/BB_Standardized_Description_of_Data_from_Related_Domains.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains](/WorkInProgress/S-BB/3-AppLayer/BB_Standardized_Procedure_and_Tooling_for_Combining_Data_from_Different_Domains.md)
        - [BB_Fleet_Management_System](/WorkInProgress/S-BB/3-AppLayer/BB_Fleet_Management_System.md)
        - [BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains](/WorkInProgress/S-BB/3-AppLayer/BB_Standardized_Procedure_and_Tooling_for_Modelling_Data_from_Different_Domains.md)
        - API
            - [BB_VAPI_Stack_Demonstrator](/WorkInProgress/S-BB/3-AppLayer/API/BB_VAPI_Stack_Demonstrator.md)
    - [2b-MWLayer](/WorkInProgress/S-BB/2b-MWLayer/README.md)
        - [BB_Standardized_authentication_of_vehicle_users](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_authentication_of_vehicle_users.md)
        - [BB_Standardized_data_formats_for_digital_twins](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_data_formats_for_digital_twins.md)
        - [BB_Standardized_HD_maps_formats](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_HD_maps_formats.md)
        - [BB_sSOA](/WorkInProgress/S-BB/2b-MWLayer/BB_sSOA.md)
        - [BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_Data_Conversion_Tools_for_Info_Knowledge_Layers.md)
        - [BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_Data_Description_for_Vehicle_Sensors_Attributes_Actuators.md)
        - [BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_cloud_services_to_support_international_roaming_of_vehicles.md)
        - [BB_Standardized_way_for_Reasoning_on_Data_Streams](/WorkInProgress/S-BB/2b-MWLayer/BB_Standardized_way_for_Reasoning_on_Data_Streams.md)
        - [BB_SOA](/WorkInProgress/S-BB/2b-MWLayer/BB_SOA.md)
        - [BB_Legally_binding_formats_for_data_exchange](/WorkInProgress/S-BB/2b-MWLayer/BB_Legally_binding_formats_for_data_exchange.md)
- [BB-CSC-TC](/WorkInProgress/BB-CSC-TC/README.md)

***
generated using [README Generator](/other/scripts/readme_generator.py)