
# SDVML

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-EST, S-BB

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Time

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
AppLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->

General approach:
- user specifies the architecture of the application and required VSS signals and their timing characteristics (execution time, latency, period, etc) and functional chains of interest;
    - (optionally) the requirements on functional chains (of form "reaction time is less than 30ms with probability 95%") 
- the system is then simulated, and the reaction time is computed as a probability distribution;
- the requirements are verified on the reaction time and reported to the user in the VS Code interface;
- in the case of non-satisfaction, the user can inspect the reaction time histograms and individual contributions of each component to it
- once a change is proposed, the analysis can be rerun to assess if the new solution is better.

## Known Implementation
https://github.com/jdeantoni/SoftwareDefinedVehicleModelingLanguage/

## ID (unique name)

## Description
<!-- General Description of the BB -->
SDVML is a domain-specific language and development environment that describes SDV applications based in Service-oriented Architecture. This approach explicitly models timing uncertainties stemming from the hardware, hardware abstraction layer (HAL), and application software. To formalize the extra-functional requirements essential for safety verification, the system description is annotated with functional chains and their respective reaction-time constraints. The framework executes simulations to generate traces, allowing for the identification of functional chain instances and the derivation of reaction-time and data-age distributions. These results are automatically verified against predefined requirements, with the output provided to the user via an open-source Visual Studio Code extension.

The semantics and implementation of the framework relies on two independent formalisms: [MRTCCSL](https://github.com/PaulRaUnite/mrtccsl), a language of logical and real-time constraints, and specifications of functional chains.

Technical aspects:
- the VS Code extension generates an MRTCCSL specification and functional chain descriptions from the description of the system;
- MRTCCSL implementation simulates the provided description as timed traces;
- functional chains are identified in the generated traces and reaction time distribution is computed;
- the analysis is driven by ninja build system, thus certain description changes (adding functional chains or changing requirements) are performed without resimulation.

Related publications:
- Pavlo Tokariev, Irman Faqrizal, Julien Deantoni. Understandable Timing Analysis of Service-Oriented Architecture Components in Software-Defined Vehicle. 20th International Conference on Information and Communication Technologies in Education, Research, and Industrial Applications (ICTERI-2025), Sep 2025, Nice, France. <[hal-05224373](https://inria.hal.science/hal-05224373)>
- Pavlo Tokariev, Yosri Ayari, Julien Deantoni. Predictable Modelling and Analysis of Software-defined Vehicle Implementations. VPPC 2026 - 23rd IEEE Vehicle Power and Propulsion Conference, Oct 2026, Lyon, France. <[hal-05747388](https://inria.hal.science/hal-05747388)>

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
The framework allows to analyse high-level reaction time of SDV applications. By experimenting with timing budgets on both application components and HAL signals, the designer can discard early solutions that do not satisfy the requirements or when reaction time probability mass is close to the requirement deadline, thus an update to the HAL can make the functionality unsafe.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
None

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
Uses [BB-EST MRTCCSL](/BB-EST/Design/BB_MRTCCSL.md).

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
Software-defined vehicle should correspond to the modelled architecture: Service-oriented architecture with VSS interface for platform access.
The designer need to be aware of the timing properties of the specified elements, or have a "good enough" guess about them.

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
As a development tool, no requirements on operation of the vehicle.

VS Code and JavaScript are required to build the framework, MRTCCSL porject is needed to perform the simulations and functional chain analysis. Linux is recommended as the only tested platform.

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
Yes, VSS signals are taken as basis for the middleware model.

## Author/Company
Julien Deantoni, Pavlo Tokariev, Irman Faqrizal / Inria

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes / Eclipse Public License 2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
Yes / Eclipse Public License 2.0

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
As a VSCode extension we expose the commands that the user interface uses. 

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
| Level		| Silver | No 		   | No		   | No	 | No |

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->

Public (Nov 2025)

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

No specific assumptions are made on the software or hardware of the described systems.

## Compliant to
 <!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
