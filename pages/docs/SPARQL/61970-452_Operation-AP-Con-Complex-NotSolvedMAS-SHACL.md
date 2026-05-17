# 61970-452_Operation-AP-Con-Complex-NotSolvedMAS-SHACL

## op452n:Measurement.Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Accumulator
- targetClass: cim:Discrete
- targetClass: cim:StringMeasurement
- targetClass: cim:Analog

**Nested Properties:**

### op452n:Measurement.Terminal-requiredCases

**Path:** `cim:Measurement.PowerSystemResource`  
The association Measurement.Terminal shall reference a Terminal of the Equipment referenced by Measurement.PowerSystemResource except in cases where Measurement.measurementType is either TapPosition or SwitchPosition in which the association is not exchanged.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value ?terminal ?terminal1 ?terminal2 ?terminal3 ?meastype
			WHERE {
             $this $PATH ?value .
             OPTIONAL {$this cim:Measurement.Terminal ?terminal}.
             $this cim:Measurement.measurementType ?meastype . 
             ?terminal1 cim:Terminal.ConductingEquipment ?value ;
                        cim:ACDCTerminal.sequenceNumber 1 .
             OPTIONAL {?terminal2 cim:Terminal.ConductingEquipment ?value ;
                        cim:ACDCTerminal.sequenceNumber 2 .}
             OPTIONAL {?terminal3 cim:Terminal.ConductingEquipment ?value ;
                        cim:ACDCTerminal.sequenceNumber 3 .}
				FILTER ((bound(?terminal) && (?meastype="TapPosition" || ?meastype="SwitchPosition" )) || (!bound(?terminal) && !(?meastype="TapPosition" || ?meastype="SwitchPosition" )) || (bound(?terminal) && ((?terminal!=?terminal1 && !bound(?terminal2) && !bound(?terminal3)) || (bound(?terminal2) && !bound(?terminal3) && ?terminal!=?terminal1 && ?terminal!=?terminal2) || (bound(?terminal2) && bound(?terminal3) && ?terminal!=?terminal1 && ?terminal!=?terminal2 && ?terminal!=?terminal3)))) .
			}
```
  - Messages: `["Either the Terminal associated by Measurement.Terminal is not a terminal of the equipment associated via Measurement.PowerSystemResource or the association is present for Measurement.measurementType TapPosition or SwitchPosition. Details: Associated terminal ID:{?terminal}; Equipment's Terminal 1 ID:{?terminal1}; Equipment's Terminal 2 ID:{?terminal2}; Equipment's Terminal 3 ID:{?terminal3}; Measurement type:{?meastype}."]`

