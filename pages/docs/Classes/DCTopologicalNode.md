# DCTopologicalNode

DC bus.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- DCTopologicalNode
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    DCTopologicalNode : +DCEquipmentContainer DCEquipmentContainer[1]
    DCTopologicalNode : +DCNode DCNodes[0..n]
    DCTopologicalNode : +DCBaseTerminal DCTerminals[0..n]
    DCTopologicalNode : +DCTopologicalIsland DCTopologicalIsland[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCEquipmentContainer | [DCEquipmentContainer](DCEquipmentContainer.md) | 1 | The connectivity node container to which the topological node belongs. |
| DCNodes | [DCNode](DCNode.md) | 0..n | The DC connectivity nodes combined together to form this DC topological node. May depend on the current state of switches in the network. |
| DCTerminals | [DCBaseTerminal](DCBaseTerminal.md) | 0..n | See association end TopologicalNode.Terminal. |
| DCTopologicalIsland | [DCTopologicalIsland](DCTopologicalIsland.md) | 0..1 | A DC topological node belongs to a DC topological island. |

