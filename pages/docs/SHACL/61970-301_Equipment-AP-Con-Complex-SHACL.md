# 61970-301_Equipment-AP-Con-Complex-SHACL

## eq:ACDCConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter
- targetClass: cim:VsConverter

**Nested Properties:**

### eq:ACDCConverter.DCTerminals-numberOfTerminals

**Path:** `^cim:ACDCConverterDCTerminal.DCConductingEquipment`  
**Name:** C:301:EQ:ACDCConverter.DCTerminals:numberOfTerminals  
A converter has two DC converter terminals.

**Severity:** sh:Violation

**Messages:**
- "The converter does not have two terminals, i.e. two instances of ACDCConverterDCTerminal."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:ACDCConverterDCTerminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:ACDCConverter.PccTerminal-valueType

**Path:** `cim:ACDCConverter.PccTerminal / cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:ACDCConverter.PccTerminal:valueType  
It is typically the terminal on the power transformer (or switch) closest to the AC network.

**Severity:** sh:Warning

**Messages:**
- "The terminal is not a terminal of a PowerTransformer or a Switch."

**Constraints:**

- **sh:OrConstraintComponent** (Severity: sh:Warning)
  - Shapes: `cim:PowerTransformer`, `cim:Switch`, `cim:Disconnector`, `cim:Fuse`, `cim:GroundDisconnector`, `cim:Jumper`, `cim:Breaker`, `cim:DisconnectingCircuitBreaker`, `cim:LoadBreakSwitch` 

## eq:ACDCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoad
- targetClass: cim:Disconnector
- targetClass: cim:DCBreaker
- targetClass: cim:DCChopper
- targetClass: cim:Switch
- targetClass: cim:CsConverter
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:GroundingImpedance
- targetClass: cim:EnergyConsumer
- targetClass: cim:AsynchronousMachine
- targetClass: cim:Ground
- targetClass: cim:DCSwitch
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCShunt
- targetClass: cim:Junction
- targetClass: cim:SeriesCompensator
- targetClass: cim:VsConverter
- targetClass: cim:NonConformLoad
- targetClass: cim:StationSupply
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:GroundDisconnector
- targetClass: cim:DCLineSegment
- targetClass: cim:DCDisconnector
- targetClass: cim:EquivalentInjection
- targetClass: cim:EquivalentBranch
- targetClass: cim:PowerTransformer
- targetClass: cim:Clamp
- targetClass: cim:BusbarSection
- targetClass: cim:PetersenCoil
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:EnergySource
- targetClass: cim:StaticVarCompensator
- targetClass: cim:Fuse
- targetClass: cim:Jumper
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Cut
- targetClass: cim:DCBusbar
- targetClass: cim:SynchronousMachine
- targetClass: cim:EquivalentShunt
- targetClass: cim:Breaker
- targetClass: cim:DCGround
- targetClass: cim:ACLineSegment

## eq:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

**Nested Properties:**

### eq:Conductor.length-length

**Path:** `cim:Conductor.length`  
**Name:** C:301:EQ:Length:valueRange  
It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:ActivePowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ActivePowerLimit

**Nested Properties:**

### eq:ActivePowerLimit.normalValue-valueRange

**Path:** `cim:ActivePowerLimit.normalValue`  
**Name:** C:301:EQ:ActivePowerLimit.normalValue:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:ApparentPowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ApparentPowerLimit

**Nested Properties:**

### eq:ApparentPowerLimit.normalValue-valueRange

**Path:** `cim:ApparentPowerLimit.normalValue`  
**Name:** C:301:EQ:ApparentPowerLimit.normalValue:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### eq:RotatingMachine.ratedPowerFactor-valueRange

**Path:** `cim:RotatingMachine.ratedPowerFactor`  
**Name:** C:301:EQ:RotatingMachine.ratedPowerFactor:valueRange  
The attribute cannot be a negative value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:RotatingMachine.ratedS-valueRange

**Path:** `cim:RotatingMachine.ratedS`  
**Name:** C:301:EQ:RotatingMachine.ratedS:valueRange  
The attribute shall have a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:RotatingMachine.ratedU-valueRange

**Path:** `cim:RotatingMachine.ratedU`  
**Name:** C:301:EQ:RotatingMachine.ratedU:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BaseVoltage

**Nested Properties:**

### eq:BaseVoltage.nominalVoltage-valueRange

**Path:** `cim:BaseVoltage.nominalVoltage`  
**Name:** C:301:EQ:BaseVoltage.nominalVoltage:valueRange  
Shall be a positive value and not zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

**Nested Properties:**

### eq:BatteryUnit.ratedE-valueRange

**Path:** `cim:BatteryUnit.ratedE`  
**Name:** C:301:EQ:BatteryUnit.ratedE:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:BoundaryPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim100:BoundaryPoint

**Nested Properties:**

### eq:BoundaryPoint.fromEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
**Name:** C:301:EQ:BoundaryPoint.fromEndIsoCode:stringLength  
The length of the string is 2 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is not 2 characters."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 

### eq:BoundaryPoint.fromEndIsoCode-valueValidity

**Path:** `cim100:BoundaryPoint.fromEndIsoCode`  
**Name:** C:301:EQ:BoundaryPoint.fromEndIsoCode:valueValidity  
The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes).

**Severity:** sh:Violation

**Messages:**
- "Not valid two-character ISO code for Europe."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[AL AT BE BG HR CY CZ DK EE FI FR DE GR HU IS IE IT LV LI LT LU MT MD ME NL NO PL PT RO RS SK SI ES SE CH TR UA MK GB BA BY TN MA RU]` 

