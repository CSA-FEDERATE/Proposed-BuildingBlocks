# Deterministic Network Configuration and Enforcement (DNCE)
## BB Tags(s)
<!-- Tag(s) define in which area(s) (cloud, in-vehicle) the BB is executed, and what type of BB it is (tool, process, microservice) -->
BB-SC 

## Functional Clusters
<!-- In which Functional Cluster the BB be located; if none of the existing fit new required -->
Communication (Deterministic Networking / Network Resource Management)

## Layer
<!-- AppLayer, MWLayer, OSLayer, HWLayer -->
MWLayer

## BB Usage
<!-- Example on how to use BB or link to documentation. Should include code snippets, information about usage,
trainings, skills, examples and how-to's. -->
The building block targets effective and efficient deterministic communication for time-critical traffic. It can be used for three purposes, each backed by an open-source repository.

**1. Model and evaluate the network (INSIM).** The user supplies a network topology and a stream set, either from the built-in automotive benchmark suite or through the GUI. INSIM generates a TSN configuration, evaluates it through an analytical delay model or an OMNeT++ discrete-event simulation, and reports success rate, end-to-end delay, and link utilization. Custom schedulers and analytical models are added through a plug-in interface without modifying the core, so alternative configuration strategies can be compared under identical timing semantics. A hosted web application is linked from the repository README for immediate access.

**2. Compute a schedule (TSN-DRL-TAS or SbDN).** Two configuration strategies are provided as INSIM plug-ins.
- *Learning-based TAS scheduling* targets networks built from TSN-capable switches. A graph neural network encodes topology and workload, a policy trained with Proximal Policy Optimization emits a compact phase-and-budget template, and a deterministic compiler expands that template into IEEE 802.1Qbv-compliant per-port gate control lists. Inference is a single forward pass, so schedules are recomputed in milliseconds when traffic patterns change.
- *Source-based scheduling (SbDN)* targets networks built from commodity switches. A central controller composed of three cooperating agents assigns collision-free release times for time-critical data flows, synthesizes a source-side gate control list covering all time-critical flows, and configures credit-based shaping for best-effort traffic. Two methods are offered: Temporal Network Partitioning for pure FIFO switches, and Traffic Prioritization for switches with strict-priority queuing.

**3. Enforce configurations (V-TSN).** SbDN and TSN configurations are pushed to the source endpoints and network switches, which enforce release times, gating, and credit-based shaping locally. Where the platform provides no TSN support, V-TSN supplies the enforcement layer entirely in software: gPTP synchronization, a virtual Time-Aware Shaper, and a virtual Credit-Based Shaper, running as ordinary user-space components on Linux endpoints and on a virtual switch. The same V-TSN layer can be used at design time to execute the unmodified application stack in real time before any target hardware exists.

## Known Implementation
- https://github.com/TUE-EE-ES/TSN-INSIM — simulation, evaluation, and benchmarking platform
- https://github.com/TUE-EE-ES/TSN-DRL-TAS — learning-based Time-Aware Shaper scheduler
- https://github.com/TUE-EE-ES/SbDN — source-based deterministic networking on commodity switches
- https://github.com/TUE-EE-ES/V-TSN — software-defined TSN overlay for general-purpose networks

## ID (unique name)
DeterministicNetworkConfigurationAndEnforcement

## Description
<!-- General Description of the BB -->
DNCE provides deterministic, bounded-latency communication for in-vehicle networks across the full range of available switching hardware, from fully TSN-capable fabrics to commodity Ethernet with no scheduling support, and without requiring the network configuration to be frozen before runtime.

The building block decouples three concerns that conventional TSN deployments bind tightly together: where a schedule is computed, where it is enforced, and how it is validated. Computation is performed by a central software controller, either by a learning-based scheduler or by a set of cooperating scheduling agents. Enforcement is placed wherever the available hardware allows, at the switch egress ports where TSN support is present, at the source endpoints where it is not, or entirely in software where the underlying network offers no hardware-supported deterministic reservations at all. Validation is performed analytically or in simulation before any configuration reaches the network, or in a controlled emulation environment using V-TSN. Because the three concerns are separated, the same configuration workflow and the same evaluation framework apply to TSN-capable switches with per-port gate control, to commodity switches with strict-priority queuing, to pure FIFO switches, and to general-purpose or virtualized networks.

