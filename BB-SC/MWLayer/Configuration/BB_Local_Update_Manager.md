
# Local Update Manager

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Configuration

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->

## Known Implementation

- AUTOSAR: UCS - but not OSS-usable
- higher-level: Eclipse Ankaios, Eclipse Kanto, Eclipse Symphony, Eclipse BlueChi

## ID (unique name)

## Description
<!-- General Description of the BB -->
A Local update manager is a local instance of an (OTA) Update master. It is meant to be deployed and operated on distributed vehicle network nodes. It must provide a similar, but limited functionality compared to the OTA master. It shall be able to manage locally backup storage and rollback of software controlled by the OTA Master. The local update manager may become necessary as the OTA master will not or just with complex implementations (which may interfere with the network capabilities and the overall in-vehicle security) be able to deploy SW updates across the vehicle network within a zonal architecture. The Local update manager will deploy/install software in a dedicated local area of the vehicle network under control of the update master. It will ensure also local API for memory control and security services control.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The local update manager may become a "must-have" within server/zone architectures to retain the capability to deploy SW updates end-to-end. Especially when there is the need to separate zones for safety/security reasons, the local update manager will be mandatory.

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
