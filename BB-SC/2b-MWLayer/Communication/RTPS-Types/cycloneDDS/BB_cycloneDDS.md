# CycloneDDS
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC; BB-MU; BB-CSC; BB-CMU

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Communication

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage, 
trainings, skills, examples and how-to's. -->


## Known Implementation
https://github.com/eclipse-cyclonedds/cyclonedds

## ID (unique name)

## Description
<!-- General Description of the BB -->
Eclipse Cyclone DDS is a very performant and robust open-source implementation of the OMG DDS specification. Cyclone DDS is developed completely in the open as an Eclipse IoT project (see eclipse-cyclone-dds) with a growing list of adopters (if you're one of them, please add your logo). It is a tier-1 middleware for the Robot Operating System ROS 2.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
Cyclone DDS aims at full coverage of the specs and today already covers most of this. With references to the individual OMG specifications, the following is available:

    [DCPS](https://www.omg.org/spec/DDS/1.4/PDF) the base specification 
             zero configuration discovery (if multicast works)
             publish/subscribe messaging
             configurable storage of data in subscribers
             many QoS settings - liveliness monitoring, deadlines, historical data, ...
             coverage includes the Minimum, Ownership and (partially) Content profiles
    [DDS Security](https://www.omg.org/spec/DDS-SECURITY/1.1/PDF) - providing authentication, access control and encryption - 
    [DDS C++ API](https://www.omg.org/spec/DDS-PSM-Cxx/1.0/PDF)
    [DDS XTypes](https://www.omg.org/spec/DDS-XTypes/1.3/PDF) - the structural type system (some [caveats](https://github.com/eclipse-cyclonedds/cyclonedds/blob/master/docs/dev/xtypes_relnotes.md) here) 
    [DDSI-RTPS](https://www.omg.org/spec/DDSI-RTPS/2.5/PDF) - the interoperable network protocol

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
OS/Runtime Envirnoment

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
In order to build Cyclone DDS you need a Linux, Mac or Windows 10 machine (or, with some caveats, a *BSD, QNX, OpenIndiana or a Solaris 2.6 one) with the following installed on your host:

C compiler (most commonly GCC on Linux, Visual Studio on Windows, Xcode on macOS);
Optionally GIT version control system;
CMake, version 3.16 or later;
Optionally OpenSSL, we recommend a fully patched and supported version but 1.1.1 will still work;
Optionally Eclipse Iceoryx version 2.0 for shared memory and zero-copy support;
Optionally Bison parser generator. A cached source is checked into the repository.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
Real Time
QOS

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->


## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->


## Author/Company
Anonymous

## Priority
<!-- High, Medium, Low -->

## Contribution through RDI projects
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework) -->
https://projects.eclipse.org/projects/iot.cyclonedds

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
YES/Eclipse Public License - v 2.0

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
|                       | Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level     | [Gold](https://cyclonedds.io/docs/) | Notdefined       | Notdefined | Notdefined | [Gold](https://cyclonedds.io/docs/) |

## State (+ date of last change)
<!-- 
- Incubating (no code yet)
- Implementation started
- First public release available
- Used in production by 1 OEM
- Used in production by >1 OEM
- Abandoned
 -->
1 OEM
- Abandoned
 --

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
regarding details see section - What is needed to build and run

## Bazel compliance status
<!-- The S-CORE project requires all BB contributions to be ready for BAZEL compliant (https://github.com/bazelbuild/bazel)-->