# 61970-600-2_Operation-AP-Con-Simple-SHACL

## op:Accumulator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Accumulator

**Nested Properties:**

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-cardinality  
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

### op:Measurement.PowerSystemResource-cardinality

**Path:** `cim:Measurement.PowerSystemResource`  
**Name:** Measurement.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.Terminal-cardinality

**Path:** `cim:Measurement.Terminal`  
**Name:** Measurement.Terminal-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-cardinality

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-datatype

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Measurement.phases-datatype

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PhaseCode.CN cim:PhaseCode.XY cim:PhaseCode.A cim:PhaseCode.s12 cim:PhaseCode.B cim:PhaseCode.ABCN cim:PhaseCode.C cim:PhaseCode.s1N cim:PhaseCode.XYN cim:PhaseCode.AB cim:PhaseCode.X cim:PhaseCode.s2N cim:PhaseCode.AC cim:PhaseCode.s2 cim:PhaseCode.ABC cim:PhaseCode.XN cim:PhaseCode.s12N cim:PhaseCode.BC cim:PhaseCode.AN cim:PhaseCode.none cim:PhaseCode.ACN cim:PhaseCode.s1 cim:PhaseCode.BN cim:PhaseCode.BCN cim:PhaseCode.N cim:PhaseCode.ABN]` 

### op:Measurement.phases-cardinality

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-cardinality

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-datatype

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Measurement.unitSymbol-cardinality

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitSymbol-datatype

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

## op:AccumulatorLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorLimit

**Nested Properties:**

### op:AccumulatorLimit.LimitSet-cardinality

**Path:** `cim:AccumulatorLimit.LimitSet`  
**Name:** AccumulatorLimit.LimitSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AccumulatorLimit.LimitSet-valueType

**Path:** `cim:AccumulatorLimit.LimitSet / rdf:type`  
**Name:** AccumulatorLimit.LimitSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:AccumulatorLimitSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AccumulatorLimitSet]` 

### op:AccumulatorLimit.value-cardinality

**Path:** `cim:AccumulatorLimit.value`  
**Name:** AccumulatorLimit.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AccumulatorLimit.value-datatype

**Path:** `cim:AccumulatorLimit.value`  
**Name:** AccumulatorLimit.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:AccumulatorLimitSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorLimitSet

**Nested Properties:**

### op:AccumulatorLimitSet.Measurements-cardinality

**Path:** `cim:AccumulatorLimitSet.Measurements`  
**Name:** AccumulatorLimitSet.Measurements-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### op:AccumulatorLimitSet.Measurements-valueType

**Path:** `cim:AccumulatorLimitSet.Measurements / rdf:type`  
**Name:** AccumulatorLimitSet.Measurements-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:Accumulator"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Accumulator]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:LimitSet.isPercentageLimits-datatype

**Path:** `cim:LimitSet.isPercentageLimits`  
**Name:** LimitSet.isPercentageLimits-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:LimitSet.isPercentageLimits-cardinality

**Path:** `cim:LimitSet.isPercentageLimits`  
**Name:** LimitSet.isPercentageLimits-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:AccumulatorReset

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorReset

**Nested Properties:**

### op:AccumulatorReset.AccumulatorValue-cardinality

**Path:** `cim:AccumulatorReset.AccumulatorValue`  
**Name:** AccumulatorReset.AccumulatorValue-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AccumulatorReset.AccumulatorValue-valueType

**Path:** `cim:AccumulatorReset.AccumulatorValue / rdf:type`  
**Name:** AccumulatorReset.AccumulatorValue-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:AccumulatorValue"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AccumulatorValue]` 

### op:Control.PowerSystemResource-cardinality

**Path:** `cim:Control.PowerSystemResource`  
**Name:** Control.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-cardinality

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-datatype

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.operationInProgress-datatype

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.operationInProgress-cardinality

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.timeStamp-datatype

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-cardinality

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-datatype

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Control.unitMultiplier-cardinality

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitSymbol-cardinality

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitSymbol-datatype

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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

## op:AccumulatorValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AccumulatorValue

**Nested Properties:**

### op:AccumulatorValue.Accumulator-cardinality

**Path:** `cim:AccumulatorValue.Accumulator`  
**Name:** AccumulatorValue.Accumulator-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AccumulatorValue.Accumulator-valueType

