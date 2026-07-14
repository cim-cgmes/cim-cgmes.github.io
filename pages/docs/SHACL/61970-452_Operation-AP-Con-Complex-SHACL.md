# 61970-452_Operation-AP-Con-Complex-SHACL

## op452c:Accumulator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Accumulator

**Nested Properties:**

### op452c:Accumulator-accumulatorValues

**Path:** `cim:Measurement.measurementType`  
**Name:** C:452:OP:Measurement.measurementType:accumulatorValues  
For Accumulator, Measurement.measurementType is restricted to the following valid values: ApparentEnergy, ReactiveEnergy, ActiveEnergy.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[ApparentEnergy ReactiveEnergy ActiveEnergy]` 

### op452c:Accumulator-accumulatorUnitValues

**Path:** `cim:Measurement.unitSymbol`  
**Name:** C:452:OP:Measurement.unitSymbol:accumulatorValues  
For Accumulator, Measurement.unitSymbol is restricted to the following valid values: VAh, VArh, Wh.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.VAh cim:UnitSymbol.VArh cim:UnitSymbol.Wh]` 

## op452c:Analog

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Analog

**Nested Properties:**

### op452c:Analog-analogValues

**Path:** `cim:Measurement.measurementType`  
**Name:** C:452:OP:Measurement.measurementType:analogValues  
For Analog, Measurement.measurementType is restricted to the following valid values: ThreePhasePower, ThreePhaseActivePower, ThreePhaseReactivePower, LineCurrent, PhaseVoltage, Voltage, Angle, Frequency and TapPosition.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[ThreePhasePower ThreePhaseActivePower ThreePhaseReactivePower LineCurrent PhaseVoltage Voltage Angle Frequency TapPosition]` 

### op452c:Analog-analogUnitValues

**Path:** `cim:Measurement.unitSymbol`  
**Name:** C:452:OP:Measurement.unitSymbol:analogValues  
For Analog, Measurement.unitSymbol is restricted to the following valid values: W, deg, VA, A, VAr, V, Hz.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.W cim:UnitSymbol.deg cim:UnitSymbol.VA cim:UnitSymbol.A cim:UnitSymbol.VAr cim:UnitSymbol.V cim:UnitSymbol.Hz]` 

## op452c:Discrete

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Discrete

**Nested Properties:**

### op452c:Discrete-discreteValues

**Path:** `cim:Measurement.measurementType`  
**Name:** C:452:OP:Measurement.measurementType:discreteValues  
For Discrete, Measurement.measurementType is restricted to the following valid values: SwitchPosition.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[SwitchPosition]` 

### op452c:Discrete-discreteUnitValues

**Path:** `cim:Measurement.unitSymbol`  
**Name:** C:452:OP:Measurement.unitSymbol:discreteValues  
For Discrete, Measurement.unitSymbol is restricted to the following valid values: none.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.none]` 

## op452c:MeasurementValueSource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MeasurementValueSource

**Nested Properties:**

### op452c:MeasurementValueSource-name

**Path:** `cim:IdentifiedObject.name`  
**Name:** C:452:OP:MeasurementValueSource:name  
For MeasurementValueSource, attribute IdentifiedObject.name is restricted to the following strings for MeasurementValueSource: ICCP, SCADA.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[ICCP SCADA]` 

