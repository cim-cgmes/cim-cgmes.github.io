# RatioTapChangerTable

Describes a curve for how the voltage magnitude and impedance varies with the tap step.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- RatioTapChangerTable
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    RatioTapChangerTable : +RatioTapChanger RatioTapChanger[0..n]
    RatioTapChangerTable : +RatioTapChangerTablePoint RatioTapChangerTablePoint[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RatioTapChanger | [RatioTapChanger](RatioTapChanger.md) | 0..n | The ratio tap changer of this tap ratio table. |
| RatioTapChangerTablePoint | [RatioTapChangerTablePoint](RatioTapChangerTablePoint.md) | 1..n | Points of this table. |