**Path:** `cim:AccumulatorValue.Accumulator / rdf:type`  
**Name:** AccumulatorValue.Accumulator-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:Accumulator"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Accumulator]` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-cardinality

**Path:** `cim:MeasurementValue.MeasurementValueSource`  
**Name:** MeasurementValue.MeasurementValueSource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-valueType

**Path:** `cim:MeasurementValue.MeasurementValueSource / rdf:type`  
**Name:** MeasurementValue.MeasurementValueSource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:MeasurementValueSource"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:MeasurementValueSource]` 

### op:MeasurementValue.sensorAccuracy-cardinality

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.sensorAccuracy-datatype

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.timeStamp-datatype

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.timeStamp-cardinality

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:Analog

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Analog

**Nested Properties:**

### op:Analog.positiveFlowIn-cardinality

**Path:** `cim:Analog.positiveFlowIn`  
**Name:** Analog.positiveFlowIn-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Analog.positiveFlowIn-datatype

**Path:** `cim:Analog.positiveFlowIn`  
**Name:** Analog.positiveFlowIn-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.PowerSystemResource-cardinality

**Path:** `cim:Measurement.PowerSystemResource`  
**Name:** Measurement.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.Terminal-cardinality

**Path:** `cim:Measurement.Terminal`  
**Name:** Measurement.Terminal-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-cardinality

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-datatype

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Measurement.phases-datatype

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PhaseCode.CN cim:PhaseCode.XY cim:PhaseCode.A cim:PhaseCode.s12 cim:PhaseCode.B cim:PhaseCode.ABCN cim:PhaseCode.C cim:PhaseCode.s1N cim:PhaseCode.XYN cim:PhaseCode.AB cim:PhaseCode.X cim:PhaseCode.s2N cim:PhaseCode.AC cim:PhaseCode.s2 cim:PhaseCode.ABC cim:PhaseCode.XN cim:PhaseCode.s12N cim:PhaseCode.BC cim:PhaseCode.AN cim:PhaseCode.none cim:PhaseCode.ACN cim:PhaseCode.s1 cim:PhaseCode.BN cim:PhaseCode.BCN cim:PhaseCode.N cim:PhaseCode.ABN]` 

### op:Measurement.phases-cardinality

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-cardinality

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-datatype

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Measurement.unitSymbol-datatype

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### op:Measurement.unitSymbol-cardinality

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:AnalogLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AnalogLimit

**Nested Properties:**

### op:AnalogLimit.LimitSet-cardinality

**Path:** `cim:AnalogLimit.LimitSet`  
**Name:** AnalogLimit.LimitSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogLimit.LimitSet-valueType

**Path:** `cim:AnalogLimit.LimitSet / rdf:type`  
**Name:** AnalogLimit.LimitSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:AnalogLimitSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AnalogLimitSet]` 

### op:AnalogLimit.value-cardinality

**Path:** `cim:AnalogLimit.value`  
**Name:** AnalogLimit.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogLimit.value-datatype

**Path:** `cim:AnalogLimit.value`  
**Name:** AnalogLimit.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:AnalogLimitSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AnalogLimitSet

**Nested Properties:**

### op:AnalogLimitSet.Measurements-cardinality

**Path:** `cim:AnalogLimitSet.Measurements`  
**Name:** AnalogLimitSet.Measurements-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Lower bound shall be 1"

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

### op:AnalogLimitSet.Measurements-valueType

**Path:** `cim:AnalogLimitSet.Measurements / rdf:type`  
**Name:** AnalogLimitSet.Measurements-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:Analog"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Analog]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-cardinality  
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

### op:LimitSet.isPercentageLimits-cardinality

**Path:** `cim:LimitSet.isPercentageLimits`  
**Name:** LimitSet.isPercentageLimits-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:LimitSet.isPercentageLimits-datatype

**Path:** `cim:LimitSet.isPercentageLimits`  
**Name:** LimitSet.isPercentageLimits-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## op:AnalogValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AnalogValue

**Nested Properties:**

### op:AnalogValue.Analog-cardinality

**Path:** `cim:AnalogValue.Analog`  
**Name:** AnalogValue.Analog-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogValue.Analog-valueType

