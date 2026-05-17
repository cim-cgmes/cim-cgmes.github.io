# 61970-600-2_GeographicalLocation-AP-Con-Simple-SHACL

## gl:CoordinateSystem

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CoordinateSystem

**Nested Properties:**

### gl:CoordinateSystem.crsUrn-datatype

**Path:** `cim:CoordinateSystem.crsUrn`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:CoordinateSystem.crsUrn-cardinality

**Path:** `cim:CoordinateSystem.crsUrn`  
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

## gl:Location

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Location

**Nested Properties:**

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

### gl:Location.CoordinateSystem-cardinality

**Path:** `cim:Location.CoordinateSystem`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Location.CoordinateSystem-valueType

**Path:** `cim:Location.CoordinateSystem / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:CoordinateSystem"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:CoordinateSystem]` 

### gl:Location.PowerSystemResources-cardinality

**Path:** `cim:Location.PowerSystemResources`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Location.mainAddress-cardinality

**Path:** `cim:Location.mainAddress`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.language-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.poBox-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.poBox-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.status-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.dateTime-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.dateTime-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.reason-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.reason-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.remark-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.remark`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.remark-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.remark`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.value-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.value-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.status-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Status]` 

### gl:StreetAddress.streetDetail-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral2-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral2-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral3-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral3-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.buildingName-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.buildingName-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.code-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.floorIdentification-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.floorIdentification-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.name-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.number-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.number`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.number-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.number`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.prefix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.prefix-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suffix-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suffix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.suiteNumber-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suiteNumber`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.suiteNumber-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suiteNumber`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.type-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.type-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.streetDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StreetDetail]` 

### gl:StreetAddress.townDetail-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.code-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.country-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.country-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.name-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.stateOrProvince-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.stateOrProvince`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.stateOrProvince-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.stateOrProvince`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.townDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TownDetail]` 

### gl:Location.mainAddress-datatype

**Path:** `cim:Location.mainAddress / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StreetAddress]` 

## gl:PositionPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PositionPoint

**Nested Properties:**

### gl:PositionPoint.Location-cardinality

**Path:** `cim:PositionPoint.Location`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.sequenceNumber-datatype

**Path:** `cim:PositionPoint.sequenceNumber`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:PositionPoint.sequenceNumber-cardinality

**Path:** `cim:PositionPoint.sequenceNumber`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.xPosition-cardinality

**Path:** `cim:PositionPoint.xPosition`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.xPosition-datatype

**Path:** `cim:PositionPoint.xPosition`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:PositionPoint.yPosition-datatype

**Path:** `cim:PositionPoint.yPosition`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:PositionPoint.yPosition-cardinality

**Path:** `cim:PositionPoint.yPosition`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.zPosition-datatype

**Path:** `cim:PositionPoint.zPosition`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:PositionPoint.zPosition-cardinality

**Path:** `cim:PositionPoint.zPosition`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## gl:PositionPoint.Location-valueTypeNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PositionPoint

**Nested Properties:**

### gl:PositionPoint.Location-valueType

**Path:** `cim:PositionPoint.Location / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following occurs: 1) The value type is not IRI; 2) The value type is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Location cim:ServiceLocation]` 

## gl:ServiceLocation

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ServiceLocation

**Nested Properties:**

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

### gl:Location.CoordinateSystem-cardinality

**Path:** `cim:Location.CoordinateSystem`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Location.CoordinateSystem-valueType

**Path:** `cim:Location.CoordinateSystem / rdf:type`  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:CoordinateSystem"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:CoordinateSystem]` 

### gl:Location.PowerSystemResources-cardinality

**Path:** `cim:Location.PowerSystemResources`  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Location.mainAddress-cardinality

**Path:** `cim:Location.mainAddress`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.poBox-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.poBox-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.status-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.dateTime-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.dateTime-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.reason-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.reason-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.remark-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.remark`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.remark-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.remark`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.value-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:Status.value-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.status-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Status]` 

### gl:StreetAddress.streetDetail-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral2-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral2-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral3-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral3-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.buildingName-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.buildingName-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.code-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.floorIdentification-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.floorIdentification-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.name-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.number-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.number`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.number-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.number`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.prefix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.prefix-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suffix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.suffix-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suiteNumber-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suiteNumber`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.suiteNumber-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suiteNumber`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.type-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.type-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.withinTownLimits-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.streetDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StreetDetail]` 

### gl:StreetAddress.townDetail-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.country-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.country-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.name`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.name-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.name`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.stateOrProvince-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.stateOrProvince`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.stateOrProvince-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.stateOrProvince`  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.townDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:TownDetail]` 

### gl:Location.mainAddress-datatype

**Path:** `cim:Location.mainAddress / rdf:type`  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StreetAddress]` 

