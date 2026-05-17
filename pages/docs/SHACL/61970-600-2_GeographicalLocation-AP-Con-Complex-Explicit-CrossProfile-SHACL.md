# 61970-600-2_GeographicalLocation-AP-Con-Complex-Explicit-CrossProfile-SHACL

## gl13cpe:Location.PowerSystemResources

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Location

**Nested Properties:**

### gl13cpe:Location.PowerSystemResources-valueType

**Path:** `cim:Location.PowerSystemResources / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class PowerSystemResource or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Cut cim:DCSwitch cim:PhaseTapChangerLinear cim:DCShunt cim:DCLine cim:CurrentTransformer cim:PowerTransformer cim:ExternalNetworkInjection cim:Line cim:VsConverter cim:AsynchronousMachine cim:DCDisconnector cim:NonConformLoad cim:Junction cim:Bay cim:NonlinearShuntCompensator cim:SynchronousMachine cim:WindGeneratingUnit cim:EnergyConsumer cim:DCChopper cim:HydroGeneratingUnit cim:ACLineSegment cim:PowerElectronicsConnection cim:TapChangerControl cim:CombinedCyclePlant cim:StationSupply cim:RegulatingControl cim:Ground cim:PetersenCoil cim:EnergySource cim:DCSeriesDevice cim:VoltageLevel cim:Disconnector cim:EquivalentShunt cim:ThermalGeneratingUnit cim:DisconnectingCircuitBreaker cim:ConformLoad cim:NuclearGeneratingUnit cim:HydroPump cim:DCConverterUnit cim:GeneratingUnit cim:Breaker cim:PotentialTransformer cim:FaultIndicator cim:PhaseTapChangerAsymmetrical cim100:SolarPowerPlant cim:CAESPlant cim:GroundDisconnector cim:Switch cim:HydroPowerPlant cim:BatteryUnit cim:LoadBreakSwitch cim:SurgeArrester cim:Substation cim:WaveTrap cim:PhaseTapChangerSymmetrical cim:Fuse cim:SolarGeneratingUnit cim:ControlArea cim:BusbarSection cim:EquivalentBranch cim:Jumper cim:DCBusbar cim100:BoundaryPoint cim:PhotoVoltaicUnit cim:RatioTapChanger cim:LinearShuntCompensator cim:DCLineSegment cim:Clamp cim:SeriesCompensator cim:CogenerationPlant cim:PowerElectronicsWindUnit cim:PostLineSensor cim:EquivalentNetwork cim:PhaseTapChangerTabular cim:DCBreaker cim:StaticVarCompensator cim100:WindPowerPlant cim:DCGround cim:EquivalentInjection cim:GroundingImpedance cim:CsConverter cim:Equipment]` 

