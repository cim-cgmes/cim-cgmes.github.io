# RatioTapChangerTablePoint

Describes each tap step in the ratio tap changer tabular curve.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TapChangerTablePoint <|-- RatioTapChangerTablePoint
    TapChangerTablePoint : +Float b[0..1]
    TapChangerTablePoint : +Float g[0..1]
    TapChangerTablePoint : +Float r[0..1]
    TapChangerTablePoint : +Float ratio[0..1]
    TapChangerTablePoint : +Integer step[1..1]
    TapChangerTablePoint : +Float x[0..1]
    click TapChangerTablePoint href "TapChangerTablePoint"
    RatioTapChangerTablePoint : +RatioTapChangerTable RatioTapChangerTable[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RatioTapChangerTable | [RatioTapChangerTable](RatioTapChangerTable.md) | 1 | Table of this point. |

