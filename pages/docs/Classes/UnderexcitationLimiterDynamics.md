# UnderexcitationLimiterDynamics

Underexcitation limiter function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- UnderexcitationLimiterDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    UnderexcitationLimiterDynamics <|-- UnderexcLimX1
    UnderexcLimX1 : +Float k[1..1]
    UnderexcLimX1 : +Float kf2[1..1]
    UnderexcLimX1 : +Float km[1..1]
    UnderexcLimX1 : +Float melmax[1..1]
    UnderexcLimX1 : +Float tf2[1..1]
    UnderexcLimX1 : +Float tm[1..1]
    click UnderexcLimX1 href "UnderexcLimX1"
    UnderexcitationLimiterDynamics <|-- UnderexcitationLimiterUserDefined
    UnderexcitationLimiterUserDefined : +ProprietaryParameterDynamics ProprietaryParameterDynamics[0..n]
    UnderexcitationLimiterUserDefined : +Boolean proprietary[1..1]
    click UnderexcitationLimiterUserDefined href "UnderexcitationLimiterUserDefined"
    UnderexcitationLimiterDynamics <|-- UnderexcLim2Simplified
    UnderexcLim2Simplified : +Float kui[1..1]
    UnderexcLim2Simplified : +Float p0[1..1]
    UnderexcLim2Simplified : +Float p1[1..1]
    UnderexcLim2Simplified : +Float q0[1..1]
    UnderexcLim2Simplified : +Float q1[1..1]
    UnderexcLim2Simplified : +Float vuimax[1..1]
    UnderexcLim2Simplified : +Float vuimin[1..1]
    click UnderexcLim2Simplified href "UnderexcLim2Simplified"
    UnderexcitationLimiterDynamics <|-- UnderexcLimIEEE2
    UnderexcLimIEEE2 : +Float k1[1..1]
    UnderexcLimIEEE2 : +Float k2[1..1]
    UnderexcLimIEEE2 : +Float kfb[1..1]
    UnderexcLimIEEE2 : +Float kuf[1..1]
    UnderexcLimIEEE2 : +Float kui[1..1]
    UnderexcLimIEEE2 : +Float kul[1..1]
    UnderexcLimIEEE2 : +Float p0[1..1]
    UnderexcLimIEEE2 : +Float p1[1..1]
    UnderexcLimIEEE2 : +Float p10[1..1]
    UnderexcLimIEEE2 : +Float p2[1..1]
    UnderexcLimIEEE2 : +Float p3[1..1]
    UnderexcLimIEEE2 : +Float p4[1..1]
    UnderexcLimIEEE2 : +Float p5[1..1]
    UnderexcLimIEEE2 : +Float p6[1..1]
    UnderexcLimIEEE2 : +Float p7[1..1]
    UnderexcLimIEEE2 : +Float p8[1..1]
    UnderexcLimIEEE2 : +Float p9[1..1]
    UnderexcLimIEEE2 : +Float q0[1..1]
    UnderexcLimIEEE2 : +Float q1[1..1]
    UnderexcLimIEEE2 : +Float q10[1..1]
    UnderexcLimIEEE2 : +Float q2[1..1]
    UnderexcLimIEEE2 : +Float q3[1..1]
    UnderexcLimIEEE2 : +Float q4[1..1]
    UnderexcLimIEEE2 : +Float q5[1..1]
    UnderexcLimIEEE2 : +Float q6[1..1]
    UnderexcLimIEEE2 : +Float q7[1..1]
    UnderexcLimIEEE2 : +Float q8[1..1]
    UnderexcLimIEEE2 : +Float q9[1..1]
    UnderexcLimIEEE2 : +Float tu1[1..1]
    UnderexcLimIEEE2 : +Float tu2[1..1]
    UnderexcLimIEEE2 : +Float tu3[1..1]
    UnderexcLimIEEE2 : +Float tu4[1..1]
    UnderexcLimIEEE2 : +Float tul[1..1]
    UnderexcLimIEEE2 : +Float tup[1..1]
    UnderexcLimIEEE2 : +Float tuq[1..1]
    UnderexcLimIEEE2 : +Float tuv[1..1]
    UnderexcLimIEEE2 : +Float vuimax[1..1]
    UnderexcLimIEEE2 : +Float vuimin[1..1]
    UnderexcLimIEEE2 : +Float vulmax[1..1]
    UnderexcLimIEEE2 : +Float vulmin[1..1]
    click UnderexcLimIEEE2 href "UnderexcLimIEEE2"
    UnderexcitationLimiterDynamics <|-- UnderexcLimX2
    UnderexcLimX2 : +Float kf2[1..1]
    UnderexcLimX2 : +Float km[1..1]
    UnderexcLimX2 : +Float melmax[1..1]
    UnderexcLimX2 : +Float qo[1..1]
    UnderexcLimX2 : +Float r[1..1]
    UnderexcLimX2 : +Float tf2[1..1]
    UnderexcLimX2 : +Float tm[1..1]
    click UnderexcLimX2 href "UnderexcLimX2"
    UnderexcitationLimiterDynamics <|-- UnderexcLimIEEE1
    UnderexcLimIEEE1 : +Float kuc[1..1]
    UnderexcLimIEEE1 : +Float kuf[1..1]
    UnderexcLimIEEE1 : +Float kui[1..1]
    UnderexcLimIEEE1 : +Float kul[1..1]
    UnderexcLimIEEE1 : +Float kur[1..1]
    UnderexcLimIEEE1 : +Float tu1[1..1]
    UnderexcLimIEEE1 : +Float tu2[1..1]
    UnderexcLimIEEE1 : +Float tu3[1..1]
    UnderexcLimIEEE1 : +Float tu4[1..1]
    UnderexcLimIEEE1 : +Float vucmax[1..1]
    UnderexcLimIEEE1 : +Float vuimax[1..1]
    UnderexcLimIEEE1 : +Float vuimin[1..1]
    UnderexcLimIEEE1 : +Float vulmax[1..1]
    UnderexcLimIEEE1 : +Float vulmin[1..1]
    UnderexcLimIEEE1 : +Float vurmax[1..1]
    click UnderexcLimIEEE1 href "UnderexcLimIEEE1"
    UnderexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    UnderexcitationLimiterDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this underexcitation limiter model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..1 | Remote input signal used by this underexcitation limiter model. |