**Path:** `cim:AnalogValue.Analog / rdf:type`  
**Name:** AnalogValue.Analog-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:Analog"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Analog]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-cardinality  
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

### op:MeasurementValue.MeasurementValueSource-cardinality

**Path:** `cim:MeasurementValue.MeasurementValueSource`  
**Name:** MeasurementValue.MeasurementValueSource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-valueType

**Path:** `cim:MeasurementValue.MeasurementValueSource / rdf:type`  
**Name:** MeasurementValue.MeasurementValueSource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:MeasurementValueSource"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:MeasurementValueSource]` 

### op:MeasurementValue.sensorAccuracy-datatype

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.sensorAccuracy-cardinality

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.timeStamp-cardinality

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.timeStamp-datatype

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## op:Command

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Command

**Nested Properties:**

### op:Command.DiscreteValue-cardinality

**Path:** `cim:Command.DiscreteValue`  
**Name:** Command.DiscreteValue-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Command.DiscreteValue-valueType

**Path:** `cim:Command.DiscreteValue / rdf:type`  
**Name:** Command.DiscreteValue-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:DiscreteValue"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:DiscreteValue]` 

### op:Command.ValueAliasSet-cardinality

**Path:** `cim:Command.ValueAliasSet`  
**Name:** Command.ValueAliasSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Command.ValueAliasSet-valueType

**Path:** `cim:Command.ValueAliasSet / rdf:type`  
**Name:** Command.ValueAliasSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:ValueAliasSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ValueAliasSet]` 

### op:Command.normalValue-cardinality

**Path:** `cim:Command.normalValue`  
**Name:** Command.normalValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Command.normalValue-datatype

**Path:** `cim:Command.normalValue`  
**Name:** Command.normalValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Command.value-datatype

**Path:** `cim:Command.value`  
**Name:** Command.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Command.value-cardinality

**Path:** `cim:Command.value`  
**Name:** Command.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.PowerSystemResource-cardinality

**Path:** `cim:Control.PowerSystemResource`  
**Name:** Control.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-datatype

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.controlType-cardinality

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.operationInProgress-cardinality

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.operationInProgress-datatype

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-datatype

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-cardinality

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-cardinality

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-datatype

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Control.unitSymbol-cardinality

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitSymbol-datatype

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:Discrete

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Discrete

**Nested Properties:**

### op:Discrete.ValueAliasSet-cardinality

**Path:** `cim:Discrete.ValueAliasSet`  
**Name:** Discrete.ValueAliasSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Discrete.ValueAliasSet-valueType

**Path:** `cim:Discrete.ValueAliasSet / rdf:type`  
**Name:** Discrete.ValueAliasSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:ValueAliasSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ValueAliasSet]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.PowerSystemResource-cardinality

**Path:** `cim:Measurement.PowerSystemResource`  
**Name:** Measurement.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.Terminal-cardinality

**Path:** `cim:Measurement.Terminal`  
**Name:** Measurement.Terminal-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-cardinality

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-datatype

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Measurement.phases-cardinality

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.phases-datatype

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PhaseCode.CN cim:PhaseCode.XY cim:PhaseCode.A cim:PhaseCode.s12 cim:PhaseCode.B cim:PhaseCode.ABCN cim:PhaseCode.C cim:PhaseCode.s1N cim:PhaseCode.XYN cim:PhaseCode.AB cim:PhaseCode.X cim:PhaseCode.s2N cim:PhaseCode.AC cim:PhaseCode.s2 cim:PhaseCode.ABC cim:PhaseCode.XN cim:PhaseCode.s12N cim:PhaseCode.BC cim:PhaseCode.AN cim:PhaseCode.none cim:PhaseCode.ACN cim:PhaseCode.s1 cim:PhaseCode.BN cim:PhaseCode.BCN cim:PhaseCode.N cim:PhaseCode.ABN]` 

### op:Measurement.unitMultiplier-cardinality

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-datatype

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Measurement.unitSymbol-datatype

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### op:Measurement.unitSymbol-cardinality

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:DiscreteValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscreteValue

**Nested Properties:**

### op:DiscreteValue.Discrete-cardinality

