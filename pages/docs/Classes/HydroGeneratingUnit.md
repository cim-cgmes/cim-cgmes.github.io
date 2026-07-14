# HydroGeneratingUnit

A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    GeneratingUnit <|-- HydroGeneratingUnit
    GeneratingUnit : +ControlAreaGeneratingUnit ControlAreaGeneratingUnit[0..n]
    GeneratingUnit : +GrossToNetActivePowerCurve GrossToNetActivePowerCurves[0..n]
    GeneratingUnit : +RotatingMachine RotatingMachine[1..n]
    GeneratingUnit : +GeneratorControlSource genControlSource[0..1]
    GeneratingUnit : +Float governorSCD[0..1]
    GeneratingUnit : +Float longPF[0..1]
    GeneratingUnit : +Float maxOperatingP[1..1]
    GeneratingUnit : +Float maximumAllowableSpinningReserve[0..1]
    GeneratingUnit : +Float minOperatingP[1..1]
    GeneratingUnit : +Float nominalP[0..1]
    GeneratingUnit : +Float normalPF[1..1]
    GeneratingUnit : +Float ratedGrossMaxP[0..1]
    GeneratingUnit : +Float ratedGrossMinP[0..1]
    GeneratingUnit : +Float ratedNetMaxP[0..1]
    GeneratingUnit : +Float shortPF[0..1]
    GeneratingUnit : +Float startupCost[0..1]
    GeneratingUnit : +Float startupTime[0..1]
    GeneratingUnit : +Float totalEfficiency[0..1]
    GeneratingUnit : +Float variableCost[0..1]
    click GeneratingUnit href "GeneratingUnit"
    HydroGeneratingUnit : +HydroPowerPlant HydroPowerPlant[0..1]
    HydroGeneratingUnit : +Float dropHeight[0..1]
    HydroGeneratingUnit : +HydroEnergyConversionKind energyConversionCapability[0..1]
    HydroGeneratingUnit : +HydroTurbineKind turbineType[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| HydroPowerPlant | [HydroPowerPlant](HydroPowerPlant.md) | 0..1 | The hydro generating unit belongs to a hydro power plant. |
| dropHeight | Float | 0..1 | The height water drops from the reservoir mid-point to the turbine. |
| energyConversionCapability | [HydroEnergyConversionKind](HydroEnergyConversionKind.md) | 0..1 | Energy conversion capability for generating. |
| turbineType | [HydroTurbineKind](HydroTurbineKind.md) | 0..1 | Type of turbine. |

