# Linux Foundation EVerest
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
S-BB

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->
Documentation: https://everest.github.io/nightly/  
Source code: https://github.com/EVerest  
EVerest provides a modular, MQTT-based framework for building complete EV charging stacks. Configure charging scenarios by composing interchangeable modules (energy management, ISO 15118, OCPP, hardware drivers) and deploy on charging station controllers.

## Known Implementation
https://everest.github.io/nightly/

## ID (unique name)

## Description
<!-- General Description of the BB -->
EVerest is an open source modular framework for setting up a full stack environment for EV charging.

The modular software architecture fosters customizability and lets you configure your dedicated charging scenarios based on interchangeable modules. All this is glued together by MQTT.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The EV charging ecosystem requires interoperable, standards-compliant software stacks (ISO 15118, OCPP) that work across diverse hardware. EVerest provides an open, vendor-neutral framework that accelerates charging station development and ensures protocol compliance without proprietary lock-in.

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
C++, Python, MQTT knowledge. Modular plugin architecture.

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
Linux. MQTT broker (Mosquitto). EV charging hardware interfaces (OCPP, ISO 15118).

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
Modular, interoperable. Supports ISO 15118 (Plug & Charge). Production-ready.

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->
MQTT broker, EV charging standards (OCPP 1.6/2.0, ISO 15118)


## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->


## Author/Company
Linux Foundation Energy

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->


## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes - APL-2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
TBD

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
Used in production

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
Linux, containers

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
none