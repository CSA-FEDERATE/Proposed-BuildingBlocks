# punit
## BB Tags(s)
BB-EST, BB-CEST, BB-SC-TC, BB-CSC-TC

## Functional Clusters
Testing

## Layer
AppLayer

## BB Usage
punit is a JUnit extension for probabilistic testing of non-deterministic systems.

Documentation and examples:
- Project page: https://mavai.org/projects/punit/
- Source code: https://github.com/mavai-org/punit
- Examples: https://mavai.org/projects/punitexamples/

Add to a Java project (Maven Central, org.mavai):

Gradle (Kotlin DSL):
```kotlin
dependencies {
    testImplementation("org.mavai:punit-core:0.9.0")
    testImplementation("org.mavai:punit-report:0.9.0")
    testImplementation("org.junit.jupiter:junit-jupiter")
}
```

Maven:
```xml
<dependency>
    <groupId>org.mavai</groupId>
    <artifactId>punit-core</artifactId>
    <version>0.9.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.mavai</groupId>
    <artifactId>punit-report</artifactId>
    <version>0.9.0</version>
    <scope>test</scope>
</dependency>
```

## Known Implementation
https://github.com/mavai-org/punit

## ID (unique name)
BB_punit

## Description
punit is a probabilistic testing framework implemented as a JUnit 5/6 extension for Java. It supports statistically rigorous validation for stochastic behavior by executing repeated trials and assessing observed success rates against confidence and threshold criteria.

## Rationale
For AI-enabled and non-deterministic services, one-shot deterministic tests can be misleading. punit enables evidence-based quality statements through repeatable probabilistic experiments, baseline generation, and structured reporting.

## Governance Applicable S-BB(s)
Potentially relevant governance BBs depend on the target system and domain constraints, for example:
- Cybersecurity and secure development governance (for connected and AI-enabled services)
- Software quality and process governance BBs in this repository

## Compose BB(s)
This BB shares statistical methodology with feotest and can be paired for cross-language validation programs:
- [BB_feotest](BB_feotest.md)

## What is needed to Design and Implement
- Java build system (Maven or Gradle)
- JUnit 5/6 based test architecture
- Definition of probabilistic service contracts and postconditions
- Team agreement on confidence/threshold policy and experiment intent (verification vs smoke)

## What is needed to build and run
- JVM runtime and CI test execution environment
- Access to non-deterministic target service(s)
- Storage of generated baseline/spec artifacts and test reports

## Non-Functional Requirements
- Statistical validity of experiment setup (sample size adequacy)
- Reproducibility and traceability of baseline evolution
- Runtime and budget control for repeated executions

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
Yes / Open source Java library API

## Type of API
Library/Framework API

## Potential obstacles
- Misinterpretation of probabilistic verdicts as deterministic guarantees
- Insufficient sample size leading to weak evidence
- Baseline mismatch due to uncontrolled covariates

## Maturity Badges
NotDefined

## State (+ date of last change)
First public release available (2026-08-26)

## System Context
- Java/JVM-based development and test environments
- JUnit-driven local and CI execution
- Suitable for cloud, edge, and off-board validation services

## Compliant to
The BB can be integrated into projects targeting established SDV quality and process frameworks when probabilistic test evidence is accepted as part of verification strategy.