### eq:BoundaryPoint.fromEndName-stringLength

**Path:** `cim100:BoundaryPoint.fromEndName`  
**Name:** C:301:EQ:BoundaryPoint.fromEndName:stringLength  
A human readable name with length of the string 64 characters maximum. 

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eq:BoundaryPoint.fromEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.fromEndNameTso`  
**Name:** C:301:EQ:BoundaryPoint.fromEndNameTso:stringLength  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eq:BoundaryPoint.toEndIsoCode-stringLength

**Path:** `cim100:BoundaryPoint.toEndIsoCode`  
**Name:** C:301:EQ:BoundaryPoint.toEndIsoCode:stringLength  
The length of the string is 2 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is not 2 characters."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 

### eq:BoundaryPoint.toEndIsoCode-valueValidity

**Path:** `cim100:BoundaryPoint.toEndIsoCode`  
**Name:** C:301:EQ:BoundaryPoint.toEndIsoCode:valueValidity  
The ISO code is a two-character country code as defined by ISO 3166 (http://www.iso.org/iso/country_codes).

**Severity:** sh:Violation

**Messages:**
- "Not valid two-character ISO code for Europe."

**Constraints:**

- **sh:MinLengthConstraintComponent** (Severity: sh:Violation)
  - MinLength: `2` 
- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `2` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[AL AT BE BG HR CY CZ DK EE FI FR DE GR HU IS IE IT LV LI LT LU MT MD ME NL NO PL PT RO RS SK SI ES SE CH TR UA MK GB BA BY TN MA RU]` 

### eq:BoundaryPoint.toEndName-stringLength

**Path:** `cim100:BoundaryPoint.toEndName`  
**Name:** C:301:EQ:BoundaryPoint.toEndName:stringLength  
A human readable name with length of the string 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

### eq:BoundaryPoint.toEndNameTso-stringLength

**Path:** `cim100:BoundaryPoint.toEndNameTso`  
**Name:** C:301:EQ:BoundaryPoint.toEndNameTso:stringLength  
The length of the string is 64 characters maximum.

**Severity:** sh:Violation

**Messages:**
- "String length is greater than 64 characters."

**Constraints:**

- **sh:MaxLengthConstraintComponent** (Severity: sh:Violation)
  - MaxLength: `64` 

## eq:Breaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:BusbarSection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BusbarSection

**Nested Properties:**

### eq:Terminal.ConductingEquipmentBusbarSection-valueType

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:BusbarSection:numberOfTerminals  
A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.

**Severity:** sh:Violation

**Messages:**
- "The BusbarSection has more than one  terminal."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq:Clamp

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Clamp

**Nested Properties:**

### eq:Clamp.lengthFromTerminal1-length

