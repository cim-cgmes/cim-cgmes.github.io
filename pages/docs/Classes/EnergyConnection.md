# EnergyConnection

A connection of energy generation or consumption on the power system model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConductingEquipment <|-- EnergyConnection
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
    click ConductingEquipment href "ConductingEquipment"
    EnergyConnection <|-- EnergySource
    EnergySource : +EnergySchedulingType EnergySchedulingType[0..1]
    EnergySource : +Float activePower[1..1]
    EnergySource : +Float nominalVoltage[0..1]
    EnergySource : +Float pMax[0..1]
    EnergySource : +Float pMin[0..1]
    EnergySource : +Float r[0..1]
    EnergySource : +Float r0[0..1]
    EnergySource : +Float reactivePower[1..1]
    EnergySource : +Float rn[0..1]
    EnergySource : +Float voltageAngle[0..1]
    EnergySource : +Float voltageMagnitude[0..1]
    EnergySource : +Float x[0..1]
    EnergySource : +Float x0[0..1]
    EnergySource : +Float xn[0..1]
    click EnergySource href "EnergySource"
    EnergyConnection <|-- EnergyConsumer
    EnergyConsumer : +LoadDynamics LoadDynamics[0..1]
    EnergyConsumer : +LoadResponseCharacteristic LoadResponse[0..1]
    EnergyConsumer : +Float p[1..1]
    EnergyConsumer : +Float pfixed[0..1]
    EnergyConsumer : +Float pfixedPct[0..1]
    EnergyConsumer : +Float q[1..1]
    EnergyConsumer : +Float qfixed[0..1]
    EnergyConsumer : +Float qfixedPct[0..1]
    click EnergyConsumer href "EnergyConsumer"
    EnergyConnection <|-- RegulatingCondEq
    RegulatingCondEq : +RegulatingControl RegulatingControl[0..1]
    RegulatingCondEq : +Boolean controlEnabled[1..1]
    click RegulatingCondEq href "RegulatingCondEq"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

