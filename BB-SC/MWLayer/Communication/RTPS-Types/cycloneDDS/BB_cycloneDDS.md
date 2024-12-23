
# CycloneDDS

## BB Tags(s)

- BB-SC; BB-MU; BB-CSC; BB-CMU


## Functional Clusters

- Communication

## Layer

- MWLayer

## Known Implementation

- https://github.com/eclipse-cyclonedds/cyclonedds

## ID (unique name)

## Description

Eclipse Cyclone DDS is a very performant and robust open-source implementation of the OMG DDS specification. Cyclone DDS is developed completely in the open as an Eclipse IoT project (see eclipse-cyclone-dds) with a growing list of adopters (if you're one of them, please add your logo). It is a tier-1 middleware for the Robot Operating System ROS 2.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->

## Governance Applicable S-BB(s)

- Cyclone DDS aims at full coverage of the specs and today already covers most of this. With references to the individual OMG specifications, the following is available:

*    [DCPS](https://www.omg.org/spec/DDS/1.4/PDF) the base specification 
     *        zero configuration discovery (if multicast works)
     *        publish/subscribe messaging
     *        configurable storage of data in subscribers
     *        many QoS settings - liveliness monitoring, deadlines, historical data, ...
     *        coverage includes the Minimum, Ownership and (partially) Content profiles
*    [DDS Security](https://www.omg.org/spec/DDS-SECURITY/1.1/PDF) - providing authentication, access control and encryption - 
*    [DDS C++ API](https://www.omg.org/spec/DDS-PSM-Cxx/1.0/PDF)
*    [DDS XTypes](https://www.omg.org/spec/DDS-XTypes/1.3/PDF) - the structural type system (some [caveats](https://github.com/eclipse-cyclonedds/cyclonedds/blob/master/docs/dev/xtypes_relnotes.md) here) 
*    [DDSI-RTPS](https://www.omg.org/spec/DDSI-RTPS/2.5/PDF) - the interoperable network protocol

## Compose BB(s)

- OS/Runtime Envirnoment


## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->

## What is needed to build and run

In order to build Cyclone DDS you need a Linux, Mac or Windows 10 machine (or, with some caveats, a *BSD, QNX, OpenIndiana or a Solaris 2.6 one) with the following installed on your host:

*    C compiler (most commonly GCC on Linux, Visual Studio on Windows, Xcode on macOS);
*    Optionally GIT version control system;
*    CMake, version 3.16 or later;
*    Optionally OpenSSL, we recommend a fully patched and supported version but 1.1.1 will still work;
*    Optionally Eclipse Iceoryx version 2.0 for shared memory and zero-copy support;
*    Optionally Bison parser generator. A cached source is checked into the repository.


## Non-Functional Requirements

* Real Time
* QOS 

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

## Related Project(s)

- https://projects.eclipse.org/projects/iot.cyclonedds

## Availability of Source Code

- YES/Eclipse Public License - v 2.0

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles

## Maturity Badges
<!-- taken over from Eclipse SDV Process -->

| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Gold		| No		    | Yes/No	   | Yes/No  		   | No		 | No		   |
| Silver	| Yes		    | Yes/No	   | Yes/No 		   | Yes	 | No		   |
| Bronze	| No	    	| Yes/No	   | Yes/No    		   | No		 | Yes		   |

<!--See Definition of Badges and their Flavors 
https://gitlab.eclipse.org/eclipse-wg/sdv-wg/sdv-technical-alignment/sdv-technical-topics/sdv-process/sdv-process-definition/-/wikis/Definition%20of%20Badges%20and%20their%20Flavors 
 -->