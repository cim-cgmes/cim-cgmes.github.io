# ApparentPowerLimit

Apparent power limit.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    OperationalLimit <|-- ApparentPowerLimit
    OperationalLimit : +OperationalLimitSet OperationalLimitSet[1]
    OperationalLimit : +OperationalLimitType OperationalLimitType[1..1]
    click OperationalLimit href "OperationalLimit"
    ApparentPowerLimit : +Float normalValue[1..1]
    ApparentPowerLimit : +Float value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | The normal apparent power limit. The attribute shall be a positive value or zero. |
| value | Float | 1..1 | The apparent power limit. The attribute shall be a positive value or zero. |

