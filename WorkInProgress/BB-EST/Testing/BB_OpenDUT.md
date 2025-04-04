# OpenDUT 
## BB Tags(s)
BB-EST, BB-CEST, BB-SC-TC, BB-CSC-TC

## Functional Clusters
(Explanation: in which Functional Cluster the BB be located; if none of the existing fit new required)

## Layer
MWLayer

## BB Usage
<!-- example on how to use BB or link to documentation -->

## Known Implementation
Github repo: https://github.com/eclipse-opendut/opendut

## ID (unique name)

## Description
Eclipse openDuT provides an open framework to automate the testing and validation process for automotive software and applications in a reliable, repeatable and observable way. Eclipse openDuT is hardware-agnostic with respect to the execution environment and accompanies different hardware interfaces and standards regarding the usability of the framework. Thereby, it is supporting both on-premise installations and hosting in a cloud infrastructure. Eclipse openDuT considers an eventually distributed network of real (HIL) and virtual devices (SIL) under test. Eclipse openDuT reflects hardware capabilities and constraints along with the chosen test method. Test cases are not limited to a specific domain, but it especially realizes functional and explorative security tests.

## Rationale
Main Use Case are:
(Fully automated) grey-box tests for single ECUs or clusters of ECUs
Execution of tests over distributed test benches
Realization of functional and explorative tests
Coverage of Complete Security attack scenarios
Easy interfacing and usability of the framework (Compatibility with external protocols, modularization, …)
Observation of the test setup to verify if the test has been effective.
Cloud/on-premises/hybrid deployments
Adaption and full functional integration of 3rd party components (OSS, proprietary/ private source)

## Governance Applicable S-BB(s)
Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system 
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X

## Compose BB(s)
E.g. BB-SC StateManagement
BB is a composition of other BBs

## What is needed to Design and Implement
We expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language 

Linux development environment, 
Peers & Client: ARM32/64, x86_64
Server: x86_64
Programming language: Rust
Test environment: THEO

## What is needed to build and run
NetBird, Wireguard, TURN Sever, Keycloak, Linux-based OS, Cannelloni for CAN support, telemetry stack (Promtail, Loki, Prometheus, Tempo, Grafana), …

## Non-Functional Requirements
With respect to Safety, Security,
Encrypted connections between clients, server and peers

## Dependencies to other Clusters
Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are  needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work

## Vehicle API Relevant
“No”

## Author/Company
Anonymous

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value, 
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework

## Availability of Source Code
Yes / Apache License Version 2.0

## Availability of API
Yes / Apache License Version 2.0

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