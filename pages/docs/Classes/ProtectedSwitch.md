# ProtectedSwitch

A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Switch <|-- ProtectedSwitch
    Switch : +SvSwitch SvSwitch[0..n]
    Switch : +SwitchSchedule SwitchSchedules[0..n]
    Switch : +Boolean locked[1..1]
    Switch : +Boolean normalOpen[1..1]
    Switch : +Boolean open[1..1]
    Switch : +Float ratedCurrent[0..1]
    Switch : +Boolean retained[1..1]
    click Switch href "Switch"
    ProtectedSwitch <|-- LoadBreakSwitch
    click LoadBreakSwitch href "LoadBreakSwitch"
    ProtectedSwitch <|-- Breaker
    click Breaker href "Breaker"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

