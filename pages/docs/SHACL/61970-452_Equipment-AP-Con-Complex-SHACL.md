# 61970-452_Equipment-AP-Con-Complex-SHACL

## eq452c:ACDCConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter
- targetClass: cim:VsConverter

**Nested Properties:**

### eq452c:DCConverterUnit.Substation-containment

**Path:** `cim:Equipment.EquipmentContainer / cim:DCConverterUnit.Substation / rdf:type`  
**Name:** C:452:EQ:ACDCConverter:containment  
For ACDCConverter (CsConverter, VsConverter) the association Equipment.EquipmentContainer is required and shall point to DCEquipmentContainer of type DCConverterUnit. In this case the association DCConverterUnit.Substation is required.

**Severity:** sh:Violation

**Messages:**
- "The DCConverterUnit.Substation association is either missing or not pointing to a Substation."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Substation]` 

### eq452c:ACDCConverter-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:ACDCConverter:containment  
For ACDCConverter (CsConverter, VsConverter) the association Equipment.EquipmentContainer is required and shall point to DCEquipmentContainer of type DCConverterUnit. In this case the association DCConverterUnit.Substation is required.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

**Nested Properties:**

### eq452c:ACLineSegment.r-valueRange

**Path:** `cim:ACLineSegment.r`  
**Name:** C:452:EQ:ACLineSegment.r:valueRange  
ACLineSegment.r shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq452c:ACLineSegment.x-valueRange

**Path:** `cim:ACLineSegment.x`  
**Name:** C:452:EQ:ACLineSegment.x:valueRange  
The attribute shall be a positive value. As negative reactance values are not allowed for ACLineSegment-s it is recommended to model series compensators explicitly.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq452c:ConductingEquipment.BaseVoltage-whereRequired

**Path:** `cim:ConductingEquipment.BaseVoltage`  
**Name:** C:452:EQ:ConductingEquipment.BaseVoltage:whereRequired  
The ConductingEquipment.BaseVoltage association is required for the following ConductingEquipment: ACLineSegment, EquivalentBranch and SeriesCompensator. For all other Equipment-s, not contained in a VoltageLevel, the association ConductingEquipment.BaseVoltage can be provided (as it is optional), however the association to BaseVoltage coming from the container or transformer ends takes precedence.

**Severity:** sh:Violation

**Messages:**
- "The association ConductingEquipment.BaseVoltage is not provided."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq452c:AuxiliaryEquipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WaveTrap
- targetClass: cim:FaultIndicator
- targetClass: cim:CurrentTransformer
- targetClass: cim:PotentialTransformer
- targetClass: cim:PostLineSensor
- targetClass: cim:SurgeArrester

**Nested Properties:**

### eq452c:AuxiliaryEquipment-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:AuxilaryEquipment:containment  
For AuxilaryEquipment (CurrentTransformer, PotentialTransformer, PostLineSensor, SurgeArrester, WaveTrap, FaultIndicator) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay or Line.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:Line]` 

## eq452c:Breaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker

## eq452c:BusbarSection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BusbarSection

**Nested Properties:**

### eq452c:BusbarSection-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:BusbarSection:containment  
For BusbarSection the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel or Bay (when a disconnector is splitting a busbar section in two).

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay or VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel]` 

## eq452c:Clamp

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Clamp

**Nested Properties:**

### eq452c:Clamp-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Clamp:containment  
For Clamp the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:Line]` 

## eq452c:ConductingEquipment-twoTerminalsShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCSwitch
- targetClass: cim:DCChopper
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:Jumper
- targetClass: cim:Breaker
- targetClass: cim:Cut
- targetClass: cim:ACLineSegment
- targetClass: cim:DCBreaker
- targetClass: cim:Disconnector
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:EquivalentBranch
- targetClass: cim:DCLineSegment
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCDisconnector
- targetClass: cim:Switch

## eq452c:Conductor

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

**Nested Properties:**

### eq452c:Conductor-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Conductor:containment  
For Conductor (ACLineSegment) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Line.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Line]` 

## eq452c:CurveData

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurveData

## eq452c:Cut

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Cut

**Nested Properties:**

### eq452c:Cut-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Cut:containment  
For Cut the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel or DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel, DCConverterUnit or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit cim:Line]` 

