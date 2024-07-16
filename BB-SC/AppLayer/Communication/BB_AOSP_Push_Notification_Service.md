
# AOSP Push Notification Service

## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Communication

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
AppLayer

## Known Implementation

<https://novu.co>

## ID (unique name)

## Description
<!-- General Description of the BB -->
This work package aims to align on a common Android Open Source Project (AOSP) push notification service (PNS). Due to the heterogenous AOSP landscape, the solution shall be defined as a protocol that is designed in a decentralized way allowing implementing parties to choose between hosting their own PNS or using an existing one.
To reduce fragmentation and to allow 3rd parties to build once and deploy anywhere, the protocol shall be guaranteed to work regardless of the underlying implementation. To help developers use the new standardized protocol, a reference implementation shall be provided.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Enable 3rd party Android apps to deliver messages, receive incoming VOIP calls or to give updates in a running app.  
Lots of apps rely on being able to send messages to their clients to deliver messages or incoming VoIP calls. Because Android apps can be killed by the system at any time, they cannot rely on being able to communicate with their backend to receive these messages. To enable these use cases, a standardized PNS for AOSP (outside of Google Automotive Services GAS) is necessary and will be provided as part of this work package.  

Repo: could be an enhancement of repo on
<https://github.com/UnifiedPush>,  

Technologies: Android Automotive OS, WebPuch Protocol, UnifiedPush.  

Partners: COVESA members, UnifiedPush

## Governance Applicable S-BB(s)
<!-- Reference to e.g. UN/EU CRA Cyber Resilience Act; UNECE 156 - Software update and software update management system
Reference to defined S-BB(s) 
Reference to e.g. IS026262, AUTOSAR Spec. X -->
Android Automotive OS, WebPuch Protocol, UnifiedPush

## Compose BB(s)
<!-- Link to required BB(s) 
E.g. BB-SC StateManagement 
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
BB Reference implementation  
New standardized protocol  

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

Anonymous

## Priority
<!-- High, Medium, Low -->
until 30.6.2025

## Related Project(s)
<!-- If Yes – e.g. The BB should be used/added in the Eclipse Blueprint A – for demo purposes, show added value,
If No – Project Proposal (e.g. WP4 in FEDERATE, or in the SDV EcoSystem Community Framework -->
See Google Automotive Services FAS  
<https://github.com/UnifiedPush>  
SHIFT2SDV

## Availability of Source Code
<!-- Yes / License (e.g. Yes/MIT) 
No – Commercial Closed Source -->

## Availability of API
<!-- Yes / License (e.g. Yes/Apache 2.0)
No - Commercial -->

## Potential obstacles
