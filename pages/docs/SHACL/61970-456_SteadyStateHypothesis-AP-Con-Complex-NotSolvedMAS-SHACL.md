# 61970-456_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL

## ssh456n:Equipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSwitch
- targetClass: cim:Disconnector
- targetClass: cim:PowerTransformer
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:Equipment
- targetClass: cim:PetersenCoil
- targetClass: cim:PotentialTransformer
- targetClass: cim:EnergyConsumer
- targetClass: cim:EquivalentShunt
- targetClass: cim:Cut
- targetClass: cim:WaveTrap
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:DCShunt
- targetClass: cim:DCDisconnector
- targetClass: cim:Clamp
- targetClass: cim:CurrentTransformer
- targetClass: cim:SynchronousMachine
- targetClass: cim:VsConverter
- targetClass: cim:EquivalentInjection
- targetClass: cim:PostLineSensor
- targetClass: cim:CsConverter
- targetClass: cim:ConformLoad
- targetClass: cim:DCChopper
- targetClass: cim:AsynchronousMachine
- targetClass: cim:SurgeArrester
- targetClass: cim:DCBreaker
- targetClass: cim:PhotoVoltaicUnit
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:PowerElectronicsWindUnit
- targetClass: cim:Breaker
- targetClass: cim:GeneratingUnit
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCGround
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:EnergySource
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:NonConformLoad
- targetClass: cim:ACLineSegment
- targetClass: cim:FaultIndicator
- targetClass: cim:StationSupply
- targetClass: cim:Switch
- targetClass: cim:Fuse
- targetClass: cim:StaticVarCompensator
- targetClass: cim:DCLineSegment
- targetClass: cim:BusbarSection
- targetClass: cim:Junction
- targetClass: cim:Ground
- targetClass: cim:EquivalentBranch
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCBusbar
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:GroundingImpedance
- targetClass: cim:GroundDisconnector
- targetClass: cim:HydroPump
- targetClass: cim:Jumper
- targetClass: cim:BatteryUnit
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### ssh456n:Equipment.inService-eqshhCardinality

**Path:** `cim:Equipment.inService`  
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
- targetClass: cim:AsynchronousMachine
- targetClass: cim:SynchronousMachine

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
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerTabular

