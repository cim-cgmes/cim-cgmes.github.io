# GovGASTWD

Woodward™ gas turbine governor. [Footnote: Woodward gas turbines are an example of suitable products available commercially. This information is given for the convenience of users of this document and does not constitute an endorsement by IEC of these products.]

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TurbineGovernorDynamics <|-- GovGASTWD
    TurbineGovernorDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +TurbineLoadControllerDynamics TurbineLoadControllerDynamics[0..1]
    click TurbineGovernorDynamics href "TurbineGovernorDynamics"
    GovGASTWD : +Float a[1..1]
    GovGASTWD : +Float af1[1..1]
    GovGASTWD : +Float af2[1..1]
    GovGASTWD : +Float b[1..1]
    GovGASTWD : +Float bf1[1..1]
    GovGASTWD : +Float bf2[1..1]
    GovGASTWD : +Float c[1..1]
    GovGASTWD : +Float cf2[1..1]
    GovGASTWD : +Float ecr[1..1]
    GovGASTWD : +Float etd[1..1]
    GovGASTWD : +Float k3[1..1]
    GovGASTWD : +Float k4[1..1]
    GovGASTWD : +Float k5[1..1]
    GovGASTWD : +Float k6[1..1]
    GovGASTWD : +Float kd[1..1]
    GovGASTWD : +Float kdroop[1..1]
    GovGASTWD : +Float kf[1..1]
    GovGASTWD : +Float ki[1..1]
    GovGASTWD : +Float kp[1..1]
    GovGASTWD : +Float mwbase[1..1]
    GovGASTWD : +Float t[1..1]
    GovGASTWD : +Float t3[1..1]
    GovGASTWD : +Float t4[1..1]
    GovGASTWD : +Float t5[1..1]
    GovGASTWD : +Float tc[1..1]
    GovGASTWD : +Float tcd[1..1]
    GovGASTWD : +Float td[1..1]
    GovGASTWD : +Float tf[1..1]
    GovGASTWD : +Float tmax[1..1]
    GovGASTWD : +Float tmin[1..1]
    GovGASTWD : +Float tr[1..1]
    GovGASTWD : +Float trate[1..1]
    GovGASTWD : +Float tt[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| a | Float | 1..1 | Valve positioner (A). |
| af1 | Float | 1..1 | Exhaust temperature parameter (Af1). |
| af2 | Float | 1..1 | Coefficient equal to 0,5(1-speed) (Af2). |
| b | Float | 1..1 | Valve positioner (B). |
| bf1 | Float | 1..1 | (Bf1). Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0,55 to 0,65 x Tr. |
| bf2 | Float | 1..1 | Turbine torque coefficient Khhv (depends on heating value of fuel stream in combustion chamber) (Bf2). |
| c | Float | 1..1 | Valve positioner (C). |
| cf2 | Float | 1..1 | Coefficient defining fuel flow where power output is 0 % (Cf2). Synchronous but no output. Typically 0,23 x Khhv (23 % fuel flow). |
| ecr | Float | 1..1 | Combustion reaction time delay (Ecr) (>= 0). |
| etd | Float | 1..1 | Turbine and exhaust delay (Etd) (>= 0). |
| k3 | Float | 1..1 | Ratio of fuel adjustment (K3). |
| k4 | Float | 1..1 | Gain of radiation shield (K4). |
| k5 | Float | 1..1 | Gain of radiation shield (K5). |
| k6 | Float | 1..1 | Minimum fuel flow (K6). |
| kd | Float | 1..1 | Drop governor gain (Kd). |
| kdroop | Float | 1..1 | (Kdroop) (>= 0). |
| kf | Float | 1..1 | Fuel system feedback (Kf). |
| ki | Float | 1..1 | Isochronous Governor Gain (Ki). |
| kp | Float | 1..1 | PID proportional gain (Kp). |
| mwbase | Float | 1..1 | Base for power values (MWbase) (> 0). Unit = MW. |
| t | Float | 1..1 | Fuel control time constant (T) (>= 0). |
| t3 | Float | 1..1 | Radiation shield time constant (T3) (>= 0). |
| t4 | Float | 1..1 | Thermocouple time constant (T4) (>= 0). |
| t5 | Float | 1..1 | Temperature control time constant (T5) (>= 0). |
| tc | Float | 1..1 | Temperature control (Tc). |
| tcd | Float | 1..1 | Compressor discharge time constant (Tcd) (>= 0). |
| td | Float | 1..1 | Power transducer time constant (Td) (>= 0). |
| tf | Float | 1..1 | Fuel system time constant (Tf) (>= 0). |
| tmax | Float | 1..1 | Maximum Turbine limit (Tmax) (> GovGASTWD.tmin). |
| tmin | Float | 1..1 | Minimum turbine limit (Tmin) (< GovGASTWD.tmax). |
| tr | Float | 1..1 | Rated temperature (Tr). |
| trate | Float | 1..1 | Turbine rating (Trate). Unit = MW. |
| tt | Float | 1..1 | Temperature controller integration rate (Tt) (>= 0). |

