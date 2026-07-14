# SynchronousMachineSimplified

The simplified model represents a synchronous generator as a constant internal voltage behind an impedance (Rs + jXp) as shown in the Simplified diagram. Since internal voltage is held constant, there is no Efd input and any excitation system model will be ignored. There is also no Ifd output. This model should not be used for representing a real generator except, perhaps, small generators whose response is insignificant. The parameters used for the simplified model include: - RotatingMachineDynamics.damping (D); - RotatingMachineDynamics.inertia (H); - RotatingMachineDynamics.statorLeakageReactance (used to exchange jXp for SynchronousMachineSimplified); - RotatingMachineDynamics.statorResistance (Rs).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SynchronousMachineDynamics <|-- SynchronousMachineSimplified
    SynchronousMachineDynamics : +CrossCompoundTurbineGovernorDynamics CrossCompoundTurbineGovernorDyanmics[0..1]
    SynchronousMachineDynamics : +CrossCompoundTurbineGovernorDynamics CrossCompoundTurbineGovernorDynamics[0..1]
    SynchronousMachineDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[0..1]
    SynchronousMachineDynamics : +GenICompensationForGenJ GenICompensationForGenJ[0..n]
    SynchronousMachineDynamics : +MechanicalLoadDynamics MechanicalLoadDynamics[0..1]
    SynchronousMachineDynamics : +SynchronousMachine SynchronousMachine[1]
    SynchronousMachineDynamics : +TurbineGovernorDynamics TurbineGovernorDynamics[0..n]
    click SynchronousMachineDynamics href "SynchronousMachineDynamics"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

