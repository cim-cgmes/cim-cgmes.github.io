# CurrentLimit

Operational limit on current.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    OperationalLimit <|-- CurrentLimit
    OperationalLimit : +OperationalLimitSet OperationalLimitSet[1]
    OperationalLimit : +OperationalLimitType OperationalLimitType[1..1]
    click OperationalLimit href "OperationalLimit"
    CurrentLimit : +Float normalValue[1..1]
    CurrentLimit : +Float value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | The normal value for limit on current flow. The attribute shall be a positive value or zero. |
| value | Float | 1..1 | Limit on current flow. The attribute shall be a positive value or zero. |

