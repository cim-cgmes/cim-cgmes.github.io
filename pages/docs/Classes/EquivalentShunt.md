# EquivalentShunt

The class represents equivalent shunts.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EquivalentEquipment <|-- EquivalentShunt
    EquivalentEquipment : +EquivalentNetwork EquivalentNetwork[0..1]
    click EquivalentEquipment href "EquivalentEquipment"
    EquivalentShunt : +Float b[1..1]
    EquivalentShunt : +Float g[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| b | Float | 1..1 | Positive sequence shunt susceptance. |
| g | Float | 1..1 | Positive sequence shunt conductance. |

