# vSOME/IP
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC; BB-MU; BB-CSC; BB-CMU

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

Communication

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->

MWLayer

## Known Implementation
[vSomeIP](https://github.com/COVESA/vsomeip)

## ID (unique name)

## Description
<!-- General Description of the BB -->

SOME/IP is an abbreviation for "Scalable service-Oriented middlewarE over IP". This middleware was designed for typical automotive use cases and for being compatible with AUTOSAR (at least on the wire-format level). A publicly accessible specification is available [at](http://some-ip.com/). In this wiki we do not want to deepen further into the reasons for another middleware specification, but want to give a rough overview about the basic structures of the SOME/IP specification and its open source implementation vsomeip without any claim of completeness.
[source](https://github.com/COVESA/vsomeip/wiki/vsomeip-in-10-minutes)

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

Open source implementation of the SOME/IP protocol.
SOME/IP is an automotive middleware solution that can be used for control messages. It was designed from beginning on to fit devices of different sizes and different operating systems perfectly. This includes small devices like cameras, AUTOSAR devices, and up to head units or telematics devices. It was also made sure that SOME/IP supports features of the Infotainment domain as well as that of other domains in the vehicle, allowing SOME/IP to be used for MOST replacement scenarios as well as more traditional CAN scenarios.
[source](https://some-ip.com/)

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->

[Standards](https://some-ip.com/standards.shtml)
 AUTOSAR Classic
 AUTOSAR Foundation
 AUTOSAR Adaptive Platform
 ISO 17215:2-2014
 Genivi/COVESA vsomeip

## Compose BB(s)
<!-- Link to required BB(s) -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->

[see COVESA Github repo](https://github.com/COVESA/vsomeip)

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
HAL4SDV, Shift2SDV

## Availability of Source Code
Yes / vSomeIP - Mozilla Public License Version 2.0
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

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

|                       | Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level     | [Silver](https://github.com/COVESA/vsomeip/wiki) | [Gold](https://github.com/COVESA/vsomeip/tree/master/test)       | [Gold](https://github.com/COVESA/vsomeip/wiki/vsomeip-Contribution-Process) | Notdefined | [Gold](https://github.com/COVESA/vsomeip/wiki/vsomeip-Release-Process) |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->

Used in several projects, proprietary implementations available
Last update Github Jan. 2025 / continuously updated

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
 
 Linux

## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->