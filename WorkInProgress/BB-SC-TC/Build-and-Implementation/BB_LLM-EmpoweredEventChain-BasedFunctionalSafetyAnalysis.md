# LLM-Empowered Event Chain-Based Functional Safety Analysis

## BB Tags(s)

BB-SC-TC, BB-CEST

## Functional Clusters

Build-and-Implementation

## Layer

AppLayer

## BB Usage

Functional safety analysis, safety-aware system topology design, event-chain modeling, and LLM-assisted analysis of vehicle behavior and communication.

## Known Implementation

https://github.com/np-tum-air/tum_hal4sdv_safety_analysis

Python-based behavior modeling implementation:

https://github.com/np-tum-air/tum_hal4sdv_safety_analysis/blob/main/behavior_modeler.py

## ID (unique name)

tum-llm-functional-safety

## Description

This component represents an LLM-empowered workflow supporting functional safety analysis in Software Defined Vehicle (SDV) development. It covers safety-aware system topology design and event-driven analysis of vehicle behavior and decision-making processes.

For behavioral analysis, the approach adopts event-chain models that provide a structured representation for systematic functional safety validation. The analysis considers the semantic validity, ordering, and timing of events and messages exchanged between key vehicle components and supports both CAN-based communication and Vehicle Signal Specification (VSS) representations.

Large Language Models (LLMs) and Vision-Language Models (VLMs) are used to generate, interpret, and analyze behavioral models and safety-relevant event chains. Retrieval-Augmented Generation (RAG) can additionally provide domain-specific context, such as vehicle signals and safety-related information. Safety and security aspects of system topology are analyzed in combination with Model-Driven Engineering (MDE) techniques and Object Constraint Language (OCL) rules.

The workflow supports both locally deployable and proprietary AI models and is evaluated using Advanced Driver-Assistance Systems (ADAS)-related scenarios. Further details about the methodology and its evaluation are provided in the related publication.

## Rationale

Functional safety analysis of increasingly complex SDV architectures requires consideration of component interactions, communication semantics, event ordering, timing constraints, and system topology. Performing these analyses manually can require significant engineering effort and makes adaptation to evolving vehicle architectures difficult.

The proposed workflow combines generative AI with event-chain modeling, formal constraints, and MDE techniques. LLMs/VLMs provide flexible interpretation and generation of safety-relevant models, while event-chain representations and validation mechanisms provide structured foundations for checking system behavior. This combination aims to increase automation while maintaining traceability and explicit validation of safety-relevant properties.

## Governance Applicable S-BB(s)

Functional safety governance, AI-assisted engineering, model validation, safety analysis, and engineering-data governance.

## Compose BB(s)

LLM/VLM inference component, RAG component, event-chain modeler, behavior modeler, topology analyzer, OCL-based validation, CAN/VSS signal processing, and n8n workflow orchestration.

## What is needed to Design and Implement

Safety-relevant vehicle architecture and behavioral information, event-chain definitions, CAN/VSS signal descriptions, safety requirements and constraints, suitable LLM/VLM models, prompting strategies, RAG infrastructure where applicable, MDE/OCL modeling support, and validation mechanisms.

The workflow also requires n8n for orchestration and integration of the individual analysis steps. Python is used for the implementation of the behavioral modeling and AI integration components, together with the libraries specified by the implementation.

Reference implementation:

https://github.com/np-tum-air/tum_hal4sdv_safety_analysis/blob/main/behavior_modeler.py

## What is needed to build and run

The implementation requires:

* Python and the required Python libraries/dependencies provided by the project.
* n8n for workflow orchestration and integration of the individual processing steps.
* Access to supported LLM and/or VLM models through the configured inference interfaces.
* Vehicle architecture, behavioral, CAN, and/or VSS information depending on the analysis scenario.
* RAG infrastructure and corresponding domain knowledge sources when retrieval-augmented analysis is enabled.
* MDE/OCL tooling when topology and formal constraint validation are performed.

Both locally deployed and externally hosted AI models can be integrated depending on deployment, privacy, and computational requirements.

## Non-Functional Requirements

Traceability of generated safety artifacts, semantic correctness of event and signal mappings, reproducibility of analyses, support for locally deployable AI models, interoperability with vehicle communication representations, extensibility of safety rules and event chains, and validation of AI-generated outputs before their use in safety-critical engineering decisions.

## Dependencies to other Clusters

Generative AI/LLM/VLM infrastructure, Model-Driven Engineering, functional safety engineering, vehicle communication and signal modeling, RAG infrastructure, and workflow orchestration.

## Vehicle API Relevant

Yes. The approach can process and reason about vehicle communication and signal information, including CAN and Vehicle Signal Specification (VSS)-based representations, for safety-related behavioral analysis.

## Author/Company

TUM

## Priority

Medium

## Contribution supported by RDI projects

HAL4SDV

## Availability of Source Code

Publicly available:

https://github.com/np-tum-air/tum_hal4sdv_safety_analysis

Behavior modeling implementation:

https://github.com/np-tum-air/tum_hal4sdv_safety_analysis/blob/main/behavior_modeler.py

## Related Publication

The methodology and evaluation of the LLM-empowered functional safety analysis approach are described in the following publication:

https://arxiv.org/abs/2601.02215

## Availability of API

Available through the implemented Python components and AI inference interfaces. Workflow-level integration and orchestration are supported through n8n.

## Type of API

Library/Framework API

## Potential obstacles

LLM/VLM hallucinations, incorrect or incomplete interpretation of safety-relevant events, inaccurate CAN/VSS signal mappings, dependency on the quality of retrieved contextual information, computational requirements of locally deployed models, integration complexity across n8n and individual analysis components, and the requirement for deterministic validation before AI-generated results can be used in safety-critical engineering workflows.

## Maturity Badges

Gold, Gold, Gold, Gold, Gold

## State (+ date of last change)

Incubating (prototype implementation available) — August 2026

## System Context

The component operates as part of an SDV engineering and functional safety analysis toolchain. Vehicle architecture, behavioral information, safety constraints, and CAN/VSS-related information are processed by an n8n-orchestrated workflow connecting LLM/VLM, RAG, behavioral modeling, and validation components.

The Python-based behavior modeler generates and processes safety-relevant behavioral representations and event chains. AI-generated results can subsequently be checked against semantic, ordering, timing, topology, and formal safety constraints before being provided to downstream engineering and safety-analysis activities.

## Compliant to

Event-chain-based behavioral modeling, Model-Driven Engineering (MDE), Object Constraint Language (OCL), CAN-based vehicle communication, and Vehicle Signal Specification (VSS) concepts.
