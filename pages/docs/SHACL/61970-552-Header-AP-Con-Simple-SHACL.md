# 61970-552-Header-AP-Con-Simple-SHACL

## mdc:DifferenceModel

**Severity:** sh:Violation

**Targets:**
- targetClass: diff:DifferenceModel

**Nested Properties:**

### mdc:DifferenceModel.forwardDifferences-cardinality

**Path:** `diff:DifferenceModel.forwardDifferences`  
**Name:** DifferenceModel.forwardDifferences-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### mdc:Statements.object-cardinality

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.object`  
**Name:** Statements.object-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required attribute."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Statements.object-datatype

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.object`  
**Name:** Statements.object-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Statements.predicate-datatype

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.predicate`  
**Name:** Statements.predicate-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Statements.predicate-cardinality

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.predicate`  
**Name:** Statements.predicate-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required attribute."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Statements.subject-cardinality

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.subject`  
**Name:** Statements.subject-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required attribute."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Statements.subject-datatype

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:Statements.subject`  
**Name:** Statements.subject-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:DifferenceModel.forwardDifferences-datatype

**Path:** `diff:DifferenceModel.forwardDifferences / rdf:type`  
**Name:** DifferenceModel.forwardDifferences-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[rdf:Statements]` 

### mdc:DifferenceModel.preconditions-cardinality

**Path:** `diff:DifferenceModel.preconditions`  
**Name:** DifferenceModel.preconditions-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### mdc:DifferenceModel.preconditions-datatype

**Path:** `diff:DifferenceModel.preconditions / rdf:type`  
**Name:** DifferenceModel.preconditions-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[rdf:Statements]` 

### mdc:DifferenceModel.reverseDifferences-cardinality

**Path:** `diff:DifferenceModel.reverseDifferences`  
**Name:** DifferenceModel.reverseDifferences-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### mdc:DifferenceModel.reverseDifferences-datatype

**Path:** `diff:DifferenceModel.reverseDifferences / rdf:type`  
**Name:** DifferenceModel.reverseDifferences-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Blank node (compound datatype) violation. Either it is not a blank node (nested structure, compound datatype) or it is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:BlankNode` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[rdf:Statements]` 

### mdc:Model.created-datatype

**Path:** `mdc:Model.created`  
**Name:** Model.created-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.created-cardinality

**Path:** `mdc:Model.created`  
**Name:** Model.created-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.description-datatype

**Path:** `mdc:Model.description`  
**Name:** Model.description-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.description-cardinality

**Path:** `mdc:Model.description`  
**Name:** Model.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.modelingAuthoritySet-datatype

**Path:** `mdc:Model.modelingAuthoritySet`  
**Name:** Model.modelingAuthoritySet-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:anyURI` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.modelingAuthoritySet-cardinality

**Path:** `mdc:Model.modelingAuthoritySet`  
**Name:** Model.modelingAuthoritySet-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.profile-cardinality

**Path:** `mdc:Model.profile`  
**Name:** Model.profile-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### mdc:Model.profile-datatype

**Path:** `mdc:Model.profile`  
**Name:** Model.profile-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:anyURI` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.scenarioTime-cardinality

**Path:** `mdc:Model.scenarioTime`  
**Name:** Model.scenarioTime-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.scenarioTime-datatype

**Path:** `mdc:Model.scenarioTime`  
**Name:** Model.scenarioTime-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.version-cardinality

**Path:** `mdc:Model.version`  
**Name:** Model.version-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.version-datatype

**Path:** `mdc:Model.version`  
**Name:** Model.version-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## mdc:FullModel

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel

**Nested Properties:**

### mdc:Model.created-cardinality

**Path:** `mdc:Model.created`  
**Name:** Model.created-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.created-datatype

**Path:** `mdc:Model.created`  
**Name:** Model.created-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.description-datatype

**Path:** `mdc:Model.description`  
**Name:** Model.description-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.description-cardinality

**Path:** `mdc:Model.description`  
**Name:** Model.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.modelingAuthoritySet-datatype

**Path:** `mdc:Model.modelingAuthoritySet`  
**Name:** Model.modelingAuthoritySet-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:anyURI` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.modelingAuthoritySet-cardinality

**Path:** `mdc:Model.modelingAuthoritySet`  
**Name:** Model.modelingAuthoritySet-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.profile-cardinality

**Path:** `mdc:Model.profile`  
**Name:** Model.profile-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### mdc:Model.profile-datatype

**Path:** `mdc:Model.profile`  
**Name:** Model.profile-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:anyURI` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.scenarioTime-datatype

**Path:** `mdc:Model.scenarioTime`  
**Name:** Model.scenarioTime-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.scenarioTime-cardinality

**Path:** `mdc:Model.scenarioTime`  
**Name:** Model.scenarioTime-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### mdc:Model.version-datatype

**Path:** `mdc:Model.version`  
**Name:** Model.version-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### mdc:Model.version-cardinality

**Path:** `mdc:Model.version`  
**Name:** Model.version-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## mdc:Model.DependentOn-valueTypeNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

**Nested Properties:**

### mdc:Model.DependentOn-valueType

**Path:** `mdc:Model.DependentOn / rdf:type`  
**Name:** Model.DependentOn-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following occurs: 1) The value type is not IRI; 2) The value type is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[diff:DifferenceModel mdc:FullModel]` 

## mdc:Model.Supersedes-valueTypeNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

**Nested Properties:**

### mdc:Model.Supersedes-valueType

**Path:** `mdc:Model.Supersedes / rdf:type`  
**Name:** Model.Supersedes-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following occurs: 1) The value type is not IRI; 2) The value type is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[diff:DifferenceModel mdc:FullModel]` 

