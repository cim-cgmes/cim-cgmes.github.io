# 61970-600-2_Operation-AP-Con-Complex-Explicit-CrossProfile-SHACL

## op452cpe:Control.PowerSystemResource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorReset
- targetClass: cim:Command
- targetClass: cim:SetPoint
- targetClass: cim:RaiseLowerCommand

**Nested Properties:**

### op452cpe:Control.PowerSystemResource-valueType

**Path:** `cim:Control.PowerSystemResource / rdf:type`  
**Name:** Control.PowerSystemResource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Cut cim:DCSwitch cim:PhaseTapChangerLinear cim:DCShunt cim:DCLine cim:CurrentTransformer cim:PowerTransformer cim:ExternalNetworkInjection cim:Line cim:VsConverter cim:AsynchronousMachine cim:DCDisconnector cim:NonConformLoad cim:Junction cim:Bay cim:NonlinearShuntCompensator cim:SynchronousMachine cim:WindGeneratingUnit cim:EnergyConsumer cim:DCChopper cim:HydroGeneratingUnit cim:ACLineSegment cim:PowerElectronicsConnection cim:TapChangerControl cim:CombinedCyclePlant cim:StationSupply cim:RegulatingControl cim:Ground cim:PetersenCoil cim:EnergySource cim:DCSeriesDevice cim:VoltageLevel cim:Disconnector cim:EquivalentShunt cim:ThermalGeneratingUnit cim:DisconnectingCircuitBreaker cim:ConformLoad cim:NuclearGeneratingUnit cim:HydroPump cim:DCConverterUnit cim:GeneratingUnit cim:Breaker cim:PotentialTransformer cim:FaultIndicator cim:PhaseTapChangerAsymmetrical cim100:SolarPowerPlant cim:CAESPlant cim:GroundDisconnector cim:Switch cim:HydroPowerPlant cim:BatteryUnit cim:LoadBreakSwitch cim:SurgeArrester cim:Substation cim:WaveTrap cim:PhaseTapChangerSymmetrical cim:Fuse cim:SolarGeneratingUnit cim:ControlArea cim:BusbarSection cim:EquivalentBranch cim:Jumper cim:DCBusbar cim100:BoundaryPoint cim:PhotoVoltaicUnit cim:RatioTapChanger cim:LinearShuntCompensator cim:DCLineSegment cim:Clamp cim:SeriesCompensator cim:CogenerationPlant cim:PowerElectronicsWindUnit cim:PostLineSensor cim:EquivalentNetwork cim:PhaseTapChangerTabular cim:DCBreaker cim:StaticVarCompensator cim100:WindPowerPlant cim:DCGround cim:EquivalentInjection cim:GroundingImpedance cim:CsConverter cim:Equipment]` 

## op452cpe:Measurement.ACDCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StringMeasurement
- targetClass: cim:Accumulator
- targetClass: cim:Analog
- targetClass: cim:Discrete

**Nested Properties:**

### op452cpe:Measurement.ACDCTerminal-valueType

**Path:** `cim:Measurement.Terminal / rdf:type`  
**Name:** Measurement.Terminal-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class ACDCTerminal or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ACDCConverterDCTerminal cim:DCTerminal cim:Terminal]` 

## op452cpe:Measurement.PowerSystemResource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Analog
- targetClass: cim:Discrete
- targetClass: cim:StringMeasurement
- targetClass: cim:Accumulator

**Nested Properties:**

### op452cpe:Measurement.PowerSystemResource-valueType

**Path:** `cim:Measurement.PowerSystemResource / rdf:type`  
**Name:** Measurement.PowerSystemResource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Cut cim:DCSwitch cim:PhaseTapChangerLinear cim:DCShunt cim:DCLine cim:CurrentTransformer cim:PowerTransformer cim:ExternalNetworkInjection cim:Line cim:VsConverter cim:AsynchronousMachine cim:DCDisconnector cim:NonConformLoad cim:Junction cim:Bay cim:NonlinearShuntCompensator cim:SynchronousMachine cim:WindGeneratingUnit cim:EnergyConsumer cim:DCChopper cim:HydroGeneratingUnit cim:ACLineSegment cim:PowerElectronicsConnection cim:TapChangerControl cim:CombinedCyclePlant cim:StationSupply cim:RegulatingControl cim:Ground cim:PetersenCoil cim:EnergySource cim:DCSeriesDevice cim:VoltageLevel cim:Disconnector cim:EquivalentShunt cim:ThermalGeneratingUnit cim:DisconnectingCircuitBreaker cim:ConformLoad cim:NuclearGeneratingUnit cim:HydroPump cim:DCConverterUnit cim:GeneratingUnit cim:Breaker cim:PotentialTransformer cim:FaultIndicator cim:PhaseTapChangerAsymmetrical cim100:SolarPowerPlant cim:CAESPlant cim:GroundDisconnector cim:Switch cim:HydroPowerPlant cim:BatteryUnit cim:LoadBreakSwitch cim:SurgeArrester cim:Substation cim:WaveTrap cim:PhaseTapChangerSymmetrical cim:Fuse cim:SolarGeneratingUnit cim:ControlArea cim:BusbarSection cim:EquivalentBranch cim:Jumper cim:DCBusbar cim100:BoundaryPoint cim:PhotoVoltaicUnit cim:RatioTapChanger cim:LinearShuntCompensator cim:DCLineSegment cim:Clamp cim:SeriesCompensator cim:CogenerationPlant cim:PowerElectronicsWindUnit cim:PostLineSensor cim:EquivalentNetwork cim:PhaseTapChangerTabular cim:DCBreaker cim:StaticVarCompensator cim100:WindPowerPlant cim:DCGround cim:EquivalentInjection cim:GroundingImpedance cim:CsConverter cim:Equipment]` 

