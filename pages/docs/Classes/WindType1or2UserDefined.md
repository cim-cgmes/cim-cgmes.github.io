# WindType1or2UserDefined

Wind type 1 or type 2 function block whose dynamic behaviour is described by a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType1or2Dynamics <|-- WindType1or2UserDefined
    WindTurbineType1or2Dynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[1]
    WindTurbineType1or2Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click WindTurbineType1or2Dynamics href "WindTurbineType1or2Dynamics"
    WindType1or2UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    WindType1or2UserDefined : +Boolean proprietary[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ProprietaryParameterDynamics | [ProprietaryParameterDynamics](ProprietaryParameterDynamics.md) | 0..n | Parameter of this proprietary user-defined model. |
| proprietary | Boolean | 1..1 | Behaviour is based on a proprietary model as opposed to a detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. |

