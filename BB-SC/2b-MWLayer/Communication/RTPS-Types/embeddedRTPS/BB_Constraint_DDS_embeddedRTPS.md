# embeddedRTPS - DDS for Ressource-constrained environments
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC, BB-CSC, BB-MU, BB-CMU

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Communication

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->


## Known Implementation
Github repo: <https://github.com/embedded-software-laboratory/embeddedRTPS>

## ID (unique name)

## Description
<!-- General Description of the BB -->
This repository contains source code for embeddedRTPS, a portable and open-source C++ implementation of the Real-Time Publish-Subscribe Protocol (RTPS) for embedded system. RTPS is based on the publish-subscribe mechanism and is at the core of the Data Distribution Service (DDS). DDS is used, among many other applications, in Robot Operating System 2 (ROS2) and is also part of the AUTOSAR Adaptive platform. embeddedRTPS allows to integrate Ethernet-capable microcontrollers into DDS-based systems as first-class participants.
embeddedRTPS is portable, as it only consumes lightweightIP and FreeRTOS APIs, which are available for a large number of embedded systems. embeddedRTPS avoids dynamic memory allocation once endpoints are constructed possible. Please note that embeddedRTPS only implements rudimentary Quality-of-Service (QoS) policies and is far from a complete RTPS implementation.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
This light-weight DDS stack allows to integrate ressource constraint devices into SOA architectures. DDS is used as a middleware in AUTOSAR Adaptive and ROS 2.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
https://www.omg.org/spec/DDS/ (deviations from spec.)
https://www.omg.org/spec/DDSI-RTPS/ (implemented partially) 
https://www.omg.org/spec/DDS-SECURITY/ (not implemented in pub version)

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
FreeRTOS or other OS/Runtime Envirnoment
lwIP (could be another NW Stack)

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
The Repo include a reference implementation which is executable on different Targets /STM32, AURIX Tricore.
Needed:
MW Layer to use it with ROS2 (RMW) or adaptive AUTOSAR (commonAPI support).
Support for Security concepts in the OSS implementation. (see Applicable S-BB(s))

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
See: Example with a getting started for STM32 (Linux/Mac)
GCC (Ubuntu 18 and above), Tasking Compiler,  
<https://github.com/embedded-software-laboratory/embeddedRTPS-STM32>

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
Real-Time
Security

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->


## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
“No”

## Author/Company
Alexandru Kampmann RWTH

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
<https://github.com/mROS-base/mros2>
<https://github.com/micro-ROS>

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes / License MIT
Commercial Closed Source Parts are available (security)

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes / License MIT

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
None

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
| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| Notdefined | Notdefined   | Notdefined   | Notdefined	 | Notdefined |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
First public release available, used in [unicaragil](https://www.unicaragil.de/en/)
last update Github Jul 2024

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
regarding details see section - What is needed to build and run

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