The block covers the full path from design-time evaluation to runtime enforcement. A modular simulation and benchmarking platform provides a common evaluation ground with a plug-in interface for custom schedulers and performance models. Two scheduling strategies are supplied: a learning-based scheduler that configures the Time-Aware Shaper adaptively at runtime on TSN-capable networks, and a source-based scheduler that computes release times, source-side gating, and credit-based shaping with formal end-to-end deadline guarantees on commodity networks. A software TSN overlay implements gPTP, TAS, and CBS in user space, serving both as the endpoint enforcement layer and as a real-time validation environment for systems whose target hardware is not yet available.

## Rationale
<!-- Explanation why we need the BB; what problem want to be solved -->
Software-defined vehicles concentrate perception, control, and actuation on a shared Ethernet backbone, where missed deadlines are safety failures rather than performance degradations. TSN is the industry answer, but it charges two prices that limit adoption.

The first is configuration cost. Computing valid TAS schedules is NP-hard, and schedules are traditionally synthesized offline. When traffic patterns shift, when software updates introduce new functions, or when after-market modifications change the workload, the configuration must be recomputed and redeployed across every affected switch. Because that transition cannot in general be performed atomically across multiple devices, many deployments avoid runtime reconfiguration altogether. This fundamentally limits flexibility in exactly the systems that need it most.

The second is infrastructure cost. TSN-capable switches carry roughly a sevenfold price premium over commodity Ethernet switches, and adoption is not incremental: every switch on the path of a time-critical flow must participate in the schedule, so the entire switching fabric has to be replaced. In an industry where design decisions turn on tens of euros per vehicle, this is the binding constraint on deployment, and no amount of scheduling improvement addresses it.

DNCE addresses both, without assuming a particular class of switching hardware. Learning-based scheduling reduces configuration of TSN-capable networks to a single inference pass, fast enough for runtime adaptation. Source-based enforcement makes deterministic communication achievable on commodity switches, which remain unaware of the schedule and therefore require no reconfiguration. A software TSN overlay removes the dependency on hardware availability during development and validation, and offers a deployment option where relaxed timing is acceptable. Together, these allow the level of hardware support, and the resulting strength of the timing guarantee, to be chosen per system rather than imposed by the architecture.

## Governance Applicable S-BB(s)


## Compose BB(s)
<!-- Link to required BB(s)
E.g. BB-SC StateManagement
BB is a composition of other BBs -->

## What is needed to Design and Implement
<!-- e.g. we expect to have a certain HW capability and or SW environment or Tool support, or a documentation, or an extra audit, or Test, or Compiler, or Prog. Language, … -->
Python runtime with a Pytorch framework for the learning-based scheduler. Each repository contains its own README, configuration examples, and the benchmark scenarios used in the corresponding publication.

## What is needed to build and run
<!-- e.g. we expect to have a certain HW capability, or Runtime Environment, or Pre-configuration, or Code-signing, or Test, … -->
Ethernet switches at any point on the capability range: TSN-capable switches with per-port gate control, commodity switches with strict-priority queuing, or pure FIFO switches. The available capability determines which configuration strategy applies and where enforcement is placed. Where enforcement is placed at the endpoints, Linux-based endpoints capable of running the source-side enforcement components are required, deployable as native processes, containers, or virtual machines.

## Non-Functional Requirements
<!-- With respect to Safety, Security, Realtime, … -->

## Dependencies to other Clusters

## Vehicle API Relevant


## Author/Company
Mohammadparsa Karimi; Majid Nabi; Andrew Nelson; Kees Goossens; Twan Basten — Electronic Systems group, Eindhoven University of Technology (TU/e)

V-TSN in collaboration with Ahmed Khalaf, Architecture and Network Solutions, AUMOVIO

## Priority


## Contribution supported by RDI projects
Yes. European Chips Joint Undertaking, Framework Partnership Agreement No 101139789 (HAL4SDV).

## Availability of Source Code
Yes. 

## Availability of API

## Type of API

## Potential obstacles
- **Endpoint software support.** Enforcement at the source requires software support on every sending device. Legacy endpoints that cannot run source-side gating, shaping, or release-time enforcement need an intermediate proxy or gateway.This constraint does not apply where enforcement is placed at TSN-capable switches.
- **Synchronization accuracy.** Temporal partitioning depends on endpoints closing their gates together, so the guard band must absorb the residual clock offset. Software synchronization currently supports millisecond-scale deadlines; microsecond-scale deadlines require hardware PTP.
- **Validation status.** Results to date are obtained through simulation and cloud-based deployment. Validation on physical automotive hardware has not yet been performed.

## Maturity Badges

## State (+ date of last change)
First public release available (research prototype). All four components are published as open source with the benchmark scenarios used in their respective evaluations; INSIM additionally provides a hosted web application. Update histories for each of the components can be traced in the respective repositories.

## System Context


## Compliant to

