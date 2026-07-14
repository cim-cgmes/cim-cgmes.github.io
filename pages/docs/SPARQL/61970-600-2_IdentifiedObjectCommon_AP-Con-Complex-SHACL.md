# 61970-600-2_IdentifiedObjectCommon_AP-Con-Complex-SHACL

## iosl:IdentifiedObjectStringLengthDescription

**Severity:** sh:Violation

**Targets:**
- targetSubjectsOf: cim:IdentifiedObject.description

**Nested Properties:**

### iosl:IdentifiedObject.description-stringLength

**Path:** `cim:IdentifiedObject.description`  
**Name:** C:452:ALL:IdentifiedObject.description:stringLength|C:600:EQBD:IdentifiedObject.description:stringLength|C:457:DY:IdentifiedObject.description:stringLength|C:456:TP:IdentifiedObject.description:stringLength  
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
        ?s $PATH ?value .
        
        FILTER (STRLEN(?value)>256) .
			}
```
  - Messages: `["String length is greater than 256 characters."]`

## iosl:IdentifiedObjectStringLengthName

**Severity:** sh:Violation

**Targets:**
- targetSubjectsOf: cim:IdentifiedObject.name

**Nested Properties:**

### iosl:IdentifiedObject.name-stringLength

**Path:** `cim:IdentifiedObject.name`  
**Name:** C:452:ALL:IdentifiedObject.name:stringLength|C:453:DL:IdentifiedObject.name:stringLength|C:456:TP:IdentifiedObject.name:stringLength|C:456:SV:IdentifiedObject.name:stringLength|C:457:DY:IdentifiedObject.name:stringLength|C:600:EQBD:IdentifiedObject.name:stringLength  
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
        ?s $PATH ?value .
        
        FILTER (STRLEN(?value)>128) .
			}
```
  - Messages: `["String length is greater than 128 characters."]`

## iosl:IdentifiedObjectStringLengthenergyIdentCodeEic

**Severity:** sh:Violation

**Targets:**
- targetSubjectsOf: cim100:IdentifiedObject.energyIdentCodeEic

**Nested Properties:**

### iosl:IdentifiedObject.energyIdentCodeEic-stringLength

**Path:** `cim100:IdentifiedObject.energyIdentCodeEic`  
**Name:** C:301:EQ:IdentifiedObject.energyIdentCodeEic:stringLength|C:301:EQBD:IdentifiedObject.energyIdentCodeEic:stringLength|C:301:TP:IdentifiedObject.energyIdentCodeEic:stringLength  
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
        ?s $PATH ?value .
        
        FILTER (STRLEN(?value)!=16) .
			}
```
  - Messages: `["String length is not 16 characters."]`

## iosl:IdentifiedObjectStringLengthshortName

**Severity:** sh:Violation

**Targets:**
- targetSubjectsOf: cim100:IdentifiedObject.shortName

**Nested Properties:**

### iosl:IdentifiedObject.shortName-stringLength

**Path:** `cim100:IdentifiedObject.shortName`  
**Name:** C:301:EQ:IdentifiedObject.shortName:stringLength|C:301:EQBD:IdentifiedObject.shortName:stringLength||C:301:TP:IdentifiedObject.shortName:stringLength  
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
        ?s $PATH ?value .
        
        FILTER (STRLEN(?value)>12) .
			}
```
  - Messages: `["String length is greater than 12 characters."]`

