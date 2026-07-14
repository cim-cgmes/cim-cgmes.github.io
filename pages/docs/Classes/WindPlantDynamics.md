# WindPlantDynamics

Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant IEC and user-defined wind plants including their control models.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- WindPlantDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    WindPlantDynamics <|-- WindPlantUserDefined
    WindPlantUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    WindPlantUserDefined : +Boolean proprietary[1..1]
    click WindPlantUserDefined href "WindPlantUserDefined"
    WindPlantDynamics <|-- WindPlantIEC
    WindPlantIEC : +WindPlantFreqPcontrolIEC WindPlantFreqPcontrolIEC[1]
    WindPlantIEC : +WindPlantReactiveControlIEC WindPlantReactiveControlIEC[1]
    click WindPlantIEC href "WindPlantIEC"
    WindPlantDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindPlantDynamics : +WindTurbineType3or4Dynamics WindTurbineType3or4Dynamics[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | The remote signal with which this power plant is associated. |
| WindTurbineType3or4Dynamics | [WindTurbineType3or4Dynamics](WindTurbineType3or4Dynamics.md) | 1..n | The wind turbine type 3 or type 4 associated with this wind plant. |

