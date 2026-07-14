# EquivalentEquipment

The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ConductingEquipment <|-- EquivalentEquipment
    ConductingEquipment : +BaseVoltage BaseVoltage[0..1]
    ConductingEquipment : +SvStatus SvStatus[0..1]
    ConductingEquipment : +Terminal Terminals[0..n]
    click ConductingEquipment href "ConductingEquipment"
    EquivalentEquipment <|-- EquivalentShunt
    EquivalentShunt : +Float b[1..1]
    EquivalentShunt : +Float g[1..1]
    click EquivalentShunt href "EquivalentShunt"
    EquivalentEquipment <|-- EquivalentInjection
    EquivalentInjection : +ReactiveCapabilityCurve ReactiveCapabilityCurve[0..1]
    EquivalentInjection : +Float maxP[0..1]
    EquivalentInjection : +Float maxQ[0..1]
    EquivalentInjection : +Float minP[0..1]
    EquivalentInjection : +Float minQ[0..1]
    EquivalentInjection : +Float p[1..1]
    EquivalentInjection : +Float q[1..1]
    EquivalentInjection : +Float r[1..1]
    EquivalentInjection : +Float r0[1..1]
    EquivalentInjection : +Float r2[1..1]
    EquivalentInjection : +Boolean regulationCapability[1..1]
    EquivalentInjection : +Boolean regulationStatus[0..1]
    EquivalentInjection : +Float regulationTarget[0..1]
    EquivalentInjection : +Float x[1..1]
    EquivalentInjection : +Float x0[1..1]
    EquivalentInjection : +Float x2[1..1]
    click EquivalentInjection href "EquivalentInjection"
    EquivalentEquipment <|-- EquivalentBranch
    EquivalentBranch : +Float negativeR12[1..1]
    EquivalentBranch : +Float negativeR21[1..1]
    EquivalentBranch : +Float negativeX12[1..1]
    EquivalentBranch : +Float negativeX21[1..1]
    EquivalentBranch : +Float positiveR12[1..1]
    EquivalentBranch : +Float positiveR21[1..1]
    EquivalentBranch : +Float positiveX12[1..1]
    EquivalentBranch : +Float positiveX21[1..1]
    EquivalentBranch : +Float r[1..1]
    EquivalentBranch : +Float r21[0..1]
    EquivalentBranch : +Float x[1..1]
    EquivalentBranch : +Float x21[0..1]
    EquivalentBranch : +Float zeroR12[1..1]
    EquivalentBranch : +Float zeroR21[1..1]
    EquivalentBranch : +Float zeroX12[1..1]
    EquivalentBranch : +Float zeroX21[1..1]
    click EquivalentBranch href "EquivalentBranch"
    EquivalentEquipment : +EquivalentNetwork EquivalentNetwork[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| EquivalentNetwork | [EquivalentNetwork](EquivalentNetwork.md) | 0..1 | The equivalent where the reduced model belongs. |

