# 61970-453_DiagramLayout-AP-Con-Complex-SHACL

## dl453c:DiagramStyle

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramStyle

**Nested Properties:**

### dl453c:DiagramStyle-allowedNameValues

**Path:** `cim:IdentifiedObject.name`  
The inherited IdentifiedObject.name shall have one of the following names: node-breaker, bus-branch, hybrid (node-breaker and bus-branch) or geoschematic.

**Severity:** sh:Violation

**Messages:**
- "Not allowed value."

**Constraints:**

- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[node-breaker bus-branch hybrid (node-breaker and bus-branch) geoschematic]` 

