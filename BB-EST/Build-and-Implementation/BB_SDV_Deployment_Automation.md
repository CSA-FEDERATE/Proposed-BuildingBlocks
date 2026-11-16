# SDV Deployment Automation

## BB Tags(s)

BB-EST

## Functional Clusters

Architecture

## Layer

AppLayer

## BB Usage

Run the automation on an `.ocyml` file with a chosen template set to produce the runtime code 
for a target. Full command-line documentation is published separately (link pending public 
release).

## Known Implementation

A Python 3 command-line tool built on the `tempy` template engine, in an open SDV toolchain. 
GitHub repository pending public release.

## ID (unique name)

## Description

The SDV Deployment Automation is a command-line tool that reads an SDV Architecture 
Description file together with the corresponding unit source code, and produces deployable 
binaries for a target platform, with the basic software stack configured automatically from 
the architecture rather than authored by hand. Its scope covers:

- middleware bindings for the topics declared in the architecture (pub/sub subscriptions, 
  remote-invocation stubs, shared-memory accessors, depending on the chosen transport)
- dispatch and scheduling scaffolding - main loops, event handlers, and task bodies that 
  invoke each unit's runnables at the right times
- operating-system configuration for the target - task priorities, stack sizes, IPC objects, 
  startup sequences
- assembly of the generated code and unit source into a self-contained build environment, 
  and execution of the build to produce the target binaries

The output and toolchain integration are template-driven; swapping template sets swaps target 
platforms without changing the tool itself. The full command-line reference is published 
separately (see BB Usage above).

## Rationale

The automation is the code-side counterpart of the SDV Unit Specification Extractor: where 
the extractor derives unit descriptions from source, the automation derives everything else 
needed to turn those units and their architecture into runnable binaries. A developer working 
in the code-first workflow authors the units and their contracts by hand, and both the 
architecture description above the units and the scaffolding around them are derived - 
nothing is authored twice.

Scaffolding here means the full path from `.ocyml` and unit source to deployable binaries: 
generating the runtime code, assembling a self-contained build environment, and running the 
build. One tool covers the entire pipeline end-to-end.

The template mechanism is the tool's target-platform boundary. Application developers use the 
automation as a fixed pipeline; developers adding support for a new middleware, RTOS, or 
hardware family write template sets that the automation consumes. The tool itself does not 
carry per-target knowledge, so an application project can move between targets without 
rewriting its architecture or its units.

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
<!-- Web API, Library/Framework API, Operating System API, Database API, Remote API, Hardware API, Other -->
Library/Framework + Other

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

Part of an Open Bottom-Up Software Development Method for SDV: produces deployable binaries 
from the composed architecture and unit sources, with the basic software stack configured 
automatically.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
