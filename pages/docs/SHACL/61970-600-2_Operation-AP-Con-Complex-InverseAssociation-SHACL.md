# 61970-600-2_Operation-AP-Con-Complex-InverseAssociation-SHACL

## op301ia:AccumulatorLimitSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorLimitSet

**Nested Properties:**

### op301ia:AccumulatorLimitSet.Limits-cardinality

**Path:** `^cim:AccumulatorLimit.LimitSet`  
**Name:** AccumulatorLimitSet.Limits-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

## op301ia:AccumulatorValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorValue

**Nested Properties:**

### op301ia:AccumulatorValue.AccumulatorReset-cardinality

**Path:** `^cim:AccumulatorReset.AccumulatorValue`  
**Name:** AccumulatorValue.AccumulatorReset-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op301ia:AnalogValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AnalogValue

**Nested Properties:**

### op301ia:AnalogValue.AnalogControl-cardinality

**Path:** `^cim:AnalogControl.AnalogValue`  
**Name:** AnalogValue.AnalogControl-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op301ia:DiscreteValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscreteValue

**Nested Properties:**

### op301ia:DiscreteValue.Command-cardinality

**Path:** `^cim:Command.DiscreteValue`  
**Name:** DiscreteValue.Command-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op301ia:MeasurementValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorValue
- targetClass: cim:AnalogValue
- targetClass: cim:DiscreteValue
- targetClass: cim:StringMeasurementValue

**Nested Properties:**

### op301ia:MeasurementValue.MeasurementValueQuality-cardinality

**Path:** `^cim:MeasurementValueQuality.MeasurementValue`  
**Name:** MeasurementValue.MeasurementValueQuality-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op301ia:ValueAliasSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ValueAliasSet

**Nested Properties:**

### op301ia:ValueAliasSet.Values-cardinality

**Path:** `^cim:ValueToAlias.ValueAliasSet`  
**Name:** ValueAliasSet.Values-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

