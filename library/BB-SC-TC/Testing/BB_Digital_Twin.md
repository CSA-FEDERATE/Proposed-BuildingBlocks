
# Digital Twin

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
The digital twin is considered as a digital representation of a vehicle (or the vehicle's configuration) as prerequisite for validation and test of SW variants prior to their deployment to a live vehicle.  
Proposal for standardization are execution model with regard to simulation level (Prostep standardization <https://www.prostep.org/>), handling of distributed simulation, co-simulation bus and services for controller including services to extract and inject data, extract and inject algorithm dynamically (or static) during simulation, services to guarantee at least software alignment between digital and vehicle.  
Defines embed service services to ensure connection with digital twin.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Enables rapid prototyping, validation, and test of vehicle configurations. In scope of OTA updates, validating as many SW variants as possible (all?) to ensure the error-prone deployment of SW updates to the live fleet. Cost saving by eliminating HIL tests with a huge amount of variants.

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
