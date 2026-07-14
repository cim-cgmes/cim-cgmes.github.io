# OperationalLimit

A value and normal value associated with a specific kind of limit. The sub class value and normalValue attributes vary inversely to the associated OperationalLimitType.acceptableDuration (acceptableDuration for short). If a particular piece of equipment has multiple operational limits of the same kind (apparent power, current, etc.), the limit with the greatest acceptableDuration shall have the smallest limit value and the limit with the smallest acceptableDuration shall have the largest limit value. Note: A large current can only be allowed to flow through a piece of equipment for a short duration without causing damage, but a lesser current can be allowed to flow for a longer duration.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- OperationalLimit
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    OperationalLimit <|-- ApparentPowerLimit
    ApparentPowerLimit : +Float normalValue[1..1]
    ApparentPowerLimit : +Float value[1..1]
    click ApparentPowerLimit href "ApparentPowerLimit"
    OperationalLimit <|-- ActivePowerLimit
    ActivePowerLimit : +Float normalValue[1..1]
    ActivePowerLimit : +Float value[1..1]
    click ActivePowerLimit href "ActivePowerLimit"
    OperationalLimit <|-- CurrentLimit
    CurrentLimit : +Float normalValue[1..1]
    CurrentLimit : +Float value[1..1]
    click CurrentLimit href "CurrentLimit"
    OperationalLimit <|-- VoltageLimit
    VoltageLimit : +Float normalValue[1..1]
    VoltageLimit : +Float value[1..1]
    click VoltageLimit href "VoltageLimit"
    OperationalLimit : +OperationalLimitSet OperationalLimitSet[1]
    OperationalLimit : +OperationalLimitType OperationalLimitType[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| OperationalLimitSet | [OperationalLimitSet](OperationalLimitSet.md) | 1 | The limit set to which the limit values belong. |
| OperationalLimitType | [OperationalLimitType](OperationalLimitType.md) | 1..1 | The limit type associated with this limit. |

