# SDV Architecture Description Format

## BB Tags(s)

BB-EST

## Functional Clusters

Architecture

## Layer

AppLayer

## BB Usage

To use the format, consult the documentation for its concepts and tag reference (link pending 
public release) and produce `.ocyml` files through the SDV toolchain.

## Known Implementation

An open SDV toolchain of components: an extractor (generates unit descriptions from C 
source), a composer (interactive editor for architecture files), and a generator (produces 
middleware bindings from architecture files). GitHub repositories pending public release.

## ID (unique name)

## Description

The SDV Architecture Description Format is a text-based, human-readable exchange format for the 
architecture of a vehicle-software system. Files use the `.ocyml` extension and are written in 
a YAML dialect. The scope of the format covers four categories of declaration:

- functional description of an application and its units, with typed role-tagged ports on each unit (`!App`, `!Unit`, `!<role>`)
- non-functional contract modeling within an application (`!Contract`)
- hardware-, network and other abstraction annotations of the target platform (`!Machinery`)
- bundling of application units into deployment nodes (`!Deployment`)

The format does not describe type information (data types, function prototypes); these live in 
the implementation source of the units and are referenced from `.ocyml` by name.

The full format reference is published separately (see BB Usage above).

## Rationale

Four properties motivate the choice of a YAML dialect: the format is composable across many 
files, diffable in the same way source code is, concise where XML would be verbose, and 
extensible through the tag mechanism (though at this stage of the project, extension is 
reserved for the format's maintainer).

The format describes composition without describing implementation: type information (data 
types, function prototypes) lives in the implementation source of the units and is referenced 
by name only. This is a deliberate departure from formats such as AUTOSAR ARXML, where every 
type must be modeled up front and the implementation must comply with the modeled definition. 
In `.ocyml`, a type authored in code becomes part of a unit's architectural interface by name, 
without a separate modeling step.

The architecture assembled in an `.ocyml` file is topic-centered. A topic can be thought of as 
an abstract link between components. Binding between unit instances happens simply by naming a 
shared topic, and no single point in the format authoritatively defines that topic. Instead it 
collects its characteristics from all the places of usage.

The set of declared concepts is deliberately designed to compose, so that a wide range of 
architectural patterns can be assembled from the same primitives; communication patterns and 
channels emerge from the composition rather than being prescribed onto it.

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
First public release available

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

Part of an Open Bottom-Up Software Development Method for SDV: the text-based exchange 
format that carries a composed application's architecture.

## Compliant to
<!-- The BB is designed in a way that enables usage or integration into one of the targets listed. That includes use of the recommended processes, APIs, tool chains,.....-->
