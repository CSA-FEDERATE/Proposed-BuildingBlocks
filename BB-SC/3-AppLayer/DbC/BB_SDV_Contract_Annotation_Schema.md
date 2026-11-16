# SDV Contract Annotation Schema

## BB Tags(s)

BB-SC

## Functional Clusters

Design-by-Contract

## Layer

AppLayer

## BB Usage

To use the schema, learn the two annotation macros from the documentation (link pending public 
release) and place them at the corresponding sites in the C source of a unit. No framework 
installation or contract-language toolchain is required to state assumptions or guarantees.

## Known Implementation

An open SDV toolchain of components: an extractor (annotation extraction from C source via 
tree-sitter), a composer (architecture editor with contract-annotation rendering), and a 
generator (integration with runtime-check, test and analysis backends). GitHub repositories 
pending public release.

## ID (unique name)

## Description

The SDV Contract Annotation Schema is a Design-by-Contract source-code convention for 
expressing Hoare-style per-function contract annotations - assumptions and guarantees - 
directly inside a unit's implementation code. A function's preconditions and postconditions are visible in the same 
place as that function's implementation - without any separate contract specification DSL or 
annotations.

The schema also covers app-level contracts: standalone contract instances placed within an 
application to constrain how the units it contains interact. These express properties that 
cannot be attributed to any single unit - most notably Wirkketten (event-chain) contracts, 
which specify the causal sequence of events flowing through a set of units to reach an 
intended system-level effect.

## Rationale

The annotation schema serves the code-first, bottom-up workflow: the unit's implementation can 
carry alongside it Hoare calculus-style contracts as extended means of specification within the 
same source. The is designed around two properties First, contract annotations are 
transparently a language extension expressed in ordinary source code, and the notation does not 
presume any particular enforcement mechanism. A block may be lowered to a runtime assertion, a 
static analysis obligation, or elided entirely in release builds, without the unit's own source 
being rewritten. Second, even complex contracts and conditions can be implemented alongside and 
in the same language as the implementation itself.

The two levels compose: per-function contracts constrain a unit's own behavior against its 
interface; app-level contracts constrain the interaction between units when they are composed. 
A unit's local assumptions and guarantees participate in the app-level obligations that reason 
across it, so a system-wide property can be discharged in part by unit-local reasoning and in 
part by composition-level reasoning.

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
Robert Rasche; Tensor embedded GmbH

## Priority
<!-- High, Medium, Low -->

## Contribution supported by RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
HAL4SDV

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
Yes / TBD (license decided at GitHub release)

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Type of API

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

## State (+ date of last change)

<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
First public release available (2026-09-21)

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

Part of an Open Bottom-Up Software Development Method for SDV: the vocabulary for asserting 
behavioral properties of functions and their compositions.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
