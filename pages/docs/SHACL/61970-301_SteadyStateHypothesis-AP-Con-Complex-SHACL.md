# 61970-301_SteadyStateHypothesis-AP-Con-Complex-SHACL

## ssh:ActivePowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ActivePowerLimit

**Nested Properties:**

### ssh:ActivePowerLimit.value-valueRange

**Path:** `cim:ActivePowerLimit.value`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ApparentPowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ApparentPowerLimit

**Nested Properties:**

### ssh:ApparentPowerLimit.value-valueRange

**Path:** `cim:ApparentPowerLimit.value`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

**Nested Properties:**

### ssh:BatteryUnit.storedE-valueRange

**Path:** `cim:BatteryUnit.storedE`  
The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ControlArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ControlArea

**Nested Properties:**

### ssh:ControlArea.pTolerance-valueRange

**Path:** `cim:ControlArea.pTolerance`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### ssh:ACDCConverter.targetUdc-valueRange

**Path:** `cim:ACDCConverter.targetUdc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetAlpha-valueRange

**Path:** `cim:CsConverter.targetAlpha`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetGamma-valueRange

**Path:** `cim:CsConverter.targetGamma`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:CsConverter.targetIdc-valueRange

**Path:** `cim:CsConverter.targetIdc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:CurrentLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurrentLimit

**Nested Properties:**

### ssh:CurrentLimit.value-valueRange

**Path:** `cim:CurrentLimit.value`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:EnergySource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergySource

**Nested Properties:**

### ssh:EnergySource.voltageAngle-valueRange

**Path:** `cim:EnergySource.voltageAngle`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:EnergySource.voltageMagnitude-valueRange

**Path:** `cim:EnergySource.voltageMagnitude`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### ssh:EquivalentInjection.regulationTarget-valueRange

**Path:** `cim:EquivalentInjection.regulationTarget`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### ssh:ShuntCompensator.sections-valueRange

**Path:** `cim:ShuntCompensator.sections`  
The attribute shall be a positive value or zero. 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### ssh:ShuntCompensator.sections-valueRange

**Path:** `cim:ShuntCompensator.sections`  
The attribute shall be a positive value or zero. 

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-valueRange

**Path:** `cim:RegulatingControl.targetDeadband`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-valueRange

**Path:** `cim:RegulatingControl.targetDeadband`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:VoltageLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageLimit

**Nested Properties:**

### ssh:VoltageLimit.value-valueRange

**Path:** `cim:VoltageLimit.value`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### ssh:ACDCConverter.targetUdc-valueRange

**Path:** `cim:ACDCConverter.targetUdc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.droop-valueRange

**Path:** `cim:VsConverter.droop`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.droopCompensation-valueRange

**Path:** `cim:VsConverter.droopCompensation`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.qShare-valueRange

**Path:** `cim:VsConverter.qShare`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPWMfactor-valueRange

**Path:** `cim:VsConverter.targetPWMfactor`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPhasePcc-valueRange

**Path:** `cim:VsConverter.targetPhasePcc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetPowerFactorPcc-valueRange

**Path:** `cim:VsConverter.targetPowerFactorPcc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh:VsConverter.targetUpcc-valueRange

**Path:** `cim:VsConverter.targetUpcc`  
The attribute shall be a positive value.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### ssh:GeneratingUnit.normalPF-valueRange

**Path:** `cim:GeneratingUnit.normalPF`  
The attribute shall be a positive value or zero.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

