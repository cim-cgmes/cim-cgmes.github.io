# RotatingMachine

A rotating machine which may be used as a generator or motor.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    RegulatingCondEq <|-- RotatingMachine
    RegulatingCondEq : +RegulatingControl RegulatingControl[0..1]
    RegulatingCondEq : +Boolean controlEnabled[1..1]
    click RegulatingCondEq href "RegulatingCondEq"
    RotatingMachine <|-- AsynchronousMachine
    AsynchronousMachine : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    AsynchronousMachine : +AsynchronousMachineKind asynchronousMachineType[1..1]
    AsynchronousMachine : +Boolean converterFedDrive[1..1]
    AsynchronousMachine : +Float efficiency[1..1]
    AsynchronousMachine : +Float iaIrRatio[1..1]
    AsynchronousMachine : +Float nominalFrequency[0..1]
    AsynchronousMachine : +Float nominalSpeed[0..1]
    AsynchronousMachine : +Integer polePairNumber[1..1]
    AsynchronousMachine : +Float ratedMechanicalPower[1..1]
    AsynchronousMachine : +Boolean reversible[1..1]
    AsynchronousMachine : +Float rxLockedRotorRatio[0..1]
    click AsynchronousMachine href "AsynchronousMachine"
    RotatingMachine <|-- SynchronousMachine
    SynchronousMachine : +ReactiveCapabilityCurve InitialReactiveCapabilityCurve[0..1]
    SynchronousMachine : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    SynchronousMachine : +Boolean earthing[1..1]
    SynchronousMachine : +Float earthingStarPointR[0..1]
    SynchronousMachine : +Float earthingStarPointX[0..1]
    SynchronousMachine : +Float ikk[0..1]
    SynchronousMachine : +Float maxQ[0..1]
    SynchronousMachine : +Float minQ[0..1]
    SynchronousMachine : +Float mu[0..1]
    SynchronousMachine : +SynchronousMachineOperatingMode operatingMode[1..1]
    SynchronousMachine : +Float qPercent[0..1]
    SynchronousMachine : +Float r[1..1]
    SynchronousMachine : +Float r0[1..1]
    SynchronousMachine : +Float r2[1..1]
    SynchronousMachine : +Integer referencePriority[1..1]
    SynchronousMachine : +Float satDirectSubtransX[1..1]
    SynchronousMachine : +Float satDirectSyncX[0..1]
    SynchronousMachine : +Float satDirectTransX[0..1]
    SynchronousMachine : +ShortCircuitRotorKind shortCircuitRotorType[0..1]
    SynchronousMachine : +SynchronousMachineKind type[1..1]
    SynchronousMachine : +Float voltageRegulationRange[0..1]
    SynchronousMachine : +Float x0[1..1]
    SynchronousMachine : +Float x2[1..1]
    click SynchronousMachine href "SynchronousMachine"
    RotatingMachine : +GeneratingUnit GeneratingUnit[0..1]
    RotatingMachine : +HydroPump HydroPump[0..1]
    RotatingMachine : +Float p[1..1]
    RotatingMachine : +Float q[1..1]
    RotatingMachine : +Float ratedPowerFactor[0..1]
    RotatingMachine : +Float ratedS[0..1]
    RotatingMachine : +Float ratedU[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| GeneratingUnit | [GeneratingUnit](GeneratingUnit.md) | 0..1 | A synchronous machine may operate as a generator and as such becomes a member of a generating unit. |
| HydroPump | [HydroPump](HydroPump.md) | 0..1 | The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. |
| p | Float | 1..1 | Active power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. |
| q | Float | 1..1 | Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. |
| ratedPowerFactor | Float | 0..1 | Power factor (nameplate data). It is primarily used for short circuit data exchange according to IEC 60909. The attribute cannot be a negative value. |
| ratedS | Float | 0..1 | Nameplate apparent power rating for the unit. The attribute shall have a positive value. |
| ratedU | Float | 0..1 | Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909. The attribute shall be a positive value. |

