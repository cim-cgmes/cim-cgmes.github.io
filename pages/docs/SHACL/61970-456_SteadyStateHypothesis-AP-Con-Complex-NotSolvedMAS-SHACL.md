# 61970-456_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL

## ssh456n:Equipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentShunt
- targetClass: cim:EquivalentBranch
- targetClass: cim:PostLineSensor
- targetClass: cim:PotentialTransformer
- targetClass: cim:Fuse
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ACLineSegment
- targetClass: cim:VsConverter
- targetClass: cim:Equipment
- targetClass: cim:ConformLoad
- targetClass: cim:CurrentTransformer
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:HydroPump
- targetClass: cim:DCBusbar
- targetClass: cim:Clamp
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:DCShunt
- targetClass: cim:DCSeriesDevice
- targetClass: cim:CsConverter
- targetClass: cim:Cut
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:StationSupply
- targetClass: cim:EnergyConsumer
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:EquivalentInjection
- targetClass: cim:AsynchronousMachine
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCBreaker
- targetClass: cim:DCLineSegment
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Jumper
- targetClass: cim:BatteryUnit
- targetClass: cim:SynchronousMachine
- targetClass: cim:DCSwitch
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:PhotoVoltaicUnit
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:PetersenCoil
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:DCChopper
- targetClass: cim:PowerElectronicsWindUnit
- targetClass: cim:Switch
- targetClass: cim:DCGround
- targetClass: cim:NonConformLoad
- targetClass: cim:PowerTransformer
- targetClass: cim:SurgeArrester
- targetClass: cim:GroundDisconnector
- targetClass: cim:StaticVarCompensator
- targetClass: cim:FaultIndicator
- targetClass: cim:GeneratingUnit
- targetClass: cim:Ground
- targetClass: cim:DCDisconnector
- targetClass: cim:Disconnector
- targetClass: cim:EnergySource
- targetClass: cim:GroundingImpedance
- targetClass: cim:Junction
- targetClass: cim:BusbarSection
- targetClass: cim:WaveTrap

**Nested Properties:**

### ssh456n:Equipment.inService-eqshhCardinality

**Path:** `cim:Equipment.inService`  
**Name:** Equipment.inService-eqshhCardinality  
This constraint validates the cardinality of the property (attribute) for classes that are in EQ but not in SSH profile.

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute). The equipment is instantiated in EQ instance but Equipment.inService is not instantiated in SSH."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## ssh456n:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

## ssh456n:ExternalNetworkInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExternalNetworkInjection

## ssh456n:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:AllGeneratingUnit

## ssh456n:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl
- targetClass: cim:TapChangerControl

## ssh456n:RotatingMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine

## ssh456n:ShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NonlinearShuntCompensator

## ssh456n:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

## ssh456n:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical

