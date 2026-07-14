# DynamicsFunctionBlock

Abstract parent class for all Dynamics function blocks.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- DynamicsFunctionBlock
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    DynamicsFunctionBlock <|-- WindPlantDynamics
    WindPlantDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindPlantDynamics : +WindTurbineType3or4Dynamics WindTurbineType3or4Dynamics[1..n]
    click WindPlantDynamics href "WindPlantDynamics"
    DynamicsFunctionBlock <|-- WindTurbineType3or4Dynamics
    WindTurbineType3or4Dynamics : +PowerElectronicsConnection PowerElectronicsConnection[1]
    WindTurbineType3or4Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    WindTurbineType3or4Dynamics : +WindPlantDynamics WindPlantDynamics[0..1]
    click WindTurbineType3or4Dynamics href "WindTurbineType3or4Dynamics"
    DynamicsFunctionBlock <|-- StaticVarCompensatorDynamics
    StaticVarCompensatorDynamics : +StaticVarCompensator StaticVarCompensator[1]
    click StaticVarCompensatorDynamics href "StaticVarCompensatorDynamics"
    DynamicsFunctionBlock <|-- MechanicalLoadDynamics
    MechanicalLoadDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    MechanicalLoadDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    click MechanicalLoadDynamics href "MechanicalLoadDynamics"
    DynamicsFunctionBlock <|-- VoltageCompensatorDynamics
    VoltageCompensatorDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    VoltageCompensatorDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click VoltageCompensatorDynamics href "VoltageCompensatorDynamics"
    DynamicsFunctionBlock <|-- ExcitationSystemDynamics
    ExcitationSystemDynamics : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    ExcitationSystemDynamics : +OverexcitationLimiterDynamics OverexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    ExcitationSystemDynamics : +PFVArControllerType2Dynamics PFVArControllerType2Dynamics[0..1]
    ExcitationSystemDynamics : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    ExcitationSystemDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    ExcitationSystemDynamics : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    ExcitationSystemDynamics : +VoltageCompensatorDynamics VoltageCompensatorDynamics[1]
    click ExcitationSystemDynamics href "ExcitationSystemDynamics"
    DynamicsFunctionBlock <|-- PFVArControllerType2Dynamics
    PFVArControllerType2Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    click PFVArControllerType2Dynamics href "PFVArControllerType2Dynamics"
    DynamicsFunctionBlock <|-- PFVArControllerType1Dynamics
    PFVArControllerType1Dynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PFVArControllerType1Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    PFVArControllerType1Dynamics : +VoltageAdjusterDynamics VoltageAdjusterDynamics[0..1]
    click PFVArControllerType1Dynamics href "PFVArControllerType1Dynamics"
    DynamicsFunctionBlock <|-- RotatingMachineDynamics
    RotatingMachineDynamics : +Float damping[1..1]
    RotatingMachineDynamics : +Float inertia[1..1]
    RotatingMachineDynamics : +Float saturationFactor[0..1]
    RotatingMachineDynamics : +Float saturationFactor120[0..1]
    RotatingMachineDynamics : +Float statorLeakageReactance[1..1]
    RotatingMachineDynamics : +Float statorResistance[1..1]
    click RotatingMachineDynamics href "RotatingMachineDynamics"
    DynamicsFunctionBlock <|-- HVDCDynamics
    click HVDCDynamics href "HVDCDynamics"
    DynamicsFunctionBlock <|-- DiscontinuousExcitationControlDynamics
    DiscontinuousExcitationControlDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    DiscontinuousExcitationControlDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click DiscontinuousExcitationControlDynamics href "DiscontinuousExcitationControlDynamics"
    DynamicsFunctionBlock <|-- WindTurbineType1or2Dynamics
    WindTurbineType1or2Dynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[1]
    WindTurbineType1or2Dynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click WindTurbineType1or2Dynamics href "WindTurbineType1or2Dynamics"
    DynamicsFunctionBlock <|-- UnderexcitationLimiterDynamics
    UnderexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    UnderexcitationLimiterDynamics : +RemoteInputSignal RemoteInputSignal[0..1]
    click UnderexcitationLimiterDynamics href "UnderexcitationLimiterDynamics"
    DynamicsFunctionBlock <|-- TurbineLoadControllerDynamics
    TurbineLoadControllerDynamics : +TurbineGovernorDynamics TurbineGovernorDynamics[1]
    click TurbineLoadControllerDynamics href "TurbineLoadControllerDynamics"
    DynamicsFunctionBlock <|-- OverexcitationLimiterDynamics
    OverexcitationLimiterDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    click OverexcitationLimiterDynamics href "OverexcitationLimiterDynamics"
    DynamicsFunctionBlock <|-- VoltageAdjusterDynamics
    VoltageAdjusterDynamics : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[1]
    click VoltageAdjusterDynamics href "VoltageAdjusterDynamics"
    DynamicsFunctionBlock <|-- TurbineGovernorDynamics
    TurbineGovernorDynamics : +AsynchronousMachineDynamics AsynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +SynchronousMachineDynamics SynchronousMachineDynamics[0..1]
    TurbineGovernorDynamics : +TurbineLoadControllerDynamics TurbineLoadControllerDynamics[0..1]
    click TurbineGovernorDynamics href "TurbineGovernorDynamics"
    DynamicsFunctionBlock <|-- PowerSystemStabilizerDynamics
    PowerSystemStabilizerDynamics : +ExcitationSystemDynamics ExcitationSystemDynamics[1]
    PowerSystemStabilizerDynamics : +RemoteInputSignal RemoteInputSignal[0..n]
    click PowerSystemStabilizerDynamics href "PowerSystemStabilizerDynamics"
    DynamicsFunctionBlock <|-- CrossCompoundTurbineGovernorDynamics
    CrossCompoundTurbineGovernorDynamics : +SynchronousMachineDynamics HighPressureSynchronousMachineDynamics[1]
    CrossCompoundTurbineGovernorDynamics : +SynchronousMachineDynamics LowPressureSynchronousMachineDynamics[1]
    click CrossCompoundTurbineGovernorDynamics href "CrossCompoundTurbineGovernorDynamics"
    DynamicsFunctionBlock : +Boolean enabled[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| enabled | Boolean | 1..1 | Function block used indicator. true = use of function block is enabled false = use of function block is disabled. |