## eq452c:DCBusbar

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBusbar

**Nested Properties:**

### eq452c:DCBusbar-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCBusbar:containment  
For DCBusbar the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DCChopper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCChopper

**Nested Properties:**

### eq452c:DCChopper-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCChopper:containment  
For DCChopper the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DCGround

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCGround

**Nested Properties:**

### eq452c:DCGround-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCGround:containment  
For DCGround the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DCLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCLineSegment

**Nested Properties:**

### eq452c:DCLineSegment.resistance-valueRange

**Path:** `cim:DCLineSegment.resistance`  
**Name:** C:452:EQ:DCLineSegment.resistance:valueRange  
The attribute DCLineSegment.resistance shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq452c:DCLineSegment-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCLineSegment:containment  
For DCLineSegment the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCLine. In the case of modelling back to back configuration the association shall point to EquipmentContainer of type Substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCLine or Substation."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCLine cim:Substation]` 

## eq452c:DCSeriesDevice

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSeriesDevice

**Nested Properties:**

### eq452c:DCSeriesDevice-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCSeriesDevice:containment  
For DCSeriesDevice the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DCShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCShunt

**Nested Properties:**

### eq452c:DCShunt-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCShunt:containment  
For DCShunt the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DCSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCDisconnector
- targetClass: cim:DCBreaker

**Nested Properties:**

### eq452c:DCSwitch-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:DCSwitch:containment  
For DCSwitch (DCDisconnector, DCBreaker) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCConverterUnit]` 

## eq452c:DayType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DayType

**Nested Properties:**

### eq452c:IdentifiedObject.name-validValues

**Path:** `cim:IdentifiedObject.name`  
**Name:** C:452:EQ:DayType.name:validValues  
For DayType the name attribute indicates the days of the week that a given DayType represents. The name attribute is restricted to the following names: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Weekday, Weekend, All. If the name attribute is All, it represents all seven days of the week. If the name attribute is Weekday, it represents Monday through Friday. If the name attribute is Weekend, it represents Saturday and Sunday.

**Severity:** sh:Violation

**Messages:**
- "Not valid value. The value is not one of the following values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Weekday, Weekend, All."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[Monday Tuesday Wednesday Thursday Friday Saturday Sunday Weekday Weekend All]` 

## eq452c:DisconnectingCircuitBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker

## eq452c:Disconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Disconnector

**Nested Properties:**

### eq452c:Disconnector-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Disconnector:containment  
For Disconnector the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel, DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel, DCConverterUnit or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit cim:Line]` 

## eq452c:EarthFaultCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil

**Nested Properties:**

### eq452c:EarthFaultCompensator-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:EarthFaultCompensator:containment  
For EarthFaultCompensator (GroundingImpedance, PetersenCoil) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VoltageLevel]` 

## eq452c:EnergyConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergySource
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:StaticVarCompensator
- targetClass: cim:SynchronousMachine
- targetClass: cim:EnergyConsumer
- targetClass: cim:NonConformLoad
- targetClass: cim:ConformLoad
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### eq452c:EnergyConnection-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:EnergyConnection:containment  
For EnergyConnection (EnergySource, EnergyConsumer, NonConformLoad, ConformLoad, LinearShuntCompensator, NonlinearShuntCompensator, ExternalNetworkInjection, StaticVarCompensator, SynchronousMachine, AsynchronousMachine) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VoltageLevel]` 

## eq452c:EquivalentBranch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch

**Nested Properties:**

### eq452c:ConductingEquipment.BaseVoltage-whereRequired

**Path:** `cim:ConductingEquipment.BaseVoltage`  
**Name:** C:452:EQ:ConductingEquipment.BaseVoltage:whereRequired  
The ConductingEquipment.BaseVoltage association is required for the following ConductingEquipment: ACLineSegment, EquivalentBranch and SeriesCompensator. For all other Equipment-s, not contained in a VoltageLevel, the association ConductingEquipment.BaseVoltage can be provided (as it is optional), however the association to BaseVoltage coming from the container or transformer ends takes precedence.

**Severity:** sh:Violation

**Messages:**
- "The association ConductingEquipment.BaseVoltage is not provided."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### eq452c:EquivalentBranch-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:EquivalentBranch:containment  
For EquivalentBranch the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel, Line or Substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel, Line or Substation."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VoltageLevel cim:Line cim:Substation]` 

