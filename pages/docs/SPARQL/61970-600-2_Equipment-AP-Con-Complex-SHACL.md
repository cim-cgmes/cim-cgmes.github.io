# 61970-600-2_Equipment-AP-Con-Complex-SHACL

## eq600-2:GeographicalRegionCountShape

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:GeographicalRegion

## eq600-2:ReactiveCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ReactiveCapabilityCurve

**Nested Properties:**

### eq600-2:ReactiveCapabilityCurve-units

**Path:** `rdf:type`  
**Name:** C:600:EQ:ReactiveCapabilityCurve:units  
For a ReactiveCapabilityCurve associated with SynchronousMachine, the Curve.xUnit shall be set to UnitSymbol.W and both Curve.y1Unit and Curve.y2Unit shall be set to UnitSymbol.VAr. As the multiplier is not included in the profile it is defined the same as the multiplier used for datatype ActivePower and ReactivePower, i.e. UnitMultiplier.M.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        $this ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/rdf:type cim:SynchronousMachine .
        $this cim:Curve.xUnit ?xunit .
        $this cim:Curve.y1Unit ?y1unit .
        $this cim:Curve.y2Unit ?y2unit .
        BIND(EXISTS{$this cim:Curve.y2Unit ?y2unitcheck} AS ?hasy2unit).
        FILTER (?hasy2unit=false && ?xunit!=cim:UnitSymbol.W && ?y2unit!=cim:UnitSymbol.VAr && ?y1unit!=cim:UnitSymbol.VAr).
        }
```
  - Messages: `["Not correct or not provided units of a ReactiveCapabilityCurve of a SynchronousMachine."]`

## eq600-2:RotatingMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine

## eq600-2:SubstationCountShape

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:SubstationCount

**Nested Properties:**

### eq600-2:Substation-count

**Path:** `rdf:type`  
**Name:** C:600:EQ:Substation:count  
The number of Substation-s shall reflect the design of the power system. Cases of a single Substation in a power system model or having a Substation per VoltageLevel are reported as warnings.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?substations ?voltagelevels
        WHERE {
        {
          SELECT $this (COUNT(?ss) AS ?substations)
          WHERE {
            ?ss rdf:type cim:Substation .
          }
          GROUP BY $this
        }
        {
          SELECT $this (COUNT(?vl) AS ?voltagelevels)
          WHERE {
            ?vl rdf:type cim:VoltageLevel .
          }
          GROUP BY $this
        }
        
        FILTER (?substations=1 || ?substations=?voltagelevels).
        }
```
  - Messages: `["The model has either one Substation or a Substation per VoltageLevel. Number of Substation-s: {?substations}. Number of VoltageLevel-s: {?voltagelevels}."]`

## eq600-2:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### eq600-2:TapChanger.neutralU-valueRangePair

**Path:** `cim:TapChanger.neutralU`  
**Name:** C:600:EQ:TapChanger.neutralU:ValueRangePair  
The TapChanger.neutralU shall be the same as PowerTransformerEnd.ratedU.

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
        OPTIONAL {$this cim:RatioTapChanger.TransformerEnd/cim:PowerTransformerEnd.ratedU ?rratedu } .
        OPTIONAL {$this cim:PhaseTapChanger.TransformerEnd/cim:PowerTransformerEnd.ratedU ?pratedu } .
        FILTER ((bound(?rratedu) && ?value!=?rratedu) || (bound(?pratedu) && ?value!=?pratedu)).
        }
```
  - Messages: `["The value is not the same as the PowerTransformerEnd.ratedU."]`