**Path:** `cim:Clamp.lengthFromTerminal1`  
**Name:** C:301:EQ:Length:valueRange  
It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:Clamp-numberOfTerminals

**Name:** C:452:EQ:Clamp:numberOfTerminals  
A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode.

**Severity:** sh:Violation

**Messages:**
- "Either the Clamp does not have exactly one Terminal or the Terminal is not associated with a ConnectivityNode."

**Targets:**
- targetClass: cim:Clamp

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1`

## eq:ConductingEquipment-oneTerminal

**Name:** C:301:EQ:ConductingEquipment:oneTerminal  
All other ConductingEquipment leaf classes (notably also including Clamp and BusbarSection) and DCConductingEquipment have a single terminal.

**Severity:** sh:Violation

**Messages:**
- "The ConductingEquipment does not have the required number of Terminal-s."

**Targets:**
- targetClass: cim:EnergyConsumer
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine
- targetClass: cim:DCGround
- targetClass: cim:EnergySource
- targetClass: cim:NonConformLoad
- targetClass: cim:EquivalentInjection
- targetClass: cim:Junction
- targetClass: cim:DCBusbar
- targetClass: cim:DCShunt
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:StaticVarCompensator
- targetClass: cim:EquivalentShunt
- targetClass: cim:Ground
- targetClass: cim:ConformLoad
- targetClass: cim:StationSupply
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:NonlinearShuntCompensator

**Constraints:**

- **sh:OrConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1`

## eq:ConductingEquipment-twoTerminals

**Name:** C:301:EQ:ConductingEquipment:twoTerminals  
The following ConductingEquipment classes have two terminals: ACLineSegment, DCLineSegment, DCSeriesDevice, DCSwitch (and its specializations), DCChopper, Switch and all its specializations (including Jumper, Fuse, Breaker, Disconnector, LoadBreakSwitch, and Cut), SeriesCompensator, and EquivalentBranch. The PowerTransformer class typically has two terminals, but may also have one or more terminals. For example a zig-zag connected grounding transformer may have one terminal. Three terminal transformers are commonly used in transmission systems and in special cases transformers may have four, five, or more terminals. 

**Severity:** sh:Violation

**Messages:**
- "The ConductingEquipment does not have the required number of Terminal-s."

**Targets:**
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DCLineSegment
- targetClass: cim:DCSeriesDevice
- targetClass: cim:GroundDisconnector
- targetClass: cim:Breaker
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Cut
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCBreaker
- targetClass: cim:DCChopper
- targetClass: cim:Switch
- targetClass: cim:Disconnector
- targetClass: cim:Jumper
- targetClass: cim:EquivalentBranch
- targetClass: cim:ACLineSegment
- targetClass: cim:DCSwitch
- targetClass: cim:DCDisconnector
- targetClass: cim:Fuse

**Constraints:**

- **sh:OrConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `2` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `2` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `2` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `2`

## eq:ConductingEquipment-twoTerminalsShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment
- targetClass: cim:DCBreaker
- targetClass: cim:Jumper
- targetClass: cim:DCLineSegment
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCDisconnector
- targetClass: cim:DCChopper
- targetClass: cim:GroundDisconnector
- targetClass: cim:Breaker
- targetClass: cim:EquivalentBranch
- targetClass: cim:Switch
- targetClass: cim:Fuse
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Cut
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCSwitch
- targetClass: cim:Disconnector

## eq:ConductingEquipment.BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Junction
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:Disconnector
- targetClass: cim:BusbarSection
- targetClass: cim:EnergyConsumer
- targetClass: cim:ConformLoad
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:SeriesCompensator
- targetClass: cim:Switch
- targetClass: cim:CsConverter
- targetClass: cim:GroundingImpedance
- targetClass: cim:StationSupply
- targetClass: cim:EquivalentShunt
- targetClass: cim:EquivalentBranch
- targetClass: cim:Breaker
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Clamp
- targetClass: cim:ACLineSegment
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:AsynchronousMachine
- targetClass: cim:Ground
- targetClass: cim:NonConformLoad
- targetClass: cim:EquivalentInjection
- targetClass: cim:Jumper
- targetClass: cim:VsConverter
- targetClass: cim:SynchronousMachine
- targetClass: cim:PowerTransformer
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:PetersenCoil
- targetClass: cim:EnergySource
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:StaticVarCompensator
- targetClass: cim:Cut