## eq452c:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### eq452c:EquivalentInjection-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:EquivalentInjection:containment  
For EquivalentInjection the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel or Line.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VoltageLevel cim:Line]` 

## eq452c:EquivalentShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentShunt

**Nested Properties:**

### eq452c:EquivalentShunt-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:EquivalentShunt:containment  
For EquivalentShunt the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:VoltageLevel]` 

## eq452c:Fuse

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Fuse

**Nested Properties:**

### eq452c:Fuse-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Fuse:containment  
For Fuse the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel, DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel, DCConverterUnit or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit cim:Line]` 

## eq452c:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

## eq452c:GeneratingUnit-containmentNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:containment  
For GeneratingUnit (SolarGeneratingUnit, NuclearGeneratingUnit, ThermalGeneratingUnit, HydroGeneratingUnit, WindGeneratingUnit) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Substation."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Substation]` 

## eq452c:GeneratingUnit.aggregate

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit

## eq452c:Ground

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Ground

**Nested Properties:**

### eq452c:Ground-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Ground:containment  
For Ground the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay or VoltageLevel.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay or VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel]` 

## eq452c:GroundDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector

**Nested Properties:**

### eq452c:GroundDisconnector-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:GroundDisconnector:containment  
For GroundDisconnector the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel, DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel, DCConverterUnit or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit cim:Line]` 

## eq452c:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

## eq452c:HydroPump

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroPump

**Nested Properties:**

### eq452c:HydroPump-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:HydroPump:containment  
For HydroPump the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Substation."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Substation]` 

## eq452c:Jumper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Jumper

**Nested Properties:**

### eq452c:Jumper-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Jumper:containment  
For Jumper the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel, DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel, DCConverterUnit or Line."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit cim:Line]` 

## eq452c:Junction

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Junction

**Nested Properties:**

### eq452c:Junction-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:Junction:containment  
For Junction the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Line (in case they model T-junction of a Line), or VoltageLevel or Bay (in case they model named join locations within a Substation).

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Line, Bay or VoltageLevel."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Line cim:Bay cim:VoltageLevel]` 

## eq452c:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### eq452c:LinearShuntCompensator.gPerSection-valueRange

**Path:** `cim:LinearShuntCompensator.gPerSection`  
**Name:** C:452:EQ:LinearShuntCompensator.gPerSection:valueRange  
LinearShuntCompensator.gPerSection shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq452c:ShuntCompensator.voltageSensitivity-valueRange

**Path:** `cim:ShuntCompensator.voltageSensitivity`  
**Name:** C:452:EQ:ShuntCompensator.voltageSensitivity:valueRange  
The ShuntCompensator.voltageSensitivity attribute shall be greater than zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq452c:LoadBreakSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch

## eq452c:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### eq452c:ShuntCompensator.voltageSensitivity-valueRange

**Path:** `cim:ShuntCompensator.voltageSensitivity`  
**Name:** C:452:EQ:ShuntCompensator.voltageSensitivity:valueRange  
The ShuntCompensator.voltageSensitivity attribute shall be greater than zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq452c:NonlinearShuntCompensatorPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensatorPoint

**Nested Properties:**

### eq452c:NonlinearShuntCompensatorPoint.g-valueRange

**Path:** `cim:NonlinearShuntCompensatorPoint.g`  
**Name:** C:452:EQ:NonlinearShuntCompensatorPoint.g:valueRange  
NonlinearShuntCompensatorPoint.g shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq452c:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

## eq452c:OperationalLimitSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitSet

## eq452c:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

## eq452c:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

## eq452c:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

## eq452c:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

## eq452c:PowerTransformer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformer

**Nested Properties:**

