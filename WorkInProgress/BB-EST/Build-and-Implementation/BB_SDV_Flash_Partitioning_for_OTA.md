# SDV Flash Partitioning for OTA

## BB Tags(s)

BB-EST

## Functional Clusters

Build-and-Implementation

## Layer

HWLayer

## BB Usage

Launch the tool with a target board selected and one or more firmware images to flash; 
partitions that are unchanged since the previous programming run are not rewritten. Full user 
documentation is published separately (link pending public release).

## Known Implementation

A Python 3 desktop application (GTK4, openocd for target programming) in an open SDV 
toolchain. Companion on-target bootloaders (for RIOT-based and FreeRTOS-based systems) support 
the partition scheme at runtime. GitHub repository pending public release.

## ID (unique name)

## Description

The SDV Flash Partitioning for OTA is a desktop tool that manages MCU firmware as a 
chain of partitions and re-links and re-programs only the partitions that have changed since 
the previous run. Its scope covers:

- laying out the target's flash as a chain of partitions in the on-flash ORX metadata format, 
  each an independently linkable block of firmware
- adding new blocks whose external symbol references resolve against the symbols exported by 
  existing blocks
- tracking inter-block symbol dependencies, so that a change to one block triggers re-linking 
  of every block that depends on it (dependency cycles are linked as a unit)
- programming only the newly built or re-linked blocks to the target board over a debug probe

The full user documentation is published separately (see BB Usage above).

## Rationale

MCU firmware flashing is slow, and flash memory has a limited number of write cycles. 
Reflashing the entire image on every code change - the default in most embedded toolchains - 
is wasteful in both time and hardware lifetime, and it discards the state accumulated in 
unrelated regions such as configuration or persistent data.

The tool provides incremental linking and programming for ELF-based MCU firmware: developers 
can build, link and program only the pieces of the software that are changing, against a 
steady base of unchanging pieces. The mechanism operates at the ELF symbol level and is not 
specific to any one runtime or application architecture. In practice this shortens the 
edit-flash-run cycle to something closer to a native-software workflow, and reduces flash 
wear proportionally to the fraction of firmware that changed. The same mechanism supports 
partial over-the-air updates of individual applications in deployed vehicles: an app 
partition can be updated in isolation without reflashing unrelated firmware.

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

Implementation started (2026-09-22)

## System Context

Part of an Open Bottom-Up Software Development Method for SDV: enables partitioned firmware 
deployment and partial field updates of applications.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
