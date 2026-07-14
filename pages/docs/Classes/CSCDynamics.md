# CSCDynamics

CSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    HVDCDynamics <|-- CSCDynamics
    click HVDCDynamics href "HVDCDynamics"
    CSCDynamics <|-- CSCUserDefined
    CSCUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    CSCUserDefined : +Boolean proprietary[1..1]
    click CSCUserDefined href "CSCUserDefined"
    CSCDynamics : +CsConverter CSConverter[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| CSConverter | [CsConverter](CsConverter.md) | 1 | Current source converter to which current source converter dynamics model applies. |

