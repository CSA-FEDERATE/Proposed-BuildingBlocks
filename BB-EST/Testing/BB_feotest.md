# feotest
## BB Tags(s)
BB-EST, BB-CEST, BB-SC-TC, BB-CSC-TC

## Functional Clusters
Testing

## Layer
AppLayer

## BB Usage
feotest is a Rust-native probabilistic testing framework for non-deterministic systems.

Documentation and examples:
- Project page: https://mavai.org/projects/feotest/
- Source code: https://github.com/mavai-org/feotest
- Examples: https://mavai.org/projects/feotest-examples/

Add to a Rust project:
```toml
[dev-dependencies]
feotest = "0.1.0"
```

Or with Cargo:
```bash
cargo add --dev feotest
```

## Known Implementation
https://github.com/mavai-org/feotest

## ID (unique name)
BB_feotest

## Description
feotest is a probabilistic testing framework for Rust, designed for systems with inherently stochastic behavior (for example LLM-backed services, ML inference, ranking/recommendation, or externally influenced APIs). Instead of a single pass/fail execution, tests are evaluated over repeated Bernoulli trials against a threshold and confidence target.

## Rationale
Conventional deterministic assertions are often insufficient for stochastic software. feotest provides statistically rigorous evidence for quality claims by controlling sample size, confidence level, and threshold, and by producing reproducible experiment artifacts.

## Governance Applicable S-BB(s)
Potentially relevant governance BBs depend on the target system and domain constraints, for example:
- Cybersecurity and secure development governance (for connected and AI-enabled services)
- Software quality and process governance BBs in this repository

## Compose BB(s)
This BB is methodologically aligned with punit and can be used together in multi-language validation strategies:
- [BB_punit](BB_punit.md)

## What is needed to Design and Implement
- Rust toolchain (stable)
- Cargo build tooling
- Definition of probabilistic service contracts and acceptance criteria
- Team agreement on confidence/threshold policy and experiment intent (verification vs smoke)

## What is needed to build and run
- Rust project with test pipeline integration
- CI environment capable of repeated executions and artifact storage
- Optional budget controls (time/token/rate limits) depending on target service

## Non-Functional Requirements
- Statistical validity of experiment setup (sample size adequacy)
- Reproducibility of baselines and verdicts across environments
- Transparent reporting of confidence intervals and latency percentiles

## Dependencies to other Clusters
- Development and Testing cluster (test orchestration and CI)
- Data Processing cluster (baseline/spec artifact handling)
- Security and Compliance cluster when testing sensitive or regulated services

## Vehicle API Relevant
No direct vehicle API definition dependency. Can be used to validate services that expose vehicle APIs.

## Author/Company
Mavai

## Priority
Medium

## Contribution supported by RDI projects
Potential candidate for integration into SDV test toolchains and probabilistic validation workflows.

## Availability of Source Code
Yes / Apache-2.0

## Availability of API
Yes / Open source Rust library API (crate)

## Type of API
Library/Framework API

## Potential obstacles
- Misinterpretation of probabilistic verdicts as deterministic guarantees
- Insufficient sample size leading to weak evidence
- Environment drift affecting baseline comparability

## Maturity Badges
NotDefined

## State (+ date of last change)
First public release available (2026-08-26)

## System Context
- Rust-based development and test environments
- Local and CI execution
- Suitable for cloud, edge, and off-board validation services

## Compliant to
The BB can be integrated into projects targeting established SDV quality and process frameworks when probabilistic test evidence is accepted as part of verification strategy.
