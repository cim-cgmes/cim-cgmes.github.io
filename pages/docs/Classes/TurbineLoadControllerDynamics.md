# TurbineLoadControllerDynamics

Turbine load controller function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- TurbineLoadControllerDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    TurbineLoadControllerDynamics <|-- TurbLCFB1
    TurbLCFB1 : +Float db[1..1]
    TurbLCFB1 : +Float emax[1..1]
    TurbLCFB1 : +Float fb[1..1]
    TurbLCFB1 : +Boolean fbf[1..1]
    TurbLCFB1 : +Float irmax[1..1]
    TurbLCFB1 : +Float ki[1..1]
    TurbLCFB1 : +Float kp[1..1]
    TurbLCFB1 : +Float mwbase[1..1]
    TurbLCFB1 : +Boolean pbf[1..1]
    TurbLCFB1 : +Float pmwset[1..1]
    TurbLCFB1 : +Boolean speedReferenceGovernor[1..1]
    TurbLCFB1 : +Float tpelec[1..1]
    click TurbLCFB1 href "TurbLCFB1"
    TurbineLoadControllerDynamics <|-- TurbineLoadControllerUserDefined
    TurbineLoadControllerUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    TurbineLoadControllerUserDefined : +Boolean proprietary[1..1]
    click TurbineLoadControllerUserDefined href "TurbineLoadControllerUserDefined"
    TurbineLoadControllerDynamics : +TurbineGovernorDynamics TurbineGovernorDynamics[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| TurbineGovernorDynamics | [TurbineGovernorDynamics](TurbineGovernorDynamics.md) | 1 | Turbine-governor controlled by this turbine load controller. |

