# DiagramStyle

The diagram style refers to a style used by the originating system for a diagram. A diagram style describes information such as schematic, geographic, etc.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- DiagramStyle
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    DiagramStyle : +Diagram Diagram[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Diagram | [Diagram](Diagram.md) | 0..n | A DiagramStyle can be used by many Diagrams. |

