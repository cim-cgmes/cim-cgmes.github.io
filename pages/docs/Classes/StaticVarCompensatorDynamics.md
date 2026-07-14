# StaticVarCompensatorDynamics

Static var compensator whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- StaticVarCompensatorDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    StaticVarCompensatorDynamics <|-- SVCUserDefined
    SVCUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    SVCUserDefined : +Boolean proprietary[1..1]
    click SVCUserDefined href "SVCUserDefined"
    StaticVarCompensatorDynamics : +StaticVarCompensator StaticVarCompensator[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| StaticVarCompensator | [StaticVarCompensator](StaticVarCompensator.md) | 1 | Static Var Compensator to which Static Var Compensator dynamics model applies. |

