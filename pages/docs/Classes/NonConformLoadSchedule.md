# NonConformLoadSchedule

An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modelled).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SeasonDayTypeSchedule <|-- NonConformLoadSchedule
    SeasonDayTypeSchedule : +DayType DayType[1..1]
    SeasonDayTypeSchedule : +Season Season[1..1]
    click SeasonDayTypeSchedule href "SeasonDayTypeSchedule"
    NonConformLoadSchedule : +NonConformLoadGroup NonConformLoadGroup[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| NonConformLoadGroup | [NonConformLoadGroup](NonConformLoadGroup.md) | 1 | The NonConformLoadGroup where the NonConformLoadSchedule belongs. |

