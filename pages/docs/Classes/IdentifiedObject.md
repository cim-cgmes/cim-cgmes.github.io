# IdentifiedObject

This is a root class to provide common identification for all classes needing identification and naming attributes.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- ReportingGroup
    ReportingGroup : +BusNameMarker BusNameMarker[0..n]
    ReportingGroup : +TopologicalNode TopologicalNode[0..n]
    click ReportingGroup href "ReportingGroup"
    IdentifiedObject <|-- CoordinateSystem
    CoordinateSystem : +Location Locations[0..n]
    CoordinateSystem : +String crsUrn[1..1]
    click CoordinateSystem href "CoordinateSystem"
    IdentifiedObject <|-- WindGenType3IEC
    WindGenType3IEC : +WindTurbineType3IEC WindTurbineType3IEC[0..1]
    WindGenType3IEC : +Float dipmax[1..1]
    WindGenType3IEC : +Float diqmax[1..1]
    WindGenType3IEC : +Float xs[1..1]
    click WindGenType3IEC href "WindGenType3IEC"
    IdentifiedObject <|-- OperationalLimitSet
    OperationalLimitSet : +Equipment Equipment[0..1]
    OperationalLimitSet : +OperationalLimit OperationalLimitValue[0..n]
    OperationalLimitSet : +ACDCTerminal Terminal[1]
    click OperationalLimitSet href "OperationalLimitSet"
    IdentifiedObject <|-- BasicIntervalSchedule
    BasicIntervalSchedule : +DateTime startTime[1..1]
    BasicIntervalSchedule : +UnitSymbol value1Unit[1..1]
    BasicIntervalSchedule : +UnitSymbol value2Unit[0..1]
    click BasicIntervalSchedule href "BasicIntervalSchedule"
    IdentifiedObject <|-- ACDCTerminal
    ACDCTerminal : +BusNameMarker BusNameMarker[0..1]
    ACDCTerminal : +Measurement Measurements[0..n]
    ACDCTerminal : +OperationalLimitSet OperationalLimitSet[0..n]
    ACDCTerminal : +Boolean connected[1..1]
    ACDCTerminal : +Integer sequenceNumber[1..1]
    click ACDCTerminal href "ACDCTerminal"
    IdentifiedObject <|-- TieFlow
    TieFlow : +ControlArea ControlArea[1]
    TieFlow : +Terminal Terminal[1]
    TieFlow : +Boolean positiveFlowIn[1..1]
    click TieFlow href "TieFlow"
    IdentifiedObject <|-- DiagramStyle
    DiagramStyle : +Diagram Diagram[0..n]
    click DiagramStyle href "DiagramStyle"
    IdentifiedObject <|-- DayType
    DayType : +SeasonDayTypeSchedule SeasonDayTypeSchedules[0..n]
    click DayType href "DayType"
    IdentifiedObject <|-- ConnectivityNode
    ConnectivityNode : +BoundaryPoint BoundaryPoint[0..1]
    ConnectivityNode : +ConnectivityNodeContainer ConnectivityNodeContainer[1]
    ConnectivityNode : +Terminal Terminals[0..n]
    ConnectivityNode : +TopologicalNode TopologicalNode[1]
    click ConnectivityNode href "ConnectivityNode"
    IdentifiedObject <|-- RatioTapChangerTable
    RatioTapChangerTable : +RatioTapChanger RatioTapChanger[0..n]
    RatioTapChangerTable : +RatioTapChangerTablePoint RatioTapChangerTablePoint[1..n]
    click RatioTapChangerTable href "RatioTapChangerTable"
    IdentifiedObject <|-- WindPitchContPowerIEC
    WindPitchContPowerIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindPitchContPowerIEC : +WindGenTurbineType1bIEC WindGenTurbineType1bIEC[0..1]
    WindPitchContPowerIEC : +WindGenTurbineType2IEC WindGenTurbineType2IEC[0..1]
    WindPitchContPowerIEC : +Float dpmax[1..1]
    WindPitchContPowerIEC : +Float dpmin[1..1]
    WindPitchContPowerIEC : +Float pmin[1..1]
    WindPitchContPowerIEC : +Float pset[1..1]
    WindPitchContPowerIEC : +Float t1[1..1]
    WindPitchContPowerIEC : +Float tr[1..1]
    WindPitchContPowerIEC : +Float uuvrt[1..1]
    click WindPitchContPowerIEC href "WindPitchContPowerIEC"
    IdentifiedObject <|-- WindProtectionIEC
    WindProtectionIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindProtectionIEC : +WindTurbineType1or2IEC WindTurbineType1or2IEC[0..1]
    WindProtectionIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[0..1]
    WindProtectionIEC : +Float dfimax[1..1]
    WindProtectionIEC : +Float fover[1..1]
    WindProtectionIEC : +Float funder[1..1]
    WindProtectionIEC : +Boolean mzc[1..1]
    WindProtectionIEC : +Float tfma[1..1]
    WindProtectionIEC : +Float uover[1..1]
    WindProtectionIEC : +Float uunder[1..1]
    click WindProtectionIEC href "WindProtectionIEC"
    IdentifiedObject <|-- GenICompensationForGenJ
    GenICompensationForGenJ : +SynchronousMachineDynamics SynchronousMachineDynamics[1]
    GenICompensationForGenJ : +VCompIEEEType2 VcompIEEEType2[1]
    GenICompensationForGenJ : +Float rcij[1..1]
    GenICompensationForGenJ : +Float xcij[1..1]
    click GenICompensationForGenJ href "GenICompensationForGenJ"
    IdentifiedObject <|-- DiagramObject
    DiagramObject : +Diagram Diagram[1]
    DiagramObject : +DiagramObjectPoint DiagramObjectPoints[0..n]
    DiagramObject : +DiagramObjectStyle DiagramObjectStyle[0..1]
    DiagramObject : +IdentifiedObject IdentifiedObject_[0..1]
    DiagramObject : +VisibilityLayer VisibilityLayers[0..n]
    DiagramObject : +Integer drawingOrder[0..1]
    DiagramObject : +Boolean isPolygon[0..1]
    DiagramObject : +Float offsetX[0..1]
    DiagramObject : +Float offsetY[0..1]
    DiagramObject : +Float rotation[0..1]
    click DiagramObject href "DiagramObject"
    IdentifiedObject <|-- WindContPitchAngleIEC
    WindContPitchAngleIEC : +WindTurbineType3IEC WindTurbineType3IEC[1]
    WindContPitchAngleIEC : +Float dthetamax[1..1]
    WindContPitchAngleIEC : +Float dthetamin[1..1]
    WindContPitchAngleIEC : +Float kic[1..1]
    WindContPitchAngleIEC : +Float kiomega[1..1]
    WindContPitchAngleIEC : +Float kpc[1..1]
    WindContPitchAngleIEC : +Float kpomega[1..1]
    WindContPitchAngleIEC : +Float kpx[1..1]
    WindContPitchAngleIEC : +Float thetamax[1..1]
    WindContPitchAngleIEC : +Float thetamin[1..1]
    WindContPitchAngleIEC : +Float ttheta[1..1]
    click WindContPitchAngleIEC href "WindContPitchAngleIEC"
    IdentifiedObject <|-- WindContPType3IEC
    WindContPType3IEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindContPType3IEC : +WindTurbineType3IEC WindTurbineType3IEC[1]
    WindContPType3IEC : +Float dpmax[1..1]
    WindContPType3IEC : +Float dprefmax[1..1]
    WindContPType3IEC : +Float dprefmin[1..1]
    WindContPType3IEC : +Float dthetamax[1..1]
    WindContPType3IEC : +Float dthetamaxuvrt[1..1]
    WindContPType3IEC : +Float kdtd[1..1]
    WindContPType3IEC : +Float kip[1..1]
    WindContPType3IEC : +Float kpp[1..1]
    WindContPType3IEC : +Boolean mpuvrt[1..1]
    WindContPType3IEC : +Float omegadtd[1..1]
    WindContPType3IEC : +Float omegaoffset[1..1]
    WindContPType3IEC : +Float pdtdmax[1..1]
    WindContPType3IEC : +Float tdvs[1..1]
    WindContPType3IEC : +Float thetaemin[1..1]
    WindContPType3IEC : +Float thetauscale[1..1]
    WindContPType3IEC : +Float tomegafiltp3[1..1]
    WindContPType3IEC : +Float tomegaref[1..1]
    WindContPType3IEC : +Float tpfiltp3[1..1]
    WindContPType3IEC : +Float tpord[1..1]
    WindContPType3IEC : +Float tufiltp3[1..1]
    WindContPType3IEC : +Float udvs[1..1]
    WindContPType3IEC : +Float updip[1..1]
    WindContPType3IEC : +Float zeta[1..1]
    click WindContPType3IEC href "WindContPType3IEC"
    IdentifiedObject <|-- WindContQPQULimIEC
    WindContQPQULimIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindContQPQULimIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[0..1]
    WindContQPQULimIEC : +Float tpfiltql[1..1]
    WindContQPQULimIEC : +Float tufiltql[1..1]
    click WindContQPQULimIEC href "WindContQPQULimIEC"
    IdentifiedObject <|-- LoadDynamics
    LoadDynamics : +EnergyConsumer EnergyConsumer[0..n]
    click LoadDynamics href "LoadDynamics"
    IdentifiedObject <|-- WindContPType4aIEC
    WindContPType4aIEC : +WindTurbineType4aIEC WindTurbineType4aIEC[1]
    WindContPType4aIEC : +Float dpmaxp4a[1..1]
    WindContPType4aIEC : +Float tpordp4a[1..1]
    WindContPType4aIEC : +Float tufiltp4a[1..1]
    click WindContPType4aIEC href "WindContPType4aIEC"
    IdentifiedObject <|-- FossilFuel
    FossilFuel : +ThermalGeneratingUnit ThermalGeneratingUnit[1]
    FossilFuel : +FuelType fossilFuelType[1..1]
    click FossilFuel href "FossilFuel"
    IdentifiedObject <|-- Diagram
    Diagram : +DiagramObject DiagramElements[0..n]
    Diagram : +DiagramStyle DiagramStyle[0..1]
    Diagram : +OrientationKind orientation[1..1]
    Diagram : +Float x1InitialView[0..1]
    Diagram : +Float x2InitialView[0..1]
    Diagram : +Float y1InitialView[0..1]
    Diagram : +Float y2InitialView[0..1]
    click Diagram href "Diagram"
    IdentifiedObject <|-- LoadStatic
    LoadStatic : +LoadAggregate LoadAggregate[1]
    LoadStatic : +Float ep1[0..1]
    LoadStatic : +Float ep2[0..1]
    LoadStatic : +Float ep3[0..1]
    LoadStatic : +Float eq1[0..1]
    LoadStatic : +Float eq2[0..1]
    LoadStatic : +Float eq3[0..1]
    LoadStatic : +Float kp1[0..1]
    LoadStatic : +Float kp2[0..1]
    LoadStatic : +Float kp3[0..1]
    LoadStatic : +Float kp4[0..1]
    LoadStatic : +Float kpf[0..1]
    LoadStatic : +Float kq1[0..1]
    LoadStatic : +Float kq2[0..1]
    LoadStatic : +Float kq3[0..1]
    LoadStatic : +Float kq4[0..1]
    LoadStatic : +Float kqf[0..1]
    LoadStatic : +StaticLoadModelKind staticLoadModelType[1..1]
    click LoadStatic href "LoadStatic"
    IdentifiedObject <|-- WindContPType4bIEC
    WindContPType4bIEC : +WindTurbineType4bIEC WindTurbineType4bIEC[1]
    WindContPType4bIEC : +Float dpmaxp4b[1..1]
    WindContPType4bIEC : +Float tpaero[1..1]
    WindContPType4bIEC : +Float tpordp4b[1..1]
    WindContPType4bIEC : +Float tufiltp4b[1..1]
    click WindContPType4bIEC href "WindContPType4bIEC"
    IdentifiedObject <|-- Limit
    click Limit href "Limit"
    IdentifiedObject <|-- Season
    Season : +SeasonDayTypeSchedule SeasonDayTypeSchedules[0..n]
    Season : +MonthDay endDate[1..1]
    Season : +MonthDay startDate[1..1]
    click Season href "Season"
    IdentifiedObject <|-- DCNode
    DCNode : +DCEquipmentContainer DCEquipmentContainer[1]
    DCNode : +DCBaseTerminal DCTerminals[0..n]
    DCNode : +DCTopologicalNode DCTopologicalNode[1]
    click DCNode href "DCNode"
    IdentifiedObject <|-- DynamicsFunctionBlock
    DynamicsFunctionBlock : +Boolean enabled[1..1]
    click DynamicsFunctionBlock href "DynamicsFunctionBlock"
    IdentifiedObject <|-- Location
    Location : +CoordinateSystem CoordinateSystem[1]
    Location : +PositionPoint PositionPoints[0..n]
    Location : +PowerSystemResource PowerSystemResources[1]
    Location : +StreetAddress mainAddress[0..1]
    click Location href "Location"
    IdentifiedObject <|-- Measurement
    Measurement : +PowerSystemResource PowerSystemResource[1..1]
    Measurement : +ACDCTerminal Terminal[0..1]
    Measurement : +String measurementType[1..1]
    Measurement : +PhaseCode phases[0..1]
    Measurement : +UnitMultiplier unitMultiplier[1..1]
    Measurement : +UnitSymbol unitSymbol[1..1]
    click Measurement href "Measurement"
    IdentifiedObject <|-- DCTopologicalIsland
    DCTopologicalIsland : +DCTopologicalNode DCTopologicalNodes[1..n]
    click DCTopologicalIsland href "DCTopologicalIsland"
    IdentifiedObject <|-- ValueToAlias
    ValueToAlias : +ValueAliasSet ValueAliasSet[1]
    ValueToAlias : +Integer value[1..1]
    click ValueToAlias href "ValueToAlias"
    IdentifiedObject <|-- WindContRotorRIEC
    WindContRotorRIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindContRotorRIEC : +WindGenTurbineType2IEC WindGenTurbineType2IEC[1]
    WindContRotorRIEC : +Float kirr[1..1]
    WindContRotorRIEC : +Float komegafilt[1..1]
    WindContRotorRIEC : +Float kpfilt[1..1]
    WindContRotorRIEC : +Float kprr[1..1]
    WindContRotorRIEC : +Float rmax[1..1]
    WindContRotorRIEC : +Float rmin[1..1]
    WindContRotorRIEC : +Float tomegafiltrr[1..1]
    WindContRotorRIEC : +Float tpfiltrr[1..1]
    click WindContRotorRIEC href "WindContRotorRIEC"
    IdentifiedObject <|-- ValueAliasSet
    ValueAliasSet : +Command Commands[0..n]
    ValueAliasSet : +Discrete Discretes[0..n]
    ValueAliasSet : +RaiseLowerCommand RaiseLowerCommands[0..n]
    ValueAliasSet : +ValueToAlias Values[1..n]
    click ValueAliasSet href "ValueAliasSet"
    IdentifiedObject <|-- WindContQLimIEC
    WindContQLimIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[0..1]
    WindContQLimIEC : +Float qmax[1..1]
    WindContQLimIEC : +Float qmin[1..1]
    click WindContQLimIEC href "WindContQLimIEC"
    IdentifiedObject <|-- TopologicalIsland
    TopologicalIsland : +TopologicalNode AngleRefTopologicalNode[1]
    TopologicalIsland : +TopologicalNode TopologicalNodes[1..n]
    click TopologicalIsland href "TopologicalIsland"
    IdentifiedObject <|-- LoadResponseCharacteristic
    LoadResponseCharacteristic : +EnergyConsumer EnergyConsumer[0..n]
    LoadResponseCharacteristic : +Boolean exponentModel[1..1]
    LoadResponseCharacteristic : +Float pConstantCurrent[0..1]
    LoadResponseCharacteristic : +Float pConstantImpedance[0..1]
    LoadResponseCharacteristic : +Float pConstantPower[0..1]
    LoadResponseCharacteristic : +Float pFrequencyExponent[0..1]
    LoadResponseCharacteristic : +Float pVoltageExponent[0..1]
    LoadResponseCharacteristic : +Float qConstantCurrent[0..1]
    LoadResponseCharacteristic : +Float qConstantImpedance[0..1]
    LoadResponseCharacteristic : +Float qConstantPower[0..1]
    LoadResponseCharacteristic : +Float qFrequencyExponent[0..1]
    LoadResponseCharacteristic : +Float qVoltageExponent[0..1]
    click LoadResponseCharacteristic href "LoadResponseCharacteristic"
    IdentifiedObject <|-- MeasurementValueSource
    MeasurementValueSource : +MeasurementValue MeasurementValues[0..n]
    click MeasurementValueSource href "MeasurementValueSource"
    IdentifiedObject <|-- TopologicalNode
    TopologicalNode : +TopologicalIsland AngleRefTopologicalIsland[0..1]
    TopologicalNode : +BaseVoltage BaseVoltage[1..1]
    TopologicalNode : +ConnectivityNodeContainer ConnectivityNodeContainer[1]
    TopologicalNode : +ConnectivityNode ConnectivityNodes[0..n]
    TopologicalNode : +ReportingGroup ReportingGroup[0..1]
    TopologicalNode : +SvInjection SvInjection[0..1]
    TopologicalNode : +SvVoltage SvVoltage[0..1]
    TopologicalNode : +Terminal Terminal[1..n]
    TopologicalNode : +TopologicalIsland TopologicalIsland[0..1]
    click TopologicalNode href "TopologicalNode"
    IdentifiedObject <|-- BusNameMarker
    BusNameMarker : +ReportingGroup ReportingGroup[0..1]
    BusNameMarker : +ACDCTerminal Terminal[1..n]
    BusNameMarker : +Integer priority[0..1]
    click BusNameMarker href "BusNameMarker"
    IdentifiedObject <|-- PowerSystemResource
    PowerSystemResource : +Control Controls[0..n]
    PowerSystemResource : +Location Location[0..1]
    PowerSystemResource : +Measurement Measurements[0..n]
    click PowerSystemResource href "PowerSystemResource"
    IdentifiedObject <|-- WindDynamicsLookupTable
    WindDynamicsLookupTable : +WindContCurrLimIEC WindContCurrLimIEC[0..1]
    WindDynamicsLookupTable : +WindContPType3IEC WindContPType3IEC[0..1]
    WindDynamicsLookupTable : +WindContQPQULimIEC WindContQPQULimIEC[0..1]
    WindDynamicsLookupTable : +WindContRotorRIEC WindContRotorRIEC[0..1]
    WindDynamicsLookupTable : +WindGenType3bIEC WindGenType3bIEC[0..1]
    WindDynamicsLookupTable : +WindPitchContPowerIEC WindPitchContPowerIEC[0..1]
    WindDynamicsLookupTable : +WindPlantFreqPcontrolIEC WindPlantFreqPcontrolIEC[0..1]
    WindDynamicsLookupTable : +WindPlantReactiveControlIEC WindPlantReactiveControlIEC[0..1]
    WindDynamicsLookupTable : +WindProtectionIEC WindProtectionIEC[0..1]
    WindDynamicsLookupTable : +Float input[1..1]
    WindDynamicsLookupTable : +WindLookupTableFunctionKind lookupTableFunctionType[1..1]
    WindDynamicsLookupTable : +Float output[1..1]
    WindDynamicsLookupTable : +Integer sequence[1..1]
    click WindDynamicsLookupTable href "WindDynamicsLookupTable"
    IdentifiedObject <|-- EnergySchedulingType
    EnergySchedulingType : +EnergySource EnergySource[0..n]
    click EnergySchedulingType href "EnergySchedulingType"
    IdentifiedObject <|-- DiagramObjectStyle
    DiagramObjectStyle : +DiagramObject StyledObjects[0..n]
    click DiagramObjectStyle href "DiagramObjectStyle"
    IdentifiedObject <|-- Curve
    Curve : +CurveData CurveDatas[1..n]
    Curve : +CurveStyle curveStyle[1..1]
    Curve : +UnitSymbol xUnit[1..1]
    Curve : +UnitSymbol y1Unit[1..1]
    Curve : +UnitSymbol y2Unit[0..1]
    click Curve href "Curve"
    IdentifiedObject <|-- WindRefFrameRotIEC
    WindRefFrameRotIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[1]
    WindRefFrameRotIEC : +Float tpll[1..1]
    WindRefFrameRotIEC : +Float upll1[1..1]
    WindRefFrameRotIEC : +Float upll2[1..1]
    click WindRefFrameRotIEC href "WindRefFrameRotIEC"
    IdentifiedObject <|-- WindGenType4IEC
    WindGenType4IEC : +WindTurbineType4aIEC WindTurbineType4aIEC[0..1]
    WindGenType4IEC : +WindTurbineType4bIEC WindTurbineType4bIEC[0..1]
    WindGenType4IEC : +Float dipmax[1..1]
    WindGenType4IEC : +Float diqmax[1..1]
    WindGenType4IEC : +Float diqmin[1..1]
    WindGenType4IEC : +Float tg[1..1]
    click WindGenType4IEC href "WindGenType4IEC"
    IdentifiedObject <|-- GeographicalRegion
    GeographicalRegion : +SubGeographicalRegion Regions[0..n]
    click GeographicalRegion href "GeographicalRegion"
    IdentifiedObject <|-- WindAeroTwoDimIEC
    WindAeroTwoDimIEC : +WindTurbineType3IEC WindTurbineType3IEC[1]
    WindAeroTwoDimIEC : +Float dpomega[1..1]
    WindAeroTwoDimIEC : +Float dptheta[1..1]
    WindAeroTwoDimIEC : +Float dpv1[1..1]
    WindAeroTwoDimIEC : +Float omegazero[1..1]
    WindAeroTwoDimIEC : +Float pavail[1..1]
    WindAeroTwoDimIEC : +Float thetav2[1..1]
    WindAeroTwoDimIEC : +Float thetazero[1..1]
    click WindAeroTwoDimIEC href "WindAeroTwoDimIEC"
    IdentifiedObject <|-- LoadGroup
    LoadGroup : +SubLoadArea SubLoadArea[1]
    click LoadGroup href "LoadGroup"
    IdentifiedObject <|-- WindPlantReactiveControlIEC
    WindPlantReactiveControlIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindPlantReactiveControlIEC : +WindPlantIEC WindPlantIEC[1]
    WindPlantReactiveControlIEC : +Float dxrefmax[1..1]
    WindPlantReactiveControlIEC : +Float dxrefmin[1..1]
    WindPlantReactiveControlIEC : +Float kiwpx[1..1]
    WindPlantReactiveControlIEC : +Float kiwpxmax[1..1]
    WindPlantReactiveControlIEC : +Float kiwpxmin[1..1]
    WindPlantReactiveControlIEC : +Float kpwpx[1..1]
    WindPlantReactiveControlIEC : +Float kwpqref[1..1]
    WindPlantReactiveControlIEC : +Float kwpqu[1..1]
    WindPlantReactiveControlIEC : +Float tuqfilt[1..1]
    WindPlantReactiveControlIEC : +Float twppfiltq[1..1]
    WindPlantReactiveControlIEC : +Float twpqfiltq[1..1]
    WindPlantReactiveControlIEC : +Float twpufiltq[1..1]
    WindPlantReactiveControlIEC : +Float txft[1..1]
    WindPlantReactiveControlIEC : +Float txfv[1..1]
    WindPlantReactiveControlIEC : +Float uwpqdip[1..1]
    WindPlantReactiveControlIEC : +WindPlantQcontrolModeKind windPlantQcontrolModesType[1..1]
    WindPlantReactiveControlIEC : +Float xrefmax[1..1]
    WindPlantReactiveControlIEC : +Float xrefmin[1..1]
    click WindPlantReactiveControlIEC href "WindPlantReactiveControlIEC"
    IdentifiedObject <|-- SubGeographicalRegion
    SubGeographicalRegion : +DCLine DCLines[0..n]
    SubGeographicalRegion : +Line Lines[0..n]
    SubGeographicalRegion : +GeographicalRegion Region[1]
    SubGeographicalRegion : +Substation Substations[0..n]
    click SubGeographicalRegion href "SubGeographicalRegion"
    IdentifiedObject <|-- OperationalLimit
    OperationalLimit : +OperationalLimitSet OperationalLimitSet[1]
    OperationalLimit : +OperationalLimitType OperationalLimitType[1..1]
    click OperationalLimit href "OperationalLimit"
    IdentifiedObject <|-- DCTopologicalNode
    DCTopologicalNode : +DCEquipmentContainer DCEquipmentContainer[1]
    DCTopologicalNode : +DCNode DCNodes[0..n]
    DCTopologicalNode : +DCBaseTerminal DCTerminals[0..n]
    DCTopologicalNode : +DCTopologicalIsland DCTopologicalIsland[0..1]
    click DCTopologicalNode href "DCTopologicalNode"
    IdentifiedObject <|-- RemoteInputSignal
    RemoteInputSignal : +DiscontinuousExcitationControlDynamics DiscontinuousExcitationControlDynamics[0..1]
    RemoteInputSignal : +PFVArControllerType1Dynamics PFVArControllerType1Dynamics[0..1]
    RemoteInputSignal : +PowerSystemStabilizerDynamics PowerSystemStabilizerDynamics[0..1]
    RemoteInputSignal : +Terminal Terminal[1]
    RemoteInputSignal : +UnderexcitationLimiterDynamics UnderexcitationLimiterDynamics[0..1]
    RemoteInputSignal : +VoltageCompensatorDynamics VoltageCompensatorDynamics[0..1]
    RemoteInputSignal : +WindPlantDynamics WindPlantDynamics[0..1]
    RemoteInputSignal : +WindTurbineType1or2Dynamics WindTurbineType1or2Dynamics[0..1]
    RemoteInputSignal : +WindTurbineType3or4Dynamics WindTurbineType3or4Dynamics[0..1]
    RemoteInputSignal : +RemoteSignalKind remoteSignalType[1..1]
    click RemoteInputSignal href "RemoteInputSignal"
    IdentifiedObject <|-- TransformerEnd
    TransformerEnd : +BaseVoltage BaseVoltage[1]
    TransformerEnd : +PhaseTapChanger PhaseTapChanger[0..1]
    TransformerEnd : +RatioTapChanger RatioTapChanger[0..1]
    TransformerEnd : +Terminal Terminal[1..1]
    TransformerEnd : +Integer endNumber[1..1]
    TransformerEnd : +Boolean grounded[1..1]
    TransformerEnd : +Float rground[0..1]
    TransformerEnd : +Float xground[0..1]
    click TransformerEnd href "TransformerEnd"
    IdentifiedObject <|-- EnergyArea
    EnergyArea : +ControlArea ControlArea[0..1]
    click EnergyArea href "EnergyArea"
    IdentifiedObject <|-- IOPoint
    click IOPoint href "IOPoint"
    IdentifiedObject <|-- VisibilityLayer
    VisibilityLayer : +DiagramObject VisibleObjects[1..n]
    VisibilityLayer : +Integer drawingOrder[0..1]
    click VisibilityLayer href "VisibilityLayer"
    IdentifiedObject <|-- WindMechIEC
    WindMechIEC : +WindTurbineType1or2IEC WindTurbineType1or2IEC[0..1]
    WindMechIEC : +WindTurbineType3IEC WindTurbineType3IEC[0..1]
    WindMechIEC : +WindTurbineType4bIEC WindTurbineType4bIEC[0..1]
    WindMechIEC : +Float cdrt[1..1]
    WindMechIEC : +Float hgen[1..1]
    WindMechIEC : +Float hwtr[1..1]
    WindMechIEC : +Float kdrt[1..1]
    click WindMechIEC href "WindMechIEC"
    IdentifiedObject <|-- PhaseTapChangerTable
    PhaseTapChangerTable : +PhaseTapChangerTablePoint PhaseTapChangerTablePoint[1..n]
    PhaseTapChangerTable : +PhaseTapChangerTabular PhaseTapChangerTabular[0..n]
    click PhaseTapChangerTable href "PhaseTapChangerTable"
    IdentifiedObject <|-- BaseVoltage
    BaseVoltage : +ConductingEquipment ConductingEquipment[0..n]
    BaseVoltage : +TopologicalNode TopologicalNode[0..n]
    BaseVoltage : +TransformerEnd TransformerEnds[0..n]
    BaseVoltage : +VoltageLevel VoltageLevel[0..n]
    BaseVoltage : +Float nominalVoltage[1..1]
    click BaseVoltage href "BaseVoltage"
    IdentifiedObject <|-- LimitSet
    LimitSet : +Boolean isPercentageLimits[0..1]
    click LimitSet href "LimitSet"
    IdentifiedObject <|-- WindAeroConstIEC
    WindAeroConstIEC : +WindGenTurbineType1aIEC WindGenTurbineType1aIEC[1]
    click WindAeroConstIEC href "WindAeroConstIEC"
    IdentifiedObject <|-- WindPlantFreqPcontrolIEC
    WindPlantFreqPcontrolIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindPlantFreqPcontrolIEC : +WindPlantIEC WindPlantIEC[1]
    WindPlantFreqPcontrolIEC : +Float dprefmax[1..1]
    WindPlantFreqPcontrolIEC : +Float dprefmin[1..1]
    WindPlantFreqPcontrolIEC : +Float dpwprefmax[1..1]
    WindPlantFreqPcontrolIEC : +Float dpwprefmin[1..1]
    WindPlantFreqPcontrolIEC : +Float kiwpp[1..1]
    WindPlantFreqPcontrolIEC : +Float kiwppmax[1..1]
    WindPlantFreqPcontrolIEC : +Float kiwppmin[1..1]
    WindPlantFreqPcontrolIEC : +Float kpwpp[1..1]
    WindPlantFreqPcontrolIEC : +Float kwppref[1..1]
    WindPlantFreqPcontrolIEC : +Float prefmax[1..1]
    WindPlantFreqPcontrolIEC : +Float prefmin[1..1]
    WindPlantFreqPcontrolIEC : +Float tpft[1..1]
    WindPlantFreqPcontrolIEC : +Float tpfv[1..1]
    WindPlantFreqPcontrolIEC : +Float twpffiltp[1..1]
    WindPlantFreqPcontrolIEC : +Float twppfiltp[1..1]
    click WindPlantFreqPcontrolIEC href "WindPlantFreqPcontrolIEC"
    IdentifiedObject <|-- WindContCurrLimIEC
    WindContCurrLimIEC : +WindDynamicsLookupTable WindDynamicsLookupTable[1..n]
    WindContCurrLimIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[1]
    WindContCurrLimIEC : +Float imax[1..1]
    WindContCurrLimIEC : +Float imaxdip[1..1]
    WindContCurrLimIEC : +Float kpqu[1..1]
    WindContCurrLimIEC : +Boolean mdfslim[1..1]
    WindContCurrLimIEC : +Boolean mqpri[1..1]
    WindContCurrLimIEC : +Float tufiltcl[1..1]
    WindContCurrLimIEC : +Float upqumax[1..1]
    click WindContCurrLimIEC href "WindContCurrLimIEC"
    IdentifiedObject <|-- OperationalLimitType
    OperationalLimitType : +OperationalLimit OperationalLimit[0..n]
    OperationalLimitType : +Float acceptableDuration[0..1]
    OperationalLimitType : +OperationalLimitDirectionKind direction[1..1]
    OperationalLimitType : +Boolean isInfiniteDuration[1..1]
    OperationalLimitType : +LimitKind kind[1..1]
    click OperationalLimitType href "OperationalLimitType"
    IdentifiedObject <|-- ControlAreaGeneratingUnit
    ControlAreaGeneratingUnit : +ControlArea ControlArea[1]
    ControlAreaGeneratingUnit : +GeneratingUnit GeneratingUnit[1]
    click ControlAreaGeneratingUnit href "ControlAreaGeneratingUnit"
    IdentifiedObject <|-- WindAeroOneDimIEC
    WindAeroOneDimIEC : +WindTurbineType3IEC WindTurbineType3IEC[1]
    WindAeroOneDimIEC : +Float ka[1..1]
    WindAeroOneDimIEC : +Float thetaomega[1..1]
    click WindAeroOneDimIEC href "WindAeroOneDimIEC"
    IdentifiedObject <|-- MutualCoupling
    MutualCoupling : +Terminal First_Terminal[1]
    MutualCoupling : +Terminal Second_Terminal[1]
    MutualCoupling : +Float b0ch[1..1]
    MutualCoupling : +Float distance11[1..1]
    MutualCoupling : +Float distance12[1..1]
    MutualCoupling : +Float distance21[1..1]
    MutualCoupling : +Float distance22[1..1]
    MutualCoupling : +Float g0ch[1..1]
    MutualCoupling : +Float r0[1..1]
    MutualCoupling : +Float x0[1..1]
    click MutualCoupling href "MutualCoupling"
    IdentifiedObject <|-- WindContQIEC
    WindContQIEC : +WindTurbineType3or4IEC WindTurbineType3or4IEC[1]
    WindContQIEC : +Float iqh1[1..1]
    WindContQIEC : +Float iqmax[1..1]
    WindContQIEC : +Float iqmin[1..1]
    WindContQIEC : +Float iqpost[1..1]
    WindContQIEC : +Float kiq[1..1]
    WindContQIEC : +Float kiu[1..1]
    WindContQIEC : +Float kpq[1..1]
    WindContQIEC : +Float kpu[1..1]
    WindContQIEC : +Float kqv[1..1]
    WindContQIEC : +Float rdroop[1..1]
    WindContQIEC : +Float tpfiltq[1..1]
    WindContQIEC : +Float tpost[1..1]
    WindContQIEC : +Float tqord[1..1]
    WindContQIEC : +Float tufiltq[1..1]
    WindContQIEC : +Float udb1[1..1]
    WindContQIEC : +Float udb2[1..1]
    WindContQIEC : +Float umax[1..1]
    WindContQIEC : +Float umin[1..1]
    WindContQIEC : +Float uqdip[1..1]
    WindContQIEC : +Float uref0[1..1]
    WindContQIEC : +WindQcontrolModeKind windQcontrolModesType[1..1]
    WindContQIEC : +WindUVRTQcontrolModeKind windUVRTQcontrolModesType[1..1]
    WindContQIEC : +Float xdroop[1..1]
    click WindContQIEC href "WindContQIEC"
    IdentifiedObject <|-- LoadMotor
    LoadMotor : +LoadAggregate LoadAggregate[1]
    LoadMotor : +Float d[1..1]
    LoadMotor : +Float h[1..1]
    LoadMotor : +Float lfac[1..1]
    LoadMotor : +Float lp[1..1]
    LoadMotor : +Float lpp[1..1]
    LoadMotor : +Float ls[1..1]
    LoadMotor : +Float pfrac[1..1]
    LoadMotor : +Float ra[1..1]
    LoadMotor : +Float tbkr[1..1]
    LoadMotor : +Float tpo[1..1]
    LoadMotor : +Float tppo[1..1]
    LoadMotor : +Float tv[1..1]
    LoadMotor : +Float vt[1..1]
    click LoadMotor href "LoadMotor"
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| DiagramObjects | [DiagramObject](DiagramObject.md) | 0..n | The diagram objects that are associated with the domain object. |
| description | String | 0..1 | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. |
| energyIdentCodeEic | String | 0..1 | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. |
| mRID | String | 1..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. |
| name | String | 1..1 | The name is any free human readable and possibly non unique text naming the object. |
| shortName | String | 0..1 | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. |

