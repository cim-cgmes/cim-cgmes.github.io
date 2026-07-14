# PFVArControllerType1Dynamics

Power factor or VAr controller type 1 function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- PFVArControllerType1Dynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    PFVArControllerType1Dynamics <|-- PFVArType1IEEEPFController
    PFVArType1IEEEPFController : +Boolean ovex[1..1]
    PFVArType1IEEEPFController : +Float tpfc[1..1]
    PFVArType1IEEEPFController : +Float vitmin[1..1]
    PFVArType1IEEEPFController : +Float vpf[1..1]
    PFVArType1IEEEPFController : +Float vpfcbw[1..1]
    PFVArType1IEEEPFController : +Float vpfref[1..1]
    PFVArType1IEEEPFController : +Float vvtmax[1..1]
    PFVArType1IEEEPFController : +Float vvtmin[1..1]
    click PFVArType1IEEEPFController href "PFVArType1IEEEPFController"
    PFVArControllerType1Dynamics <|-- PFVArType1IEEEVArController
    PFVArType1IEEEVArController : +Float tvarc[1..1]
    PFVArType1IEEEVArController : +Float vvar[1..1]
    PFVArType1IEEEVArController : +Float vvarcbw[1..1]
    PFVArType1IEEEVArController : +Float vvarref[1..1]
    PFVArType1IEEEVArController : +Float vvtmax[1..1]
    PFVArType1IEEEVArController : +Float vvtmin[1..1]
    click PFVArType1IEEEVArController href "PFVArType1IEEEVArController"
    PFVArControllerType1Dynamics <|-- PFVArControllerType1UserDefined
    PFVArControllerType1UserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    PFVArControllerType1UserDefined : +Boolean proprietary[1..1]
    click PFVArControllerType1UserDefined href "PFVArControllerType1UserDefined"
    PFVArControllerType1Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PFVArControllerType1Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    PFVArControllerType1Dynamics : +VoltageAdjusterDynamics VoltageAdjusterDynamics[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this power actor or VAr controller type 1 model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this power factor or VAr controller type 1 model. |
| VoltageAdjusterDynamics | [VoltageAdjusterDynamics](VoltageAdjusterDynamics.md) | 0..1 | Voltage adjuster model associated with this power factor or VAr controller type 1 model. |

