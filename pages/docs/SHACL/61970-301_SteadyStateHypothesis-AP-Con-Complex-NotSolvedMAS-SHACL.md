# 61970-301_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL

## ssh301n:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

**Nested Properties:**

### ssh301n:BatteryUnit.storedE-valueRangePair

**Path:** `cim:BatteryUnit.storedE`  
The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE.

**Severity:** sh:Violation

**Messages:**
- "The value is either greater than or equal to BatteryUnit.ratedE."

**Constraints:**

- **sh:LessThanConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:BatteryUnit.ratedE` 

## ssh301n:ControlArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ControlArea

## ssh301n:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### ssh301n:CsConverter.targetAlpha-valueRangePairTo

**Path:** `cim:CsConverter.targetAlpha`  
Allowed values are within the range minAlpha<=targetAlpha<=maxAlpha.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than CsConverter.maxAlpha."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:CsConverter.maxAlpha` 

### ssh301n:CsConverter.targetGamma-valueRangePairTo

**Path:** `cim:CsConverter.targetGamma`  
Allowed values are within the range minGamma<=targetGamma<=maxGamma. 

**Severity:** sh:Violation

**Messages:**
- "The value is greater than CsConverter.maxGamma."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:CsConverter.maxGamma` 

## ssh301n:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

## ssh301n:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

## ssh301n:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

**Nested Properties:**

### ssh301n:TapChanger.step-valueRangePairTo

**Path:** `cim:TapChanger.step`  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## ssh301n:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### ssh301n:TapChanger.step-valueRangePairTo

**Path:** `cim:TapChanger.step`  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## ssh301n:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### ssh301n:TapChanger.step-valueRangePairTo

**Path:** `cim:TapChanger.step`  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## ssh301n:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

**Nested Properties:**

### ssh301n:TapChanger.step-valueRangePairTo

**Path:** `cim:TapChanger.step`  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## ssh301n:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

**Nested Properties:**

### ssh301n:TapChanger.step-valueRangePairTo

**Path:** `cim:TapChanger.step`  
The attribute shall be equal to or greater than lowStep and equal to or less than highStep.

**Severity:** sh:Violation

**Messages:**
- "The value is greater than TapChanger.highStep."

**Constraints:**

- **sh:LessThanOrEqualsConstraintComponent** (Severity: sh:Violation)
  - Path: `cim:TapChanger.highStep` 

## ssh301n:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl
- targetClass: cim:TapChangerControl

## ssh301n:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:RatioTapChanger

