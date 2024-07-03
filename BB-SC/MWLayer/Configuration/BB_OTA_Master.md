
# OTA Master

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Configuration

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## Known Implementation

- AUTOSAR: UCS - but not OSS-usable
- higher-level: Eclipse Ankaios, Eclipse Kanto, Eclipse Symphony, Eclipse BlueChi

## ID (unique name)

## Description
<!-- General Description of the BB -->
The OTA master is a central SWC to deploy OTA SW updates within the vehicle network. Besides the basic functionality of SW installation, it implements the necessary failsafe or failover behavior to ensure the robustness of the update process (such as backup and rollover mechanism). In addition, it must manage and verify the integrity of the installed SW after it has been transferred from the backend, potentially even before installing the SW. It also coordinates local OTA salves distributed in the vehicle, by self-contained interface and command control. As a prerequisite for a successful update, the update master has also to be capable to read the vehicle configuration and control reprogramming history.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Existing, IoT based implementations of OTA Master will not carry over to zonal architectures as they - if ever - have limited ability to deploy SW across servers and zone controllers within the vehicle network. Scaling is an issue as well, as those solutions usually need continuous backend connection during the update process, thus demanding a highly scalable, costly backend infrastructure to deploy SW updates OTA for a bigger fleet. A UCM Master enables the use of standardized interfaces and Software components for OTA updates within upcoming EE architectures. A POSIX based update master can be a reasonable replacement in non-AUTOSAR environments when it implements the same basic mechanism as an UCM master.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
OTA master POSIX  
OTA master ASR Adaptive (UCM Master)  

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->

## Author/Company

Conti

## Priority
<!-- High, Medium, Low -->
High

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles
