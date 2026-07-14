# WindTurbineType3or4IEC

Parent class supporting relationships to IEC wind turbines type 3 and type 4 including their control models.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType3or4Dynamics <|-- WindTurbineType3or4IEC
    WindTurbineType3or4Dynamics : +PowerElectronicsConnection PowerElectronicsConnection[1]
    WindTurbineType3or4Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindTurbineType3or4Dynamics : +WindPlantDynamics WindPlantDynamics[0..1]
    click WindTurbineType3or4Dynamics href "WindTurbineType3or4Dynamics"
    WindTurbineType3or4IEC <|-- WindTurbineType3IEC
    WindTurbineType3IEC : +WindAeroOneDimIEC WindAeroOneDimIEC[0..1]
    WindTurbineType3IEC : +WindAeroTwoDimIEC WindAeroTwoDimIEC[0..1]
    WindTurbineType3IEC : +WindContPType3IEC WindContPType3IEC[1]
    WindTurbineType3IEC : +WindContPitchAngleIEC WindContPitchAngleIEC[1]
    WindTurbineType3IEC : +WindGenType3IEC WindGenType3IEC[0..1]
    WindTurbineType3IEC : +WindMechIEC WindMechIEC[1]
    click WindTurbineType3IEC href "WindTurbineType3IEC"
    WindTurbineType3or4IEC <|-- WindTurbineType4IEC
    WindTurbineType4IEC : +WindGenType3aIEC WindGenType3aIEC[0..1]
    click WindTurbineType4IEC href "WindTurbineType4IEC"
    WindTurbineType3or4IEC : +WindContQIEC WIndContQIEC[1]
    WindTurbineType3or4IEC : +WindContCurrLimIEC WindContCurrLimIEC[1]
    WindTurbineType3or4IEC : +WindContQLimIEC WindContQLimIEC[0..1]
    WindTurbineType3or4IEC : +WindContQPQULimIEC WindContQPQULimIEC[0..1]
    WindTurbineType3or4IEC : +WindProtectionIEC WindProtectionIEC[1]
    WindTurbineType3or4IEC : +WindRefFrameRotIEC WindRefFrameRotIEC[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WIndContQIEC | [WindContQIEC](WindContQIEC.md) | 1 | Wind control Q model associated with this wind turbine type 3 or type 4 model. |
| WindContCurrLimIEC | [WindContCurrLimIEC](WindContCurrLimIEC.md) | 1 | Wind control current limitation model associated with this wind turbine type 3 or type 4 model. |
| WindContQLimIEC | [WindContQLimIEC](WindContQLimIEC.md) | 0..1 | Constant Q limitation model associated with this wind generator type 3 or type 4 model. |
| WindContQPQULimIEC | [WindContQPQULimIEC](WindContQPQULimIEC.md) | 0..1 | QP and QU limitation model associated with this wind generator type 3 or type 4 model. |
| WindProtectionIEC | [WindProtectionIEC](WindProtectionIEC.md) | 1 | Wind turbune protection model associated with this wind generator type 3 or type 4 model. |
| WindRefFrameRotIEC | [WindRefFrameRotIEC](WindRefFrameRotIEC.md) | 1 | Reference frame rotation model associated with this wind turbine type 3 or type 4 model. |

