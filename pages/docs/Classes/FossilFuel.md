# FossilFuel

The fossil fuel consumed by the non-nuclear thermal generating unit. For example, coal, oil, gas, etc. These are the specific fuels that the generating unit can consume.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- FossilFuel
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    FossilFuel : +ThermalGeneratingUnit ThermalGeneratingUnit[1]
    FossilFuel : +FuelType fossilFuelType[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ThermalGeneratingUnit | [ThermalGeneratingUnit](ThermalGeneratingUnit.md) | 1 | A thermal generating unit may have one or more fossil fuels. |
| fossilFuelType | [FuelType](FuelType.md) | 1..1 | The type of fossil fuel, such as coal, oil, or gas. |

