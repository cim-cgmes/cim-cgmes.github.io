# LoadDynamics

Load whose behaviour is described by reference to a standard model or by definition of a user-defined model. A standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single load definition. The load model is always applied to individual bus loads (energy consumers).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- LoadDynamics
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    LoadDynamics <|-- LoadAggregate
    LoadAggregate : +LoadMotor LoadMotor[0..1]
    LoadAggregate : +LoadStatic LoadStatic[0..1]
    click LoadAggregate href "LoadAggregate"
    LoadDynamics <|-- LoadComposite
    LoadComposite : +Float epfd[1..1]
    LoadComposite : +Float epfs[1..1]
    LoadComposite : +Float epvd[1..1]
    LoadComposite : +Float epvs[1..1]
    LoadComposite : +Float eqfd[1..1]
    LoadComposite : +Float eqfs[1..1]
    LoadComposite : +Float eqvd[1..1]
    LoadComposite : +Float eqvs[1..1]
    LoadComposite : +Float h[1..1]
    LoadComposite : +Float lfac[1..1]
    LoadComposite : +Float pfrac[1..1]
    click LoadComposite href "LoadComposite"
    LoadDynamics <|-- LoadUserDefined
    LoadUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    LoadUserDefined : +Boolean proprietary[1..1]
    click LoadUserDefined href "LoadUserDefined"
    LoadDynamics <|-- LoadGenericNonLinear
    LoadGenericNonLinear : +Float bs[1..1]
    LoadGenericNonLinear : +Float bt[1..1]
    LoadGenericNonLinear : +GenericNonLinearLoadModelKind genericNonLinearLoadModelType[1..1]
    LoadGenericNonLinear : +Float ls[1..1]
    LoadGenericNonLinear : +Float lt[1..1]
    LoadGenericNonLinear : +Float tp[1..1]
    LoadGenericNonLinear : +Float tq[1..1]
    click LoadGenericNonLinear href "LoadGenericNonLinear"
    LoadDynamics : +EnergyConsumer EnergyConsumer[0..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| EnergyConsumer | [EnergyConsumer](EnergyConsumer.md) | 0..n | Energy consumer to which this dynamics load model applies. |

