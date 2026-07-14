# ConnectivityNodeContainer

A base class for all objects that may contain connectivity nodes or topological nodes.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemResource <|-- ConnectivityNodeContainer
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    ConnectivityNodeContainer <|-- EquipmentContainer
    EquipmentContainer : +Equipment Equipments[0..n]
    click EquipmentContainer href "EquipmentContainer"
    ConnectivityNodeContainer <|-- EquivalentNetwork
    EquivalentNetwork : +EquivalentEquipment EquivalentEquipments[0..n]
    click EquivalentNetwork href "EquivalentNetwork"
    ConnectivityNodeContainer : +ConnectivityNode ConnectivityNodes[0..n]
    ConnectivityNodeContainer : +TopologicalNode TopologicalNode[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ConnectivityNodes | [ConnectivityNode](ConnectivityNode.md) | 0..n | Connectivity nodes which belong to this connectivity node container. |
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 0..n | The topological nodes which belong to this connectivity node container. |

