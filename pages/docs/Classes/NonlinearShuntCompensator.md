# NonlinearShuntCompensator

A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ShuntCompensator <|-- NonlinearShuntCompensator
    ShuntCompensator : +SvShuntCompensatorSections SvShuntCompensatorSections[0..1]
    ShuntCompensator : +Float aVRDelay[0..1]
    ShuntCompensator : +Boolean grounded[0..1]
    ShuntCompensator : +Integer maximumSections[1..1]
    ShuntCompensator : +Float nomU[1..1]
    ShuntCompensator : +Integer normalSections[1..1]
    ShuntCompensator : +Float sections[1..1]
    ShuntCompensator : +Float voltageSensitivity[0..1]
    click ShuntCompensator href "ShuntCompensator"
    NonlinearShuntCompensator : +NonlinearShuntCompensatorPoint NonlinearShuntCompensatorPoints[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| NonlinearShuntCompensatorPoints | [NonlinearShuntCompensatorPoint](NonlinearShuntCompensatorPoint.md) | 1..n | All points of the non-linear shunt compensator. |

