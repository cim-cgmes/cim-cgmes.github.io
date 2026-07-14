# WindGenTurbineType2IEC

Wind turbine IEC type 2. Reference: IEC 61400-27-1:2015, 5.5.3.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType1or2IEC <|-- WindGenTurbineType2IEC
    WindTurbineType1or2IEC : +WindMechIEC WindMechIEC[1]
    WindTurbineType1or2IEC : +WindProtectionIEC WindProtectionIEC[1]
    click WindTurbineType1or2IEC href "WindTurbineType1or2IEC"
    WindGenTurbineType2IEC : +WindContRotorRIEC WindContRotorRIEC[1]
    WindGenTurbineType2IEC : +WindPitchContPowerIEC WindPitchContPowerIEC[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindContRotorRIEC | [WindContRotorRIEC](WindContRotorRIEC.md) | 1 | Wind control rotor resistance model associated with wind turbine type 2 model. |
| WindPitchContPowerIEC | [WindPitchContPowerIEC](WindPitchContPowerIEC.md) | 1 | Pitch control power model associated with this wind turbine type 2 model. |