## eq:ControlAreaGeneratingUnit.GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:WindGeneratingUnit

## eq:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### eq:ACDCConverter.baseS-valueRange

**Path:** `cim:ACDCConverter.baseS`  
**Name:** C:301:EQ:ACDCConverter.baseS:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.idleLoss-valueRange

**Path:** `cim:ACDCConverter.idleLoss`  
**Name:** C:301:EQ:ACDCConverter.idleLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.maxUdc-valueRange

**Path:** `cim:ACDCConverter.maxUdc`  
**Name:** C:301:EQ:ACDCConverter.maxUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.minUdc-valueRange

**Path:** `cim:ACDCConverter.minUdc`  
**Name:** C:301:EQ:ACDCConverter.minUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.ratedUdc-valueRange

**Path:** `cim:ACDCConverter.ratedUdc`  
**Name:** C:301:EQ:ACDCConverter.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.resistiveLoss-valueRange

**Path:** `cim:ACDCConverter.resistiveLoss`  
**Name:** C:301:EQ:ACDCConverter.resistiveLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.switchingLoss-valueRange

**Path:** `cim:ACDCConverter.switchingLoss`  
**Name:** C:301:EQ:ACDCConverter.switchingLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.maxAlpha-valueRange

**Path:** `cim:CsConverter.maxAlpha`  
**Name:** C:301:EQ:CsConverter.maxAlpha:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.maxGamma-valueRange

**Path:** `cim:CsConverter.maxGamma`  
**Name:** C:301:EQ:CsConverter.maxGamma:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.maxIdc-valueRange

**Path:** `cim:CsConverter.maxIdc`  
**Name:** C:301:EQ:CsConverter.maxIdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.minAlpha-valueRange

**Path:** `cim:CsConverter.minAlpha`  
**Name:** C:301:EQ:CsConverter.minAlpha:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.minGamma-valueRange

**Path:** `cim:CsConverter.minGamma`  
**Name:** C:301:EQ:CsConverter.minGamma:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.minIdc-valueRange

**Path:** `cim:CsConverter.minIdc`  
**Name:** C:301:EQ:CsConverter.minIdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:CsConverter.ratedIdc-valueRange

**Path:** `cim:CsConverter.ratedIdc`  
**Name:** C:301:EQ:CsConverter.ratedIdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:CurrentLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurrentLimit

**Nested Properties:**

### eq:CurrentLimit.normalValue-valueRange

**Path:** `cim:CurrentLimit.normalValue`  
**Name:** C:301:EQ:CurrentLimit.normalValue:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:Cut

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Cut

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Cut.lengthFromTerminal1-length

**Path:** `cim:Cut.lengthFromTerminal1`  
**Name:** C:301:EQ:Length:valueRange  
It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBreaker

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCBusbar

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBusbar

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCChopper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCChopper

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCDisconnector

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCGround

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCGround

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCLineSegment

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:DCLineSegment.length-length

**Path:** `cim:DCLineSegment.length`  
**Name:** C:301:EQ:Length:valueRange  
It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCSeriesDevice

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSeriesDevice

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCShunt

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DCSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSwitch

**Nested Properties:**

### eq:DCConductingEquipment.ratedUdc-valueRange

**Path:** `cim:DCConductingEquipment.ratedUdc`  
**Name:** C:301:EQ:DCConductingEquipment.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:DisconnectingCircuitBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:Disconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Disconnector

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:EarthFaultCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil

**Nested Properties:**

### eq:EarthFaultCompensator-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:EarthFaultCompensator:numberOfTerminals  
The EarthFaultCompensator can have either one or two terminals modelled. If the second terminal of an EarthFaultCompensator is omitted, it is assumed the terminal solidly connects to ground. If there is some kind of topology or local earth resistivity that is important to model on the ground side of the device, then a second terminal is added.

**Severity:** sh:Violation

**Messages:**
- "The EarthFaultCompensator does not have the required number of Terminal-s."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

