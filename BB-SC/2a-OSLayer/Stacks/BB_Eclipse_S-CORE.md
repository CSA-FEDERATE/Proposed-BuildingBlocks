# Eclipse S-CORE
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC, BB-EST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer, OSLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->


## Known Implementation
https://eclipse-score.github.io/

## ID (unique name)

## Description
<!-- General Description of the BB -->
Safe Open Vehicle Core is targeting to be the non-differentiating core of a software stack running on HPC ECUs of a software-defined vehicle. Consequently, this project’s scope are the “inner layers” of such a stack between a hardware abstraction as its ‘lower bound’, ‘southbound interface’ and a platform API towards vehicle function applications as its ‘upper bound’, ‘northbound interface’.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
With the upcoming of central EE architectures in vehicles, computing power has been upgraded on few central components called ‘High Performance Computers’ or HPC. Together with these computing units comes an upgrade of operating systems towards multi-threaded schedulers with memory and resource separation in processes. There is a gap between these operating systems and the application layer that requires a common interface with functions and features for applications and application domains. The sum of these common and domain-agnostic functions is generally called “Middleware”. The project uses the term “Core Software Stack” for this kind of functionality in differentiation to domain specific software stacks.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
ISO26262

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
BB Eclipse S-CORE_LOLA, BB Eclipse S-CORE_FEO, BB Eclipse_OpenSOVD

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->

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
Eclipse Foundation

## Priority
<!-- High, Medium, Low -->

## Contribution through RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
TBD

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
YES - APL-2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
various

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
1 OEM
- Abandoned
 --

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
QNX, Linux

## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->
compatible