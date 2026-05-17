# 61970-600-2_EquipmentBoundary-AP-Con-Complex-InverseAssociation-SHACL

## eqbd301ia:ConnectivityNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConnectivityNode

**Nested Properties:**

### eqbd301ia:ConnectivityNode.BoundaryPoint-cardinality

**Path:** `^cim100:BoundaryPoint.ConnectivityNode`  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

