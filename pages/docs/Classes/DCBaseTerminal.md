# DCBaseTerminal

An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model requires that DC connections are distinct from AC connections.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ACDCTerminal <|-- DCBaseTerminal
    ACDCTerminal : +BusNameMarker BusNameMarker[0..1]
    ACDCTerminal : +Measurement Measurements[0..n]
    ACDCTerminal : +OperationalLimitSet OperationalLimitSet[0..n]
    ACDCTerminal : +Boolean connected[1..1]
    ACDCTerminal : +Integer sequenceNumber[1..1]
    click ACDCTerminal href "ACDCTerminal"
    DCBaseTerminal <|-- DCTerminal
    DCTerminal : +DCConductingEquipment DCConductingEquipment[1]
    click DCTerminal href "DCTerminal"
    DCBaseTerminal <|-- ACDCConverterDCTerminal
    ACDCConverterDCTerminal : +ACDCConverter DCConductingEquipment[1]
    ACDCConverterDCTerminal : +DCPolarityKind polarity[1..1]
    click ACDCConverterDCTerminal href "ACDCConverterDCTerminal"
    DCBaseTerminal : +DCNode DCNode[0..1]
    DCBaseTerminal : +DCTopologicalNode DCTopologicalNode[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DCNode | [DCNode](DCNode.md) | 0..1 | The DC connectivity node to which this DC base terminal connects with zero impedance. |
| DCTopologicalNode | [DCTopologicalNode](DCTopologicalNode.md) | 1 | See association end Terminal.TopologicalNode. |

