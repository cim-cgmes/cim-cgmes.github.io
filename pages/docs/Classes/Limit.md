# Limit

Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- Limit
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    Limit <|-- AccumulatorLimit
    AccumulatorLimit : +AccumulatorLimitSet LimitSet[1]
    AccumulatorLimit : +Integer value[1..1]
    click AccumulatorLimit href "AccumulatorLimit"
    Limit <|-- AnalogLimit
    AnalogLimit : +AnalogLimitSet LimitSet[1]
    AnalogLimit : +Float value[1..1]
    click AnalogLimit href "AnalogLimit"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

