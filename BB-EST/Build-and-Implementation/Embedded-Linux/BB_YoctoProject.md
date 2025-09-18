
# Yocto project

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-EST, BB-CEST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->

## BB Usage
<!-- example on how to use BB or link to documentation -->

## Known Implementation
https://git.yoctoproject.org/

## ID (unique name)

## Description
<!-- General Description of the BB -->
The Yocto Project (YP) is an open source collaboration project that helps developers create custom Linux-based systems regardless of the 
hardware architecture.

The project provides a flexible set of tools and a space where embedded developers worldwide can share technologies, software stacks, 
configurations, and best practices that can be used to create tailored Linux images for embedded and IOT devices, or anywhere a customized 
Linux OS is needed.

[source:](https://www.yoctoproject.org/)

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->


The Yocto Project is an open source collaboration project that provides templates, tools and methods to help you create custom Linux-based 
systems for embedded system deployments in connected edge devices, servers, or virtual environments, regardless of the hardware architecture.

As an open source project, the Yocto Project operates with a hierarchical governance structure led by maintainers and coordinated by 
the Yocto Project Governance Board. The governance model is based on the principles, best practices, and values of Open Source culture, 
and pursues the goals set out in the Yocto Project Charter. This enables the project to remain independent of any one of its member 
organizations, who participate in various ways and provide resources to the project.

The project is supported and governed by high-tech industry leaders who have committed financially with platform support and marketing 
efforts to make Yocto Project a secure, stable, and adaptable industry standard.

The Yocto Project is a collaborative project under the Linux Foundation umbrella.

[source:](https://www.yoctoproject.org/about/project-overview/)

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
TBD

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
TBD

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
-

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
Linux build envrionment

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
No

## Author/Company
<!-- How is the caretaker, maintainer or contact for this BB, … -->
VIF

## Priority
<!-- High, Medium, Low -->
-

## Contribution through RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
Pat of the buildsystem for the BB - Automotove Grade Linux

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
YES -  
[soruce: Understanding licenses in a Yocto Project Build](https://hub.mender.io/t/understanding-licenses-in-a-yocto-project-build/4848) 

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
TBD

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
TBD

## Potential obstacles
<!-- What are possible obstacles that should be considered in a joint open solution?  -->

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

## Skills, Manuals and Trainings
<!-- What prior knowledge is required to use the BB efficiently, or where is training material available or who offers training?  -->
Yocto, Linux basics
[Yocto training:](https://www.yoctoproject.org/community/learn/)

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
Used in serveral embedded projects
[May 2025 vistited May 2025](https://git.yoctoproject.org/)


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
Linux, AGL

 ## Bazel compliance status
 <!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->
 TBD