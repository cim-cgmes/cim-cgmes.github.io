# Disconnector

A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Switch <|-- Disconnector
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

