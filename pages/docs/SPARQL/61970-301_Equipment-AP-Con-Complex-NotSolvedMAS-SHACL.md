# 61970-301_Equipment-AP-Con-Complex-NotSolvedMAS-SHACL

## eq301n:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

**Nested Properties:**

### eq301n:ACLineSegment-baseVoltage

**Path:** `rdf:type`  
**Name:** C:301:EQ:ACLineSegment:baseVoltage  
The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines may have slightly different BaseVoltage.nominalVoltages and variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?voltage1 ?voltage2
			WHERE {
        ?terminal1 cim:Terminal.ConductingEquipment $this .
        ?terminal2 cim:Terminal.ConductingEquipment $this .
        ?terminal1 cim:ACDCTerminal.sequenceNumber 1 .
        ?terminal2 cim:ACDCTerminal.sequenceNumber 2 .
        ?terminal1 cim:Terminal.TopologicalNode ?topologicalnode1 .
        ?terminal2 cim:Terminal.TopologicalNode ?topologicalnode2 .
        ?topologicalnode1 cim:TopologicalNode.BaseVoltage/cim:BaseVoltage.nominalVoltage ?voltage1 .
        ?topologicalnode2 cim:TopologicalNode.BaseVoltage/cim:BaseVoltage.nominalVoltage ?voltage2 .
				FILTER (?terminal1 != ?terminal2 && ?voltage1 != ?voltage2 && ?topologicalnode1 != ?topologicalnode2) .
			}
```
  - Messages: `["The ACLineSegment has different BaseVoltage.nominalVoltage at the two end of the ACLineSegment. Voltage at end 1 is: {?voltage1}. Voltage at end 2 is: {?voltage2}."]`

