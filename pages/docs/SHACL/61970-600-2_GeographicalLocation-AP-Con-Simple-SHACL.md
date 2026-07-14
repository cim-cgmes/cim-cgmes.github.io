# 61970-600-2_GeographicalLocation-AP-Con-Simple-SHACL

## gl:CoordinateSystem

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CoordinateSystem

**Nested Properties:**

### gl:CoordinateSystem.crsUrn-cardinality

**Path:** `cim:CoordinateSystem.crsUrn`  
**Name:** CoordinateSystem.crsUrn-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:CoordinateSystem.crsUrn-datatype

**Path:** `cim:CoordinateSystem.crsUrn`  
**Name:** CoordinateSystem.crsUrn-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.mRID-datatype

**Path:** `cim:IdentifiedObject.mRID`  
**Name:** IdentifiedObject.mRID-datatype  
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
**Name:** IdentifiedObject.mRID-cardinality  
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
**Name:** IdentifiedObject.name-datatype  
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
**Name:** IdentifiedObject.name-cardinality  
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

### io:IdentifiedObject.mRID-datatype

**Path:** `cim:IdentifiedObject.mRID`  
**Name:** IdentifiedObject.mRID-datatype  
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
**Name:** IdentifiedObject.mRID-cardinality  
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
**Name:** IdentifiedObject.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-datatype  
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
**Name:** Location.CoordinateSystem-cardinality  
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
**Name:** Location.CoordinateSystem-valueType  
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
**Name:** Location.PowerSystemResources-cardinality  
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
**Name:** Location.mainAddress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
**Name:** StreetAddress.language-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
**Name:** StreetAddress.language-datatype  
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
**Name:** StreetAddress.poBox-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.poBox-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
**Name:** StreetAddress.poBox-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.postalCode-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
**Name:** StreetAddress.postalCode-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.postalCode-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
**Name:** StreetAddress.postalCode-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.status-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status`  
**Name:** StreetAddress.status-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.dateTime-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
**Name:** Status.dateTime-datatype  
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
**Name:** Status.dateTime-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.reason-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
**Name:** Status.reason-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.reason-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
**Name:** Status.reason-datatype  
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
**Name:** Status.remark-datatype  
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
**Name:** Status.remark-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.value-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
**Name:** Status.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.value-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
**Name:** Status.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.status-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / rdf:type`  
**Name:** StreetAddress.status-datatype  
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
**Name:** StreetAddress.streetDetail-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
**Name:** StreetDetail.addressGeneral-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
**Name:** StreetDetail.addressGeneral-datatype  
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
**Name:** StreetDetail.addressGeneral2-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral2-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
**Name:** StreetDetail.addressGeneral2-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral3-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
**Name:** StreetDetail.addressGeneral3-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral3-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
**Name:** StreetDetail.addressGeneral3-datatype  
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
**Name:** StreetDetail.buildingName-datatype  
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
**Name:** StreetDetail.buildingName-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
**Name:** StreetDetail.code-datatype  
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
**Name:** StreetDetail.code-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.floorIdentification-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
**Name:** StreetDetail.floorIdentification-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.floorIdentification-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
**Name:** StreetDetail.floorIdentification-datatype  
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
**Name:** StreetDetail.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
**Name:** StreetDetail.name-datatype  
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
**Name:** StreetDetail.number-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.number-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.number`  
**Name:** StreetDetail.number-datatype  
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
**Name:** StreetDetail.prefix-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.prefix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
**Name:** StreetDetail.prefix-datatype  
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
**Name:** StreetDetail.suffix-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suffix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
**Name:** StreetDetail.suffix-datatype  
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
**Name:** StreetDetail.suiteNumber-datatype  
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
**Name:** StreetDetail.suiteNumber-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.type-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
**Name:** StreetDetail.type-datatype  
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
**Name:** StreetDetail.type-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
**Name:** StreetDetail.withinTownLimits-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.withinTownLimits-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
**Name:** StreetDetail.withinTownLimits-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.streetDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / rdf:type`  
**Name:** StreetAddress.streetDetail-datatype  
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
**Name:** StreetAddress.townDetail-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
**Name:** TownDetail.code-datatype  
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
**Name:** TownDetail.code-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.country-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
**Name:** TownDetail.country-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.country-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
**Name:** TownDetail.country-datatype  
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
**Name:** TownDetail.name-datatype  
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
**Name:** TownDetail.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
**Name:** TownDetail.section-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.section-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
**Name:** TownDetail.section-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.stateOrProvince-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.stateOrProvince`  
**Name:** TownDetail.stateOrProvince-datatype  
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
**Name:** TownDetail.stateOrProvince-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.townDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / rdf:type`  
**Name:** StreetAddress.townDetail-datatype  
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
**Name:** Location.mainAddress-datatype  
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
**Name:** PositionPoint.Location-cardinality  
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
**Name:** PositionPoint.sequenceNumber-datatype  
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
**Name:** PositionPoint.sequenceNumber-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.xPosition-datatype

