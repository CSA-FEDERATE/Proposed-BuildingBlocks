# Determi.FLOW

## BB Tags(s)
BB-SC

## Functional Clusters
Communication

## Layer
MWLayer

## BB Usage
Use Determi.FLOW when you need DDS/RTPS communication with predictable behavior in safety-critical systems.

Typical runtime usage in an application loop:
```cpp
rtps::Scheduler::DiagnosticsSnapshot diagnostics{};
while (running)
{
    if (!scheduler.work(diagnostics))
    {
        // switch to fallback / safe state
        break;
    }
}
```
How-to and examples:
- Main documentation: https://determion.github.io/Determi.FLOW
- Project README: https://github.com/determion/Determi.FLOW
- Step-by-step runnable examples: `public_examples/01_stateless_pub_sub` to `public_examples/06_multithread_manual_liveliness`

## Known Implementation
https://github.com/determion/Determi.FLOW

## ID (unique name)
BB_Determi_FLOW

## Description
Determi.FLOW is an open-source deterministic DDS/RTPS middleware from Determion GmbH for safety-critical embedded systems.  
It allows for communication of safety-critical data using the black channel concept with integrity protection and sequence counters.

It is based on a single-threaded execution model (`Scheduler::work(...)`) so middleware operations are executed in a deterministic and predictable order.  

Determi.FLOW provides APIs for
- robust discovery with mutual discovery confirmation
- manual liveliness supervision, and delivery/deadline monitoring.

The implementation is 100% compliant with all mendatroy and required MISRA C++ rules, is lock free and has no dynamic memory allocation.

Its small footprint also allows for execution on embedded systems. All public APIs are non-blocking and the implenentation does not use OS-level synchronization mechanisms.

Determi.FLOW comes with a preliminary IDL generator that emmits serialization code with static memory allocation that is also MISRA compliant.

Determi.FLOW has no thirdparty dependencies for the core stack.

## Rationale
Automotive systems need communication middleware for safety-critical data  with a small compute and memory footprint that exhibits a predictable execution behavior.
Determi.FLOW addresses this through its single-threaded design that guarantees a predictable execution order of middleware operations, built-in supervision mechanisms for discovery, liveliness, integrity, and delivery progress.

## Governance Applicable S-BB(s)
- S-BB Functional-Safety: `BB_ISO26262-1_2018`
- OMG DDS / DDSI-RTPS specifications
- MISRA C++:2023 Mandatory and Required rules (as stated by project)

## Compose BB(s)
Not applicable

## What is needed to Design and Implement
- C++17 development environment

## What is needed to build and run
- Linux runtime 
- CMake (>= 3.10) and C++17 compiler toolchain
- Python3 for IDL generator

## Non-Functional Requirements
- Deterministic runtime behavior
- Real-time guarantees with upper bounds on execution time for all operations 
- Pre-allocated/controlled memory usage
- Communication with integrity protection
- Compliance with MISRA C++ 2023

## Dependencies to other Clusters
- Security (integrity strategy, key management, deployment hardening)
- Diagnostics/Observability (runtime fault handling, monitoring integration)
- OS/Platform (threading, timing, networking primitives)
- Testing/Verification (integration tests, fault injection, safety evidence)

## Vehicle API Relevant
No

## Author/Company
Determion GmbH

## Priority
High

## Contribution supported by RDI projects
No explicit public RDI project reference is stated in the repository.

## Availability of Source Code
Yes / Apache License 2.0

## Availability of API
Yes / Apache License 2.0

## Type of API
- Library/Framework API
- CLI Tool API for IDL Generator (`determiflow-idlgen`)

## Potential obstacles
- Current release is beta and not yet intended for production use.
- Limited maximum message size in current public release.
- No shared-memory support in current public release.
- Public test suite is not yet published.
- Public release support is currently Linux-focused.

## Maturity Badges
| 			| Documentation | Requirements | Coding Guidelines | Testing | Release Process |
| --------- |:-------------:|:------------:|:-----------------:|:-------:|:---------------:|
| Level		| [Silver](https://determion.github.io/Determi.FLOW) | No | Bronze | No | NotDefined |

## State (+ date of last change)
First public release available (beta), implementation active.  

## System Context
- Linux
- C++17
- CMake-based build
- Scheduler-driven runtime integration
- UDP/IP DDS networking

## Compliant to
- MISRA C++ 2023
- DDS/RTPS-based communication architecture
- Apache 2.0 open-source licensing model
