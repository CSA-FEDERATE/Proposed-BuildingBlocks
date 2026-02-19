
# Virtualization: Neutral Configuration Layer

## BB Tags(s)

S-BB, BB-EST

## Functional Clusters

Testing, Verification & Validation

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
Not applicable. This building block resides outside of the vehicle.

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->

## Known Implementation

AVL Virtual Studio Composer
<https://www.avl.com/en/development-speed-and-methodology/virtualization-solutions/virtual-studio>

## ID (unique name)

## Description

This building block defines a neutral configuration format for the virtualization environment of test systems (SiL, HiL, ...). The purpose of the "Neutral Configuration Layer" is to enable switching between different simulation environments and test systems without losing the effort of configuring the virtualization environment, while increasing the replicability of tests across different environments.

The "Neutral Configuration Layer" is supported by adapters, so-called "Target Converters", which enable fetching configuration information from a target test system (SiL, HiL, ...) into the neutral format and converting the neutral format into a configuration for the target system.

With each target converter onboarded, the transferability of configuration across different test systems increases.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
During Testing, Validation & Verification workflows, an artifact (e.g., a software component) will go through several stages of testing (unit tests, integration testing in simulation, integration testing with real hardware). For each of those environments, the remaining part of the system that is not present as real hardware or as a concrete component must be substituted by either rest-bus simulation or complex vehicle simulation.

There are two major motivations:

- Generate the ability to carry over the virtualization environment (or parts of it) from one test system to the next (e.g., from SiL to HiL).
- Create (or pull) the virtualization configuration from one test system and, using the neutral configuration, be able to run it anywhere (e.g., pull from one HiL system, execute on another HiL system).

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

AVL List GmbH

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
No – Commercial Closed Source.

Two future options under investigation:

- Option 1: Create an open-source ecosystem from the target converter adaptors.
- Option 2: Standardize the neutral configuration layer.

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
No - Commercial.

## Type of API
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->

- CLI
- REST API

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

## Compliant to
 <!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->