# 61970-456_Topology-AP-Con-Complex-SHACL

## tp456c:IdentifiedObjectNameCardinality

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode
- targetClass: cim:DCTopologicalNode

**Nested Properties:**

### tp456c:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** C:456:TP:IdentifiedObject.name:instance  
Name is required for all classes in the profile except ACDCTerminal.

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute). "

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

