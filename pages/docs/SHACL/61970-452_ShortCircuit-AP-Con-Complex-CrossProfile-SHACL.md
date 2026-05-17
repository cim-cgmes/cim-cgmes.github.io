# 61970-452_ShortCircuit-AP-Con-Complex-CrossProfile-SHACL

## sc452cp:MutualCoupling.First_Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MutualCoupling

**Nested Properties:**

### sc452cp:MutualCoupling.First_Terminal-valueType

**Path:** `cim:MutualCoupling.First_Terminal / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Terminal or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Terminal]` 

## sc452cp:MutualCoupling.Second_Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MutualCoupling

**Nested Properties:**

### sc452cp:MutualCoupling.Second_Terminal-valueType

**Path:** `cim:MutualCoupling.Second_Terminal / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class Terminal or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Terminal]` 

