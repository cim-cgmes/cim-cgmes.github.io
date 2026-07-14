# WindTurbineType3or4Dynamics

Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant including their control models.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- WindTurbineType3or4Dynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    WindTurbineType3or4Dynamics <|-- WindType3or4UserDefined
    WindType3or4UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    WindType3or4UserDefined : +Boolean proprietary[1..1]
    click WindType3or4UserDefined href "WindType3or4UserDefined"
    WindTurbineType3or4Dynamics <|-- WindTurbineType3or4IEC
    WindTurbineType3or4IEC : +WindContQIEC WIndContQIEC[1]
    WindTurbineType3or4IEC : +WindContCurrLimIEC WindContCurrLimIEC[1]
    WindTurbineType3or4IEC : +WindContQLimIEC WindContQLimIEC[0..1]
    WindTurbineType3or4IEC : +WindContQPQULimIEC WindContQPQULimIEC[0..1]
    WindTurbineType3or4IEC : +WindProtectionIEC WindProtectionIEC[1]
    WindTurbineType3or4IEC : +WindRefFrameRotIEC WindRefFrameRotIEC[1]
    click WindTurbineType3or4IEC href "WindTurbineType3or4IEC"
    WindTurbineType3or4Dynamics : +PowerElectronicsConnection PowerElectronicsConnection[1]
    WindTurbineType3or4Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindTurbineType3or4Dynamics : +WindPlantDynamics WindPlantDynamics[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PowerElectronicsConnection | [PowerElectronicsConnection](PowerElectronicsConnection.md) | 1 | The power electronics connection associated with this wind turbine type 3 or type 4 dynamics model. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by these wind turbine type 3 or type 4 models. |
| WindPlantDynamics | [WindPlantDynamics](WindPlantDynamics.md) | 0..1 | The wind plant with which the wind turbines type 3 or type 4 are associated. |

