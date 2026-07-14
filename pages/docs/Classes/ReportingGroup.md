# ReportingGroup

A reporting group is used for various ad-hoc groupings used for reporting.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- ReportingGroup
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    ReportingGroup : +BusNameMarker BusNameMarker[0..n]
    ReportingGroup : +TopologicalNode TopologicalNode[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| BusNameMarker | [BusNameMarker](BusNameMarker.md) | 0..n | The bus name markers that belong to this reporting group. |
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 0..n | The topological nodes that belong to the reporting group. |