## eq:Equipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch
- targetClass: cim:EquivalentShunt
- targetClass: cim:EquivalentInjection

## eq:EquivalentBranch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch

## eq:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

## eq:Fuse

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Fuse

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:GeneratingUnit.nominalP

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit

## eq:GroundDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:HydroGeneratingUnit.dropHeight-length

**Path:** `cim:HydroGeneratingUnit.dropHeight`  
**Name:** C:301:EQ:Length:valueRange  
It shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:Jumper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Jumper

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:LimitKind

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitType

## eq:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### eq:ShuntCompensator-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:ShuntCompensator:numberOfTerminals  
ShuntCompensator is a single terminal device. 

**Severity:** sh:Violation

**Messages:**
- "The ShuntCompensator does not have one terminal."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### eq:ShuntCompensator.normalSections-valueRangePair

**Path:** `cim:ShuntCompensator.normalSections`  
**Name:** C:301:EQ:ShuntCompensator.normalSections:valueRangePair  
The value shall be between zero and ShuntCompensator.maximumSections.

**Severity:** sh:Violation

**Messages:**
- "The value is either negative or greater than ShuntCompensator.maximumSections."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ShuntCompensator.maximumSections` 

## eq:LoadBreakSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:LoadResponseCharacteristic

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadResponseCharacteristic

## eq:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### eq:ShuntCompensator-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:ShuntCompensator:numberOfTerminals  
ShuntCompensator is a single terminal device. 

**Severity:** sh:Violation

**Messages:**
- "The ShuntCompensator does not have one terminal."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### eq:ShuntCompensator.normalSections-valueRangePair

**Path:** `cim:ShuntCompensator.normalSections`  
**Name:** C:301:EQ:ShuntCompensator.normalSections:valueRangePair  
The value shall be between zero and ShuntCompensator.maximumSections.

**Severity:** sh:Violation

**Messages:**
- "The value is either negative or greater than ShuntCompensator.maximumSections."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 
- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:ShuntCompensator.maximumSections` 

## eq:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:OperationalLimitType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitType

## eq:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

**Nested Properties:**

### eq:TapChanger.normalStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.normalStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.normalStep` 

### eq:TapChanger.neutralStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.neutralStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.neutralStep` 

### eq:TapChanger.highStep-valueRangePair

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.highStep:valueRangePair  
The attribute shall be greater than lowStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than or equal to the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.neutralStep-valueRangePairTo

**Path:** `cim:TapChanger.neutralStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.neutralStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairTo

**Path:** `cim:TapChanger.normalStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.normalStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## eq:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### eq:TapChanger.neutralStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.neutralStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.neutralStep` 

### eq:TapChanger.highStep-valueRangePair

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.highStep:valueRangePair  
The attribute shall be greater than lowStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than or equal to the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.normalStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.normalStep` 

### eq:TapChanger.neutralStep-valueRangePairTo

**Path:** `cim:TapChanger.neutralStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.neutralStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairTo

**Path:** `cim:TapChanger.normalStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.normalStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## eq:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### eq:TapChanger.neutralStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.neutralStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.neutralStep` 

### eq:TapChanger.highStep-valueRangePair

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.highStep:valueRangePair  
The attribute shall be greater than lowStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than or equal to the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.normalStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.normalStep` 

### eq:TapChanger.neutralStep-valueRangePairTo

**Path:** `cim:TapChanger.neutralStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.neutralStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairTo

**Path:** `cim:TapChanger.normalStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.normalStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## eq:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

**Nested Properties:**

### eq:TapChanger.neutralStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.neutralStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.neutralStep` 

### eq:TapChanger.highStep-valueRangePair

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.highStep:valueRangePair  
The attribute shall be greater than lowStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than or equal to the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.normalStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.normalStep` 

### eq:TapChanger.neutralStep-valueRangePairTo

**Path:** `cim:TapChanger.neutralStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.neutralStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairTo

