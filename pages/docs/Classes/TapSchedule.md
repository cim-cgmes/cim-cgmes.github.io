# TapSchedule

A pre-established pattern over time for a tap step.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SeasonDayTypeSchedule <|-- TapSchedule
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
    click SeasonDayTypeSchedule href "SeasonDayTypeSchedule"
    TapSchedule : +TapChanger TapChanger[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TapChanger | [TapChanger](TapChanger.md) | 1 | A TapSchedule is associated with a TapChanger. |

