# ThermalGeneratingUnit

A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    GeneratingUnit <|-- ThermalGeneratingUnit
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
    ThermalGeneratingUnit : +CAESPlant CAESPlant[0..1]
    ThermalGeneratingUnit : +CogenerationPlant CogenerationPlant[0..1]
    ThermalGeneratingUnit : +CombinedCyclePlant CombinedCyclePlant[0..1]
    ThermalGeneratingUnit : +FossilFuel FossilFuels[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| CAESPlant | [CAESPlant](CAESPlant.md) | 0..1 | A thermal generating unit may be a member of a compressed air energy storage plant. |
| CogenerationPlant | [CogenerationPlant](CogenerationPlant.md) | 0..1 | A thermal generating unit may be a member of a cogeneration plant. |
| CombinedCyclePlant | [CombinedCyclePlant](CombinedCyclePlant.md) | 0..1 | A thermal generating unit may be a member of a combined cycle plant. |
| FossilFuels | [FossilFuel](FossilFuel.md) | 0..n | A thermal generating unit may have one or more fossil fuels. |

