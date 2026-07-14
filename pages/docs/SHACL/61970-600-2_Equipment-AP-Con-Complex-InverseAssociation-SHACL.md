# 61970-600-2_Equipment-AP-Con-Complex-InverseAssociation-SHACL

## eq301ia:BusNameMarker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BusNameMarker

**Nested Properties:**

### eq301ia:BusNameMarker.Terminal-cardinality

**Path:** `^cim:ACDCTerminal.BusNameMarker`  
**Name:** BusNameMarker.Terminal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:CAESPlant

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CAESPlant

**Nested Properties:**

### eq301ia:CAESPlant.ThermalGeneratingUnit-cardinality

**Path:** `^cim:ThermalGeneratingUnit.CAESPlant`  
**Name:** CAESPlant.ThermalGeneratingUnit-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq301ia:ConformLoadGroup

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoadGroup

**Nested Properties:**

### eq301ia:ConformLoadGroup.EnergyConsumers-cardinality

**Path:** `^cim:ConformLoad.LoadGroup`  
**Name:** ConformLoadGroup.EnergyConsumers-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:ConnectivityNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConnectivityNode

**Nested Properties:**

### eq301ia:ConnectivityNode.BoundaryPoint-cardinality

**Path:** `^cim100:BoundaryPoint.ConnectivityNode`  
**Name:** ConnectivityNode.BoundaryPoint-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq301ia:Curve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsCapabilityCurve
- targetClass: cim:GrossToNetActivePowerCurve
- targetClass: cim:ReactiveCapabilityCurve

**Nested Properties:**

### eq301ia:Curve.CurveDatas-cardinality

**Path:** `^cim:CurveData.Curve`  
**Name:** Curve.CurveDatas-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:EnergyArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadArea
- targetClass: cim:SubLoadArea

**Nested Properties:**

### eq301ia:EnergyArea.ControlArea-cardinality

**Path:** `^cim:ControlArea.EnergyArea`  
**Name:** EnergyArea.ControlArea-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq301ia:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### eq301ia:GeneratingUnit.RotatingMachine-cardinality

**Path:** `^cim:RotatingMachine.GeneratingUnit`  
**Name:** GeneratingUnit.RotatingMachine-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:LoadArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadArea

**Nested Properties:**

### eq301ia:LoadArea.SubLoadAreas-cardinality

**Path:** `^cim:SubLoadArea.LoadArea`  
**Name:** LoadArea.SubLoadAreas-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:NonConformLoadGroup

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonConformLoadGroup

**Nested Properties:**

### eq301ia:NonConformLoadGroup.EnergyConsumers-cardinality

**Path:** `^cim:NonConformLoad.LoadGroup`  
**Name:** NonConformLoadGroup.EnergyConsumers-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### eq301ia:NonlinearShuntCompensator.NonlinearShuntCompensatorPoints-cardinality

**Path:** `^cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator`  
**Name:** NonlinearShuntCompensator.NonlinearShuntCompensatorPoints-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:PhaseTapChangerTable

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTable

**Nested Properties:**

### eq301ia:PhaseTapChangerTable.PhaseTapChangerTablePoint-cardinality

**Path:** `^cim:PhaseTapChangerTablePoint.PhaseTapChangerTable`  
**Name:** PhaseTapChangerTable.PhaseTapChangerTablePoint-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:PowerElectronicsUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerElectronicsWindUnit
- targetClass: cim:PhotoVoltaicUnit
- targetClass: cim:BatteryUnit

**Nested Properties:**

### eq301ia:PowerElectronicsUnit.PowerElectronicsConnection-cardinality

**Path:** `^cim:PowerElectronicsConnection.PowerElectronicsUnit`  
**Name:** PowerElectronicsUnit.PowerElectronicsConnection-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq301ia:RatioTapChangerTable

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChangerTable

**Nested Properties:**

### eq301ia:RatioTapChangerTable.RatioTapChangerTablePoint-cardinality

**Path:** `^cim:RatioTapChangerTablePoint.RatioTapChangerTable`  
**Name:** RatioTapChangerTable.RatioTapChangerTablePoint-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:ReactiveCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ReactiveCapabilityCurve

**Nested Properties:**

### eq301ia:ReactiveCapabilityCurve.InitiallyUsedBySynchronousMachines-cardinality

**Path:** `^cim:SynchronousMachine.InitialReactiveCapabilityCurve`  
**Name:** ReactiveCapabilityCurve.InitiallyUsedBySynchronousMachines-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:RegularIntervalSchedule

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoadSchedule
- targetClass: cim:NonConformLoadSchedule
- targetClass: cim:RegulationSchedule
- targetClass: cim:SwitchSchedule
- targetClass: cim:TapSchedule

**Nested Properties:**

### eq301ia:RegularIntervalSchedule.TimePoints-cardinality

**Path:** `^cim:RegularTimePoint.IntervalSchedule`  
**Name:** RegularIntervalSchedule.TimePoints-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:RotatingMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### eq301ia:RotatingMachine.HydroPump-cardinality

**Path:** `^cim:HydroPump.RotatingMachine`  
**Name:** RotatingMachine.HydroPump-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## eq301ia:SubLoadArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SubLoadArea

**Nested Properties:**

### eq301ia:SubLoadArea.LoadGroups-cardinality

**Path:** `^cim:LoadGroup.SubLoadArea`  
**Name:** SubLoadArea.LoadGroups-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### eq301ia:TapChangerControl.TapChanger-cardinality

**Path:** `^cim:TapChanger.TapChangerControl`  
**Name:** TapChangerControl.TapChanger-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## eq301ia:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Terminal

**Nested Properties:**

### eq301ia:Terminal.TieFlow-cardinality

**Path:** `^cim:TieFlow.Terminal`  
**Name:** Terminal.TieFlow-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `2` 

## eq301ia:TransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### eq301ia:TransformerEnd.PhaseTapChanger-cardinality

**Path:** `^cim:PhaseTapChanger.TransformerEnd`  
**Name:** TransformerEnd.PhaseTapChanger-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### eq301ia:TransformerEnd.RatioTapChanger-cardinality

**Path:** `^cim:RatioTapChanger.TransformerEnd`  
**Name:** TransformerEnd.RatioTapChanger-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

