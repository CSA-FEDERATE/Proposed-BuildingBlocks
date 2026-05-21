
#  UN Regulation No. 156 - Software update and software update management system

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->

S-BB

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

All

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->

AppLayer, MWLayer, OSLayer, (HWLayer BSPs)

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->

## Known Implementation

https://unece.org/transport/documents/2021/03/standards/un-regulation-no-156-software-update-and-software-update

## ID (unique name)

## Description
<!-- General Description of the BB -->

1. Scope

1.1. This Regulation applies to vehicles of Categories1 M, N, O, R, S and T that permit software updates

[source unece.org](https://unece.org/sites/default/files/2024-03/R156e%20%282%29.pdf)

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

2. Definitions

2.1. "Vehicle type" means vehicles which do not differ in at least the following:
	(a) The manufacturer’s designation of the vehicle type;
	(b) Essential aspects of the design of the vehicle type with respect to software update processes.
	
2.2. "RX Software Identification Number (RXSWIN)" means a dedicated identifier,
defined by the vehicle manufacturer, representing information about the type
approval relevant software of the Electronic Control System contributing to
the Regulation N° X type approval relevant characteristics of the vehicle.

2.3. "Software update" means a package used to upgrade software to a new version
including a change of the configuration parameters.

2.4. "Execution" means the process of installing and activating an update that has
been downloaded.

2.5. "Software Update Management System (SUMS)" means a systematic approach
defining organizational processes and procedures to comply with the
requirements for delivery of software updates according to this Regulation.

2.6. "Vehicle user" means a person operating or driving the vehicle, a vehicle
owner, an authorised representative or employee of a fleet manager, an
authorised representative or employee of the vehicle manufacturer, or an
authorized technician.

2.7. "Safe state" means an operating mode in case of a failure of an item without
an unreasonable level of risk.

2.8. "Software" means the part of an Electronic Control System that consists of
digital data and instruction.

2.9. "Over-the-Air (OTA) update" means any method of making data transfers
wirelessly instead of using a cable or other local connection.

2.10. "System" means a set of components and/or sub-systems that implement a
function of functions.

2.11. "Integrity validation data" means a representation of digital data, against
which comparisons can be made to detect errors or changes in the data. This
may include checksums and hash values.

[source unece.org](https://unece.org/sites/default/files/2024-03/R156e%20%282%29.pdf)

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->

Connectivity-OTA

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

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->

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

 ## Compliant to
 <!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