**Path:** `cim:TapChanger.normalStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.normalStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## eq:PowerElectronicsConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerElectronicsConnection

**Nested Properties:**

### eq:PowerElectronicsConnection.ratedS-valueRange

**Path:** `cim:PowerElectronicsConnection.ratedS`  
**Name:** C:301:EQ:PowerElectronicsConnection.ratedS:valueRange  
The attribute shall have a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:PowerElectronicsConnection.ratedU-valueRange

**Path:** `cim:PowerElectronicsConnection.ratedU`  
**Name:** C:301:EQ:PowerElectronicsConnection.ratedU:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:PowerTransformer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformer

## eq:PowerTransformer-twoWinding

**Severity:** sh:Violation

**Targets:**
- sparqlTarget: 

## eq:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### eq:PowerTransformerEnd.ratedS-valueRange

**Path:** `cim:PowerTransformerEnd.ratedS`  
**Name:** C:301:EQ:PowerTransformerEnd.ratedS:valueRange  
The attribute shall be a positive value. 

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

**Nested Properties:**

### eq:TapChanger.normalStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.normalStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.normalStep` 

### eq:TapChanger.neutralStep-valueRangePairFrom

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairFrom  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than the value of TapChanger.neutralStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.neutralStep` 

### eq:TapChanger.highStep-valueRangePair

**Path:** `cim:TapChanger.lowStep`  
**Name:** C:301:EQ:TapChanger.highStep:valueRangePair  
The attribute shall be greater than lowStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.lowStep is greater than or equal to the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.neutralStep-valueRangePairTo

**Path:** `cim:TapChanger.neutralStep`  
**Name:** C:301:EQ:TapChanger.neutralStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.neutralStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

### eq:TapChanger.normalStep-valueRangePairTo

**Path:** `cim:TapChanger.normalStep`  
**Name:** C:301:EQ:TapChanger.normalStep:valueRangePairTo  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value of TapChanger.normalStep is greater than the value of TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## eq:ReactiveCapabilityCurve-curveYvalues

**Name:** C:301:EQ:ReactiveCapabilityCurve:yvalues  
For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure. 

**Severity:** sh:Violation

**Messages:**
- "CurveData associated with a ReactiveCapabilityCurve does not have both .y1value and .y2value defined."

**Targets:**
- targetClass: cim:CurveData

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Violation)

  **Item 1:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1` 
  **Item 2:**

  **Constraints:**

  - **sh:MinCountConstraintComponent**
    - MinCount: `1` 
  - **sh:MaxCountConstraintComponent**
    - MaxCount: `1`

## eq:RegularTimePoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegularTimePoint

**Nested Properties:**

### eq:RegularTimePoint.sequenceNumber-valueRange

**Path:** `cim:RegularTimePoint.sequenceNumber`  
**Name:** C:301:EQ:RegularTimePoint.sequenceNumber:valueRange  
The sequence number cannot be negative.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

## eq:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

**Nested Properties:**

### eq:SeriesCompensator-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:SeriesCompensator:numberOfTerminals  
It is a two terminal device.

**Severity:** sh:Violation

**Messages:**
- "The SeriesCompensator does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

## eq:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator

**Nested Properties:**

### eq:StaticVarCompensator.capacitiveRating-valueRange

**Path:** `cim:StaticVarCompensator.capacitiveRating`  
**Name:** C:301:EQ:StaticVarCompensator.capacitiveRating:valueRange  
Shall always be positive.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:StaticVarCompensator.inductiveRating-valueRange

**Path:** `cim:StaticVarCompensator.inductiveRating`  
**Name:** C:301:EQ:StaticVarCompensator.inductiveRating:valueRange  
Shall always be negative.  

**Severity:** sh:Violation

**Messages:**
- "The value is positive or zero."

**Constraints:**

- **sh:MaxExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:StaticVarCompensator.slope-valueRange

**Path:** `cim:StaticVarCompensator.slope`  
**Name:** C:301:EQ:StaticVarCompensator.slope:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Switch

**Nested Properties:**

### eq:Switch-numberOfTerminals

**Path:** `^cim:Terminal.ConductingEquipment`  
**Name:** C:301:EQ:Switch:numberOfTerminals  
All switches are two terminal devices including grounding switches. 

**Severity:** sh:Violation

**Messages:**
- "The Switch (or subclass) does not have two terminals."

**Constraints:**

