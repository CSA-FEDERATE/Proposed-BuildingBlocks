# Agentic Resilience Validation for Plug-and-Play Sensors

## BB Tags(s)
BB-EST, BB-SC-TC

## Functional Clusters
Testing (Fault Injection / Resilience Validation)

## Layer
MWLayer

## BB Usage
The building block is an autonomous test agent that validates how an SDV software stack reacts to faulty plug-and-play sensors. A ReAct-style LLM agent plans test sessions, injects sensor faults at three levels of a co-simulation (physics simulation, VSS signal layer, emulated ECU), observes the system response and lets an independent critic agent grade the result. Results are stored in a vector knowledge base so that later sessions avoid repetition and target uncovered fault classes.

Co-simulation stack under test:
```
Gazebo Harmonic             physics simulation of the vehicle and the ultrasonic sensor
    |  ROS 2 Jazzy           bridge nodes
Eclipse KUKSA Databroker    VSS 4.0 signal layer
    |
QEMU ARM64 ECU              safety-gate application reading VSS and commanding the vehicle
    ^
ReAct LLM test agent        orchestrates all of the above
```

Components:
- **Test agent** (`agent.py`): selects fault type, intensity and duration; starts and stops simulation, Databroker and ECU; calls the tools below.
- **Executor**: injects faults (drop-out, stuck-at, noise, drift, latency, spikes, out-of-range, intermittent) into the simulation, the VSS signal or the ECU input.
- **Observer**: records VSS signals and ECU reactions during the session.
- **Analyzer**: computes detection time, recovery time and safety-gate behaviour.
- **Critic agent**: separate LLM call that issues PASS / PARTIAL / FAIL with reasoning and recommends the next tests.
- **Knowledge base**: ChromaDB store of all past sessions for cross-session learning; HTML report per session.

Run:
```bash
source ~/kuksa_venv/bin/activate   # anthropic, kuksa-client, chromadb
export ANTHROPIC_API_KEY=...
python3 agent.py                    # starts Gazebo, ROS 2 bridges, Databroker and the QEMU ECU itself
```

## Known Implementation
None public yet. Prototype implemented at IAS, University of Stuttgart; publication of the source code is planned.

## ID (unique name)
IAS-Agentic-Resilience-Validation

## Description
Plug-and-play sensors (see BB AAS-based Sensor Plug-and-Play) change the hardware configuration of a vehicle at runtime. The software stack must therefore tolerate sensors that are faulty, degraded or disappear. Testing this exhaustively by hand is not feasible because the fault space (type, intensity, duration, injection point) is large and the interesting cases are the ones a test engineer did not think of.

This building block replaces the hand-written fault test plan with an LLM agent that acts as a test engineer in a closed loop. The agent reasons about which faults have already been covered, decides the next fault scenario, executes it through deterministic tools against a co-simulated vehicle (Gazebo, ROS 2, KUKSA Databroker, QEMU-emulated ECU), and hands the recorded evidence to an independent critic agent. The critic grades detection, recovery and safety behaviour and recommends follow-up tests. All verdicts and metrics are kept in a vector knowledge base, so coverage grows across sessions without repeating scenarios.

In the evaluation the agent ran 56 autonomous sessions over 8 fault types against an ultrasonic-sensor safety gate; 95 % of injected faults were detected by the system under test within 0.33 s, with no crash of the test harness.

## Rationale
Resilience of SDV software against sensor faults is usually validated with static fault-injection scripts written for a fixed sensor set. Plug-and-play makes the sensor set dynamic, so the validation has to be regenerated whenever hardware changes. LLM agents can plan and adapt test campaigns, but unconstrained LLM use in a test loop produces unreproducible results. The design here keeps the LLM in the planning and judging roles only; fault injection, observation and metric computation are deterministic tools, and the critic is a separate model call so the planner does not grade its own work. This gives adaptive coverage with reproducible evidence per session.

## Governance Applicable S-BB(s)
- ISO 26262 (S-BB BB_ISO26262-1_2018) and ISO 21448 SOTIF (S-BB BB_ISO21448_2022) as the standards whose fault-tolerance arguments the generated evidence supports
- COVESA VSS (S-BB BB_VSS) as the signal layer at which faults are injected and observed

## Compose BB(s)
- BB-SC BB_Eclipse_KUKSA (Databroker as the VSS signal layer)
- BB AAS-based Sensor Plug-and-Play (system under test)
- Gazebo / ROS 2 simulation (external)
- LLM inference (Anthropic API in the current implementation; local models possible)

## What is needed to Design and Implement
Ubuntu 24.04 host with at least 16 GB RAM, ROS 2 Jazzy, Gazebo Harmonic, QEMU for ARM64 with an Ubuntu ARM64 cloud image, Eclipse KUKSA Databroker (built from source or container), Python 3 with anthropic, kuksa-client and chromadb, and an LLM API key. Knowledge of the ROS 2 topics and VSS signal paths of the system under test is required to adapt the executor and observer to a new sensor.

## What is needed to build and run
Same as above. The agent starts all simulation components itself in separate terminals and shuts them down at the end of a session. No vehicle hardware is required.

## Non-Functional Requirements
- Reproducibility: every session stores its scenario, raw observer log, metrics and critic verdict.
- Separation of concerns: planning (LLM), execution (deterministic tools) and judgement (independent LLM call) are separate components.
- Security/privacy: scenario descriptions and signal logs are sent to the LLM provider; a local model is required where this is not acceptable.
- Not real-time; the test loop runs at simulation speed.

## Dependencies to other Clusters
- FC Communication: ROS 2 and KUKSA Databroker.
- FC Testing / simulation tools: Gazebo, QEMU.
- FC Security: handling of API keys and of logs sent to external LLM services.

## Vehicle API Relevant
Yes, exists: faults are injected and observed on COVESA VSS paths through the KUKSA Databroker. No new signals proposed.

## Author/Company
akshay.narla AT ias DOT uni-stuttgart DOT de / Institute of Industrial Automation and Software Engineering (IAS), University of Stuttgart

## Priority
Medium

## Contribution supported by RDI projects
Yes. Chips Joint Undertaking, Framework Partnership Agreement No 101139789 (HAL4SDV).

## Availability of Source Code
Not yet published (open-source release planned).

## Availability of API
Not applicable (tool with CLI; tool functions exposed to the agent as Python functions).

## Type of API
Other (CLI / agent tool interface)

## Potential obstacles
- Evaluated with one sensor type (ultrasonic) and one safety-gate application; generalization to cameras and other sensors needs new executor and observer adapters.
- LLM non-determinism in planning; the same campaign is not repeated identically, only the per-session evidence is reproducible.
- Dependence on an external LLM API in the current implementation.
- Heavy host requirements (Gazebo plus QEMU plus ROS 2 on one machine).
- Code not yet published.

## Maturity Badges


## State (+ date of last change)
Implementation started (research prototype complete, not yet publicly released). April 2026.

## System Context
- Ubuntu 24.04 host
- ROS 2 Jazzy, Gazebo Harmonic
- QEMU ARM64 (emulated ECU)
- Eclipse KUKSA Databroker
- Python 3, LLM API

## Compliant to
Eclipse KUKSA / COVESA VSS, ROS 2.