**Path:** `cim:DiscreteValue.Discrete`  
**Name:** DiscreteValue.Discrete-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:DiscreteValue.Discrete-valueType

**Path:** `cim:DiscreteValue.Discrete / rdf:type`  
**Name:** DiscreteValue.Discrete-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:Discrete"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Discrete]` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-cardinality

**Path:** `cim:MeasurementValue.MeasurementValueSource`  
**Name:** MeasurementValue.MeasurementValueSource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-valueType

**Path:** `cim:MeasurementValue.MeasurementValueSource / rdf:type`  
**Name:** MeasurementValue.MeasurementValueSource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:MeasurementValueSource"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:MeasurementValueSource]` 

### op:MeasurementValue.sensorAccuracy-datatype

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.sensorAccuracy-cardinality

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.timeStamp-datatype

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.timeStamp-cardinality

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:Measurement.Terminal-valueTypeNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Accumulator
- targetClass: cim:Analog
- targetClass: cim:Discrete
- targetClass: cim:StringMeasurement

**Nested Properties:**

### op:Measurement.Terminal-valueType

**Path:** `cim:Measurement.Terminal / rdf:type`  
**Name:** Measurement.Terminal-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following occurs: 1) The value type is not IRI; 2) The value type is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `<nil>` 

## op:MeasurementValueQuality

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MeasurementValueQuality

**Nested Properties:**

### op:MeasurementValueQuality.MeasurementValue-cardinality

**Path:** `cim:MeasurementValueQuality.MeasurementValue`  
**Name:** MeasurementValueQuality.MeasurementValue-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.badReference-datatype

**Path:** `cim:Quality61850.badReference`  
**Name:** Quality61850.badReference-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.badReference-cardinality

**Path:** `cim:Quality61850.badReference`  
**Name:** Quality61850.badReference-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.estimatorReplaced-datatype

**Path:** `cim:Quality61850.estimatorReplaced`  
**Name:** Quality61850.estimatorReplaced-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.estimatorReplaced-cardinality

**Path:** `cim:Quality61850.estimatorReplaced`  
**Name:** Quality61850.estimatorReplaced-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.failure-cardinality

**Path:** `cim:Quality61850.failure`  
**Name:** Quality61850.failure-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.failure-datatype

**Path:** `cim:Quality61850.failure`  
**Name:** Quality61850.failure-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.oldData-datatype

**Path:** `cim:Quality61850.oldData`  
**Name:** Quality61850.oldData-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.oldData-cardinality

**Path:** `cim:Quality61850.oldData`  
**Name:** Quality61850.oldData-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.operatorBlocked-cardinality

**Path:** `cim:Quality61850.operatorBlocked`  
**Name:** Quality61850.operatorBlocked-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.operatorBlocked-datatype

**Path:** `cim:Quality61850.operatorBlocked`  
**Name:** Quality61850.operatorBlocked-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.oscillatory-cardinality

**Path:** `cim:Quality61850.oscillatory`  
**Name:** Quality61850.oscillatory-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.oscillatory-datatype

**Path:** `cim:Quality61850.oscillatory`  
**Name:** Quality61850.oscillatory-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.outOfRange-datatype

**Path:** `cim:Quality61850.outOfRange`  
**Name:** Quality61850.outOfRange-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.outOfRange-cardinality

**Path:** `cim:Quality61850.outOfRange`  
**Name:** Quality61850.outOfRange-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.overFlow-cardinality

**Path:** `cim:Quality61850.overFlow`  
**Name:** Quality61850.overFlow-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.overFlow-datatype

**Path:** `cim:Quality61850.overFlow`  
**Name:** Quality61850.overFlow-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.source-cardinality

**Path:** `cim:Quality61850.source`  
**Name:** Quality61850.source-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.source-datatype