- **sh:ClassConstraintComponent** (Severity: sh:Violation)
  - Class: `cim:Terminal` 
- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

### eq:Switch.ratedCurrent-valueRange

**Path:** `cim:Switch.ratedCurrent`  
**Name:** C:301:EQ:Switch.ratedCurrent:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### eq:RotatingMachine.ratedPowerFactor-valueRange

**Path:** `cim:RotatingMachine.ratedPowerFactor`  
**Name:** C:301:EQ:RotatingMachine.ratedPowerFactor:valueRange  
The attribute cannot be a negative value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:RotatingMachine.ratedS-valueRange

**Path:** `cim:RotatingMachine.ratedS`  
**Name:** C:301:EQ:RotatingMachine.ratedS:valueRange  
The attribute shall have a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:RotatingMachine.ratedU-valueRange

**Path:** `cim:RotatingMachine.ratedU`  
**Name:** C:301:EQ:RotatingMachine.ratedU:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular

## eq:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

## eq:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil
- targetClass: cim:GroundDisconnector
- targetClass: cim:Ground

**Nested Properties:**

### eq:Terminal.phases-phaseCodeN

**Path:** `^cim:Terminal.ConductingEquipment / cim:Terminal.phases`  
**Name:** C:301:EQ:Terminal.phases:phaseCode  
If the attribute is missing, three phases (ABC) shall be assumed, except for terminals of grounding classes (specializations of EarthFaultCompensator, GroundDisconnector, and Ground) which will be assumed to be N. Therefore, phase code ABCN is explicitly declared when needed, e.g. for star point grounding equipment.

**Severity:** sh:Violation

**Messages:**
- "Terminal.phases differs from PhaseCode.N for a grounding related class."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PhaseCode.N]` 

## eq:Terminal.phases

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConnectivityNode

## eq:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:VoltageLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageLimit

**Nested Properties:**

### eq:VoltageLimit.normalValue-valueRange

**Path:** `cim:VoltageLimit.normalValue`  
**Name:** C:301:EQ:VoltageLimit.normalValue:valueRange  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## eq:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### eq:ACDCConverter.baseS-valueRange

**Path:** `cim:ACDCConverter.baseS`  
**Name:** C:301:EQ:ACDCConverter.baseS:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.idleLoss-valueRange

**Path:** `cim:ACDCConverter.idleLoss`  
**Name:** C:301:EQ:ACDCConverter.idleLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.maxUdc-valueRange

**Path:** `cim:ACDCConverter.maxUdc`  
**Name:** C:301:EQ:ACDCConverter.maxUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.minUdc-valueRange

**Path:** `cim:ACDCConverter.minUdc`  
**Name:** C:301:EQ:ACDCConverter.minUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.ratedUdc-valueRange

**Path:** `cim:ACDCConverter.ratedUdc`  
**Name:** C:301:EQ:ACDCConverter.ratedUdc:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.resistiveLoss-valueRange

**Path:** `cim:ACDCConverter.resistiveLoss`  
**Name:** C:301:EQ:ACDCConverter.resistiveLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:ACDCConverter.switchingLoss-valueRange

**Path:** `cim:ACDCConverter.switchingLoss`  
**Name:** C:301:EQ:ACDCConverter.switchingLoss:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:VsConverter.maxModulationIndex-valueRangeTypical

**Path:** `cim:VsConverter.maxModulationIndex`  
**Name:** C:301:EQ:VsConverter.maxModulationIndex:valueRangeTypical  
A factor typically less than 1.

**Severity:** sh:Warning

**Messages:**
- "The value is greater than 1."

**Constraints:**

- **sh:MaxInclusiveConstraintComponent** (Severity: sh:Warning)
  - Value: `1.0` 

## eq:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.ratedGrossMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedGrossMinP-valueRange

**Path:** `cim:GeneratingUnit.ratedGrossMinP`  
**Name:** C:301:EQ:GeneratingUnit.ratedGrossMinP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### eq:GeneratingUnit.ratedNetMaxP-valueRange

**Path:** `cim:GeneratingUnit.ratedNetMaxP`  
**Name:** C:301:EQ:GeneratingUnit.ratedNetMaxP:valueRange  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

