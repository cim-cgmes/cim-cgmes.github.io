# ConnectivityNode

Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- ConnectivityNode
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    ConnectivityNode : +BoundaryPoint BoundaryPoint[0..1]
    ConnectivityNode : +ConnectivityNodeContainer ConnectivityNodeContainer[1]
    ConnectivityNode : +Terminal Terminals[0..n]
    ConnectivityNode : +TopologicalNode TopologicalNode[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| BoundaryPoint | [BoundaryPoint](BoundaryPoint.md) | 0..1 | The boundary point associated with the connectivity node. |
| ConnectivityNodeContainer | [ConnectivityNodeContainer](ConnectivityNodeContainer.md) | 1 | Container of this connectivity node. |
| Terminals | [Terminal](Terminal.md) | 0..n | Terminals interconnected with zero impedance at a this connectivity node. |
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 1 | The topological node to which this connectivity node is assigned. May depend on the current state of switches in the network. |