### eq452c:PowerTransformer-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:PowerTransformer:containment  
For PowerTransformer the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Substation or DCConverterUnit. For the case of a transformer that connects two substations, the terminal of one of the PowerTransformerEnd-s can be connected to a ConnectivityNode defined in another substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Substation or DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Substation cim:DCConverterUnit]` 

## eq452c:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### eq452c:PowerTransformerEnd.b-valueRange

**Path:** `cim:PowerTransformerEnd.b`  
**Name:** C:452:EQ:PowerTransformerEnd.b:valueRange  
PowerTransformerEnd.b shall be negative value or zero. Negative magnetising branch susceptance (PowerTransformerEnd.b) means inductive reactive power losses in no load. 

**Severity:** sh:Violation

**Messages:**
- "The value is positive."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq452c:PowerTransformerEnd.g-valueRange

**Path:** `cim:PowerTransformerEnd.g`  
**Name:** C:452:EQ:PowerTransformerEnd.g:valueRange  
PowerTransformerEnd.g shall be positive value or zero. Positive magnetising branch conductance (PowerTransformerEnd.g) means positive active power losses in no load.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq452c:ProtectedSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:LoadBreakSwitch

**Nested Properties:**

### eq452c:ProtectedSwitch-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:ProtectedSwitch:containment  
For ProtectedSwitch (Breaker, DisconnectingCircuitBreaker, LoadBreakSwitch) the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type Bay, VoltageLevel or DCConverterUnit.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not Bay, VoltageLevel or DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Bay cim:VoltageLevel cim:DCConverterUnit]` 

## eq452c:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

## eq452c:ReactiveCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ReactiveCapabilityCurve

## eq452c:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

**Nested Properties:**

### eq452c:RegulatingControl-RegulatingEquipment

**Path:** `^cim:RegulatingCondEq.RegulatingControl`  
**Name:** C:452:EQ:RegulatingControl:RegulatingEquipment  
A RegulatingControl that is not a TapChangerControl must have at least one regulating equipment associated through the RegulatingCondEq.RegulatingControl. That is, a RegulatingControl cannot exist without some equipment using it for regulating.

**Severity:** sh:Violation

**Messages:**
- "The RegulatingControl is not associated with an Equpment via RegulatingCondEq.RegulatingControl."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq452c:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

**Nested Properties:**

### eq452c:ConductingEquipment.BaseVoltage-whereRequired

**Path:** `cim:ConductingEquipment.BaseVoltage`  
**Name:** C:452:EQ:ConductingEquipment.BaseVoltage:whereRequired  
The ConductingEquipment.BaseVoltage association is required for the following ConductingEquipment: ACLineSegment, EquivalentBranch and SeriesCompensator. For all other Equipment-s, not contained in a VoltageLevel, the association ConductingEquipment.BaseVoltage can be provided (as it is optional), however the association to BaseVoltage coming from the container or transformer ends takes precedence.

**Severity:** sh:Violation

**Messages:**
- "The association ConductingEquipment.BaseVoltage is not provided."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### eq452c:SeriesCompensator-containment

**Path:** `cim:Equipment.EquipmentContainer / rdf:type`  
**Name:** C:452:EQ:SeriesCompensator:containment  
For SeriesCompensator the association Equipment.EquipmentContainer is required and shall point to EquipmentContainer of type VoltageLevel when in substation, DCConverterUnit or Line when outside substation.

**Severity:** sh:Violation

**Messages:**
- "The containment is either missing or it is not VoltageLevel, Line or DCConverterUnit."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Line cim:VoltageLevel cim:DCConverterUnit]` 

## eq452c:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

## eq452c:StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator

## eq452c:Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Switch

## eq452c:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### eq452c:SynchronousMachine.minQ-valueRangePair

**Path:** `cim:SynchronousMachine.minQ`  
**Name:** C:452:EQ:SynchronousMachine.maxQ:valueRangePair  
SynchronousMachine.maxQ shall be greater than or equal to SynchronousMachine.minQ.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of SynchronousMachine.maxQ."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:SynchronousMachine.maxQ` 

## eq452c:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

## eq452c:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

## eq452c:VsCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsCapabilityCurve

## eq452c:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.minOperatingP-valueRangePair

**Path:** `cim:GeneratingUnit.minOperatingP`  
**Name:** C:452:EQ:GeneratingUnit.minOperatingP:valueRangePair  
GeneratingUnit.maxOperatingP shall be greater than or equal to GeneratingUnit.minOperatingP.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than the value of GeneratingUnit.maxOperatingP."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:GeneratingUnit.maxOperatingP` 

