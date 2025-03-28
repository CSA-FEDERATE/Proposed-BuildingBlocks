# RemotiveCloud
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-CEST; BB-CSC-TC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Diagnostics (could also be used for feeding vehicle data to emulators and other prototyping tools)

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
Not Specified

## Known Implementation
https://cloud.remotivelabs.com/

## ID (unique name)

## Description
<!-- General Description of the BB -->
RemotiveCloud - for sharing vehicle recordings, both for debugging purposes as well as for prototyping (feed data into e.g. ProtoPie and Android AAOS / AOSP emulators). The recordings can be made with the RemotiveBroker or some other logging devices following standard formats.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
RemotiveCloud enables an easy way of sharing recordings - upload to cloud and share with relevant people as suppliers and service providers to have a common place for vehicle network data (CAN etc.) for debugging and 3rd party application developers.

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
None

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->
None

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
Nothing, create an account and get going (there is a free tier available).

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
Nothing in addition to an account.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->
None

## Dependencies to other Clusters
<!-- Other clusters are needed. FC Security, FC Storage, …
e.g. If FC Security : Security BBs are needed but you can choose for example crypto BB-SC from company A or crypto BB-SC from company B; several compositions may work -->
None

## Vehicle API Relevant
<!-- If “Yes exists” – where – e.g. COVESA VSS 
If “No” – nothing more to do 
If “Yes, proposal for additional Signals/Information – what should be made available, and where e.g. via (COVESA) VSS/VISS -->
Yes, the output can be made in COVESA VSS / VISS format - both to make it easy for 3rd parties as well as to hide OEM proprietary info

## Author/Company
Emil Dautovic / RemotiveLabs

## Priority
<!-- High, Medium, Low -->

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
Yes, part of Playground under the COVESA umbrella. 
No active role in FEDERATE yet but there should be a good fit under WP2 projects where there is a need to collaborate in an easy way when it comes to vehicle data (from a test rig or an actual vehicle) for both debugging as well as prototyping purposes (either OEM propritary format or COVESA VSS).

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->
The core RemotiveLabs components are Commercial Closed Source but reference integrations are available as source code https://github.com/remotivelabs

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->
https://docs.remotivelabs.com/docs/category/remotivecloud

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