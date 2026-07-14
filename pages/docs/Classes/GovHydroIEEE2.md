# GovHydroIEEE2

IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors. Reference: IEEE Transactions on Power Apparatus and Systems, November/December 1973, Volume PAS-92, Number 6, Dynamic Models for Steam and Hydro Turbines in Power System Studies, page 1904.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TurbineGovernorDynamics <|-- GovHydroIEEE2
    TurbineGovernorDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +TurbineLoadControllerDynamics TurbineLoadControllerDynamics[0..1]
    click TurbineGovernorDynamics href "TurbineGovernorDynamics"
    GovHydroIEEE2 : +Float aturb[1..1]
    GovHydroIEEE2 : +Float bturb[1..1]
    GovHydroIEEE2 : +Float gv1[1..1]
    GovHydroIEEE2 : +Float gv2[1..1]
    GovHydroIEEE2 : +Float gv3[1..1]
    GovHydroIEEE2 : +Float gv4[1..1]
    GovHydroIEEE2 : +Float gv5[1..1]
    GovHydroIEEE2 : +Float gv6[1..1]
    GovHydroIEEE2 : +Float kturb[1..1]
    GovHydroIEEE2 : +Float mwbase[1..1]
    GovHydroIEEE2 : +Float pgv1[1..1]
    GovHydroIEEE2 : +Float pgv2[1..1]
    GovHydroIEEE2 : +Float pgv3[1..1]
    GovHydroIEEE2 : +Float pgv4[1..1]
    GovHydroIEEE2 : +Float pgv5[1..1]
    GovHydroIEEE2 : +Float pgv6[1..1]
    GovHydroIEEE2 : +Float pmax[1..1]
    GovHydroIEEE2 : +Float pmin[1..1]
    GovHydroIEEE2 : +Float rperm[1..1]
    GovHydroIEEE2 : +Float rtemp[1..1]
    GovHydroIEEE2 : +Float tg[1..1]
    GovHydroIEEE2 : +Float tp[1..1]
    GovHydroIEEE2 : +Float tr[1..1]
    GovHydroIEEE2 : +Float tw[1..1]
    GovHydroIEEE2 : +Float uc[1..1]
    GovHydroIEEE2 : +Float uo[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| aturb | Float | 1..1 | Turbine numerator multiplier (Aturb). Typical value = -1. |
| bturb | Float | 1..1 | Turbine denominator multiplier (Bturb) (> 0). Typical value = 0,5. |
| gv1 | Float | 1..1 | Nonlinear gain point 1, PU gv (Gv1). Typical value = 0. |
| gv2 | Float | 1..1 | Nonlinear gain point 2, PU gv (Gv2). Typical value = 0. |
| gv3 | Float | 1..1 | Nonlinear gain point 3, PU gv (Gv3). Typical value = 0. |
| gv4 | Float | 1..1 | Nonlinear gain point 4, PU gv (Gv4). Typical value = 0. |
| gv5 | Float | 1..1 | Nonlinear gain point 5, PU gv (Gv5). Typical value = 0. |
| gv6 | Float | 1..1 | Nonlinear gain point 6, PU gv (Gv6). Typical value = 0. |
| kturb | Float | 1..1 | Turbine gain (Kturb). Typical value = 1. |
| mwbase | Float | 1..1 | Base for power values (MWbase) (> 0). Unit = MW. |
| pgv1 | Float | 1..1 | Nonlinear gain point 1, PU power (Pgv1). Typical value = 0. |
| pgv2 | Float | 1..1 | Nonlinear gain point 2, PU power (Pgv2). Typical value = 0. |
| pgv3 | Float | 1..1 | Nonlinear gain point 3, PU power (Pgv3). Typical value = 0. |
| pgv4 | Float | 1..1 | Nonlinear gain point 4, PU power (Pgv4). Typical value = 0. |
| pgv5 | Float | 1..1 | Nonlinear gain point 5, PU power (Pgv5). Typical value = 0. |
| pgv6 | Float | 1..1 | Nonlinear gain point 6, PU power (Pgv6). Typical value = 0. |
| pmax | Float | 1..1 | Maximum gate opening (Pmax) (> GovHydroIEEE2.pmin). Typical value = 1. |
| pmin | Float | 1..1 | Minimum gate opening (Pmin) (<GovHydroIEEE2.pmax). Typical value = 0. |
| rperm | Float | 1..1 | Permanent droop (Rperm). Typical value = 0,05. |
| rtemp | Float | 1..1 | Temporary droop (Rtemp). Typical value = 0,5. |
| tg | Float | 1..1 | Gate servo time constant (Tg) (>= 0). Typical value = 0,5. |
| tp | Float | 1..1 | Pilot servo valve time constant (Tp) (>= 0). Typical value = 0,03. |
| tr | Float | 1..1 | Dashpot time constant (Tr) (>= 0). Typical value = 12. |
| tw | Float | 1..1 | Water inertia time constant (Tw) (>= 0). Typical value = 2. |
| uc | Float | 1..1 | Maximum gate closing velocity (Uc) (<0). Typical value = -0,1. |
| uo | Float | 1..1 | Maximum gate opening velocity (Uo). Unit = PU / s. Typical value = 0,1. |

