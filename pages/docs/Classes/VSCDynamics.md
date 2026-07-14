# VSCDynamics

VSC function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    HVDCDynamics <|-- VSCDynamics
    click HVDCDynamics href "HVDCDynamics"
    VSCDynamics <|-- VSCUserDefined
    VSCUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    VSCUserDefined : +Boolean proprietary[1..1]
    click VSCUserDefined href "VSCUserDefined"
    VSCDynamics : +VsConverter VsConverter[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| VsConverter | [VsConverter](VsConverter.md) | 1 | Voltage source converter to which voltage source converter dynamics model applies. |

