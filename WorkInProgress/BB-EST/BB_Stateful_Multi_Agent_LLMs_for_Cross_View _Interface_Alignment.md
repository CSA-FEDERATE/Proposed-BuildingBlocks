# Stateful Multi-Agent LLMs for Cross-View Interface Alignment

## BB Tags(s)

BB-EST, BB-SC-TC

## Functional Clusters

Build-and-Implementation

## Layer

AppLayer

## BB Usage

AI-assisted Model-Based Systems Engineering (MBSE), automated UML model generation, cross-view interface alignment, automotive architecture modeling, VSS-based signal grounding, model validation, and multi-agent orchestration for Software Defined Vehicle (SDV) engineering.

## Known Implementation

Prototype implementation based on an n8n-orchestrated multi-agent workflow integrating LLM-based model generation, Vehicle Signal Specification (VSS)-grounded Retrieval-Augmented Generation (RAG), deterministic PlantUML syntax validation, semantic validation, and stateful backtracking.

The implementation generates and validates multiple related architectural views in the sequence:

Class → Activity → Sequence

The methodology and evaluation are described in:

Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering

Aleksei Velsh, Nenad Petrovic, and Alois Knoll

https://arxiv.org/abs/2608.08038

## ID (unique name)

tum-stateful-multi-agent-mbse

## Description

This component represents a stateful multi-agent LLM workflow for automated Model-Based Systems Engineering (MBSE) in Software Defined Vehicle (SDV) development. The approach addresses cross-view inconsistencies and architectural hallucinations that can occur when Large Language Models independently generate structural, behavioral, and interaction models.

The workflow follows a sequential model-generation process consisting of Class, Activity, and Sequence diagrams. The Class diagram establishes the structural baseline of the system, including components, interfaces, methods, and vehicle signals. This validated architectural state is subsequently propagated to the Activity and Sequence diagram generation stages, constraining downstream model generation.

Vehicle Signal Specification (VSS) information is integrated through Retrieval-Augmented Generation (RAG). Relevant standardized vehicle signals and their associated data types are retrieved from a VSS knowledge base and supplied to the generation agents. This grounding mechanism reduces the risk of introducing incorrect or hallucinated signal identifiers into generated automotive models.

An independent AI Validator Agent performs semantic and cross-view validation of generated artifacts. Newly generated models are compared with previously validated architectural states. Detected inconsistencies are classified according to a structured error taxonomy covering diagram misalignment, syntax and logic errors, hallucinated components, missing requirements, unintended deletions, and interface incompatibilities.

The component maintains persistent architectural state across the generation workflow. Previously validated model information is propagated to subsequent agents so that structural and behavioral decisions made in earlier stages constrain downstream generation.

When an inconsistency cannot be resolved at the current modeling stage, a stateful backtracking mechanism allows the workflow to return to an earlier stage. For example, if generation of a Sequence diagram requires an interface that is missing from the Class diagram, the workflow can return to the Class generation stage, update the structural model, validate it again, and subsequently regenerate the dependent Activity and Sequence views.

This cyclic generation and validation process enables LLM-based model generation to operate as an iterative engineering workflow rather than as a sequence of independent model-generation requests.

The approach was evaluated using an automotive Child Presence Detection (CPD) ADAS scenario and demonstrated improved cross-view consistency compared with zero-shot, RAG-only, and RAG with static-validation configurations.

## Rationale

LLMs provide significant opportunities for automating MBSE activities, including the generation of UML/SysML-like engineering models from natural-language requirements. However, independently generated models can suffer from architectural drift, where components, signals, methods, parameters, or data types introduced in one architectural view are inconsistent with those defined in another.

This problem becomes particularly important when multiple related views of the same system are generated. A structurally valid Class diagram, behaviorally valid Activity diagram, and individually valid Sequence diagram do not necessarily constitute a consistent overall architecture if their interfaces and entities differ.

