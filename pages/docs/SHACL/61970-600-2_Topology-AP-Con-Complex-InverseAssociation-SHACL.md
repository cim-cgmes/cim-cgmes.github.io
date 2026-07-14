# 61970-600-2_Topology-AP-Con-Complex-InverseAssociation-SHACL

## tp301ia:TopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### tp301ia:TopologicalNode.Terminal-cardinality

**Path:** `^cim:Terminal.TopologicalNode`  
**Name:** TopologicalNode.Terminal-cardinality  
This constraint validates the cardinality of the association at the inverse direction.

**Severity:** sh:Violation

**Messages:**
- "Wrong number of associated instances."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

