# WindType3or4UserDefined

Wind type 3 or type 4 function block whose dynamic behaviour is described by a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType3or4Dynamics <|-- WindType3or4UserDefined
    WindTurbineType3or4Dynamics : +PowerElectronicsConnection PowerElectronicsConnection[1]
    WindTurbineType3or4Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindTurbineType3or4Dynamics : +WindPlantDynamics WindPlantDynamics[0..1]
    click WindTurbineType3or4Dynamics href "WindTurbineType3or4Dynamics"
    WindType3or4UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    WindType3or4UserDefined : +Boolean proprietary[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ProprietaryParameterDynamics | [ProprietaryParameterDynamics](ProprietaryParameterDynamics.md) | 0..n | Parameter of this proprietary user-defined model. |
| proprietary | Boolean | 1..1 | Behaviour is based on a proprietary model as opposed to a detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. |

