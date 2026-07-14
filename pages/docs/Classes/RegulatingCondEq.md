# RegulatingCondEq

A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    EnergyConnection <|-- RegulatingCondEq
    click EnergyConnection href "EnergyConnection"
    RegulatingCondEq <|-- RotatingMachine
    RotatingMachine : +GeneratingUnit GeneratingUnit[0..1]
    RotatingMachine : +HydroPump HydroPump[0..1]
    RotatingMachine : +Float p[1..1]
    RotatingMachine : +Float q[1..1]
    RotatingMachine : +Float ratedPowerFactor[0..1]
    RotatingMachine : +Float ratedS[0..1]
    RotatingMachine : +Float ratedU[0..1]
    click RotatingMachine href "RotatingMachine"
    RegulatingCondEq <|-- ExternalNetworkInjection
    ExternalNetworkInjection : +Float governorSCD[1..1]
    ExternalNetworkInjection : +Boolean ikSecond[0..1]
    ExternalNetworkInjection : +Float maxInitialSymShCCurrent[1..1]
    ExternalNetworkInjection : +Float maxP[1..1]
    ExternalNetworkInjection : +Float maxQ[1..1]
    ExternalNetworkInjection : +Float maxR0ToX0Ratio[1..1]
    ExternalNetworkInjection : +Float maxR1ToX1Ratio[1..1]
    ExternalNetworkInjection : +Float maxZ0ToZ1Ratio[1..1]
    ExternalNetworkInjection : +Float minInitialSymShCCurrent[1..1]
    ExternalNetworkInjection : +Float minP[1..1]
    ExternalNetworkInjection : +Float minQ[1..1]
    ExternalNetworkInjection : +Float minR0ToX0Ratio[1..1]
    ExternalNetworkInjection : +Float minR1ToX1Ratio[1..1]
    ExternalNetworkInjection : +Float minZ0ToZ1Ratio[1..1]
    ExternalNetworkInjection : +Float p[1..1]
    ExternalNetworkInjection : +Float q[1..1]
    ExternalNetworkInjection : +Integer referencePriority[1..1]
    ExternalNetworkInjection : +Float voltageFactor[0..1]
    click ExternalNetworkInjection href "ExternalNetworkInjection"
    RegulatingCondEq <|-- ShuntCompensator
    ShuntCompensator : +SvShuntCompensatorSections SvShuntCompensatorSections[0..1]
    ShuntCompensator : +Float aVRDelay[0..1]
    ShuntCompensator : +Boolean grounded[0..1]
    ShuntCompensator : +Integer maximumSections[1..1]
    ShuntCompensator : +Float nomU[1..1]
    ShuntCompensator : +Integer normalSections[1..1]
    ShuntCompensator : +Float sections[1..1]
    ShuntCompensator : +Float voltageSensitivity[0..1]
    click ShuntCompensator href "ShuntCompensator"
    RegulatingCondEq <|-- PowerElectronicsConnection
    PowerElectronicsConnection : +PowerElectronicsUnit PowerElectronicsUnit[0..1]
    PowerElectronicsConnection : +WindTurbineType3or4Dynamics WindTurbineType3or4Dynamics[0..1]
    PowerElectronicsConnection : +Float maxQ[0..1]
    PowerElectronicsConnection : +Float minQ[0..1]
    PowerElectronicsConnection : +Float p[1..1]
    PowerElectronicsConnection : +Float q[1..1]
    PowerElectronicsConnection : +Float ratedS[0..1]
    PowerElectronicsConnection : +Float ratedU[0..1]
    click PowerElectronicsConnection href "PowerElectronicsConnection"
    RegulatingCondEq <|-- StaticVarCompensator
    StaticVarCompensator : +StaticVarCompensatorDynamics StaticVarCompensatorDynamics[0..1]
    StaticVarCompensator : +Float capacitiveRating[1..1]
    StaticVarCompensator : +Float inductiveRating[1..1]
    StaticVarCompensator : +Float q[1..1]
    StaticVarCompensator : +SVCControlMode sVCControlMode[0..1]
    StaticVarCompensator : +Float slope[1..1]
    StaticVarCompensator : +Float voltageSetPoint[0..1]
    click StaticVarCompensator href "StaticVarCompensator"
    RegulatingCondEq : +RegulatingControl RegulatingControl[0..1]
    RegulatingCondEq : +Boolean controlEnabled[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| RegulatingControl | [RegulatingControl](RegulatingControl.md) | 0..1 | The regulating control scheme in which this equipment participates. |
| controlEnabled | Boolean | 1..1 | Specifies the regulation status of the equipment. True is regulating, false is not regulating. |

