# BatteryUnit

An electrochemical energy storage device.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerElectronicsUnit <|-- BatteryUnit
    PowerElectronicsUnit : +PowerElectronicsConnection PowerElectronicsConnection[1]
    PowerElectronicsUnit : +Float maxP[0..1]
    PowerElectronicsUnit : +Float minP[0..1]
    click PowerElectronicsUnit href "PowerElectronicsUnit"
    BatteryUnit : +BatteryStateKind batteryState[1..1]
    BatteryUnit : +Float ratedE[1..1]
    BatteryUnit : +Float storedE[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| batteryState | [BatteryStateKind](BatteryStateKind.md) | 1..1 | The current state of the battery (charging, full, etc.). |
| ratedE | Float | 1..1 | Full energy storage capacity of the battery. The attribute shall be a positive value. |
| storedE | Float | 1..1 | Amount of energy currently stored. The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE. |

