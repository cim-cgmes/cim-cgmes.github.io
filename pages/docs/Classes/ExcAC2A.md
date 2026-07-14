# ExcAC2A

Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    ExcitationSystemDynamics <|-- ExcAC2A
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    ExcAC2A : +Boolean hvgate[1..1]
    ExcAC2A : +Float ka[1..1]
    ExcAC2A : +Float kb[1..1]
    ExcAC2A : +Float kb1[1..1]
    ExcAC2A : +Float kc[1..1]
    ExcAC2A : +Float kd[1..1]
    ExcAC2A : +Float ke[1..1]
    ExcAC2A : +Float kf[1..1]
    ExcAC2A : +Float kh[1..1]
    ExcAC2A : +Float kl[1..1]
    ExcAC2A : +Float kl1[1..1]
    ExcAC2A : +Float ks[1..1]
    ExcAC2A : +Boolean lvgate[1..1]
    ExcAC2A : +Float seve1[1..1]
    ExcAC2A : +Float seve2[1..1]
    ExcAC2A : +Float ta[1..1]
    ExcAC2A : +Float tb[1..1]
    ExcAC2A : +Float tc[1..1]
    ExcAC2A : +Float te[1..1]
    ExcAC2A : +Float tf[1..1]
    ExcAC2A : +Float vamax[1..1]
    ExcAC2A : +Float vamin[1..1]
    ExcAC2A : +Float ve1[1..1]
    ExcAC2A : +Float ve2[1..1]
    ExcAC2A : +Float vfemax[1..1]
    ExcAC2A : +Float vlr[1..1]
    ExcAC2A : +Float vrmax[1..1]
    ExcAC2A : +Float vrmin[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| hvgate | Boolean | 1..1 | Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical value = true. |
| ka | Float | 1..1 | Voltage regulator gain (Ka) (> 0). Typical value = 400. |
| kb | Float | 1..1 | Second stage regulator gain (Kb) (> 0). Exciter field current controller gain. Typical value = 25. |
| kb1 | Float | 1..1 | Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to represent a variant of the ExcAC2A model. Typical value = 25. |
| kc | Float | 1..1 | Rectifier loading factor proportional to commutating reactance (Kc) (>= 0). Typical value = 0,28. |
| kd | Float | 1..1 | Demagnetizing factor, a function of exciter alternator reactances (Kd) (>= 0). Typical value = 0,35. |
| ke | Float | 1..1 | Exciter constant related to self-excited field (Ke). Typical value = 1. |
| kf | Float | 1..1 | Excitation control system stabilizer gains (Kf) (>= 0). Typical value = 0,03. |
| kh | Float | 1..1 | Exciter field current feedback gain (Kh) (>= 0). Typical value = 1. |
| kl | Float | 1..1 | Exciter field current limiter gain (Kl). Typical value = 10. |
| kl1 | Float | 1..1 | Coefficient to allow different usage of the model (Kl1). Typical value = 1. |
| ks | Float | 1..1 | Coefficient to allow different usage of the model-speed coefficient (Ks) (>= 0). Typical value = 0. |
| lvgate | Boolean | 1..1 | Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical value = true. |
| seve1 | Float | 1..1 | Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]) (>= 0). Typical value = 0,037. |
| seve2 | Float | 1..1 | Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]) (>= 0). Typical value = 0,012. |
| ta | Float | 1..1 | Voltage regulator time constant (Ta) (> 0). Typical value = 0,02. |
| tb | Float | 1..1 | Voltage regulator time constant (Tb) (>= 0). Typical value = 0. |
| tc | Float | 1..1 | Voltage regulator time constant (Tc) (>= 0). Typical value = 0. |
| te | Float | 1..1 | Exciter time constant, integration rate associated with exciter control (Te) (> 0). Typical value = 0,6. |
| tf | Float | 1..1 | Excitation control system stabilizer time constant (Tf) (> 0). Typical value = 1. |
| vamax | Float | 1..1 | Maximum voltage regulator output (Vamax) (> 0). Typical value = 8. |
| vamin | Float | 1..1 | Minimum voltage regulator output (Vamin) (< 0). Typical value = -8. |
| ve1 | Float | 1..1 | Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) (> 0). Typical value = 4,4. |
| ve2 | Float | 1..1 | Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2) (> 0). Typical value = 3,3. |
| vfemax | Float | 1..1 | Exciter field current limit reference (Vfemax) (>= 0). Typical value = 4,4. |
| vlr | Float | 1..1 | Maximum exciter field current (Vlr) (> 0). Typical value = 4,4. |
| vrmax | Float | 1..1 | Maximum voltage regulator outputs (Vrmax) (> 0). Typical value = 105. |
| vrmin | Float | 1..1 | Minimum voltage regulator outputs (Vrmin) (< 0). Typical value = -95. |

