# DCNode

DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- DCNode
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    DCNode : +DCEquipmentContainer DCEquipmentContainer[1]
    DCNode : +DCBaseTerminal DCTerminals[0..n]
    DCNode : +DCTopologicalNode DCTopologicalNode[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCEquipmentContainer | [DCEquipmentContainer](DCEquipmentContainer.md) | 1 | The DC container for the DC nodes. |
| DCTerminals | [DCBaseTerminal](DCBaseTerminal.md) | 0..n | DC base terminals interconnected with zero impedance at a this DC connectivity node. |
| DCTopologicalNode | [DCTopologicalNode](DCTopologicalNode.md) | 1 | The DC topological node to which this DC connectivity node is assigned. May depend on the current state of switches in the network. |

