# CSCDynamics

CSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    HVDCDynamics <|-- CSCDynamics
    CSCDynamics <|-- CSCUserDefined
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| CSConverter | [CsConverter](CsConverter.md) | 1 | Current source converter to which current source converter dynamics model applies. |