**Path:** `cim:Quality61850.source`  
**Name:** Quality61850.source-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Source.SUBSTITUTED cim:Source.PROCESS cim:Source.DEFAULTED]` 

### op:Quality61850.suspect-datatype

**Path:** `cim:Quality61850.suspect`  
**Name:** Quality61850.suspect-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.suspect-cardinality

**Path:** `cim:Quality61850.suspect`  
**Name:** Quality61850.suspect-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.test-datatype

**Path:** `cim:Quality61850.test`  
**Name:** Quality61850.test-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Quality61850.test-cardinality

**Path:** `cim:Quality61850.test`  
**Name:** Quality61850.test-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.validity-cardinality

**Path:** `cim:Quality61850.validity`  
**Name:** Quality61850.validity-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Quality61850.validity-datatype

**Path:** `cim:Quality61850.validity`  
**Name:** Quality61850.validity-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:Validity.INVALID cim:Validity.GOOD cim:Validity.QUESTIONABLE]` 

## op:MeasurementValueQuality.MeasurementValue-valueTypeNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MeasurementValueQuality

**Nested Properties:**

### op:MeasurementValueQuality.MeasurementValue-valueType

**Path:** `cim:MeasurementValueQuality.MeasurementValue / rdf:type`  
**Name:** MeasurementValueQuality.MeasurementValue-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following occurs: 1) The value type is not IRI; 2) The value type is not the right class."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AnalogValue cim:AccumulatorValue cim:DiscreteValue cim:StringMeasurementValue]` 

## op:MeasurementValueSource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:MeasurementValueSource

**Nested Properties:**

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:RaiseLowerCommand

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RaiseLowerCommand

**Nested Properties:**

### op:AnalogControl.AnalogValue-cardinality

**Path:** `cim:AnalogControl.AnalogValue`  
**Name:** AnalogControl.AnalogValue-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogControl.AnalogValue-valueType

**Path:** `cim:AnalogControl.AnalogValue / rdf:type`  
**Name:** AnalogControl.AnalogValue-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:AnalogValue"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AnalogValue]` 

### op:AnalogControl.maxValue-datatype

**Path:** `cim:AnalogControl.maxValue`  
**Name:** AnalogControl.maxValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:AnalogControl.maxValue-cardinality

**Path:** `cim:AnalogControl.maxValue`  
**Name:** AnalogControl.maxValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogControl.minValue-datatype

**Path:** `cim:AnalogControl.minValue`  
**Name:** AnalogControl.minValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:AnalogControl.minValue-cardinality

**Path:** `cim:AnalogControl.minValue`  
**Name:** AnalogControl.minValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.PowerSystemResource-cardinality

**Path:** `cim:Control.PowerSystemResource`  
**Name:** Control.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-cardinality

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-datatype

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.operationInProgress-cardinality

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.operationInProgress-datatype

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-datatype

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-cardinality

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-cardinality

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-datatype

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Control.unitSymbol-datatype

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### op:Control.unitSymbol-cardinality

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:RaiseLowerCommand.ValueAliasSet-cardinality

**Path:** `cim:RaiseLowerCommand.ValueAliasSet`  
**Name:** RaiseLowerCommand.ValueAliasSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:RaiseLowerCommand.ValueAliasSet-valueType

**Path:** `cim:RaiseLowerCommand.ValueAliasSet / rdf:type`  
**Name:** RaiseLowerCommand.ValueAliasSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:ValueAliasSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ValueAliasSet]` 

## op:SetPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SetPoint

**Nested Properties:**

### op:AnalogControl.AnalogValue-cardinality

**Path:** `cim:AnalogControl.AnalogValue`  
**Name:** AnalogControl.AnalogValue-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogControl.AnalogValue-valueType

**Path:** `cim:AnalogControl.AnalogValue / rdf:type`  
**Name:** AnalogControl.AnalogValue-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:AnalogValue"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:AnalogValue]` 

### op:AnalogControl.maxValue-datatype

**Path:** `cim:AnalogControl.maxValue`  
**Name:** AnalogControl.maxValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:AnalogControl.maxValue-cardinality

**Path:** `cim:AnalogControl.maxValue`  
**Name:** AnalogControl.maxValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:AnalogControl.minValue-datatype

**Path:** `cim:AnalogControl.minValue`  
**Name:** AnalogControl.minValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:AnalogControl.minValue-cardinality

**Path:** `cim:AnalogControl.minValue`  
**Name:** AnalogControl.minValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.PowerSystemResource-cardinality

**Path:** `cim:Control.PowerSystemResource`  
**Name:** Control.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.controlType-datatype

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.controlType-cardinality

