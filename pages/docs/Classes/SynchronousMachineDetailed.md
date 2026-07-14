# SynchronousMachineDetailed

All synchronous machine detailed types use a subset of the same data parameters and input/output variables. The several variations differ in the following ways: - the number of equivalent windings that are included; - the way in which saturation is incorporated into the model; - whether or not “subtransient saliency” (X''q not = X''d) is represented. It is not necessary for each simulation tool to have separate models for each of the model types. The same model can often be used for several types by alternative logic within the model. Also, differences in saturation representation might not result in significant model performance differences so model substitutions are often acceptable.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    SynchronousMachineDynamics <|-- SynchronousMachineDetailed
    SynchronousMachineDynamics : +CrossCompoundTurbineGovernorDynamics CrossCompoundTurbineGovernorDyanmics[0..1]
    SynchronousMachineDynamics : +CrossCompoundTurbineGovernorDynamics CrossCompoundTurbineGovernorDynamics[0..1]
    SynchronousMachineDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[0..1]
    SynchronousMachineDynamics : +GenICompensationForGenJ GenICompensationForGenJ[0..n]
    SynchronousMachineDynamics : +MechanicalLoadDynamics MechanicalLoadDynamics[0..1]
    SynchronousMachineDynamics : +SynchronousMachine SynchronousMachine[1]
    SynchronousMachineDynamics : +TurbineGovernorDynamics TurbineGovernorDynamics[0..n]
    click SynchronousMachineDynamics href "SynchronousMachineDynamics"
    SynchronousMachineDetailed <|-- SynchronousMachineTimeConstantReactance
    SynchronousMachineTimeConstantReactance : +Float ks[1..1]
    SynchronousMachineTimeConstantReactance : +SynchronousMachineModelKind modelType[1..1]
    SynchronousMachineTimeConstantReactance : +RotorKind rotorType[0..1]
    SynchronousMachineTimeConstantReactance : +Float tc[1..1]
    SynchronousMachineTimeConstantReactance : +Float tpdo[1..1]
    SynchronousMachineTimeConstantReactance : +Float tppdo[1..1]
    SynchronousMachineTimeConstantReactance : +Float tppqo[1..1]
    SynchronousMachineTimeConstantReactance : +Float tpqo[0..1]
    SynchronousMachineTimeConstantReactance : +Float xDirectSubtrans[1..1]
    SynchronousMachineTimeConstantReactance : +Float xDirectSync[1..1]
    SynchronousMachineTimeConstantReactance : +Float xDirectTrans[1..1]
    SynchronousMachineTimeConstantReactance : +Float xQuadSubtrans[1..1]
    SynchronousMachineTimeConstantReactance : +Float xQuadSync[1..1]
    SynchronousMachineTimeConstantReactance : +Float xQuadTrans[0..1]
    click SynchronousMachineTimeConstantReactance href "SynchronousMachineTimeConstantReactance"
    SynchronousMachineDetailed <|-- SynchronousMachineEquivalentCircuit
    SynchronousMachineEquivalentCircuit : +Float r1d[1..1]
    SynchronousMachineEquivalentCircuit : +Float r1q[1..1]
    SynchronousMachineEquivalentCircuit : +Float r2q[1..1]
    SynchronousMachineEquivalentCircuit : +Float rfd[1..1]
    SynchronousMachineEquivalentCircuit : +Float x1d[1..1]
    SynchronousMachineEquivalentCircuit : +Float x1q[1..1]
    SynchronousMachineEquivalentCircuit : +Float x2q[1..1]
    SynchronousMachineEquivalentCircuit : +Float xad[1..1]
    SynchronousMachineEquivalentCircuit : +Float xaq[1..1]
    SynchronousMachineEquivalentCircuit : +Float xf1d[1..1]
    SynchronousMachineEquivalentCircuit : +Float xfd[1..1]
    click SynchronousMachineEquivalentCircuit href "SynchronousMachineEquivalentCircuit"
    SynchronousMachineDetailed : +Float efdBaseRatio[1..1]
    SynchronousMachineDetailed : +IfdBaseKind ifdBaseType[1..1]
    SynchronousMachineDetailed : +Float saturationFactor120QAxis[0..1]
    SynchronousMachineDetailed : +Float saturationFactorQAxis[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| efdBaseRatio | Float | 1..1 | Ratio (exciter voltage/generator voltage) of Efd bases of exciter and generator models (> 0). Typical value = 1. |
| ifdBaseType | [IfdBaseKind](IfdBaseKind.md) | 1..1 | Excitation base system mode. It should be equal to the value of WLMDV given by the user. WLMDV is the PU ratio between the field voltage and the excitation current: Efd = WLMDV x Ifd. Typical value = ifag. |
| saturationFactor120QAxis | Float | 0..1 | Quadrature-axis saturation factor at 120% of rated terminal voltage (S12q) (>= SynchonousMachineDetailed.saturationFactorQAxis). Typical value = 0,12. |
| saturationFactorQAxis | Float | 0..1 | Quadrature-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical value = 0,02. |

