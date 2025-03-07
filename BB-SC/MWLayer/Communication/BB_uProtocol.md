
# uProtocol

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
https://github.com/eclipse-uprotocol

## ID (unique name)

## Description
<!-- General Description of the BB -->
A communication protocol enabling developers to build apps and services that communicate seamlessly across one or multiple inter-connected messaging middleware. uProtocol provides a small number of communication patterns, exposed with a set of programming APIs available and consistent across the vehicle eco-system (in-vehicle ECUs, cloud and mobile). This approach enables seamless communication between applications and services, wherever they are hosted. Using uProtocol, application developers can focus on the functionality they need to develop, rather than the plumbing necessary to access the relevant services they require, and service providers develop their service once for all consumers, wherever they are hosted.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->

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
Daniel; Krippner; Etas, Bosch

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
[Eclipse](https://projects.eclipse.org/projects/automotive.uprotocol)

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Apache License, Version 2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles


## Maturity Badges
<!-- taken over from Eclipse SDV Process 
See Definition of Badges and their Flavors 
https://gitlab.eclipse.org/eclipse-wg/sdv-wg/sdv-technical-alignment/sdv-technical-topics/sdv-process/sdv-process-definition/-/wikis/Definition%20of%20Badges%20and%20their%20Flavors 


| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Gold		| Badgelevel    | Badgelevel   | Badgelevel		   | Badgelevel	 | Badgelevel  |
| Silver	| Badgelevel    | Badgelevel   | Badgelevel	  	   | Badgelevel	 | Badgelevel  |
| Bronze	| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |
| No		| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |
| NotDefined| Badgelevel   	| Badgelevel   | Badgelevel	       | Badgelevel	 | Badgelevel  |

Options:
NotDefined/No/Bronze/Silver/Gold

Example:
| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| [Gold](urlToDoc)| No 		   | Notdefined		   | Bronze	 | [Silver](urlToDoc) |


-->

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
 Implementation started

## System Context

<!-- 
OS and runtime/framework requirements

eg.

- AGL
- QNX
- ROS-based
- container runtime
- web assembly
- web service
 -->