# LoadGroup

The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- LoadGroup
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    LoadGroup <|-- NonConformLoadGroup
    NonConformLoadGroup : +NonConformLoad EnergyConsumers[1..n]
    NonConformLoadGroup : +NonConformLoadSchedule NonConformLoadSchedules[0..n]
    click NonConformLoadGroup href "NonConformLoadGroup"
    LoadGroup <|-- ConformLoadGroup
    ConformLoadGroup : +ConformLoadSchedule ConformLoadSchedules[0..n]
    ConformLoadGroup : +ConformLoad EnergyConsumers[1..n]
    click ConformLoadGroup href "ConformLoadGroup"
    LoadGroup : +SubLoadArea SubLoadArea[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| SubLoadArea | [SubLoadArea](SubLoadArea.md) | 1 | The SubLoadArea where the Loadgroup belongs. |

