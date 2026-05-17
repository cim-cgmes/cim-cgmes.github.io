# 61970-453_DiagramLayout-AP-Con-Complex-Explicit-CrossProfile-SHACL

## dl453cpe:DiagramObject.IdentifiedObject

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramObject

**Nested Properties:**

### dl453cpe:DiagramObject.IdentifiedObject-valueType

**Path:** `cim:DiagramObject.IdentifiedObject / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class IdentifiedObject or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ActivePowerLimit cim:BusNameMarker cim:Ground cim:PhotoVoltaicUnit cim:LoadBreakSwitch cim:StationSupply cim:CurrentTransformer cim:ReportingGroup cim:WaveTrap cim:ReactiveCapabilityCurve cim:PowerTransformerEnd cim:Junction cim:TapSchedule cim:EnergySchedulingType cim:PhaseTapChangerSymmetrical cim:NonConformLoad cim:NonConformLoadSchedule cim:PhaseTapChangerTable cim:ExternalNetworkInjection cim:ControlAreaGeneratingUnit cim:PhaseTapChangerTabular cim:GrossToNetActivePowerCurve cim:AsynchronousMachine cim:Substation cim:HydroGeneratingUnit cim:DCConverterUnit cim:Bay cim:OperationalLimitSet cim:VsCapabilityCurve cim:ConformLoadSchedule cim:GeneratingUnit cim:CombinedCyclePlant cim:SwitchSchedule cim:SubLoadArea cim:Line cim:Jumper cim:PetersenCoil cim:GeographicalRegion cim:PostLineSensor cim:RatioTapChangerTable cim:EquivalentShunt cim:ConformLoad cim:HydroPump cim100:WindPowerPlant cim:NonConformLoadGroup cim:Breaker cim:DCTerminal cim:DCLine cim:DCChopper cim:Fuse cim:DCGround cim:SubGeographicalRegion cim:LoadResponseCharacteristic cim:PotentialTransformer cim:DayType cim:FossilFuel cim:ConnectivityNode cim:CurrentLimit cim:SolarGeneratingUnit cim:WindGeneratingUnit cim:StaticVarCompensator cim:DCDisconnector cim:SeriesCompensator cim:RegulatingControl cim:BatteryUnit cim:LinearShuntCompensator cim:LoadArea cim:FaultIndicator cim:TapChangerControl cim:EnergySource cim:BusbarSection cim:DCShunt cim:RegulationSchedule cim:OperationalLimitType cim:DCBreaker cim:Terminal cim:PhaseTapChangerLinear cim:VoltageLimit cim:NuclearGeneratingUnit cim:DCLineSegment cim:DCNode cim:ACDCConverterDCTerminal cim:Switch cim:Clamp cim:Season cim:SynchronousMachine cim:EquivalentBranch cim:ConformLoadGroup cim:BaseVoltage cim:Disconnector cim100:SolarPowerPlant cim:GroundingImpedance cim:Cut cim:ThermalGeneratingUnit cim:GroundDisconnector cim:ApparentPowerLimit cim:RatioTapChanger cim:PowerTransformer cim:SurgeArrester cim:EnergyConsumer cim100:BoundaryPoint cim:CsConverter cim:DCSeriesDevice cim:ACLineSegment cim:PhaseTapChangerAsymmetrical cim:VsConverter cim:CAESPlant cim:NonlinearShuntCompensator cim:HydroPowerPlant cim:PowerElectronicsWindUnit cim:PowerElectronicsConnection cim:VoltageLevel cim:DCSwitch cim:EquivalentNetwork cim:ControlArea cim:TieFlow cim:CogenerationPlant cim:EquivalentInjection cim:DisconnectingCircuitBreaker cim:DCBusbar cim:Equipment]` 

