# 61970-600-2_Topology-AP-Con-Simple-SHACL

## tp:ACDCConverterDCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACDCConverterDCTerminal

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:DCBaseTerminal.DCTopologicalNode-cardinality

**Path:** `cim:DCBaseTerminal.DCTopologicalNode`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:DCBaseTerminal.DCTopologicalNode-valueType

**Path:** `cim:DCBaseTerminal.DCTopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:DCTopologicalNode"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCTopologicalNode]` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## tp:ConnectivityNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConnectivityNode

**Nested Properties:**

### tp:ConnectivityNode.TopologicalNode-cardinality

**Path:** `cim:ConnectivityNode.TopologicalNode`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:ConnectivityNode.TopologicalNode-valueType

**Path:** `cim:ConnectivityNode.TopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:TopologicalNode"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

## tp:DCNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCNode

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### tp:DCNode.DCTopologicalNode-cardinality

**Path:** `cim:DCNode.DCTopologicalNode`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:DCNode.DCTopologicalNode-valueType

**Path:** `cim:DCNode.DCTopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:DCTopologicalNode"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCTopologicalNode]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## tp:DCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCTerminal

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### tp:DCBaseTerminal.DCTopologicalNode-cardinality

**Path:** `cim:DCBaseTerminal.DCTopologicalNode`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:DCBaseTerminal.DCTopologicalNode-valueType

**Path:** `cim:DCBaseTerminal.DCTopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:DCTopologicalNode"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DCTopologicalNode]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## tp:DCTopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCTopologicalNode

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:DCTopologicalNode.DCEquipmentContainer-cardinality

**Path:** `cim:DCTopologicalNode.DCEquipmentContainer`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.mRID-cardinality

**Path:** `cim:IdentifiedObject.mRID`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.mRID-datatype

**Path:** `cim:IdentifiedObject.mRID`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## tp:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Terminal

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### tp:Terminal.TopologicalNode-cardinality

**Path:** `cim:Terminal.TopologicalNode`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:Terminal.TopologicalNode-valueType

**Path:** `cim:Terminal.TopologicalNode / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:TopologicalNode"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TopologicalNode]` 

## tp:TopologicalNode

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TopologicalNode

**Nested Properties:**

### io:IdentifiedObject.energyIdentCodeEic-datatype

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.energyIdentCodeEic-cardinality

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.shortName-datatype

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.shortName-cardinality

**Path:** `cim100:IdentifiedObject.shortName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.mRID-cardinality

**Path:** `cim:IdentifiedObject.mRID`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.mRID-datatype

**Path:** `cim:IdentifiedObject.mRID`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:TopologicalNode.BaseVoltage-cardinality

**Path:** `cim:TopologicalNode.BaseVoltage`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:TopologicalNode.ConnectivityNodeContainer-cardinality

**Path:** `cim:TopologicalNode.ConnectivityNodeContainer`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### tp:TopologicalNode.ReportingGroup-cardinality

**Path:** `cim:TopologicalNode.ReportingGroup`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

