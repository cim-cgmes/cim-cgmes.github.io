# 61970-600-2_IdentifiedObjectCommon_AP-Con-Complex-SHACL

## iosl:IdentifiedObjectStringLength

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:IdentifiedObjectStringLength

**Nested Properties:**

### iosl:IdentifiedObject.shortName-stringLength

**Path:** `rdf:type`  
Length of the string 12 characters maximum.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value  
			WHERE {      
        ?s eu:IdentifiedObject.shortName ?value
        
        FILTER (STRLEN(?value)>12) .
			}
```
  - Messages: `["String length is greater than 12 characters."]`

### iosl:IdentifiedObject.energyIdentCodeEic-stringLength

**Path:** `rdf:type`  
The length of the string is 16 characters as defined by the EIC code.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value  
			WHERE {      
        ?s eu:IdentifiedObject.energyIdentCodeEic ?value
        
        FILTER (STRLEN(?value)!=16) .
			}
```
  - Messages: `["String length is not 16 characters."]`

### iosl:IdentifiedObject.name-stringLength

**Path:** `rdf:type`  
The string IdentifiedObject.name has a maximum of 128 characters.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value  
			WHERE {      
        ?s cim:IdentifiedObject.name ?value
        
        FILTER (STRLEN(?value)>128) .
			}
```
  - Messages: `["String length is greater than 128 characters."]`

### iosl:IdentifiedObject.description-stringLength

**Path:** `rdf:type`  
The string IdentifiedObject.description is maximum 256 characters.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value  
			WHERE {      
        ?s cim:IdentifiedObject.description ?value
        
        FILTER (STRLEN(?value)>256) .
			}
```
  - Messages: `["String length is greater than 256 characters."]`

