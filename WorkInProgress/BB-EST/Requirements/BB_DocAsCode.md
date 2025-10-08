# DocAsCode
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-EST

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Requirements

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
None

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->


## Known Implementation
[Open Fast Trace](https://github.com/itsallcode/openfasttrace)

## ID (unique name)

## Description
<!-- General Description of the BB -->
This BB aims to track and manage the software requirements of the different variants of the source code.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

Several model based approaches for systems engineering and methods and tools are already established and state-of-the-art and available on the market, as well established in other industries (avionics, defense, etc.). The challenge in the automotive sector lies strongly in the variety of variants.

Driven by different product variants and the possibility of choice by the customer, this results in a high degree of combinatorics and almost exponential complexity in the subsystems.

In contrast to other industries, the automotive market with high international competition and price pressure, a wide variety of variants, functional safety and security with very long product life cycles of the vehicles in the field and the necessary software updates and hardware upgrades come together. It has become apparent that most complex, tool-based approaches to managing software requirements cannot keep pace with the capabilities of modern software development through git with the inherent capabilities of code management and automation.

If the source code of the systems is maintained in variants (branches) and developed by means of CI/CD (Continuous Integration & Development) up to the control unit, the software requirements must also be manageable and versionable, just like the source code. This then allows the transfer of customized requirements from one branch to another (merge), the comparison of requirements (diff) and the automated check that all requirements along the necessary V-model artifacts (architecture, design, code, tests, test results) are covered (tracing).

To this end, we as OEMs see it as essential to use these so-called "DocAsCode" approaches more efficiently directly in the development of ECU software internally as well as along the supply chain. Of course, this does not exempt us from overall systems engineering and model-based development, in any case we consider basic research to be less relevant there.

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
Tom Fleischmann

## Priority
<!-- High, Medium, Low -->
High

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


## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->