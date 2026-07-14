# MechLoad1

Mechanical load model type 1.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    MechanicalLoadDynamics <|-- MechLoad1
    MechanicalLoadDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    MechanicalLoadDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    click MechanicalLoadDynamics href "MechanicalLoadDynamics"
    MechLoad1 : +Float a[1..1]
    MechLoad1 : +Float b[1..1]
    MechLoad1 : +Float d[1..1]
    MechLoad1 : +Float e[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| a | Float | 1..1 | Speed squared coefficient (a). |
| b | Float | 1..1 | Speed coefficient (b). |
| d | Float | 1..1 | Speed to the exponent coefficient (d). |
| e | Float | 1..1 | Exponent (e). |

