
# MRTCCSL

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-EST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Time

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
Not applicable (can describe timing behaviour at any level).

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->
MRTCCSL allows to gradually describe (refine) timing specification of a system from high-level requirements to operation (communication and execution assumptions => application and hardware components => execution time and latency timing budgets => representative simulation).

## Known Implementation
https://github.com/PaulRaUnite/mrtccsl/

## ID (unique name)

## Description
<!-- General Description of the BB -->
MRTCCSL is a declarative constraint language on logical clocks. Logical clocks represent events in the modelled system and by using constraints in a specification, the designer can describe the overall behaviour of the system by the intersection of the individual constraint behaviours. 
As a constraint language, existence of a valid solution is not guaranteed and should be analysed. In a case, when the MRTCCSL specification represents a system specification, non-existence of a solution indicates a non-consistency of the system requirements.

Unique features of MRTCCSL in relation to CCSL are real-time constraints and stochastic annotations. Using the real-time constraints, one can refine an abstract specification (i.e. an architecture description) to real-time behaviour, and stochastic annotations to refine up to a operational model (simulation representative of the system).
The real-time behaviour and the operational model then can be explored by a simulation to detect conflicts between high level requirements and timing budgets, or to evaluate operational behaviour, for example, via functional chains.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Detecting non-consistency between system requirements and assumptions early while gradually making more precise the timing specification.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
None

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
None

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
No preliminary information about the system is needed.

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
OCaml and some libraries.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
None

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->
None

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
No

## Author/Company

Pavlo Tokariev / Inria

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
None

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes / Apache License 2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes / Apache License 2.0

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
Command Line Interface/Library API (but no backward compatibility effort is made)

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
| Level		| Bronze | No 		   | No		   | Bronze	 | Bronze |

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->

Public (June 2026)

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
Any system that support OCaml language and gmplib.

## Compliant to
 <!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->