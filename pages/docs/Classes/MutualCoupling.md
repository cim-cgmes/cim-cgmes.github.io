# MutualCoupling

This class represents the zero sequence line mutual coupling.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- MutualCoupling
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    MutualCoupling : +Terminal First_Terminal[1]
    MutualCoupling : +Terminal Second_Terminal[1]
    MutualCoupling : +Float b0ch[1..1]
    MutualCoupling : +Float distance11[1..1]
    MutualCoupling : +Float distance12[1..1]
    MutualCoupling : +Float distance21[1..1]
    MutualCoupling : +Float distance22[1..1]
    MutualCoupling : +Float g0ch[1..1]
    MutualCoupling : +Float r0[1..1]
    MutualCoupling : +Float x0[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| First_Terminal | [Terminal](Terminal.md) | 1 | The starting terminal for the calculation of distances along the first branch of the mutual coupling. Normally MutualCoupling would only be used for terminals of AC line segments. The first and second terminals of a mutual coupling should point to different AC line segments. |
| Second_Terminal | [Terminal](Terminal.md) | 1 | The starting terminal for the calculation of distances along the second branch of the mutual coupling. |
| b0ch | Float | 1..1 | Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. |
| distance11 | Float | 1..1 | Distance to the start of the coupled region from the first line's terminal having sequence number equal to 1. |
| distance12 | Float | 1..1 | Distance to the end of the coupled region from the first line's terminal with sequence number equal to 1. |
| distance21 | Float | 1..1 | Distance to the start of coupled region from the second line's terminal with sequence number equal to 1. |
| distance22 | Float | 1..1 | Distance to the end of coupled region from the second line's terminal with sequence number equal to 1. |
| g0ch | Float | 1..1 | Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. |
| r0 | Float | 1..1 | Zero sequence branch-to-branch mutual impedance coupling, resistance. |
| x0 | Float | 1..1 | Zero sequence branch-to-branch mutual impedance coupling, reactance. |

