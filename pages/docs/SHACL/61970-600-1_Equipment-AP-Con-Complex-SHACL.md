# 61970-600-1_Equipment-AP-Con-Complex-SHACL

## eq600:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Terminal

**Nested Properties:**

### eq600:Terminal-EXCH8ConnectivityNode

**Path:** `cim:Terminal.ConnectivityNode`  
**Name:** C:600:EQ:Terminal:EXCH8ConnectivityNode  
ConnectivityNode object instances shall be included in Core Equipment profile instance. The association end Terminal.ConnectivityNode is optional in the Core Equipment profile instance. However, a model including topology requires Terminals to have an association to either ConnectivityNode, TopologyNode or both.	The association end Terminal.TopologicalNode is required in cases where a RegulatingControl is associated with a Terminal.

**Severity:** sh:Violation

**Messages:**
- "The Terminal is not associated with a ConnectivityNode."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

