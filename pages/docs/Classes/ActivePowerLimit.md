# ActivePowerLimit

Limit on active power flow.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    OperationalLimit <|-- ActivePowerLimit
    OperationalLimit : +OperationalLimitSet OperationalLimitSet[1]
    OperationalLimit : +OperationalLimitType OperationalLimitType[1..1]
    click OperationalLimit href "OperationalLimit"
    ActivePowerLimit : +Float normalValue[1..1]
    ActivePowerLimit : +Float value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | The normal value of active power limit. The attribute shall be a positive value or zero. |
| value | Float | 1..1 | Value of active power limit. The attribute shall be a positive value or zero. |

