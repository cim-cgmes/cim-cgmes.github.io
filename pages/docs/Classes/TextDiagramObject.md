# TextDiagramObject

A diagram object for placing free-text or text derived from an associated domain object.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DiagramObject <|-- TextDiagramObject
    DiagramObject : +Diagram Diagram[1]
    DiagramObject : +DiagramObjectPoint DiagramObjectPoints[0..n]
    DiagramObject : +DiagramObjectStyle DiagramObjectStyle[0..1]
    DiagramObject : +IdentifiedObject IdentifiedObject_[0..1]
    DiagramObject : +VisibilityLayer VisibilityLayers[0..n]
    DiagramObject : +Integer drawingOrder[0..1]
    DiagramObject : +Boolean isPolygon[0..1]
    DiagramObject : +Float offsetX[0..1]
    DiagramObject : +Float offsetY[0..1]
    DiagramObject : +Float rotation[0..1]
    click DiagramObject href "DiagramObject"
    TextDiagramObject : +String text[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| text | String | 1..1 | The text that is displayed by this text diagram object. |

