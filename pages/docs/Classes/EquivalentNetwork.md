# EquivalentNetwork

A class that groups electrical equivalents, including internal nodes, of a network that has been reduced. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are not contained by the equivalent.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConnectivityNodeContainer <|-- EquivalentNetwork
    ConnectivityNodeContainer : +ConnectivityNode ConnectivityNodes[0..n]
    ConnectivityNodeContainer : +TopologicalNode TopologicalNode[0..n]
    click ConnectivityNodeContainer href "ConnectivityNodeContainer"
    EquivalentNetwork : +EquivalentEquipment EquivalentEquipments[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| EquivalentEquipments | [EquivalentEquipment](EquivalentEquipment.md) | 0..n | The associated reduced equivalents. |

