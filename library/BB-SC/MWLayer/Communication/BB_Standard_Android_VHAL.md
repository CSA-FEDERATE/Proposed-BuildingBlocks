
# Standard Android VHAL

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Communication

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## Known Implementation

## ID (unique name)

## Description
<!-- General Description of the BB -->
The standard Android VHAL implementation should be a building block enabling to seamlessly mapping of car data from underlying data middleware to Android Car API.  
The solution should be able to use any data middleware using VSS and standard transport protocols enabling get, set, sub, pub, e.g. MQTT, WS. All the standard properties defined by Google shall be reused. All missing properties shall be defined using vendor properties in a standard, cross-OEM way. It should enable VSS to VHAL Property mapping using and updatable mapping file enabling:  

a) definition and agreement of vendor mapping cross-OEM  
b) OTA updatability  
c) OEM specific mappings.  

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The building block will be used using the standard Google Car API within the Android Framework

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
Android Automotive OS
Android VHAL
Android Car API

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
BB Reference implementation / API  
Standardized way (Vehicle Data mapping)

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

Anonymous

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
SHIFT2SDV

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles
