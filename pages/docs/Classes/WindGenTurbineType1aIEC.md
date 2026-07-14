# WindGenTurbineType1aIEC

Wind turbine IEC type 1A. Reference: IEC 61400-27-1:2015, 5.5.2.2.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    WindTurbineType1or2IEC <|-- WindGenTurbineType1aIEC
    WindTurbineType1or2IEC : +WindMechIEC WindMechIEC[1]
    WindTurbineType1or2IEC : +WindProtectionIEC WindProtectionIEC[1]
    click WindTurbineType1or2IEC href "WindTurbineType1or2IEC"
    WindGenTurbineType1aIEC : +WindAeroConstIEC WindAeroConstIEC[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| WindAeroConstIEC | [WindAeroConstIEC](WindAeroConstIEC.md) | 1 | Wind aerodynamic model associated with this wind turbine type 1A model. |

