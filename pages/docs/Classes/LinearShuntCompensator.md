# LinearShuntCompensator

A linear shunt compensator has banks or sections with equal admittance values.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ShuntCompensator <|-- LinearShuntCompensator
    ShuntCompensator : +SvShuntCompensatorSections SvShuntCompensatorSections[0..1]
    ShuntCompensator : +Float aVRDelay[0..1]
    ShuntCompensator : +Boolean grounded[0..1]
    ShuntCompensator : +Integer maximumSections[1..1]
    ShuntCompensator : +Float nomU[1..1]
    ShuntCompensator : +Integer normalSections[1..1]
    ShuntCompensator : +Float sections[1..1]
    ShuntCompensator : +Float voltageSensitivity[0..1]
    click ShuntCompensator href "ShuntCompensator"
    LinearShuntCompensator : +Float b0PerSection[1..1]
    LinearShuntCompensator : +Float bPerSection[1..1]
    LinearShuntCompensator : +Float g0PerSection[1..1]
    LinearShuntCompensator : +Float gPerSection[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| b0PerSection | Float | 1..1 | Zero sequence shunt (charging) susceptance per section. |
| bPerSection | Float | 1..1 | Positive sequence shunt (charging) susceptance per section. |
| g0PerSection | Float | 1..1 | Zero sequence shunt (charging) conductance per section. |
| gPerSection | Float | 1..1 | Positive sequence shunt (charging) conductance per section. |

