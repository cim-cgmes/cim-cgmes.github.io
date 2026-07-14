# Fuse

An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Switch <|-- Fuse
    Switch : +SvSwitch SvSwitch[0..n]
    Switch : +SwitchSchedule SwitchSchedules[0..n]
    Switch : +Boolean locked[1..1]
    Switch : +Boolean normalOpen[1..1]
    Switch : +Boolean open[1..1]
    Switch : +Float ratedCurrent[0..1]
    Switch : +Boolean retained[1..1]
    click Switch href "Switch"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