**Path:** `cim:Control.controlType`  
**Name:** Control.controlType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.operationInProgress-cardinality

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.operationInProgress-datatype

**Path:** `cim:Control.operationInProgress`  
**Name:** Control.operationInProgress-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:boolean` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.timeStamp-cardinality

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.timeStamp-datatype

**Path:** `cim:Control.timeStamp`  
**Name:** Control.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Control.unitMultiplier-cardinality

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Control.unitMultiplier-datatype

**Path:** `cim:Control.unitMultiplier`  
**Name:** Control.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Control.unitSymbol-datatype

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

### op:Control.unitSymbol-cardinality

**Path:** `cim:Control.unitSymbol`  
**Name:** Control.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:SetPoint.normalValue-datatype

**Path:** `cim:SetPoint.normalValue`  
**Name:** SetPoint.normalValue-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:SetPoint.normalValue-cardinality

**Path:** `cim:SetPoint.normalValue`  
**Name:** SetPoint.normalValue-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:SetPoint.value-cardinality

**Path:** `cim:SetPoint.value`  
**Name:** SetPoint.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:SetPoint.value-datatype

**Path:** `cim:SetPoint.value`  
**Name:** SetPoint.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

## op:StringMeasurement

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StringMeasurement

**Nested Properties:**

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.PowerSystemResource-cardinality

**Path:** `cim:Measurement.PowerSystemResource`  
**Name:** Measurement.PowerSystemResource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.Terminal-cardinality

**Path:** `cim:Measurement.Terminal`  
**Name:** Measurement.Terminal-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-cardinality

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.measurementType-datatype

**Path:** `cim:Measurement.measurementType`  
**Name:** Measurement.measurementType-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:string` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:Measurement.phases-datatype

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:PhaseCode.CN cim:PhaseCode.XY cim:PhaseCode.A cim:PhaseCode.s12 cim:PhaseCode.B cim:PhaseCode.ABCN cim:PhaseCode.C cim:PhaseCode.s1N cim:PhaseCode.XYN cim:PhaseCode.AB cim:PhaseCode.X cim:PhaseCode.s2N cim:PhaseCode.AC cim:PhaseCode.s2 cim:PhaseCode.ABC cim:PhaseCode.XN cim:PhaseCode.s12N cim:PhaseCode.BC cim:PhaseCode.AN cim:PhaseCode.none cim:PhaseCode.ACN cim:PhaseCode.s1 cim:PhaseCode.BN cim:PhaseCode.BCN cim:PhaseCode.N cim:PhaseCode.ABN]` 

### op:Measurement.phases-cardinality

**Path:** `cim:Measurement.phases`  
**Name:** Measurement.phases-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitMultiplier-datatype

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitMultiplier.k cim:UnitMultiplier.da cim:UnitMultiplier.Z cim:UnitMultiplier.y cim:UnitMultiplier.micro cim:UnitMultiplier.Y cim:UnitMultiplier.z cim:UnitMultiplier.G cim:UnitMultiplier.h cim:UnitMultiplier.T cim:UnitMultiplier.E cim:UnitMultiplier.f cim:UnitMultiplier.c cim:UnitMultiplier.none cim:UnitMultiplier.d cim:UnitMultiplier.a cim:UnitMultiplier.P cim:UnitMultiplier.p cim:UnitMultiplier.m cim:UnitMultiplier.M cim:UnitMultiplier.n]` 

### op:Measurement.unitMultiplier-cardinality

**Path:** `cim:Measurement.unitMultiplier`  
**Name:** Measurement.unitMultiplier-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitSymbol-cardinality

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:Measurement.unitSymbol-datatype

