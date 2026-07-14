# MechanicalLoadDynamics

Mechanical load function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- MechanicalLoadDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    MechanicalLoadDynamics <|-- MechanicalLoadUserDefined
    MechanicalLoadUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    MechanicalLoadUserDefined : +Boolean proprietary[1..1]
    click MechanicalLoadUserDefined href "MechanicalLoadUserDefined"
    MechanicalLoadDynamics <|-- MechLoad1
    MechLoad1 : +Float a[1..1]
    MechLoad1 : +Float b[1..1]
    MechLoad1 : +Float d[1..1]
    MechLoad1 : +Float e[1..1]
    click MechLoad1 href "MechLoad1"
    MechanicalLoadDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    MechanicalLoadDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AsynchronousMachineDynamics | [AsynchronousMachineDynamics](AsynchronousMachineDynamics.md) | 0..1 | Asynchronous machine model with which this mechanical load model is associated. MechanicalLoadDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics. |
| SynchronousMachineDynamics | [SynchronousMachineDynamics](SynchronousMachineDynamics.md) | 0..1 | Synchronous machine model with which this mechanical load model is associated. MechanicalLoadDynamics shall have either an association to SynchronousMachineDynamics or AsynchronousMachineDyanmics. |

