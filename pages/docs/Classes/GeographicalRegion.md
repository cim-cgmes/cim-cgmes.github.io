# GeographicalRegion

A geographical region of a power system network model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- GeographicalRegion
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    GeographicalRegion : +SubGeographicalRegion Regions[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Regions | [SubGeographicalRegion](SubGeographicalRegion.md) | 0..n | All sub-geographical regions within this geographical region. |

