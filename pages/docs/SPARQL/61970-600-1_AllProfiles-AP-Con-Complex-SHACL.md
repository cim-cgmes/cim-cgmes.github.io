# 61970-600-1_AllProfiles-AP-Con-Complex-SHACL

## all600:Float

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:FloatSpecialValues

**Nested Properties:**

### all600:Float-specialValues

**Path:** `rdf:type`  
**Name:** C:301:ALL:Float:specialValues  
W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes allows use of the following special values: INF, NaN to express quantities such as positive infinity, negative infinity, and not a number. CIM data types in general and the primitive Float are restricted not to use INF and NaN, if not explicitly allowed in a description of an attribute.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
          ?s ?p ?value .
          #BIND(str($this) AS ?value).
          FILTER(isLiteral(?this) && DATATYPE(?value)=xsd:float && (!isNumeric($this) || CONTAINS(?value, "NaN") || CONTAINS(?value, "INF"))).
          #FILTER(!isNumeric($this) || CONTAINS(?value, "NaN") || CONTAINS(?value, "INF")).
			}
```
  - Messages: `["INF or NaN used in an attributes defined as float or the values is not a numeric value."]`

## all600:FullModel

**Severity:** sh:Violation

## all600:FullModelDateTime

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

**Nested Properties:**

### all600:Model.created-HGEN4

**Path:** `mdc:Model.created`  
**Name:** C:600:ALL:Model.created:HGEN4  
Applications shall comply with the following additions (compared to IEC 61970-552:2016, Table 2) to the header definition amended by CGMES: Model.created - It is the time of the serialization. The format is an extended format according to the ISO 8601-2005. European exchanges shall refer to UTC.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
          $this $PATH ?value .
          FILTER(!STRENDS(str(?value),"Z")).
			}
```
  - Messages: `["File header Model.created is not a valid UTC date time."]`

### all600:Model.scenarioTime-HGEN4

**Path:** `mdc:Model.scenarioTime`  
**Name:** C:600:ALL:Model.scenarioTime:HGEN4  
Applications shall comply with the following additions (compared to IEC 61970-552:2016, Table 2) to the header definition amended by CGMES: Model.scenarioTime - This is the date and time that this model represents, i.e. for which the model is valid. The format is an extended format according to the ISO 8601-2005. European exchanges shall refer to UTC.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
          $this $PATH ?value .
          FILTER(!STRENDS(str(?value),"Z")).
			}
```
  - Messages: `["File header Model.scenarioTime is not a valid UTC date time."]`

## all600:FullModelProf11

**Severity:** sh:Violation

**Targets:**
- targetClass: diff:DifferenceModel
- targetClass: mdc:FullModel

## all600:IDuniqueness

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:IDuniqueness

**Nested Properties:**

### all600:All-GENC1

**Path:** `rdf:type`  
**Name:** C:600:ALL:NA:GENC1  
All IdentifiedObject-s shall have a persistent and globally unique identifier (Master Resource Identifier - mRID).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this (COUNT(?value) AS ?counts) ?value
			WHERE {
          ?value rdf:type ?o.
          FILTER(?o!=cim:Equipment).
			}
      GROUP BY $this ?value
      HAVING(?counts>1)
      
```
  - Messages: `["Not an unique identifier."]`

## all600:IDuuidCheck

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:IDchecks

**Nested Properties:**

### all600:All-GENC5

**Path:** `rdf:type`  
**Name:** C:600:ALL:NA:GENC5  
(deprecated) A requirement to ensure transition until all systems and entities fully comply with GENC4. The CGMES defines the identifier as a non-case sensitive string which conforms to W3C (ISO 8859-1:1998, Information technology — 8-bit single-byte coded graphic character sets — Part 1: Latin alphabet No. 1, http://www.w3.org/MarkUp/html3/specialchars.html). A prefix may be added, if necessary, to ensure global uniqueness. The rdf:ID is the mRID plus an underscore _ added in the beginning of the string. The maximum character limit of the string is 60 characters (including an underscore and a prefix, if any).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
          ?value rdf:type ?o.
          #BIND(str(?s) AS ?uuid) .
          #$this rdf:type ?value .
          #BIND(str($this) AS ?uuid) .
          BIND(STRAFTER(str(?value),"#_") AS ?secondpart) .
          FILTER(STRLEN(?secondpart)>59 && ?secondpart="" && !REGEX(STR(?uuid), "^urn:uuid:[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$", "i") ).
			}
```
  - Messages: `["The ID string is more than 60 characters or the string does not begin with underscore."]`

### all600:All-GENC4

**Path:** `rdf:type`  
**Name:** C:600:ALL:NA:GENC4  
IEC 61970-301 strongly recommends to use UUID, as specified in RFC 4122, for the .mRID. CGMES requires the usage of UUID.

**Severity:** sh:Info

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Info)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
          ?value rdf:type ?o.
          BIND(str(?value) AS ?uuid) .
          #BIND(str($this) AS ?uuid) .
          BIND(STRAFTER(?uuid,"#_") AS ?secondpart) .
          FILTER(!REGEX(?secondpart, "^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$", "i") && !REGEX(STR(?uuid), "^urn:uuid:[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$", "i")).
			}
```
  - Messages: `["Invalid syntax of ID (rdf:ID or rdf:about)."]`

## all600:MarpRule

**Severity:** sh:Violation

**Targets:**
- targetClass: mdc:FullModel
- targetClass: diff:DifferenceModel

**Nested Properties:**

### all600:Model.modelingAuthoritySet-marp10-12

**Path:** `mdc:Model.modelingAuthoritySet`  
**Name:** C:600:ALL:Model.modelingAuthoritySet:marp10-12  
MARP10: The model authority set defined in file header of a state variable instance file of a merged model is the model authority set which creates the state variables. MARP11:The model authority set defined in file header of a diagram layout instance file of a merged model is the model authority set which creates the diagram layout. MARP12:The model authority set defined in file header of a topology instance file of a merged model is the model authority set which creates the topology as an output of topology processing.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value 
			WHERE {
          $this $PATH ?value .
          FILTER(STRLEN(str(?value))=0).
			}
```
  - Messages: `["The property is defined as empty property."]`