**Path:** `cim:PositionPoint.xPosition`  
**Name:** PositionPoint.xPosition-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:PositionPoint.xPosition-cardinality

**Path:** `cim:PositionPoint.xPosition`  
**Name:** PositionPoint.xPosition-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:PositionPoint.yPosition-datatype

**Path:** `cim:PositionPoint.yPosition`  
**Name:** PositionPoint.yPosition-datatype  
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
**Name:** PositionPoint.yPosition-cardinality  
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
**Name:** PositionPoint.zPosition-datatype  
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
**Name:** PositionPoint.zPosition-cardinality  
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
**Name:** PositionPoint.Location-valueType  
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
**Name:** IdentifiedObject.mRID-datatype  
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
**Name:** IdentifiedObject.mRID-cardinality  
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
**Name:** IdentifiedObject.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.name-datatype

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-datatype  
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
**Name:** Location.CoordinateSystem-cardinality  
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
**Name:** Location.CoordinateSystem-valueType  
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
**Name:** Location.PowerSystemResources-cardinality  
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
**Name:** Location.mainAddress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.language-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.language`  
**Name:** StreetAddress.language-datatype  
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
**Name:** StreetAddress.language-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.poBox-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.poBox`  
**Name:** StreetAddress.poBox-datatype  
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
**Name:** StreetAddress.poBox-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
**Name:** StreetAddress.postalCode-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.postalCode-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.postalCode`  
**Name:** StreetAddress.postalCode-datatype  
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
**Name:** StreetAddress.status-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.dateTime-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.dateTime`  
**Name:** Status.dateTime-datatype  
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
**Name:** Status.dateTime-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.reason-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.reason`  
**Name:** Status.reason-datatype  
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
**Name:** Status.reason-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.remark-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.remark`  
**Name:** Status.remark-datatype  
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
**Name:** Status.remark-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.value-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
**Name:** Status.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:Status.value-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / cim:Status.value`  
**Name:** Status.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetAddress.status-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.status / rdf:type`  
**Name:** StreetAddress.status-datatype  
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
**Name:** StreetAddress.streetDetail-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
**Name:** StreetDetail.addressGeneral-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral`  
**Name:** StreetDetail.addressGeneral-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral2-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
**Name:** StreetDetail.addressGeneral2-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.addressGeneral2-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral2`  
**Name:** StreetDetail.addressGeneral2-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral3-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
**Name:** StreetDetail.addressGeneral3-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:StreetDetail.addressGeneral3-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.addressGeneral3`  
**Name:** StreetDetail.addressGeneral3-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.buildingName-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
**Name:** StreetDetail.buildingName-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.buildingName-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.buildingName`  
**Name:** StreetDetail.buildingName-datatype  
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
**Name:** StreetDetail.code-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.code`  
**Name:** StreetDetail.code-datatype  
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
**Name:** StreetDetail.floorIdentification-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.floorIdentification-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.floorIdentification`  
**Name:** StreetDetail.floorIdentification-datatype  
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
**Name:** StreetDetail.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.name`  
**Name:** StreetDetail.name-datatype  
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
**Name:** StreetDetail.number-datatype  
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
**Name:** StreetDetail.number-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.prefix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.prefix`  
**Name:** StreetDetail.prefix-datatype  
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
**Name:** StreetDetail.prefix-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suffix-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suffix`  
**Name:** StreetDetail.suffix-datatype  
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
**Name:** StreetDetail.suffix-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.suiteNumber-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.suiteNumber`  
**Name:** StreetDetail.suiteNumber-datatype  
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
**Name:** StreetDetail.suiteNumber-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.type-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.type`  
**Name:** StreetDetail.type-datatype  
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
**Name:** StreetDetail.type-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
**Name:** StreetDetail.withinTownLimits-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetDetail.withinTownLimits-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.streetDetail / cim:StreetDetail.withinTownLimits`  
**Name:** StreetDetail.withinTownLimits-datatype  
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
**Name:** StreetAddress.streetDetail-datatype  
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
**Name:** StreetAddress.townDetail-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
**Name:** TownDetail.code-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.code-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.code`  
**Name:** TownDetail.code-datatype  
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
**Name:** TownDetail.country-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.country-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.country`  
**Name:** TownDetail.country-datatype  
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
**Name:** TownDetail.name-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.name-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.name`  
**Name:** TownDetail.name-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### gl:TownDetail.section-cardinality

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
**Name:** TownDetail.section-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:TownDetail.section-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / cim:TownDetail.section`  
**Name:** TownDetail.section-datatype  
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
**Name:** TownDetail.stateOrProvince-datatype  
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
**Name:** TownDetail.stateOrProvince-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### gl:StreetAddress.townDetail-datatype

**Path:** `cim:Location.mainAddress / cim:StreetAddress.townDetail / rdf:type`  
**Name:** StreetAddress.townDetail-datatype  
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
**Name:** Location.mainAddress-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StreetAddress]` 