Retrieval-Augmented Generation improves factual grounding by supplying domain-specific information such as standardized VSS signals. However, retrieval alone cannot guarantee structural compatibility and semantic consistency across multiple generated models.

The proposed component therefore combines domain grounding with persistent architectural state, sequential model generation, deterministic syntax validation, semantic AI-based validation, and dynamic backtracking.

The structural model acts as the architectural foundation for subsequent behavioral and interaction views. Each downstream model is constrained by previously validated artifacts. When inconsistencies appear, the workflow can automatically revise upstream models and regenerate affected downstream views.

This provides a structured mechanism for reducing hallucinations, limiting architectural drift, and improving traceability and consistency when generative AI is applied to automotive systems engineering.

## Governance Applicable S-BB(s)

AI-assisted engineering governance, model validation, engineering-data governance, traceability management, architecture consistency validation, human oversight, and validation of AI-generated engineering artifacts.

## Compose BB(s)

LLM inference component, Generator Agent, AI Validator Agent, RAG component, VSS knowledge base, vector database, PlantUML model generator, deterministic syntax validator, state-management component, dynamic backtracking mechanism, diagram rendering component, and n8n workflow orchestration.

## What is needed to Design and Implement

Automotive system requirements, architectural modeling rules, UML/PlantUML representations, Vehicle Signal Specification (VSS) information, suitable LLM models, prompting strategies, RAG infrastructure, vector database infrastructure, semantic validation rules, cross-view consistency criteria, state-management mechanisms, and workflow orchestration.

The workflow requires explicit dependencies between architectural views. In the demonstrated implementation, these dependencies follow the sequence:

Class → Activity → Sequence

The Class diagram establishes the structural system state. The Activity diagram describes behavioral logic based on this state, while the Sequence diagram describes component interactions while remaining constrained by both structural and behavioral information.

A persistent state-management mechanism is required to propagate validated architectural information between agents and model-generation stages.

A semantic Validator Agent is additionally required to compare newly generated artifacts with previously validated architectural states and determine whether the generated model can be accepted, should be regenerated, or requires backtracking to an earlier architectural stage.

The workflow orchestration layer must support cyclic execution because validation of downstream models can trigger modification and regeneration of upstream models.

## What is needed to build and run

The implementation requires a Python/AI execution environment together with n8n for multi-agent workflow orchestration and state management.

Access to suitable LLM models through configured inference interfaces is required for model generation and semantic validation.

The domain-grounding functionality requires a RAG pipeline, a vector database containing Vehicle Signal Specification information, VSS data represented in a machine-processable format such as JSONL, and an embedding model for indexing and retrieving relevant vehicle signals.

Generated models require PlantUML-compatible representations, deterministic syntax-validation mechanisms, and diagram-rendering infrastructure.

An AI Validator Agent is required for semantic and cross-view consistency validation, while persistent workflow state is needed to propagate validated architectural information between generation stages and support dynamic backtracking.

Locally deployed or externally hosted AI models can be integrated depending on privacy, computational, latency, and deployment requirements.

## Non-Functional Requirements

Traceability between architectural views, semantic consistency of generated interfaces, reproducibility of model generation, deterministic syntax validation, preservation of validated architectural state, interoperability with automotive signal standards, extensibility of validation rules, explainability of detected inconsistencies, support for iterative correction, and validation of AI-generated artifacts before their use in safety-critical engineering activities.

The component should preserve identifiers, interfaces, methods, signals, parameters, and data types across dependent architectural views whenever they represent the same system entities.

Persistent architectural state should remain consistent throughout cyclic model generation and backtracking.

Scalability must also be considered because larger automotive architectures increase LLM context size, validation complexity, model-generation latency, state-management requirements, and visualization complexity.

## Dependencies to other Clusters

