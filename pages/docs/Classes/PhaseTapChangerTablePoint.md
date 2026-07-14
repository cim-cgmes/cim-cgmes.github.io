# PhaseTapChangerTablePoint

Describes each tap step in the phase tap changer tabular curve.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TapChangerTablePoint <|-- PhaseTapChangerTablePoint
    TapChangerTablePoint : +Float b[0..1]
    TapChangerTablePoint : +Float g[0..1]
    TapChangerTablePoint : +Float r[0..1]
    TapChangerTablePoint : +Float ratio[0..1]
    TapChangerTablePoint : +Integer step[1..1]
    TapChangerTablePoint : +Float x[0..1]
    click TapChangerTablePoint href "TapChangerTablePoint"
    PhaseTapChangerTablePoint : +PhaseTapChangerTable PhaseTapChangerTable[1]
    PhaseTapChangerTablePoint : +Float angle[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| PhaseTapChangerTable | [PhaseTapChangerTable](PhaseTapChangerTable.md) | 1 | The table of this point. |
| angle | Float | 1..1 | The angle difference in degrees. A positive value indicates a positive angle variation from the Terminal at the PowerTransformerEnd, where the TapChanger is located, into the transformer. |

