# PFVArType1IEEEVArController

IEEE VAR controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005, 11.3.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PFVArControllerType1Dynamics <|-- PFVArType1IEEEVArController
    PFVArControllerType1Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PFVArControllerType1Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    PFVArControllerType1Dynamics : +VoltageAdjusterDynamics VoltageAdjusterDynamics[0..1]
    click PFVArControllerType1Dynamics href "PFVArControllerType1Dynamics"
    PFVArType1IEEEVArController : +Float tvarc[1..1]
    PFVArType1IEEEVArController : +Float vvar[1..1]
    PFVArType1IEEEVArController : +Float vvarcbw[1..1]
    PFVArType1IEEEVArController : +Float vvarref[1..1]
    PFVArType1IEEEVArController : +Float vvtmax[1..1]
    PFVArType1IEEEVArController : +Float vvtmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| tvarc | Float | 1..1 | Var controller time delay (TVARC) (>= 0). Typical value = 5. |
| vvar | Float | 1..1 | Synchronous machine power factor (VVAR). |
| vvarcbw | Float | 1..1 | Var controller deadband (VVARC_BW). Typical value = 0,02. |
| vvarref | Float | 1..1 | Var controller reference (VVARREF). |
| vvtmax | Float | 1..1 | Maximum machine terminal voltage needed for pf/VAr controller to be enabled (VVTMAX) (> PVFArType1IEEEVArController.vvtmin). |
| vvtmin | Float | 1..1 | Minimum machine terminal voltage needed to enable pf/var controller (VVTMIN) (< PVFArType1IEEEVArController.vvtmax). |

