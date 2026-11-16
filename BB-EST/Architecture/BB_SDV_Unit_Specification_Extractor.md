# SDV Unit Specification Extractor

## BB Tags(s)

BB-EST

## Functional Clusters

Architecture

## Layer

AppLayer

## BB Usage

Run the extractor over one or more C source files and redirect its stdout to an `.ocyml` file, 
or pass an existing `.ocyml` file to update it in place. Full command-line documentation is 
published separately (link pending public release).

## Known Implementation

A Python 3 command-line tool (tree-sitter) in an open SDV toolchain. GitHub repository 
pending public release.

## ID (unique name)

## Description

The SDV Unit Specification Extractor is a command-line tool that reads C source files with 
function code that uses the SDV Function API and Contract Annotations Schema, and produces the 
corresponding software unit declarations in the SDV Architecture Description Format. Its scope 
covers:

- detection of typed communication API accesses (communication-role, datatype, handle) - e.g. 
  `I(brake_pedal)` in the source yields the definition of an input port in the unit 
  description, with the data type automatically inferred from the source.
- extraction of contract annotations from unit implementations - e.g. `A(name) { ... }` blocks 
  become that unit's assumptions and `G(name) { ... }` blocks become its guarantees

The full reference is published separately (see BB Usage above).

## Rationale

The extractor enables the code-first workflow that the SDV Function API Schema and SDV Contract 
Annotation Schema are designed for: unit interfaces and their contract annotations are authored 
in C source as the bottom-level source of truth for a unit's shape and specification, and the 
architecture description is derived from that source rather than authored in parallel. This 
removes the manual synchronization burden that arises when an architecture model and its 
implementation are maintained as two separate authoritative artifacts.

The tool operates by analysing the C source code for API or Contract patterns with a resilient 
parser so the extraction works even on in-progress or incomplete code without requiring the
code to build completely.

Updates are incremental via a user-chosen diff tool that merges the new declarations into an 
existing architecture file, so anything not derived from source persists across regenerations.

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

Other

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
First public release available (2026-09-22)

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

Part of an Open Bottom-Up Software Development Method for SDV: derives unit descriptions 
from their C source, keeping the architecture in step with the code.

## Compliant to

 <!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
