# TapChangerControl

Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    RegulatingControl <|-- TapChangerControl
    RegulatingControl : +RegulatingCondEq RegulatingCondEq[0..n]
    RegulatingControl : +RegulationSchedule RegulationSchedule[0..n]
    RegulatingControl : +Terminal Terminal[1..1]
    RegulatingControl : +Boolean discrete[1..1]
    RegulatingControl : +Boolean enabled[1..1]
    RegulatingControl : +Float maxAllowedTargetValue[0..1]
    RegulatingControl : +Float minAllowedTargetValue[0..1]
    RegulatingControl : +RegulatingControlModeKind mode[1..1]
    RegulatingControl : +Float targetDeadband[0..1]
    RegulatingControl : +Float targetValue[1..1]
    RegulatingControl : +UnitMultiplier targetValueUnitMultiplier[1..1]
    click RegulatingControl href "RegulatingControl"
    TapChangerControl : +TapChanger TapChanger[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TapChanger | [TapChanger](TapChanger.md) | 1..n | The tap changers that participates in this regulating tap control scheme. |