**Path:** `cim:Measurement.unitSymbol`  
**Name:** Measurement.unitSymbol-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not IRI (Internationalized Resource Identifier) or it is enumerated value not part of the profile."

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:UnitSymbol.WPerm2 cim:UnitSymbol.molPerkg cim:UnitSymbol.HPerm cim:UnitSymbol.Ah cim:UnitSymbol.N cim:UnitSymbol.mPerm3 cim:UnitSymbol.sPers cim:UnitSymbol.mol cim:UnitSymbol.m3Uncompensated cim:UnitSymbol.VPerV cim:UnitSymbol.kgm2 cim:UnitSymbol.radPers cim:UnitSymbol.m3Perkg cim:UnitSymbol.SPerm cim:UnitSymbol.Wb cim:UnitSymbol.bar cim:UnitSymbol.kat cim:UnitSymbol.V2 cim:UnitSymbol.cosPhi cim:UnitSymbol.Oe cim:UnitSymbol.min cim:UnitSymbol.Vs cim:UnitSymbol.Q cim:UnitSymbol.V2h cim:UnitSymbol.VA cim:UnitSymbol.dBm cim:UnitSymbol.CPerkg cim:UnitSymbol.Btu cim:UnitSymbol.JPerkg cim:UnitSymbol.lm cim:UnitSymbol.Qh cim:UnitSymbol.mPers2 cim:UnitSymbol.ha cim:UnitSymbol.s cim:UnitSymbol.rotPers cim:UnitSymbol.tonne cim:UnitSymbol.NPerm cim:UnitSymbol.A cim:UnitSymbol.A2 cim:UnitSymbol.Pa cim:UnitSymbol.VAh cim:UnitSymbol.none cim:UnitSymbol.HzPers cim:UnitSymbol.JPerm2 cim:UnitSymbol.JPerkgK cim:UnitSymbol.Nm cim:UnitSymbol.deg cim:UnitSymbol.S cim:UnitSymbol.kgPerJ cim:UnitSymbol.As cim:UnitSymbol.ohm cim:UnitSymbol.A2h cim:UnitSymbol.JPerm3 cim:UnitSymbol.T cim:UnitSymbol.m2Pers cim:UnitSymbol.onePerm cim:UnitSymbol.lx cim:UnitSymbol.lPers cim:UnitSymbol.d cim:UnitSymbol.C cim:UnitSymbol.WPersr cim:UnitSymbol.JPerK cim:UnitSymbol.character cim:UnitSymbol.APerA cim:UnitSymbol.rad cim:UnitSymbol.kg cim:UnitSymbol.V cim:UnitSymbol.therm cim:UnitSymbol.CPerm3 cim:UnitSymbol.VArh cim:UnitSymbol.Mx cim:UnitSymbol.ppm cim:UnitSymbol.WPerW cim:UnitSymbol.JPermolK cim:UnitSymbol.WPermK cim:UnitSymbol.ohmPerm cim:UnitSymbol.cd cim:UnitSymbol.WPerm2sr cim:UnitSymbol.h cim:UnitSymbol.G cim:UnitSymbol.VPerm cim:UnitSymbol.Bq cim:UnitSymbol.F cim:UnitSymbol.Vh cim:UnitSymbol.W cim:UnitSymbol.lPerl cim:UnitSymbol.GyPers cim:UnitSymbol.HzPerHz cim:UnitSymbol.Sv cim:UnitSymbol.H cim:UnitSymbol.molPerm3 cim:UnitSymbol.degC cim:UnitSymbol.mmHg cim:UnitSymbol.JPermol cim:UnitSymbol.sr cim:UnitSymbol.count cim:UnitSymbol.CPerm2 cim:UnitSymbol.mPers cim:UnitSymbol.radPers2 cim:UnitSymbol.m3Pers cim:UnitSymbol.KPers cim:UnitSymbol.anglemin cim:UnitSymbol.PaPers cim:UnitSymbol.VPerHz cim:UnitSymbol.ohmm cim:UnitSymbol.J cim:UnitSymbol.m2 cim:UnitSymbol.Hz cim:UnitSymbol.APerm cim:UnitSymbol.m3Perh cim:UnitSymbol.rev cim:UnitSymbol.WPerA cim:UnitSymbol.l cim:UnitSymbol.K cim:UnitSymbol.m3 cim:UnitSymbol.katPerm3 cim:UnitSymbol.WPers cim:UnitSymbol.lPerh cim:UnitSymbol.dB cim:UnitSymbol.m cim:UnitSymbol.FPerm cim:UnitSymbol.A2s cim:UnitSymbol.gal cim:UnitSymbol.kn cim:UnitSymbol.Pas cim:UnitSymbol.VPerVAr cim:UnitSymbol.VPerVA cim:UnitSymbol.VAr cim:UnitSymbol.anglesec cim:UnitSymbol.ft3 cim:UnitSymbol.charPers cim:UnitSymbol.m3Compensated cim:UnitSymbol.molPermol cim:UnitSymbol.M cim:UnitSymbol.onePerHz cim:UnitSymbol.JPers cim:UnitSymbol.Wh cim:UnitSymbol.Gy cim:UnitSymbol.gPerg cim:UnitSymbol.kgm cim:UnitSymbol.kgPerm3]` 

## op:StringMeasurementValue

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StringMeasurementValue

**Nested Properties:**

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-cardinality  
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

### op:MeasurementValue.MeasurementValueSource-cardinality

**Path:** `cim:MeasurementValue.MeasurementValueSource`  
**Name:** MeasurementValue.MeasurementValueSource-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.MeasurementValueSource-valueType

**Path:** `cim:MeasurementValue.MeasurementValueSource / rdf:type`  
**Name:** MeasurementValue.MeasurementValueSource-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:MeasurementValueSource"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:MeasurementValueSource]` 

