# Generation ROS 2 from SYSML
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-EST, BB-CEST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Build-and-Implementation

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->
The Robotics customization of the open source Eclipse modeling tool Papyrus provides a UML-based robotic modeling language inspired by the abstractions of the RobMoSys project. The language supports several viewpoints, for instance, the specification of services, components, and a system assembly. The former should be done by an expert in robotics or the automotive domain. Having common service definitions enables interoperability between components. The tool comes with libraries that include services defined by the standard ROS2 message packages, which may also be useful in the automotive domain. By using the export capabilities from VSS (BB_VSS_UML_SysML), it would be possible to provide libraries with the corresponding data types. The tool can also generate C++ or Python code (skeletons) as well as build and launch files from the robotic definitions
See https://gitlab.eclipse.org/eclipse/papyrus/org.eclipse.papyrus-robotics/-/wikis for documentation on the UML version. A SysMLv2 version is under construction

## Known Implementation
https://gitlab.eclipse.org/eclipse/papyrus/org.eclipse.papyrus-robotics/

## ID (unique name)
BB_SYSML_ROS2

## Description
<!-- General Description of the BB -->
The Robotics customization of the open source Eclipse modeling tool Papyrus provides a UML-based robotic modeling language inspired by the abstractions of the RobMoSys project. The language supports several viewpoints, for instance, the specification of services, components, and a system assembly. The former should be done by an expert in robotics or the automotive domain. Having common service definitions enables interoperability between components. The tool comes with libraries that include services defined by the standard ROS2 message packages, which may also be useful in the automotive domain. By using the export capabilities from VSS (BB_VSS_UML_SysML), it would be possible to provide libraries with the corresponding data types. The tool can also generate C++ or Python code (skeletons) as well as build and launch files from the robotic definitions
See https://gitlab.eclipse.org/eclipse/papyrus/org.eclipse.papyrus-robotics/-/wikis for documentation on the UML version. A SysMLv2 version is under construction

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The potential use of the tool is twofold:

- The building block provides the generation of code skeletons and ROS 2 message packages from SysML v2. If the system architecture and data models are present in SysML, the tool facilitates targeting ROS 2 middleware
- The building block provides model libraries for services/data definitions, such as those in ROS 2 message packages, in a standardized format, i.e., currently UML and SysML v2 (the latter is under development, results are already available for ROS 2 standard messages)enables UML or SysML (once implemented) system definition tools to reference these services. For instance, the transversal activity A1 of the project Shift2SDV proposes the use the definition of some ROS 2 message packages.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
By using the export capabilities from VSS (BB_VSS_UML_SysML), it would be possible to provide SysML v2 libraries for VSS services.

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
The existing UML based Papyrus customization consists of a set Eclipse plugins. Development is done in the Eclipse SDK with JDK, Xtend IDE and a base Papyrus installed.

In case of SysML v2, the use of the tool Eclipse SysON is forseen. Development can be done via VS-code or Eclipse (details will follow)

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
The existing UML based Papyrus customization can be installed into an Eclipse SDK (standalone versions and an update site is provided).

In case of SysML v2, the use of the tool Eclipse SysON is forseen. This tool consists of a front-end running in the browser and a backend that can be installed via docker compose.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
VSS, ROS2 subset selected from TA-BB-A1 (Shift2SDV)

## Author/Company
CEA

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
Shift2SDV

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes, EPL-v2

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes, EPL-v2

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
Library/Framework API

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
| | Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --- |:---:|:---:|:---:|:---:|:---:|
| Level | [Bronze](https://gitlab.eclipse.org/eclipse/papyrus/org.eclipse.papyrus-robotics/-/wikis) | Gold | Gold | Gold | Gold |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
Implementation started (2026-10-09)

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
With respect to the state above, keep in mind that there are two different implementations:
- A quite mature Eclipse Desktop for UML
- An upcoming one extending/customizing the Web-based tool Eclipse SysON. Implementation has started, but has not been made public yet.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
none stated