Generative AI/LLM infrastructure, Model-Based Systems Engineering, Model-Driven Engineering, automotive architecture engineering, Vehicle Signal Specification infrastructure, RAG infrastructure, vector databases, UML/PlantUML tooling, workflow orchestration, and engineering validation infrastructure.

## Vehicle API Relevant

Yes.

The approach uses Vehicle Signal Specification (VSS) information to ground generated architectural interfaces and behavioral models in standardized vehicle signals and corresponding data types.

Generated models can therefore represent interactions between SDV components and Vehicle API-compatible signal structures.

VSS-based retrieval also reduces the probability that generated models introduce arbitrary or incompatible vehicle-signal identifiers when defining interfaces between automotive components.

## Author/Company

TUM

## Priority

Medium

## Contribution supported by RDI projects

Not specified.

## Availability of Source Code

Not publicly available / not specified.

## Availability of API

Available as a prototype software framework/workflow. A dedicated externally exposed API is not specified.

## Type of API

Library/Framework API

## Potential obstacles

LLM hallucinations, architectural drift, incorrect interpretation of natural-language requirements, inconsistent interfaces between architectural views, incorrect VSS mappings, dependency on the completeness of the VSS knowledge base, semantic errors that cannot be detected through syntax validation alone, increasing context size for large architectures, multi-agent execution latency, and computational requirements of iterative validation.

Additional challenges include critic hallucinations, where the AI Validator Agent incorrectly rejects an otherwise valid model, model-version drift affecting reproducibility, sensitivity to prompts and generation parameters, and scalability limitations when generating or visualizing large UML architectures.

Stateful backtracking introduces additional workflow complexity because modifications to an upstream architectural view can invalidate multiple downstream artifacts and require their regeneration.

The approach validates syntactic, semantic, and cross-view architectural consistency but does not replace formal verification or physical system simulation. Generated architectures therefore require additional engineering validation before deployment in safety-critical vehicle systems.

## Maturity Badges

Gold, Gold, Gold, Gold, Gold

## State (+ date of last change)

Incubating (no code yet) — August 2026

## System Context

The component is positioned within an AI-assisted MBSE and SDV engineering toolchain between natural-language system requirements, automotive domain knowledge, and downstream architecture-engineering activities.

Natural-language automotive requirements provide the initial engineering context. Vehicle Signal Specification information is retrieved through a RAG subsystem and supplied as additional domain grounding to the model-generation agents.

The workflow then incrementally generates related architectural views:

Requirements + VSS Knowledge
→ Class Diagram
→ Activity Diagram
→ Sequence Diagram

The Class diagram establishes the primary architectural state by defining components, interfaces, methods, signals, and other structural entities.

After deterministic syntax validation and semantic validation, the accepted Class model becomes persistent architectural context for Activity-diagram generation. The validated Activity model subsequently becomes additional context for Sequence-diagram generation.

The overall processing flow is:

Automotive Requirements
→ VSS-Grounded RAG
→ Generator Agent
→ PlantUML Model
→ Deterministic Syntax Validation
→ AI Semantic Validator
→ Validated Architectural State
→ Next Modeling Stage

The architectural-state dependencies are:

Class
↓
Activity
↓
Sequence

Validation introduces a feedback loop across these stages. When the Validator Agent identifies an inconsistency that originates in an earlier architectural view, the stateful workflow can backtrack to that view.

For example:

Sequence validation detects missing interface
→ Backtrack to Class model
→ Add/correct interface
→ Validate Class model
→ Regenerate Activity model if affected
→ Regenerate Sequence model
→ Validate cross-view consistency

n8n orchestrates the multi-agent workflow, maintains state transitions, and coordinates cyclic generation and validation.

The resulting validated architectural views can subsequently be provided to downstream MBSE, model transformation, simulation, software-generation, or engineering-validation components.

## Compliant to

Vehicle Signal Specification (VSS) concepts and UML/PlantUML modeling concepts.

No additional formal compliance standard is stated in the provided implementation description.
