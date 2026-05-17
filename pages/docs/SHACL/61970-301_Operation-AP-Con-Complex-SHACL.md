# 61970-301_Operation-AP-Con-Complex-SHACL

## op:AccumulatorLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorLimit

**Nested Properties:**

### op:AccumulatorLimit.value-valueRange

**Path:** `cim:AccumulatorLimit.value`  
The value is positive.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## op:AccumulatorValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorValue

**Nested Properties:**

### op:AccumulatorValue.value-valueRange

**Path:** `cim:AccumulatorValue.value`  
The value is positive.

**Severity:** sh:Violation

**Messages:**
- "The value is negative or zero."

**Constraints:**

- **sh:MinExclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

