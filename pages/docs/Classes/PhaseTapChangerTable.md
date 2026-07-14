# PhaseTapChangerTable

Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- PhaseTapChangerTable
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    PhaseTapChangerTable : +PhaseTapChangerTablePoint PhaseTapChangerTablePoint[1..n]
    PhaseTapChangerTable : +PhaseTapChangerTabular PhaseTapChangerTabular[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PhaseTapChangerTablePoint | [PhaseTapChangerTablePoint](PhaseTapChangerTablePoint.md) | 1..n | The points of this table. |
| PhaseTapChangerTabular | [PhaseTapChangerTabular](PhaseTapChangerTabular.md) | 0..n | The phase tap changers to which this phase tap table applies. |

