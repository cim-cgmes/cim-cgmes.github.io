# 61970-452_ShortCircuit-AP-Con-Complex-SHACL

## sc452c:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### sc452c:SynchronousMachine-attributes

**Path:** `cim:SynchronousMachine.earthing`  
**Name:** C:452:SC:SynchronousMachine.earthing:attributes  
If SynchronousMachine.earthing is true, then SynchronousMachine.earthingStarPointR and SynchronousMachine.earthingStarPointX are required.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:SynchronousMachine.earthingStarPointR ?earthingStarPointR} .
        OPTIONAL {$this cim:SynchronousMachine.earthingStarPointX ?earthingStarPointX} .
        FILTER (?value=true && (!bound(?earthingStarPointR) || !bound(?earthingStarPointX))) .        
			}
```
  - Messages: `["Missing required properties .earthingStarPointR or .earthingStarPointX."]`

## sc452c:TransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### sc452c:TransformerEnd-grounding

**Path:** `cim:TransformerEnd.grounded`  
**Name:** C:452:SC:PowerTransformerEnd.grounded:grounding  
If TransformerEnd.grounded is true, then TransformerEnd.rground and TransformerEnd.xground are required.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:TransformerEnd.rground ?rground} .
        OPTIONAL {$this cim:TransformerEnd.xground ?xground} .
        FILTER (?value=true && (!bound(?xground) || !bound(?rground))) .        
			}
```
  - Messages: `["Missing required properties .rground or .xground."]`

