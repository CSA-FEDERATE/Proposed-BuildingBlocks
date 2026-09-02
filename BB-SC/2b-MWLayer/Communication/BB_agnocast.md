# Agnocast (Zero-Copy IPC Middleware)

## Overview
Agnocast is a zero-copy inter-process communication (IPC) middleware designed for ROS2 and autonomous driving workloads. It provides true zero-copy data exchange between processes, eliminating serialization overhead and enabling high-performance, real-time communication critical for perception, planning, and control loops.

## Purpose
- Ultra-low-latency, zero-copy message passing for autonomous driving
- Seamless integration with ROS2 message types and ecosystems
- Shared-memory-based communication with minimal copying
- Support for complex data structures (nested messages, arrays, structs)
- Efficient scaling to multi-core and heterogeneous compute platforms

## Key Capabilities
- Zero-copy serialization leveraging rosidl message definitions
- Kernel module support for advanced memory management
- Seamless ROS2 rmw (ROS Middleware) integration
- Support for Zenoh discovery and other pub/sub patterns
- Performance optimizations for real-time workloads
- Multi-architecture support (x86, ARM, automotive SoCs)

## Usage
Agnocast is deployed in high-performance autonomous driving and robotics systems where latency and bandwidth efficiency are critical.

**Typical deployment:**
```
ROS2 Application (Perception, Planning, Control)
    ↓
ROS2 DDS/RMW Layer
    ↓
Agnocast zero-copy transport (shared memory + kernel module)
    ↓
Hardware (multi-core CPU, GPU, sensor hardware)
```

## Known Implementations
- Autoware Foundation reference: https://github.com/autowarefoundation/agnocast
- Integrated into Autoware and autonomous driving reference stacks
- Used in production autonomous vehicle platforms
- Active contributions from Tier-1 automotive suppliers

## Rationale
Agnocast addresses the latency and efficiency requirements of autonomous driving by providing zero-copy communication, enabling real-time perception-to-control pipelines without sacrificing performance or losing ROS2 ecosystem compatibility.

## Dependencies
- **Requires:** ROS2 ecosystem, C++ compiler (C++17+), Linux kernel with IPC support
- **Composes with:** [BB_openadkit](../../../BB-CEST/Cloud-Infrastructure-and-Deployment/Containerization/BB_openadkit.md), perception and planning modules, real-time middleware stacks
- **Integrates with:** Autoware modules, sensor drivers, hardware abstraction layers, vehicle control systems

## State
Active, rapidly evolving. Growing adoption in autonomous driving community and commercial platforms.

## Tags
`BB-SC`, `BB-CEST`, `Middleware`, `Communication`, `IPC`, `ZeroCopy`, `ROS2`, `Autonomous`, `HighPerformance`, `Automotive`
