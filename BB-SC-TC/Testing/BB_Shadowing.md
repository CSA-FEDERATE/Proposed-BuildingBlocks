
# Shadowing

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC-TC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Testing

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## Known Implementation

## ID (unique name)

## Description
<!-- General Description of the BB -->
A system working passively in the background that uses recorded data and input from sensors and cameras in the car to make its own hypothetical driving decisions. These hypothetical driving decisions are then compared to the decisions the (human) driver of the car makes. Both the recorded data and the comparison are used, amongst others, to discover unthought of edge and corner cases, and to evaluate and demonstrate the safety of autonomous functionalities.
Proposal for standardization of recording services, comparison services, and process execution services are standardized in conjunction data collector and orchestrator. The rest seems to be added value of the functionality.

A digital shadow mirrors the current state and behavior of a physical entity or system.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The use of shadowing during development (and potentially even during operation) of vehicles can enhance the ADAS algorithm/configuration development which will otherwise mostly be based on artificial test data and test drives. Shadowing will support the improvement of the vehicles in the field and enhance the safety of the users.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
TDB

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

## Priority
<!-- High, Medium, Low -->

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
