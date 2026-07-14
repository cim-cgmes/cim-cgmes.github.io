# WindTurbineType1or2IEC

Parent class supporting relationships to IEC wind turbines type 1 and type 2 including their control models. Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous generator model. Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType1or2Dynamics <|-- WindTurbineType1or2IEC
    WindTurbineType1or2Dynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[1]
    WindTurbineType1or2Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click WindTurbineType1or2Dynamics href "WindTurbineType1or2Dynamics"
    WindTurbineType1or2IEC <|-- WindGenTurbineType1aIEC
    WindGenTurbineType1aIEC : +WindAeroConstIEC WindAeroConstIEC[1]
    click WindGenTurbineType1aIEC href "WindGenTurbineType1aIEC"
    WindTurbineType1or2IEC <|-- WindGenTurbineType1bIEC
    WindGenTurbineType1bIEC : +WindPitchContPowerIEC WindPitchContPowerIEC[1]
    click WindGenTurbineType1bIEC href "WindGenTurbineType1bIEC"
    WindTurbineType1or2IEC <|-- WindGenTurbineType2IEC
    WindGenTurbineType2IEC : +WindContRotorRIEC WindContRotorRIEC[1]
    WindGenTurbineType2IEC : +WindPitchContPowerIEC WindPitchContPowerIEC[1]
    click WindGenTurbineType2IEC href "WindGenTurbineType2IEC"
    WindTurbineType1or2IEC : +WindMechIEC WindMechIEC[1]
    WindTurbineType1or2IEC : +WindProtectionIEC WindProtectionIEC[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindMechIEC | [WindMechIEC](WindMechIEC.md) | 1 | Wind mechanical model associated with this wind generator type 1 or type 2 model. |
| WindProtectionIEC | [WindProtectionIEC](WindProtectionIEC.md) | 1 | Wind turbune protection model associated with this wind generator type 1 or type 2 model. |

