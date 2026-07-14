# GovCT2

General governor with frequency-dependent fuel flow limit. This model is a modification of the GovCT1 model in order to represent the frequency-dependent fuel flow limit of a specific gas turbine manufacturer.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    TurbineGovernorDynamics <|-- GovCT2
    TurbineGovernorDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +TurbineLoadControllerDynamics TurbineLoadControllerDynamics[0..1]
    click TurbineGovernorDynamics href "TurbineGovernorDynamics"
    GovCT2 : +Float aset[1..1]
    GovCT2 : +Float db[1..1]
    GovCT2 : +Float dm[1..1]
    GovCT2 : +Float flim1[1..1]
    GovCT2 : +Float flim10[1..1]
    GovCT2 : +Float flim2[1..1]
    GovCT2 : +Float flim3[1..1]
    GovCT2 : +Float flim4[1..1]
    GovCT2 : +Float flim5[1..1]
    GovCT2 : +Float flim6[1..1]
    GovCT2 : +Float flim7[1..1]
    GovCT2 : +Float flim8[1..1]
    GovCT2 : +Float flim9[1..1]
    GovCT2 : +Float ka[1..1]
    GovCT2 : +Float kdgov[1..1]
    GovCT2 : +Float kigov[1..1]
    GovCT2 : +Float kiload[1..1]
    GovCT2 : +Float kimw[1..1]
    GovCT2 : +Float kpgov[1..1]
    GovCT2 : +Float kpload[1..1]
    GovCT2 : +Float kturb[1..1]
    GovCT2 : +Float ldref[1..1]
    GovCT2 : +Float maxerr[1..1]
    GovCT2 : +Float minerr[1..1]
    GovCT2 : +Float mwbase[1..1]
    GovCT2 : +Float plim1[1..1]
    GovCT2 : +Float plim10[1..1]
    GovCT2 : +Float plim2[1..1]
    GovCT2 : +Float plim3[1..1]
    GovCT2 : +Float plim4[1..1]
    GovCT2 : +Float plim5[1..1]
    GovCT2 : +Float plim6[1..1]
    GovCT2 : +Float plim7[1..1]
    GovCT2 : +Float plim8[1..1]
    GovCT2 : +Float plim9[1..1]
    GovCT2 : +Float prate[1..1]
    GovCT2 : +Float r[1..1]
    GovCT2 : +Float rclose[1..1]
    GovCT2 : +Float rdown[1..1]
    GovCT2 : +Float ropen[1..1]
    GovCT2 : +DroopSignalFeedbackKind rselect[1..1]
    GovCT2 : +Float rup[1..1]
    GovCT2 : +Float ta[1..1]
    GovCT2 : +Float tact[1..1]
    GovCT2 : +Float tb[1..1]
    GovCT2 : +Float tc[1..1]
    GovCT2 : +Float tdgov[1..1]
    GovCT2 : +Float teng[1..1]
    GovCT2 : +Float tfload[1..1]
    GovCT2 : +Float tpelec[1..1]
    GovCT2 : +Float tsa[1..1]
    GovCT2 : +Float tsb[1..1]
    GovCT2 : +Float vmax[1..1]
    GovCT2 : +Float vmin[1..1]
    GovCT2 : +Float wfnl[1..1]
    GovCT2 : +Boolean wfspd[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| aset | Float | 1..1 | Acceleration limiter setpoint (Aset). Unit = PU / s. Typical value = 10. |
| db | Float | 1..1 | Speed governor deadband in PU speed (db). In the majority of applications, it is recommended that this value be set to zero. Typical value = 0. |
| dm | Float | 1..1 | Speed sensitivity coefficient (Dm). Dm can represent either the variation of the engine power with the shaft speed or the variation of maximum power capability with shaft speed. If it is positive it describes the falling slope of the engine speed verses power characteristic as speed increases. A slightly falling characteristic is typical for reciprocating engines and some aero-derivative turbines. If it is negative the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to exhaust temperature limits. Typical value = 0. |
| flim1 | Float | 1..1 | Frequency threshold 1 (Flim1). Unit = Hz. Typical value = 59. |
| flim10 | Float | 1..1 | Frequency threshold 10 (Flim10). Unit = Hz. Typical value = 0. |
| flim2 | Float | 1..1 | Frequency threshold 2 (Flim2). Unit = Hz. Typical value = 0. |
| flim3 | Float | 1..1 | Frequency threshold 3 (Flim3). Unit = Hz. Typical value = 0. |
| flim4 | Float | 1..1 | Frequency threshold 4 (Flim4). Unit = Hz. Typical value = 0. |
| flim5 | Float | 1..1 | Frequency threshold 5 (Flim5). Unit = Hz. Typical value = 0. |
| flim6 | Float | 1..1 | Frequency threshold 6 (Flim6). Unit = Hz. Typical value = 0. |
| flim7 | Float | 1..1 | Frequency threshold 7 (Flim7). Unit = Hz. Typical value = 0. |
| flim8 | Float | 1..1 | Frequency threshold 8 (Flim8). Unit = Hz. Typical value = 0. |
| flim9 | Float | 1..1 | Frequency threshold 9 (Flim9). Unit = Hz. Typical value = 0. |
| ka | Float | 1..1 | Acceleration limiter gain (Ka). Typical value = 10. |
| kdgov | Float | 1..1 | Governor derivative gain (Kdgov). Typical value = 0. |
| kigov | Float | 1..1 | Governor integral gain (Kigov). Typical value = 0,45. |
| kiload | Float | 1..1 | Load limiter integral gain for PI controller (Kiload). Typical value = 1. |
| kimw | Float | 1..1 | Power controller (reset) gain (Kimw). The default value of 0,01 corresponds to a reset time of 100 seconds. A value of 0,001 corresponds to a relatively slow-acting load controller. Typical value = 0. |
| kpgov | Float | 1..1 | Governor proportional gain (Kpgov). Typical value = 4. |
| kpload | Float | 1..1 | Load limiter proportional gain for PI controller (Kpload). Typical value = 1. |
| kturb | Float | 1..1 | Turbine gain (Kturb). Typical value = 1,9168. |
| ldref | Float | 1..1 | Load limiter reference value (Ldref). Typical value = 1. |
| maxerr | Float | 1..1 | Maximum value for speed error signal (Maxerr) (> GovCT2.minerr). Typical value = 1. |
| minerr | Float | 1..1 | Minimum value for speed error signal (Minerr) (< GovCT2.maxerr). Typical value = -1. |
| mwbase | Float | 1..1 | Base for power values (MWbase) (> 0). Unit = MW. |
| plim1 | Float | 1..1 | Power limit 1 (Plim1). Typical value = 0,8325. |
| plim10 | Float | 1..1 | Power limit 10 (Plim10). Typical value = 0. |
| plim2 | Float | 1..1 | Power limit 2 (Plim2). Typical value = 0. |
| plim3 | Float | 1..1 | Power limit 3 (Plim3). Typical value = 0. |
| plim4 | Float | 1..1 | Power limit 4 (Plim4). Typical value = 0. |
| plim5 | Float | 1..1 | Power limit 5 (Plim5). Typical value = 0. |
| plim6 | Float | 1..1 | Power limit 6 (Plim6). Typical value = 0. |
| plim7 | Float | 1..1 | Power limit 7 (Plim7). Typical value = 0. |
| plim8 | Float | 1..1 | Power limit 8 (Plim8). Typical value = 0. |
| plim9 | Float | 1..1 | Power Limit 9 (Plim9). Typical value = 0. |
| prate | Float | 1..1 | Ramp rate for frequency-dependent power limit (Prate). Typical value = 0,017. |
| r | Float | 1..1 | Permanent droop (R). Typical value = 0,05. |
| rclose | Float | 1..1 | Minimum valve closing rate (Rclose). Unit = PU / s. Typical value = -99. |
| rdown | Float | 1..1 | Maximum rate of load limit decrease (Rdown). Typical value = -99. |
| ropen | Float | 1..1 | Maximum valve opening rate (Ropen). Unit = PU / s. Typical value = 99. |
| rselect | [DroopSignalFeedbackKind](DroopSignalFeedbackKind.md) | 1..1 | Feedback signal for droop (Rselect). Typical value = electricalPower. |
| rup | Float | 1..1 | Maximum rate of load limit increase (Rup). Typical value = 99. |
| ta | Float | 1..1 | Acceleration limiter time constant (Ta) (>= 0). Typical value = 1. |
| tact | Float | 1..1 | Actuator time constant (Tact) (>= 0). Typical value = 0,4. |
| tb | Float | 1..1 | Turbine lag time constant (Tb) (>= 0). Typical value = 0,1. |
| tc | Float | 1..1 | Turbine lead time constant (Tc) (>= 0). Typical value = 0. |
| tdgov | Float | 1..1 | Governor derivative controller time constant (Tdgov) (>= 0). Typical value = 1. |
| teng | Float | 1..1 | Transport time delay for diesel engine used in representing diesel engines where there is a small but measurable transport delay between a change in fuel flow setting and the development of torque (Teng) (>= 0). Teng should be zero in all but special cases where this transport delay is of particular concern. Typical value = 0. |
| tfload | Float | 1..1 | Load limiter time constant (Tfload) (>= 0). Typical value = 3. |
| tpelec | Float | 1..1 | Electrical power transducer time constant (Tpelec) (>= 0). Typical value = 2,5. |
| tsa | Float | 1..1 | Temperature detection lead time constant (Tsa) (>= 0). Typical value = 0. |
| tsb | Float | 1..1 | Temperature detection lag time constant (Tsb) (>= 0). Typical value = 50. |
| vmax | Float | 1..1 | Maximum valve position limit (Vmax) (> GovCT2.vmin). Typical value = 1. |
| vmin | Float | 1..1 | Minimum valve position limit (Vmin) (< GovCT2.vmax). Typical value = 0,175. |
| wfnl | Float | 1..1 | No load fuel flow (Wfnl). Typical value = 0,187. |
| wfspd | Boolean | 1..1 | Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow independent of engine speed. Typical value = false. |

