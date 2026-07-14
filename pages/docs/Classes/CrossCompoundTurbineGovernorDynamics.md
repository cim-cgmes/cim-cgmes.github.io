# CrossCompoundTurbineGovernorDynamics

Turbine-governor cross-compound function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    DynamicsFunctionBlock <|-- CrossCompoundTurbineGovernorDynamics
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    CrossCompoundTurbineGovernorDynamics <|-- GovSteamCC
    GovSteamCC : +Float dhp[1..1]
    GovSteamCC : +Float dlp[1..1]
    GovSteamCC : +Float fhp[1..1]
    GovSteamCC : +Float flp[1..1]
    GovSteamCC : +Float mwbase[1..1]
    GovSteamCC : +Float pmaxhp[1..1]
    GovSteamCC : +Float pmaxlp[1..1]
    GovSteamCC : +Float rhp[1..1]
    GovSteamCC : +Float rlp[1..1]
    GovSteamCC : +Float t1hp[1..1]
    GovSteamCC : +Float t1lp[1..1]
    GovSteamCC : +Float t3hp[1..1]
    GovSteamCC : +Float t3lp[1..1]
    GovSteamCC : +Float t4hp[1..1]
    GovSteamCC : +Float t4lp[1..1]
    GovSteamCC : +Float t5hp[1..1]
    GovSteamCC : +Float t5lp[1..1]
    click GovSteamCC href "GovSteamCC"
    CrossCompoundTurbineGovernorDynamics : +SynchronousMachineDynamics HighPressureSynchronousMachineDynamics[1]
    CrossCompoundTurbineGovernorDynamics : +SynchronousMachineDynamics LowPressureSynchronousMachineDynamics[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| HighPressureSynchronousMachineDynamics | [SynchronousMachineDynamics](SynchronousMachineDynamics.md) | 1 | High-pressure synchronous machine with which this cross-compound turbine governor is associated. |
| LowPressureSynchronousMachineDynamics | [SynchronousMachineDynamics](SynchronousMachineDynamics.md) | 1 | Low-pressure synchronous machine with which this cross-compound turbine governor is associated. |

