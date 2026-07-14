# 61970-600-2_DiagramLayout-AP-Con-Complex-InverseAssociation-SHACL

## dl301ia:DiagramObjectGluePoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramObjectGluePoint

**Nested Properties:**

### dl301ia:DiagramObjectGluePoint.DiagramObjectPoints-cardinality

**Path:** `^cim:DiagramObjectPoint.DiagramObjectGluePoint`  
**Name:** DiagramObjectGluePoint.DiagramObjectPoints-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `2` 

