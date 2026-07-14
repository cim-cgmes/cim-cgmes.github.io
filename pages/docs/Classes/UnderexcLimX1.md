# UnderexcLimX1

Allis-Chalmers minimum excitation limiter.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    UnderexcitationLimiterDynamics <|-- UnderexcLimX1
    UnderexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    UnderexcitationLimiterDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click UnderexcitationLimiterDynamics href "UnderexcitationLimiterDynamics"
    UnderexcLimX1 : +Float k[1..1]
    UnderexcLimX1 : +Float kf2[1..1]
    UnderexcLimX1 : +Float km[1..1]
    UnderexcLimX1 : +Float melmax[1..1]
    UnderexcLimX1 : +Float tf2[1..1]
    UnderexcLimX1 : +Float tm[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| k | Float | 1..1 | Minimum excitation limit slope (K) (> 0). |
| kf2 | Float | 1..1 | Differential gain (KF2). |
| km | Float | 1..1 | Minimum excitation limit gain (KM). |
| melmax | Float | 1..1 | Minimum excitation limit value (MELMAX). |
| tf2 | Float | 1..1 | Differential time constant (TF2) (>= 0). |
| tm | Float | 1..1 | Minimum excitation limit time constant (TM) (>= 0). |

