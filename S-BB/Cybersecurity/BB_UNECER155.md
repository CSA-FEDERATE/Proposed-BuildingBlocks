
#  UN Regulation No. 155 - Cyber security and cyber security management system

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->

S-BB

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->

## Known Implementation

https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security

## ID (unique name)

## Description
<!-- General Description of the BB -->

1. Scope
 
1.1 This Regulation applies to vehicles, with regard to cyber security, of the
Categories M and N.

This Regulation also applies to vehicles of Category O if fitted with at least
one electronic control unit.

1.2. This Regulation also applies to vehicles of the Categories L6 and L7 if equipped
with automated driving functionalities from level 3 onwards, as defined in the
reference document with definitions of Automated Driving under WP.29 and
the General Principles for developing a UN Regulation on automated vehicles
(ECE/TRANS/WP.29/1140).

1.3. This Regulation is without prejudice to other UN Regulations, regional or
national legislations governing the access by authorized parties to the vehicle,
its data, functions and resources, and conditions of such access. It is also
without prejudice to the application of national and regional legislation on
privacy and the protection of natural persons with regard to the processing of
their personal data.

1.4. This Regulation is without prejudice to other UN Regulations, national or
regional legislation governing the development and installation/system
integration of replacement parts and components, physical and digital, with
regards to cybersecurity.

[source unece.org](https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf)

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

2. Definitions

For the purpose of this Regulation the following definitions shall apply:

2.1. "Vehicle type" means vehicles which do not differ in at least the following
essential respects:

    (a) The manufacturer’s designation of the vehicle type;

    (b) Essential aspects of the electric/electronic architecture and external interfaces with respect to cyber security.

2.2. "Cyber security" means the condition in which road vehicles and their
functions are protected from cyber threats to electrical or electronic
components.

2.3. "Cyber Security Management System (CSMS)" means a systematic risk-based
approach defining organisational processes, responsibilities and governance to
treat risk associated with cyber threats to vehicles and protect them from cyber-
attacks.

2.4. "System" means a set of components and/or sub-systems that implements a
function or functions.

2.5. "Development phase" means the period before a vehicle type is type approved.

2.6. "Production phase" refers to the duration of production of a vehicle type.

2.7. "Post-production phase" refers to the period in which a vehicle type is no
longer produced until the end-of-life of all vehicles under the vehicle type.
Vehicles incorporating a specific vehicle type will be operational during this
phase but will no longer be produced. The phase ends when there are no longer
any operational vehicles of a specific vehicle type.

2.8. "Mitigation" means a measure that is reducing risk.

2.9. "Risk" means the potential that a given threat will exploit vulnerabilities of a
vehicle and thereby cause harm to the organization or to an individual.

2.10. "Risk Assessment" means the overall process of finding, recognizing and
describing risks (risk identification), to comprehend the nature of risk and to
E/ECE/TRANS/505/Rev.3/Add.1545 determine the level of risk (risk analysis), and of comparing the results of risk
analysis with risk criteria to determine whether the risk and/or its magnitude is
acceptable or tolerable (risk evaluation). 

2.11. "Risk Management" means coordinated activities to direct and control an
organization with regard to risk.

2.12. "Threat" means a potential cause of an unwanted incident, which may result in
harm to a system, organization or individual.

2.13. "Vulnerability" means a weakness of an asset or mitigation that can be
exploited by one or more threats.

[source unece.org](https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf)

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->

Cybersecurity

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

## Priority
<!-- High, Medium, Low -->

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