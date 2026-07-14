# PssELIN2

Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    PowerSystemStabilizerDynamics <|-- PssELIN2
    PowerSystemStabilizerDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PowerSystemStabilizerDynamics : +RemoteInputSignal RemoteInputSignal[0..n]
    click PowerSystemStabilizerDynamics href "PowerSystemStabilizerDynamics"
    PssELIN2 : +Float apss[1..1]
    PssELIN2 : +Float ks1[1..1]
    PssELIN2 : +Float ks2[1..1]
    PssELIN2 : +Float ppss[1..1]
    PssELIN2 : +Float psslim[1..1]
    PssELIN2 : +Float ts1[1..1]
    PssELIN2 : +Float ts2[1..1]
    PssELIN2 : +Float ts3[1..1]
    PssELIN2 : +Float ts4[1..1]
    PssELIN2 : +Float ts5[1..1]
    PssELIN2 : +Float ts6[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| apss | Float | 1..1 | Coefficient (a_PSS). Typical value = 0,1. |
| ks1 | Float | 1..1 | Gain (Ks1). Typical value = 1. |
| ks2 | Float | 1..1 | Gain (Ks2). Typical value = 0,1. |
| ppss | Float | 1..1 | Coefficient (p_PSS) (>= 0 and <= 4). Typical value = 0,1. |
| psslim | Float | 1..1 | PSS limiter (psslim). Typical value = 0,1. |
| ts1 | Float | 1..1 | Time constant (Ts1) (>= 0). Typical value = 0. |
| ts2 | Float | 1..1 | Time constant (Ts2) (>= 0). Typical value = 1. |
| ts3 | Float | 1..1 | Time constant (Ts3) (>= 0). Typical value = 1. |
| ts4 | Float | 1..1 | Time constant (Ts4) (>= 0). Typical value = 0,1. |
| ts5 | Float | 1..1 | Time constant (Ts5) (>= 0). Typical value = 0. |
| ts6 | Float | 1..1 | Time constant (Ts6) (>= 0). Typical value = 1. |

