# PowerElectronicsUnit

A generating unit or battery or aggregation that connects to the AC network using power electronics rather than rotating machines.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Equipment <|-- PowerElectronicsUnit
    Equipment : +EquipmentContainer EquipmentContainer[0..1]
    Equipment : +OperationalLimitSet OperationalLimitSet[0..n]
    Equipment : +Boolean aggregate[0..1]
    Equipment : +Boolean inService[1..1]
    Equipment : +Boolean normallyInService[0..1]
    click Equipment href "Equipment"
    PowerElectronicsUnit <|-- PhotoVoltaicUnit
    click PhotoVoltaicUnit href "PhotoVoltaicUnit"
    PowerElectronicsUnit <|-- PowerElectronicsWindUnit
    click PowerElectronicsWindUnit href "PowerElectronicsWindUnit"
    PowerElectronicsUnit <|-- BatteryUnit
    BatteryUnit : +BatteryStateKind batteryState[1..1]
    BatteryUnit : +Float ratedE[1..1]
    BatteryUnit : +Float storedE[1..1]
    click BatteryUnit href "BatteryUnit"
    PowerElectronicsUnit : +PowerElectronicsConnection PowerElectronicsConnection[1]
    PowerElectronicsUnit : +Float maxP[0..1]
    PowerElectronicsUnit : +Float minP[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PowerElectronicsConnection | [PowerElectronicsConnection](PowerElectronicsConnection.md) | 1 | A power electronics unit has a connection to the AC network. |
| maxP | Float | 0..1 | Maximum active power limit. This is the maximum (nameplate) limit for the unit. |
| minP | Float | 0..1 | Minimum active power limit. This is the minimum (nameplate) limit for the unit. |

