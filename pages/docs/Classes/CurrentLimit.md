# CurrentLimit

Operational limit on current.

## Inheritance

```mermaid
classDiagram
    OperationalLimit <|-- CurrentLimit
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| normalValue | Float | 1..1 | The normal value for limit on current flow. The attribute shall be a positive value or zero. |
| value | Float | 1..1 | Limit on current flow. The attribute shall be a positive value or zero. |

