# BaseVoltage

Defines a system base voltage which is referenced.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- BaseVoltage
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    BaseVoltage : +ConductingEquipment ConductingEquipment[0..n]
    BaseVoltage : +TopologicalNode TopologicalNode[0..n]
    BaseVoltage : +TransformerEnd TransformerEnds[0..n]
    BaseVoltage : +VoltageLevel VoltageLevel[0..n]
    BaseVoltage : +Float nominalVoltage[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ConductingEquipment | [ConductingEquipment](ConductingEquipment.md) | 0..n | All conducting equipment with this base voltage. Use only when there is no voltage level container used and only one base voltage applies. For example, not used for transformers. |
| TopologicalNode | [TopologicalNode](TopologicalNode.md) | 0..n | The topological nodes at the base voltage. |
| TransformerEnds | [TransformerEnd](TransformerEnd.md) | 0..n | Transformer ends at the base voltage. This is essential for PU calculation. |
| VoltageLevel | [VoltageLevel](VoltageLevel.md) | 0..n | The voltage levels having this base voltage. |
| nominalVoltage | Float | 1..1 | The power system resource's base voltage. Shall be a positive value and not zero. |

