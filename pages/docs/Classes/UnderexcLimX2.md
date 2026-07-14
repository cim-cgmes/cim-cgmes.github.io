# UnderexcLimX2

Westinghouse minimum excitation limiter.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    UnderexcitationLimiterDynamics <|-- UnderexcLimX2
    UnderexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    UnderexcitationLimiterDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click UnderexcitationLimiterDynamics href "UnderexcitationLimiterDynamics"
    UnderexcLimX2 : +Float kf2[1..1]
    UnderexcLimX2 : +Float km[1..1]
    UnderexcLimX2 : +Float melmax[1..1]
    UnderexcLimX2 : +Float qo[1..1]
    UnderexcLimX2 : +Float r[1..1]
    UnderexcLimX2 : +Float tf2[1..1]
    UnderexcLimX2 : +Float tm[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| kf2 | Float | 1..1 | Differential gain (KF2). |
| km | Float | 1..1 | Minimum excitation limit gain (KM). |
| melmax | Float | 1..1 | Minimum excitation limit value (MELMAX). |
| qo | Float | 1..1 | Excitation centre setting (QO). |
| r | Float | 1..1 | Excitation radius (R). |
| tf2 | Float | 1..1 | Differential time constant (TF2) (>= 0). |
| tm | Float | 1..1 | Minimum excitation limit time constant (TM) (>= 0). |

