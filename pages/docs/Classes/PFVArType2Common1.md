# PFVArType2Common1

Power factor / reactive power regulator. This model represents the power factor or reactive power controller such as the Basler SCP-250. The controller measures power factor or reactive power (PU on generator rated power) and compares it with the operator's set point. [Footnote: Basler SCP-250 is an example of a suitable product available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of this product.]

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PFVArControllerType2Dynamics <|-- PFVArType2Common1
    PFVArControllerType2Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    click PFVArControllerType2Dynamics href "PFVArControllerType2Dynamics"
    PFVArType2Common1 : +Boolean j[1..1]
    PFVArType2Common1 : +Float ki[1..1]
    PFVArType2Common1 : +Float kp[1..1]
    PFVArType2Common1 : +Float max[1..1]
    PFVArType2Common1 : +Float ref[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| j | Boolean | 1..1 | Selector (J). true = control mode for reactive power false = control mode for power factor. |
| ki | Float | 1..1 | Reset gain (Ki). |
| kp | Float | 1..1 | Proportional gain (Kp). |
| max | Float | 1..1 | Output limit (max). |
| ref | Float | 1..1 | Reference value of reactive power or power factor (Ref). The reference value is initialised by this model. This initialisation can override the value exchanged by this attribute to represent a plant operator's change of the reference setting. |

