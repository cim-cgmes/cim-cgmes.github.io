# 61970-456_Topology-AP-Con-Complex-Explicit-CrossProfile-SHACL

## tp456cpe:DCTopologicalNode.DCEquipmentContainer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCTopologicalNode

**Nested Properties:**

### tp456cpe:DCTopologicalNode.DCEquipmentContainer-valueType

**Path:** `cim:DCTopologicalNode.DCEquipmentContainer / rdf:type`  
**Name:** DCTopologicalNode.DCEquipmentContainer-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class DCEquipmentContainer or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCLine cim:DCConverterUnit]` 

## tp456cpe:TopologicalNode.BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### tp456cpe:TopologicalNode.BaseVoltage-valueType

**Path:** `cim:TopologicalNode.BaseVoltage / rdf:type`  
**Name:** TopologicalNode.BaseVoltage-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class BaseVoltage or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:BaseVoltage]` 

## tp456cpe:TopologicalNode.ConnectivityNodeContainer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### tp456cpe:TopologicalNode.ConnectivityNodeContainer-valueType

**Path:** `cim:TopologicalNode.ConnectivityNodeContainer / rdf:type`  
**Name:** TopologicalNode.ConnectivityNodeContainer-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type is not an instance of the class ConnectivityNodeContainer or its subclass."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:EquivalentNetwork cim:DCLine cim:DCConverterUnit cim:Bay cim:Line cim:Substation cim:VoltageLevel]` 

