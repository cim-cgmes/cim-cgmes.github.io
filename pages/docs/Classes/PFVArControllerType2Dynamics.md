# PFVArControllerType2Dynamics

Power factor or VAr controller type 2 function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- PFVArControllerType2Dynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    PFVArControllerType2Dynamics <|-- PFVArType2IEEEPFController
    PFVArType2IEEEPFController : +Boolean exlon[1..1]
    PFVArType2IEEEPFController : +Float ki[1..1]
    PFVArType2IEEEPFController : +Float kp[1..1]
    PFVArType2IEEEPFController : +Float pfref[1..1]
    PFVArType2IEEEPFController : +Float vclmt[1..1]
    PFVArType2IEEEPFController : +Float vref[1..1]
    PFVArType2IEEEPFController : +Float vs[1..1]
    click PFVArType2IEEEPFController href "PFVArType2IEEEPFController"
    PFVArControllerType2Dynamics <|-- PFVArType2Common1
    PFVArType2Common1 : +Boolean j[1..1]
    PFVArType2Common1 : +Float ki[1..1]
    PFVArType2Common1 : +Float kp[1..1]
    PFVArType2Common1 : +Float max[1..1]
    PFVArType2Common1 : +Float ref[1..1]
    click PFVArType2Common1 href "PFVArType2Common1"
    PFVArControllerType2Dynamics <|-- PFVArControllerType2UserDefined
    PFVArControllerType2UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    PFVArControllerType2UserDefined : +Boolean proprietary[1..1]
    click PFVArControllerType2UserDefined href "PFVArControllerType2UserDefined"
    PFVArControllerType2Dynamics <|-- PFVArType2IEEEVArController
    PFVArType2IEEEVArController : +Boolean exlon[1..1]
    PFVArType2IEEEVArController : +Float ki[1..1]
    PFVArType2IEEEVArController : +Float kp[1..1]
    PFVArType2IEEEVArController : +Float qref[1..1]
    PFVArType2IEEEVArController : +Float vclmt[1..1]
    PFVArType2IEEEVArController : +Float vref[1..1]
    PFVArType2IEEEVArController : +Float vs[1..1]
    click PFVArType2IEEEVArController href "PFVArType2IEEEVArController"
    PFVArControllerType2Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this power factor or VAr controller type 2 is associated. |

