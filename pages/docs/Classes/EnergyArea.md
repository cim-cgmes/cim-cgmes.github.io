# EnergyArea

Describes an area having energy production or consumption. Specializations are intended to support the load allocation function as typically required in energy management systems or planning studies to allocate hypothesized load levels to individual load points for power flow analysis. Often the energy area can be linked to both measured and forecast load levels.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- EnergyArea
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    EnergyArea <|-- SubLoadArea
    SubLoadArea : +LoadArea LoadArea[1]
    SubLoadArea : +LoadGroup LoadGroups[1..n]
    click SubLoadArea href "SubLoadArea"
    EnergyArea <|-- LoadArea
    LoadArea : +SubLoadArea SubLoadAreas[1..n]
    click LoadArea href "LoadArea"
    EnergyArea : +ControlArea ControlArea[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ControlArea | [ControlArea](ControlArea.md) | 0..1 | The control area specification that is used for the load forecast. |

