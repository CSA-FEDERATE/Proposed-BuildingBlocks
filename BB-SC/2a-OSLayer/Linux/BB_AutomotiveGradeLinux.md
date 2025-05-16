
#  AGL Automotive Grade Linux

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC, BB-EST, BB-EST-TC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
APPLayer, MWLayer, OSLayer

## BB Usage
<!-- example on how to use BB or link to documentation -->

## Known Implementation
https://github.com/orgs/agl-ic-eg/repositories?type=all

## ID (unique name)

## Description
<!-- General Description of the BB -->
Automotive Grade Linux is a collaborative, open source project that brings together automakers, suppliers, and technology companies 
for the purpose of building Linux-based, open source software platforms for automotive applications that can serve as de facto industry standards.

AGL address all software in the vehicle: infotainment, instrument cluster, heads-up-display (HUD), telematics, connected car, 
advanced driver assistance systems (ADAS), functional safety, and autonomous driving.

[source:](https://docs.automotivelinux.org/en/master/##01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images/)

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Adopting a shared platform across the industry reduces fragmentation and allows automakers and suppliers to reuse the same code base, which leads to rapid innovation and faster time-to-market for new products.

AGL is a Linux Foundation project and its goals are as follows:

    Build a single platform for the entire industry
    Develop 70 to 80% of the starting point for a production project
    Reduce fragmentation by combining the best of open source
    Develop an ecosystem of developers, suppliers, and expertise that all use a single platform

[source:](https://docs.automotivelinux.org/en/master/##01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images/)


## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
TBD

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
[Yocto Project](https://www.yoctoproject.org/)
[QEMU](https://www.qemu.org/) 

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
Linux Build System 

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->

See supported [Hardware](https://docs.automotivelinux.org/en/master/#02_Hardware_Support/01_Supported_Hardware_Overview/ 


## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
TBD

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->
TBD

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
Yes - Demonstrator use COVESA VSS implementation

## Author/Company
VIF

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
TBD


## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
YES GPL, MIT
 
## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
TBD

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
TBD

## Potential obstacles
TBD

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
TBD

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
Used in production by >1 OEM
[last change May 2025 visted 16.06.2025](https://github.com/orgs/agl-ic-eg/repositories?type=all)

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
AGL Automotive Grade Linux

 ## Bazel compliance status
 <!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->
 TBD