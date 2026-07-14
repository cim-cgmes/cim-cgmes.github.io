# ACDCTerminal

An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- ACDCTerminal
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    ACDCTerminal <|-- DCBaseTerminal
    DCBaseTerminal : +DCNode DCNode[0..1]
    DCBaseTerminal : +DCTopologicalNode DCTopologicalNode[1]
    click DCBaseTerminal href "DCBaseTerminal"
    ACDCTerminal <|-- Terminal
    Terminal : +AuxiliaryEquipment AuxiliaryEquipment[0..n]
    Terminal : +ConductingEquipment ConductingEquipment[1]
    Terminal : +ConnectivityNode ConnectivityNode[0..1]
    Terminal : +ACDCConverter ConverterDCSides[0..n]
    Terminal : +MutualCoupling HasFirstMutualCoupling[0..n]
    Terminal : +MutualCoupling HasSecondMutualCoupling[0..n]
    Terminal : +RegulatingControl RegulatingControl[0..n]
    Terminal : +RemoteInputSignal RemoteInputSignal[0..n]
    Terminal : +SvPowerFlow SvPowerFlow[0..1]
    Terminal : +TieFlow TieFlow[0..2]
    Terminal : +TopologicalNode TopologicalNode[0..1]
    Terminal : +TransformerEnd TransformerEnd[0..n]
    Terminal : +PhaseCode phases[0..1]
    click Terminal href "Terminal"
    ACDCTerminal : +BusNameMarker BusNameMarker[0..1]
    ACDCTerminal : +Measurement Measurements[0..n]
    ACDCTerminal : +OperationalLimitSet OperationalLimitSet[0..n]
    ACDCTerminal : +Boolean connected[1..1]
    ACDCTerminal : +Integer sequenceNumber[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| BusNameMarker | [BusNameMarker](BusNameMarker.md) | 0..1 | The bus name marker used to name the bus (topological node). |
| Measurements | [Measurement](Measurement.md) | 0..n | Measurements associated with this terminal defining where the measurement is placed in the network topology. It may be used, for instance, to capture the sensor position, such as a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. |
| OperationalLimitSet | [OperationalLimitSet](OperationalLimitSet.md) | 0..n | The operational limit sets at the terminal. |
| connected | Boolean | 1..1 | The connected status is related to a bus-branch model and the topological node to terminal relation. True implies the terminal is connected to the related topological node and false implies it is not. In a bus-branch model, the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the topological node to terminal relation. A valid case is that conducting equipment can be connected in one end and open in the other. In particular for an AC line segment, where the reactive line charging can be significant, this is a relevant case. |
| sequenceNumber | Integer | 1..1 | The orientation of the terminal connections for a multiple terminal conducting equipment. The sequence numbering starts with 1 and additional terminals should follow in increasing order. The first terminal is the 'starting point' for a two terminal branch. |

