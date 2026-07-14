# NonConformLoadGroup

Loads that do not follow a daily and seasonal load variation pattern.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    LoadGroup <|-- NonConformLoadGroup
    LoadGroup : +SubLoadArea SubLoadArea[1]
    click LoadGroup href "LoadGroup"
    NonConformLoadGroup : +NonConformLoad EnergyConsumers[1..n]
    NonConformLoadGroup : +NonConformLoadSchedule NonConformLoadSchedules[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| EnergyConsumers | [NonConformLoad](NonConformLoad.md) | 1..n | Conform loads assigned to this ConformLoadGroup. |
| NonConformLoadSchedules | [NonConformLoadSchedule](NonConformLoadSchedule.md) | 0..n | The NonConformLoadSchedules in the NonConformLoadGroup. |

