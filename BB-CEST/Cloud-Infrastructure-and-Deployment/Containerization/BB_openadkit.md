# OpenADKit (Autoware Container Kit)

## Overview
OpenADKit provides a containerized, modular component library and deployment toolkit for Autoware-based autonomous driving stacks. It packages reference implementations of autonomous vehicle perception, planning, and control modules as OCI containers with clear interfaces and dependency specifications.

## Purpose
- Containerized reference implementations of AD (autonomous driving) components
- Simplified deployment and integration of Autoware software stacks
- Hardware-in-the-loop and hardware abstraction for multiple vehicle platforms
- Standardized container orchestration patterns for autonomous driving systems
- Support for simulation-to-hardware deployment transitions

## Key Capabilities
- Pre-built OCI container images for Autoware modules
- Compose-based and Kubernetes deployment configurations
- ROS2 node containerization with message compatibility
- LGSVL simulator integration for testing and validation
- Multi-architecture support (x86, ARM, automotive compute platforms)
- Documentation and tutorials for end-to-end deployment

## Usage
OpenADKit is deployed in autonomous driving projects, simulations, and vehicle platforms to accelerate Autoware adoption and reduce integration effort.

**Typical deployment:**
```
OpenADKit Containers
├─ Perception stack (LiDAR, camera, sensor fusion)
├─ Localization and mapping
├─ Planning and decision making
├─ Control and actuation
└─ Simulation bridge (ROS2 bridge)

Orchestrated via: Docker Compose or Kubernetes
Tested against: LGSVL simulator, real vehicle hardware
```

## Known Implementations
- Autoware Foundation reference: https://github.com/autowarefoundation/openadkit
- Used in Autoware demonstrators and proof-of-concept deployments
- Integration with Eclipse Leda and automotive container ecosystems

## Rationale
OpenADKit reduces the barrier to entry for autonomous driving development by providing containerized, pre-integrated reference components that can be deployed consistently across development, simulation, and vehicle environments.

## Dependencies
- **Requires:** Container runtime (Docker, Podman), Kubernetes or Docker Compose, ROS2 ecosystem
- **Composes with:** [BB_agnocast](../../../BB-SC/2b-MWLayer/Communication/BB_agnocast.md), LGSVL simulator, cloud orchestration platforms (AKS, EKS)
- **Integrates with:** Autoware repositories, vehicle hardware abstraction layers, CI/CD pipelines

## State
Active, maintained by Autoware Foundation. Regular updates and component additions.

## Tags
`BB-CEST`, `Container`, `Deployment`, `AutowareAD`, `ROS2`, `Autonomous`, `OpenADKit`, `Docker`, `Kubernetes`, `Automotive`
