# 61970-456_SteadyStateHypothesis-AP-Con-Complex-SHACL

## ssh456c:ConformLoad

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoad

**Nested Properties:**

### ssh456c:EnergyConsumer.p-valueRange

**Path:** `cim:EnergyConsumer.p`  
Negative active power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh456c:EnergyConsumer.q-valueRange

**Path:** `cim:EnergyConsumer.q`  
Negative reactive power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh456c:EnergyConsumer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergyConsumer

**Nested Properties:**

### ssh456c:EnergyConsumer.p-valueRange

**Path:** `cim:EnergyConsumer.p`  
Negative active power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh456c:EnergyConsumer.q-valueRange

**Path:** `cim:EnergyConsumer.q`  
Negative reactive power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh456c:EnergySource-EnergySourcePQ

The attributes voltageAngle and voltageMagnitude shall not be used when the EnergySource is representing a constant active and reactive power injection (PQ injection), i.e. they shall only be used when the EnergySource is modelling a voltage source.

**Severity:** sh:Warning

**Messages:**
- "EnergySource modelled as voltage source (attributes voltageAngle and voltageMagnitude are used). Please assess depending on the use case."

**Targets:**
- targetClass: cim:EnergySource

**Constraints:**

- **sh:AndConstraintComponent** (Severity: sh:Warning)
  - Shapes: `[[{[cim:EnergySource.voltageMagnitude] sh:Violation    sh:MinCountConstraintComponent map[MinCount:0]} {[cim:EnergySource.voltageMagnitude] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:0]}] [{[cim:EnergySource.voltageAngle] sh:Violation    sh:MinCountConstraintComponent map[MinCount:0]} {[cim:EnergySource.voltageAngle] sh:Violation    sh:MaxCountConstraintComponent map[MaxCount:0]}]]` 

## ssh456c:NonConformLoad

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonConformLoad

**Nested Properties:**

### ssh456c:EnergyConsumer.p-valueRange

**Path:** `cim:EnergyConsumer.p`  
Negative active power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh456c:EnergyConsumer.q-valueRange

**Path:** `cim:EnergyConsumer.q`  
Negative reactive power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

## ssh456c:StationSupply

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StationSupply

**Nested Properties:**

### ssh456c:EnergyConsumer.p-valueRange

**Path:** `cim:EnergyConsumer.p`  
Negative active power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

### ssh456c:EnergyConsumer.q-valueRange

**Path:** `cim:EnergyConsumer.q`  
Negative reactive power loads shall not be exchanged. In cases where this is needed EquivalentInjection is used instead.

**Severity:** sh:Violation

**Messages:**
- "The value is negative."

**Constraints:**

- **sh:MinInclusiveConstraintComponent** (Severity: sh:Violation)
  - Value: `0.0` 

