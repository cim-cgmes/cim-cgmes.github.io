# ActivePowerLimit

Limit on active power flow.

## Inheritance

```mermaid
classDiagram
    OperationalLimit <|-- ActivePowerLimit
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | The normal value of active power limit. The attribute shall be a positive value or zero. |
| value | Float | 1..1 | Value of active power limit. The attribute shall be a positive value or zero. |

