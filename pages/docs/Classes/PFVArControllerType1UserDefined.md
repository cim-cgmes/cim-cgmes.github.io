# PFVArControllerType1UserDefined

Power factor or VAr controller type 1 function block whose dynamic behaviour is described by a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PFVArControllerType1Dynamics <|-- PFVArControllerType1UserDefined
    PFVArControllerType1Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PFVArControllerType1Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    PFVArControllerType1Dynamics : +VoltageAdjusterDynamics VoltageAdjusterDynamics[0..1]
    click PFVArControllerType1Dynamics href "PFVArControllerType1Dynamics"
    PFVArControllerType1UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    PFVArControllerType1UserDefined : +Boolean proprietary[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ProprietaryParameterDynamics | [ProprietaryParameterDynamics](ProprietaryParameterDynamics.md) | 0..n | Parameter of this proprietary user-defined model. |
| proprietary | Boolean | 1..1 | Behaviour is based on a proprietary model as opposed to a detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. |

