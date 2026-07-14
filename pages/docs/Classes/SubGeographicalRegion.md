# SubGeographicalRegion

A subset of a geographical region of a power system network model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- SubGeographicalRegion
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    SubGeographicalRegion : +DCLine DCLines[0..n]
    SubGeographicalRegion : +Line Lines[0..n]
    SubGeographicalRegion : +GeographicalRegion Region[1]
    SubGeographicalRegion : +Substation Substations[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCLines | [DCLine](DCLine.md) | 0..n | The DC lines in this sub-geographical region. |
| Lines | [Line](Line.md) | 0..n | The lines within the sub-geographical region. |
| Region | [GeographicalRegion](GeographicalRegion.md) | 1 | The geographical region which this sub-geographical region is within. |
| Substations | [Substation](Substation.md) | 0..n | The substations in this sub-geographical region. |

