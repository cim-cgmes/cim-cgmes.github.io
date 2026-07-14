# GroundingImpedance

A fixed impedance device used for grounding.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EarthFaultCompensator <|-- GroundingImpedance
    EarthFaultCompensator : +Float r[0..1]
    click EarthFaultCompensator href "EarthFaultCompensator"
    GroundingImpedance : +Float x[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| x | Float | 1..1 | Reactance of device. |

