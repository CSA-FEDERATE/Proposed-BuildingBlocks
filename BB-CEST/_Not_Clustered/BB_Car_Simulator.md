
# Car Simulator

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-CEST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
None

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
Cross-Layer

## Known Implementation

Eclipse SDV - kanto.auto (old) will be published under a new name
Eclipse OpenDUT

## ID (unique name)

## Description
<!-- General Description of the BB -->
Based on the W3C VISSv2 standardized interface the car simulator can act as a car and simulate VISSv2 related interfaces.  
The simulator is able to create, provide and replay recorded data as well as simulate static data on the published VISSv2 based interfaces.  
The solution should be able to publish data via standard transport protocols supported by the VISSv2 standard enabling get, set, sub, pub, e.g. MQTT, WS.  
The car simulator offers an UI to configure data of the loaded VSS data model. Within the UI car related data can be manipulated or routes with changing data can be simulated.  
The car simulator should support the whole VSS data model and data types and the interfaces should support the W3C standard of VISSv2.  
The application should run locally as well as on a dedicated server based on newest web technologies

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Based on a standardized interface and data model the car simulator is able to manipulate and simulate data for services consuming data of the underlying VSS based data infrastructure.  
This enables developers to simulate states without a physical car as well as quality and test engineers to verify failures and fixes based on recorded standardized data.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
CARLA

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
BB Reference implementation, extension of a Car Simulator support
VSSv2 and VSS data model

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

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles
