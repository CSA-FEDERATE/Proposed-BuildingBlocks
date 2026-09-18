
# Model-Based Quality and Resource Management (MB-QRM)

## BB Tags(s)
BB-SC

## Functional Clusters

## Layer
MWLayer

## BB Usage
The MB-QRM framework is composed of multiple tools. First, a tool to find time-triggered schedules for data-dependent applications. Second, an embedded DSL (eDSL) to model QRM characteristics of hardware/software components that compose the to-be orchestrated system (such as the schedules obtained with the scheduling tool). Lastly, an orchestrator that finds and deploys a fitting configurations (as described in the eDSL) for the entire set of components. 

## Known Implementation
Time-triggered Application Scheduler: <git@github.com:TUE-EE-ES/APSP-toolset.git>
eDSL for QRM Modeling: <git@github.com:TUE-EE-ES/QRML-eDSL.git>

## ID (unique name)

## Description
The key component of the BB is an orchestrator managing application Qualities and platform Resources at runtime. The orchestrator selects and configures a specific system configuration given application performance requirements (e.g., requested frame rates). The orchestrator builds on computational models of applications and tools to map these applications onto the E/E architecture. A tool generating time-triggered schedules for dataflow applications is currently part of the BB.

## Rationale
In today’s world, cyber-physical systems (CPSs) are all around us. While the world changes, the need for more complex CPSs increases. However, new technological advancements come with new concerns such as energy management and real-time reliability. It is important that we effectively manage and optimize computation in CPSs to deal with these new concerns.

Quality and Resource Management (QRM) can help us optimize these new CPSs. The aim of QRM is to achieve real-time reconfiguration of the automotive platform resource utilization that aligns with the continuously changing application load. QRM integrates hardware and software abstraction models with mathematical optimization to identify system configurations that satisfy expected qualities, such as energy efficiency and real-time performance.

## Governance Applicable S-BB(s)

## Compose BB(s)

## What is needed to Design and Implement
The Haskell toolchain is needed to use the eDSL.

## What is needed to build and run
Linux (x86_64, aarch64), cgroups V2 and/or Docker, IBM CPLEX Optimization Solver, Z3 Solver, Python

## Non-Functional Requirements
Real-time Runtime

## Dependencies to other Clusters

## Vehicle API Relevant

## Author/Company
Electronic Systems Group, Faculty of Electrical Engineering, Eindhoven University of Technology (TUE)

## Priority

## Contribution supported by RDI projects

## Availability of Source Code
Yes (MIT Licence / BSD3 Licence)


## Availability of API

## Type of API

## Potential obstacles

## Maturity Badges

## State (+ date of last change)

- Incubating (no code yet) / Implementation started

## System Context

 ## Compliant to
