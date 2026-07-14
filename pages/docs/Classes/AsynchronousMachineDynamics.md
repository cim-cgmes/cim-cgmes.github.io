# AsynchronousMachineDynamics

Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant reactance form or equivalent circuit form or by definition of a user-defined model. Parameter details: Asynchronous machine parameters such as Xl, Xs, etc. are actually used as inductances in the model, but are commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some references use the symbol L instead of X.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    RotatingMachineDynamics <|-- AsynchronousMachineDynamics
    RotatingMachineDynamics : +Float damping[1..1]
    RotatingMachineDynamics : +Float inertia[1..1]
    RotatingMachineDynamics : +Float saturationFactor[0..1]
    RotatingMachineDynamics : +Float saturationFactor120[0..1]
    RotatingMachineDynamics : +Float statorLeakageReactance[1..1]
    RotatingMachineDynamics : +Float statorResistance[1..1]
    click RotatingMachineDynamics href "RotatingMachineDynamics"
    AsynchronousMachineDynamics <|-- AsynchronousMachineUserDefined
    AsynchronousMachineUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    AsynchronousMachineUserDefined : +Boolean proprietary[1..1]
    click AsynchronousMachineUserDefined href "AsynchronousMachineUserDefined"
    AsynchronousMachineDynamics <|-- AsynchronousMachineTimeConstantReactance
    AsynchronousMachineTimeConstantReactance : +Float tpo[1..1]
    AsynchronousMachineTimeConstantReactance : +Float tppo[1..1]
    AsynchronousMachineTimeConstantReactance : +Float xp[1..1]
    AsynchronousMachineTimeConstantReactance : +Float xpp[1..1]
    AsynchronousMachineTimeConstantReactance : +Float xs[1..1]
    click AsynchronousMachineTimeConstantReactance href "AsynchronousMachineTimeConstantReactance"
    AsynchronousMachineDynamics <|-- AsynchronousMachineEquivalentCircuit
    AsynchronousMachineEquivalentCircuit : +Float rr1[1..1]
    AsynchronousMachineEquivalentCircuit : +Float rr2[1..1]
    AsynchronousMachineEquivalentCircuit : +Float xlr1[1..1]
    AsynchronousMachineEquivalentCircuit : +Float xlr2[1..1]
    AsynchronousMachineEquivalentCircuit : +Float xm[1..1]
    click AsynchronousMachineEquivalentCircuit href "AsynchronousMachineEquivalentCircuit"
    AsynchronousMachineDynamics : +AsynchronousMachine AsynchronousMachine[1]
    AsynchronousMachineDynamics : +MechanicalLoadDynamics MechanicalLoadDynamics[0..1]
    AsynchronousMachineDynamics : +TurbineGovernorDynamics TurbineGovernorDynamics[0..1]
    AsynchronousMachineDynamics : +WindTurbineType1or2Dynamics WindTurbineType1or2Dynamics[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AsynchronousMachine | [AsynchronousMachine](AsynchronousMachine.md) | 1 | Asynchronous machine to which this asynchronous machine dynamics model applies. |
| MechanicalLoadDynamics | [MechanicalLoadDynamics](MechanicalLoadDynamics.md) | 0..1 | Mechanical load model associated with this asynchronous machine model. |
| TurbineGovernorDynamics | [TurbineGovernorDynamics](TurbineGovernorDynamics.md) | 0..1 | Turbine-governor model associated with this asynchronous machine model. |
| WindTurbineType1or2Dynamics | [WindTurbineType1or2Dynamics](WindTurbineType1or2Dynamics.md) | 0..1 | Wind generator type 1 or type 2 model associated with this asynchronous machine model. |

