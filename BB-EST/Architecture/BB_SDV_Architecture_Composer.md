# SDV Architecture Composer

## BB Tags(s)

BB-EST

## Functional Clusters

Architecture

## Layer

AppLayer

## BB Usage

Launch the composer with an `.ocyml` file to open, or with no argument to start from an empty 
diagram. Full user documentation is published separately (link pending public release).

## Known Implementation

A Python 3 desktop application (GTK4, Cairo) in an open SDV toolchain. GitHub repository 
pending public release.

## ID (unique name)

## Description

The SDV Architecture Composer is a graphical desktop application for editing the composition of 
a vehicle-software application as a two-dimensional diagram. The tool reads and writes files in 
the SDV Architecture Description Format. Its scope covers:

- placing typed instances (functional or otherwise) and authoring bindings between them, which
  creates the topics they share
- collecting instances into applications (`!App`)
- collecting instances into deployment nodes (`!Deployment`), which doubles as the deployment
  workflow
- arranging instances in a 2D diagram, assisted by a force-directed layout
- authoring `!Machinery` attributes and placing driver instances

The diagram is drawn on an infinite canvas navigable by pan and zoom, on which elements are 
placed, connected and assigned through drag and drop. A "focus perspective" feature can be 
invoked to temporarily re-lay-out a selected portion of the diagram for a specific task 
(review, binding-edit, annotation-edit); the authored layout is restored on dismissal.

The full user documentation is published separately (see BB Usage above).

## Rationale

The composer is designed to feel like sketching rather than operating a CAD system. Interaction 
is direct rather than mediated by forms and dialogs, and the tool is not finicky about precise 
element placement; the automatic layout absorbs the imprecision.

The composer sits within a rapid-prototyping workflow: incremental changes to the architecture 
file authored elsewhere - by a scripted transformation or by the associated extractor - are 
handled gracefully without resetting the diagram or disturbing it too much. The tool's design 
keeps the door open for that loop to be completed as the toolchain matures.

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

HAL4SDV

## Availability of Source Code

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

Part of an Open Bottom-Up Software Development Method for SDV: the graphical editor for 
composing an application from typed units and their bindings.

## Compliant to

<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
