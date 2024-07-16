
# Secure Onboard Communication

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

Security

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## Known Implementation

## ID (unique name)

## Description
<!-- General Description of the BB -->
Define secure communication between different ECU. This includes messages signed messages with a hash (CMAC) and a counter information to be able to detect security violations (like replay attacks etc.). These services need to applied for different communication protocol common at the vehicle level to be aligned for set of secure communication routines.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Extend the concept of AUTOSAR SecOC with a common implementation at the vehicle level.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
AUTOSAR SecOC

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
[BB_SecOS](/BB-SC/MWLayer/Communication/BB_SecOS.md)

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
<!-- High, Mid, Low -->
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