### op:MeasurementValue.sensorAccuracy-cardinality

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.sensorAccuracy-datatype

**Path:** `cim:MeasurementValue.sensorAccuracy`  
**Name:** MeasurementValue.sensorAccuracy-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:float` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:MeasurementValue.timeStamp-cardinality

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:MeasurementValue.timeStamp-datatype

**Path:** `cim:MeasurementValue.timeStamp`  
**Name:** MeasurementValue.timeStamp-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:dateTime` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

### op:StringMeasurementValue.StringMeasurement-cardinality

**Path:** `cim:StringMeasurementValue.StringMeasurement`  
**Name:** StringMeasurementValue.StringMeasurement-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:StringMeasurementValue.StringMeasurement-valueType

**Path:** `cim:StringMeasurementValue.StringMeasurement / rdf:type`  
**Name:** StringMeasurementValue.StringMeasurement-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:StringMeasurement"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:StringMeasurement]` 

## op:ValueAliasSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ValueAliasSet

**Nested Properties:**

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

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
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

## op:ValueToAlias

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ValueToAlias

**Nested Properties:**

### io:IdentifiedObject.description-cardinality

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Cardinality violation. Upper bound shall be 1"

**Constraints:**

- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### io:IdentifiedObject.description-datatype

**Path:** `cim:IdentifiedObject.description`  
**Name:** IdentifiedObject.description-datatype  
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

### io:IdentifiedObject.name-cardinality

**Path:** `cim:IdentifiedObject.name`  
**Name:** IdentifiedObject.name-cardinality  
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

### op:ValueToAlias.ValueAliasSet-cardinality

**Path:** `cim:ValueToAlias.ValueAliasSet`  
**Name:** ValueToAlias.ValueAliasSet-cardinality  
This constraint validates the cardinality of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "Missing required association."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:ValueToAlias.ValueAliasSet-valueType

**Path:** `cim:ValueToAlias.ValueAliasSet / rdf:type`  
**Name:** ValueToAlias.ValueAliasSet-valueType  
This constraint validates the value type of the association at the used direction.

**Severity:** sh:Violation

**Messages:**
- "One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall be an instance of the class: cim:ValueAliasSet"

**Constraints:**

- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:IRI` 
- **sh:InConstraintComponent** (Severity: sh:Violation)
  - Values: `[cim:ValueAliasSet]` 

### op:ValueToAlias.value-cardinality

**Path:** `cim:ValueToAlias.value`  
**Name:** ValueToAlias.value-cardinality  
This constraint validates the cardinality of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "Missing required property (attribute)."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 
- **sh:MaxCountConstraintComponent** (Severity: sh:Violation)
  - MaxCount: `1` 

### op:ValueToAlias.value-datatype

**Path:** `cim:ValueToAlias.value`  
**Name:** ValueToAlias.value-datatype  
This constraint validates the datatype of the property (attribute).

**Severity:** sh:Violation

**Messages:**
- "The datatype is not literal or it violates the xsd datatype."

**Constraints:**

- **sh:DatatypeConstraintComponent** (Severity: sh:Violation)
  - Datatype: `xsd:integer` 
- **sh:NodeKindConstraintComponent** (Severity: sh:Violation)
  - NodeKind: `sh:Literal` 

