# 61970-452_Equipment-AP-Con-Complex-SHACL

## eq452c:ACDCConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter
- targetClass: cim:VsConverter

## eq452c:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

## eq452c:AuxiliaryEquipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WaveTrap
- targetClass: cim:FaultIndicator
- targetClass: cim:CurrentTransformer
- targetClass: cim:PotentialTransformer
- targetClass: cim:PostLineSensor
- targetClass: cim:SurgeArrester

## eq452c:Breaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:BusbarSection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BusbarSection

## eq452c:Clamp

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Clamp

## eq452c:ConductingEquipment-twoTerminalsShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCSwitch
- targetClass: cim:DCChopper
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:Jumper
- targetClass: cim:Breaker
- targetClass: cim:Cut
- targetClass: cim:ACLineSegment
- targetClass: cim:DCBreaker
- targetClass: cim:Disconnector
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:EquivalentBranch
- targetClass: cim:DCLineSegment
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCDisconnector
- targetClass: cim:Switch

**Nested Properties:**

### eq452c:Terminal-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Terminal:connection  
Terminal-s of the two sides of a two-terminal ConductingEquipment (or any of its subclasses) shall not be connected to the same ConnectivityNode.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value
        WHERE {
          ?term1 cim:Terminal.ConductingEquipment $this .
          ?term2 cim:Terminal.ConductingEquipment $this .

          ?term1 cim:ACDCTerminal.sequenceNumber 1 .
          ?term2 cim:ACDCTerminal.sequenceNumber 2 .
          
          ?term1 cim:Terminal.ConnectivityNode ?cn1 .         
          ?term2 cim:Terminal.ConnectivityNode ?cn2 .
          FILTER (?cn1=?cn2).
        } 
```
  - Messages: `["Terminal-s of a  two-terminal ConductingEquipment (or any of its subclasses) connect to the same ConnectivityNode."]`

## eq452c:Conductor

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

## eq452c:CurveData

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurveData

**Nested Properties:**

### eq452c:CurveData-equationY2

**Path:** `cim:CurveData.Curve`  
**Name:** C:452:EQ:CurveData.Curve:equationY2  
If CurveData.Curve is a ReactiveCapabilityCurve, each CurveData shall satisfy the following relation: CurveData.xvalue^2+CurveData.y2value^2 shall be less than or equal to RotatingMachine.ratedS^2.

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
        ?value rdf:type cim:ReactiveCapabilityCurve .
        $this cim:CurveData.xvalue ?xvalue .
        $this cim:CurveData.y2value ?y2value.
        #OPTIONAL {$this cim:CurveData.y2value ?y2value } .
        #BIND (EXISTS{?value ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:RotatingMachine.ratedS ?rateds} AS ?smrateds).
        ?value ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:RotatingMachine.ratedS ?rateds .
        #FILTER (?smrateds=true && bound(?y2value) && (?xvalue*?xvalue+?y2value*?y2value)>?rateds*?rateds) .
        FILTER ((?xvalue*?xvalue+?y2value*?y2value)>?rateds*?rateds) .
        } 
```
  - Messages: `["The following is not fulfilled: CurveData.xvalue^2+CurveData.y2value^2 shall be less than or equal to RotatingMachine.ratedS^2."]`

### eq452c:CurveData-equationY1

**Path:** `cim:CurveData.Curve`  
**Name:** C:452:EQ:CurveData.Curve:equationY1  
If CurveData.Curve is a ReactiveCapabilityCurve, each CurveData shall satisfy the following relation: CurveData.xvalue^2+CurveData.y1value^2 shall be less than or equal to RotatingMachine.ratedS^2.

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
        ?value rdf:type cim:ReactiveCapabilityCurve .
        $this cim:CurveData.xvalue ?xvalue .
        $this cim:CurveData.y1value ?y1value  .
        #BIND (EXISTS{?value ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:RotatingMachine.ratedS ?rateds} AS ?smrateds).
        ?value ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:RotatingMachine.ratedS ?rateds .
        #FILTER ( ?smrateds=true && (?xvalue*?xvalue+?y1value*?y1value)>?rateds*?rateds) .
        FILTER ( (?xvalue*?xvalue+?y1value*?y1value)>?rateds*?rateds) .
        } 
```
  - Messages: `["The following is not fulfilled: CurveData.xvalue^2+CurveData.y1value^2 shall be less than or equal to RotatingMachine.ratedS^2."]`

### eq452c:CurveData-reactive

**Path:** `rdf:type`  
**Name:** C:452:EQ:CurveData.Curve:reactive  
If CurveData.Curve is a ReactiveCapabilityCurve, the CurveData.y2value shall be greater than or equal to CurveData.y1value.It is not allowed that all CurveData.y2value values are equal to CurveData.y1value values.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	    SELECT $this ?value ?countcd ?sumy1v ?sumy2v
      WHERE {
        {
        SELECT $this (COUNT(?curvedtype) AS ?countcd) (SUM(?y1v) AS ?sumy1v) (SUM(?y2v) AS ?sumy2v)
        WHERE {
        $this cim:CurveData.Curve/rdf:type cim:ReactiveCapabilityCurve .
        $this cim:CurveData.Curve/^cim:CurveData.Curve ?curved .
        #$this cim:CurveData.Curve ?rcc .
        #?rcc rdf:type ?curvetype .
        #?rcc ^cim:CurveData.Curve ?curved .
        ?curved rdf:type ?curvedtype .
        ?curved cim:CurveData.y1value ?y1v.
        ?curved cim:CurveData.y2value ?y2v.
        #OPTIONAL {?curved cim:CurveData.y2value ?y2v }.
        #FILTER(bound(?y2v)).
        }
        GROUP BY $this ?curvedtype
        }
        
        $this cim:CurveData.Curve ?value .
        #?value rdf:type ?curvetype .
        ?value rdf:type cim:ReactiveCapabilityCurve .
        $this cim:CurveData.y1value ?y1value  .
        $this cim:CurveData.y2value ?y2value.
        #OPTIONAL {$this cim:CurveData.y2value ?y2value }.
        #FILTER (?curvetype=cim:ReactiveCapabilityCurve && bound(?y2value) && (?y2value<?y1value || (?y2value=?sumy1v/?countcd && ?y1value=?sumy2v/?countcd ))) .
        FILTER ((?y2value<?y1value || (?y2value=?sumy1v/?countcd && ?y1value=?sumy2v/?countcd ))) .
        } 
```
  - Messages: `["Either CurveData.y2value is not >= CurveData.y1value or CurveData.y2value = CurveData.y1value for all curve points."]`

## eq452c:Cut

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Cut

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:DCBusbar

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBusbar

## eq452c:DCChopper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCChopper

## eq452c:DCGround

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCGround

## eq452c:DCLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCLineSegment

## eq452c:DCSeriesDevice

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSeriesDevice

## eq452c:DCShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCShunt

## eq452c:DCSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCDisconnector
- targetClass: cim:DCBreaker

## eq452c:DayType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DayType

## eq452c:DisconnectingCircuitBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:Disconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Disconnector

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:EarthFaultCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil

## eq452c:EnergyConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergySource
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:StaticVarCompensator
- targetClass: cim:SynchronousMachine
- targetClass: cim:EnergyConsumer
- targetClass: cim:NonConformLoad
- targetClass: cim:ConformLoad
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:AsynchronousMachine

## eq452c:EquivalentBranch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch

## eq452c:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

## eq452c:EquivalentShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentShunt

## eq452c:Fuse

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Fuse

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

## eq452c:GeneratingUnit-containmentNodeShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit

## eq452c:GeneratingUnit.aggregate

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### eq452c:AsynchronousMachine-aggregate

**Path:** `cim:Equipment.aggregate`  
**Name:** C:452:EQ:AsynchronousMachine:aggregate  
If one AsynchronousMachine is associated with one GeneratingUnit the flag Equipment.aggregate shall be consistent in case it is provided at both AsynchronousMachine and GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	    SELECT $this ?sms ?value 
      WHERE {
        {
        SELECT $this (COUNT(?typesm) AS ?sms) 
        WHERE {
        #BIND(EXISTS{$this ^cim:RotatingMachine.GeneratingUnit/rdf:type cim:AsynchronousMachine} AS ?hasam).
        $this ^cim:RotatingMachine.GeneratingUnit/rdf:type ?typesm.
        #OPTIONAL {?sm cim:RotatingMachine.GeneratingUnit $this }.
        #OPTIONAL {?sm rdf:type ?typesm }.
        #FILTER(?typesm=cim:AsynchronousMachine && ?hasam=true).
        FILTER(?typesm=cim:AsynchronousMachine).
        }
        GROUP BY $this ?typesm 
        }
        $this $PATH ?value.
        #OPTIONAL {$this $PATH ?value }.
        #OPTIONAL {?sm cim:RotatingMachine.GeneratingUnit $this }.
        #OPTIONAL {?sm cim:Equipment.aggregate ?smaggregate }.
        $this ^cim:RotatingMachine.GeneratingUnit/cim:Equipment.aggregate ?smaggregate .
        #BIND(EXISTS{$this ^cim:RotatingMachine.GeneratingUnit/cim:Equipment.aggregate ?smaggregatea} AS ?hasaggr).
        #FILTER (?sms=1 && bound(?value) && ?hasaggr=true && ?value!=?smaggregate ) .
        FILTER (?sms=1 && ?value!=?smaggregate ) .
        } 
```
  - Messages: `["The value is not consistent with .aggregate for the associated GeneratingUnit."]`

### eq452c:SynchronousMachine-aggregate

**Path:** `cim:Equipment.aggregate`  
**Name:** C:452:EQ:SynchronousMachine:aggregate  
If only one SynchronousMachine is associated with the GeneratingUnit then the Equipment.aggregate flag shall be consistent between the SynchronousMachine and GeneratingUnit if it exists in both.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	    SELECT $this ?sms ?value 
      WHERE {
        {
        SELECT $this (COUNT(?typesm) AS ?sms) 
        WHERE {
        #BIND(EXISTS{$this ^cim:RotatingMachine.GeneratingUnit/rdf:type cim:SynchronousMachine} AS ?hasam).
        $this ^cim:RotatingMachine.GeneratingUnit/rdf:type ?typesm.
        #OPTIONAL {?sm cim:RotatingMachine.GeneratingUnit $this }.
        #OPTIONAL {?sm rdf:type ?typesm }.
        FILTER(?typesm=cim:SynchronousMachine ).
        }
        GROUP BY $this ?typesm 
        }
        $this $PATH ?value.
        #OPTIONAL {$this $PATH ?value }.
        #OPTIONAL {?sm cim:RotatingMachine.GeneratingUnit $this }.
        #OPTIONAL {?sm cim:Equipment.aggregate ?smaggregate }.
        $this ^cim:RotatingMachine.GeneratingUnit/cim:Equipment.aggregate ?smaggregate .
        #BIND(EXISTS{$this ^cim:RotatingMachine.GeneratingUnit/cim:Equipment.aggregate ?smaggregatea} AS ?hasaggr).
        #FILTER (?sms=1 && bound(?value) && ?hasaggr=true && ?value!=?smaggregate ) .
        FILTER (?sms=1 && ?value!=?smaggregate ) .
        } 
```
  - Messages: `["The value is not consistent with .aggregate for the associated GeneratingUnit."]`

## eq452c:Ground

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Ground

## eq452c:GroundDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

### eq452c:HydroGeneratingUnit.energyConversionCapability-typeConsistency

**Path:** `rdf:type`  
**Name:** C:452:EQ:HydroGeneratingUnit.energyConversionCapability:typeConsistency  
If HydroGeneratingUnit.energyConversionCapability is generator the associated SynchronousMachine shall have SynchronousMachine.type set to generator or generatorOrCondenser. If HydroGeneratingUnit.energyConversionCapability is pumpAndGenerator the associated SynchronousMachine shall have SynchronousMachine.type set to motor, generatorOrMotor or generatorOrCondenserOrMotor.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value
        WHERE {
          $this cim:HydroGeneratingUnit.energyConversionCapability ?value .
          #OPTIONAL {$this cim:HydroGeneratingUnit.energyConversionCapability ?value }.
          $this ^cim:RotatingMachine.GeneratingUnit/cim:SynchronousMachine.type ?type.
          #FILTER ((bound(?value) && ?value=cim:HydroEnergyConversionKind.generator && ?type NOT IN (cim:SynchronousMachineKind.generator, cim:SynchronousMachineKind.generatorOrCondenser ) ) || (bound(?value) && ?value=cim:HydroEnergyConversionKind.pumpAndGenerator && ?type NOT IN (cim:SynchronousMachineKind.motor, cim:SynchronousMachineKind.generatorOrMotor, cim:SynchronousMachineKind.generatorOrCondenserOrMotor) )).
          FILTER ((?value=cim:HydroEnergyConversionKind.generator && ?type NOT IN (cim:SynchronousMachineKind.generator, cim:SynchronousMachineKind.generatorOrCondenser ) ) || (?value=cim:HydroEnergyConversionKind.pumpAndGenerator && ?type NOT IN (cim:SynchronousMachineKind.motor, cim:SynchronousMachineKind.generatorOrMotor, cim:SynchronousMachineKind.generatorOrCondenserOrMotor) )).
        } 
```
  - Messages: `["The HydroGeneratingUnit.energyConversionCapability of the associated SynchronousMachine is not consistent with SynchronousMachine.type."]`

## eq452c:HydroPump

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroPump

## eq452c:Jumper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Jumper

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:Junction

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Junction

## eq452c:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### eq452c:ShuntCompensator-controlMode

**Path:** `rdf:type`  
**Name:** C:452:EQ:ShuntCompensator:controlMode  
For ShuntCompensator, the association RegulatingCondEq.RequlatingControl shall only point to a RequlatingControl that has the following control modes for RegulatingControl.mode: voltage, reactivePower and powerFactor.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:RegulatingCondEq.RegulatingControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:RegulatingCondEq.RegulatingControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.reactivePower && ?value!=cim:RegulatingControlModeKind.voltage && ?value!=cim:RegulatingControlModeKind.powerFactor).
        }
```
  - Messages: `["Unallowed regulating control mode for a ShuntCompensator."]`

## eq452c:LoadBreakSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### eq452c:ShuntCompensator-controlMode

**Path:** `rdf:type`  
**Name:** C:452:EQ:ShuntCompensator:controlMode  
For ShuntCompensator, the association RegulatingCondEq.RequlatingControl shall only point to a RequlatingControl that has the following control modes for RegulatingControl.mode: voltage, reactivePower and powerFactor.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:RegulatingCondEq.RegulatingControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:RegulatingCondEq.RegulatingControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.reactivePower && ?value!=cim:RegulatingControlModeKind.voltage && ?value!=cim:RegulatingControlModeKind.powerFactor).
        }
```
  - Messages: `["Unallowed regulating control mode for a ShuntCompensator."]`

## eq452c:NonlinearShuntCompensatorPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensatorPoint

## eq452c:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

## eq452c:OperationalLimitSet

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitSet

**Nested Properties:**

### eq452c:OperationalLimitSet-limits

**Path:** `rdf:type`  
**Name:** C:452:EQ:OperationalLimitSet:limits  
In case the OperationalLimitSet is the operational limit of the AuxiliaryEquipment, then the association end OperationalLimitSet.Equipment is also required. In the case where OperationalLimitSet.Equipment is associated with an instance of ConductingEquipment, OperationalLimitSet.Terminal shall be one of the ConductingEquipment’s Terminal-s.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT DISTINCT $this ?value
        WHERE {
          $this cim:OperationalLimitSet.Terminal ?olsterm .
          OPTIONAL{$this cim:OperationalLimitSet.Terminal/^cim:AuxiliaryEquipment.Terminal ?auxeq } .
          OPTIONAL{$this cim:OperationalLimitSet.Equipment ?equipment .
                   ?equipment rdf:type ?value .
                   BIND(EXISTS{?equipment ^cim:Terminal.ConductingEquipment ?olsterm} AS ?termmatch).
                  }.
          
          FILTER ((!bound(?equipment) && bound(?auxeq)) ||
                  (bound(?equipment) && ?termmatch=false && ?value NOT IN (cim:CurrentTransformer, cim:PotentialTransformer, cim:PostLineSensor, cim:SurgeArrester, cim:WaveTrap, cim:FaultIndicator, cim:PowerElectronicsWindUnit, cim:PhotoVoltaicUnit, cim:BatteryUnit, cim:HydroPump, cim:GeneratingUnit, cim:HydroGeneratingUnit, cim:NuclearGeneratingUnit, cim:SolarGeneratingUnit, cim:ThermalGeneratingUnit, cim:WindGeneratingUnit, cim:Equipment) )
                   ).
        }
```
  - Messages: `["Either OperationalLimitSet.Equipment is not provided for a Terminal that is associated with AuxiliaryEquipment or in case of ConductingEquipment the OperationalLimitSet.Terminal is not one of the the ConductingEquipment’s Terminal-s."]`

## eq452c:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

**Nested Properties:**

### eq452c:PhaseTapChanger-controlModeP

**Path:** `rdf:type`  
**Name:** C:452:EQ:PhaseTapChanger:controlModeP  
The association TapChanger.TapChangerControl for PhaseTapChanger-s shall only point to a TapChangerControl that has the following control modes for RegulatingControl.mode: activePower or voltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:TapChanger.TapChangerControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.activePower && ?value!=cim:RegulatingControlModeKind.voltage).
        }
```
  - Messages: `["Unallowed regulating control mode for a PhaseTapChanger."]`

## eq452c:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### eq452c:PhaseTapChanger-controlModeP

**Path:** `rdf:type`  
**Name:** C:452:EQ:PhaseTapChanger:controlModeP  
The association TapChanger.TapChangerControl for PhaseTapChanger-s shall only point to a TapChangerControl that has the following control modes for RegulatingControl.mode: activePower or voltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:TapChanger.TapChangerControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.activePower && ?value!=cim:RegulatingControlModeKind.voltage).
        }
```
  - Messages: `["Unallowed regulating control mode for a PhaseTapChanger."]`

## eq452c:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### eq452c:PhaseTapChanger-controlModeP

**Path:** `rdf:type`  
**Name:** C:452:EQ:PhaseTapChanger:controlModeP  
The association TapChanger.TapChangerControl for PhaseTapChanger-s shall only point to a TapChangerControl that has the following control modes for RegulatingControl.mode: activePower or voltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:TapChanger.TapChangerControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.activePower && ?value!=cim:RegulatingControlModeKind.voltage).
        }
```
  - Messages: `["Unallowed regulating control mode for a PhaseTapChanger."]`

## eq452c:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

**Nested Properties:**

### eq452c:PhaseTapChanger-controlModeP

**Path:** `rdf:type`  
**Name:** C:452:EQ:PhaseTapChanger:controlModeP  
The association TapChanger.TapChangerControl for PhaseTapChanger-s shall only point to a TapChangerControl that has the following control modes for RegulatingControl.mode: activePower or voltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:TapChanger.TapChangerControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.activePower && ?value!=cim:RegulatingControlModeKind.voltage).
        }
```
  - Messages: `["Unallowed regulating control mode for a PhaseTapChanger."]`

## eq452c:PowerTransformer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformer

**Nested Properties:**

### eq452c:PowerTransformerEnd.x-value

**Path:** `rdf:type`  
**Name:** C:452:EQ:PowerTransformerEnd.x:value  
Transformers with zero series reactance do not exist. PowerTransformerEnd.x of high voltage end in case of a two winding transformer shall be a positive value. In case of a three winding transformer the PowerTransformerEnd.x shall not be zero.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT DISTINCT $this  
        WHERE {
          
          $this ^cim:PowerTransformerEnd.PowerTransformer ?end1 ; 
                ^cim:PowerTransformerEnd.PowerTransformer ?end2 ;
                ^cim:PowerTransformerEnd.PowerTransformer ?end3 .
          
          #?end1 cim:PowerTransformerEnd.PowerTransformer $this .
          #?end2 cim:PowerTransformerEnd.PowerTransformer $this .
          #?end3 cim:PowerTransformerEnd.PowerTransformer $this .
          ?end1 cim:TransformerEnd.endNumber 1.
          ?end2 cim:TransformerEnd.endNumber 2.
          ?end1 cim:PowerTransformerEnd.x ?x1 .
          ?end2 cim:PowerTransformerEnd.x ?x2 .
          #?end3 cim:TransformerEnd.endNumber 3 .
          #?end3 cim:PowerTransformerEnd.x ?x3 .
          OPTIONAL{?end3 cim:TransformerEnd.endNumber 3 .
                   ?end3 cim:PowerTransformerEnd.x ?x3 } .
          BIND(EXISTS{$this ^cim:PowerTransformerEnd.PowerTransformer/cim:TransformerEnd.endNumber 3 } AS ?threewin) .
          
          #FILTER ((!(?x1>0 && ?x2=0) && ?threewin=false )|| (?threewin=true && !(?x1!=0 && ?x2!=0 && ?x3!=0)) ).
          FILTER ((!(?x1>0 && ?x2=0) && ?threewin=false )|| (?threewin=true && !(?x1!=0 && ?x2!=0 && ?x3!=0)) ).
        } 
```
  - Messages: `["One of of the following occurs: 1) The value is negative or zero for winding one a two-winding transformer. 2) The value is zero for a three-winding transformer."]`

## eq452c:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

## eq452c:ProtectedSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:LoadBreakSwitch

## eq452c:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

**Nested Properties:**

### eq452c:RatioTapChanger-controlMode

**Path:** `rdf:type`  
**Name:** C:452:EQ:RatioTapChanger:controlMode  
The association TapChanger.TapChangerControl for RatioTapChanger-s shall only point to a TapChangerControl the has the following control modes for RegulatingControl.mode: voltage, reactivePower and powerFactor.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:TapChanger.TapChangerControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:TapChanger.TapChangerControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.reactivePower && ?value!=cim:RegulatingControlModeKind.voltage && ?value!=cim:RegulatingControlModeKind.powerFactor).
        }
```
  - Messages: `["Unallowed regulating control mode for a RatioTapChanger."]`

## eq452c:ReactiveCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ReactiveCapabilityCurve

**Nested Properties:**

### eq452c:ReactiveCapabilityCurve-reactiveCountP

**Path:** `rdf:type`  
**Name:** C:452:EQ:CurveData.Curve:reactiveCountP  
For a SynchronousMachine with a ReactiveCapabilityCurve the number of CurveData instances depends on the attribute SynchronousMachine.type as follows: - condenser, ReactiveCapabilityCurve is given by SynchronousMachine.maxQ and SynchronousMachine.minQ. There shall not be any association to ReactiveCapabilityCurve. - generator or generatorOrCondenser, at least two CurveData instances with CurveData.xvalue greater than or equal to 0. - motor or motorOrCondenser, at least two CurveData instances with CurveData.xvalue less than or equal to 0. - generatorOrMotor or generatorOrCondenserOrMotor, at least three CurveData instances with at least one having CurveData.xvalue greater than or equal to 0 and one having CurveData.xvalue less than or equal to 0. In general, it is required that the points defined by the ReactiveCapabilityCurve form an area of reactive capability different than 0.   

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	    SELECT $this ?curvedatas  ?value
      WHERE {
        {
        SELECT $this (COUNT(?typecd) AS ?curvedatas) (MAX(?xvalue) AS ?maxxvalue) (MIN(?xvalue) AS ?minxvalue)
        WHERE {
        $this  ^cim:CurveData.Curve/rdf:type ?typecd .
        $this  ^cim:CurveData.Curve/cim:CurveData.xvalue ?xvalue .
        #?curvedata cim:CurveData.Curve $this .
        #?curvedata rdf:type ?typecd .
        #?curvedata cim:CurveData.xvalue ?xvalue .
        }
        GROUP BY $this ?typecd 
        }
        
        $this ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:SynchronousMachine.type ?type .
        #BIND(EXISTS{$this ^cim:SynchronousMachine.InitialReactiveCapabilityCurve/cim:SynchronousMachine.type ?a} AS ?hasrcc).
        
        #OPTIONAL {?sm cim:SynchronousMachine.InitialReactiveCapabilityCurve $this }.
        #OPTIONAL {?sm cim:SynchronousMachine.type ?type }.
        #OPTIONAL {$this ^cim:SynchronousMachine.InitialReactiveCapabilityCurve ?mach }.
        $this ^cim:CurveData.Curve/cim:CurveData.xvalue ?xvalue1 .
        #?curvedata1 cim:CurveData.Curve $this .
        #?curvedata1 cim:CurveData.xvalue ?xvalue1 .
        BIND("" as ?value).


        #FILTER (?hasrcc=true && ((?type=cim:SynchronousMachineKind.condenser ) ||
        #((?type=cim:SynchronousMachineKind.generator || ?type=cim:SynchronousMachineKind.generatorOrCondenser) && (?curvedatas<2 || ?xvalue1<0)) ||
        #((?type=cim:SynchronousMachineKind.motor || ?type=cim:SynchronousMachineKind.motorOrCondenser) && (?curvedatas<2 || ?xvalue1>0)) ||
        #((?type=cim:SynchronousMachineKind.generatorOrMotor || ?type=cim:SynchronousMachineKind.generatorOrCondenserOrMotor) && (?curvedatas<3 || !(?maxxvalue>=0 && ?minxvalue<=0))))
        #) .
        FILTER (((?type=cim:SynchronousMachineKind.condenser ) ||
        ((?type=cim:SynchronousMachineKind.generator || ?type=cim:SynchronousMachineKind.generatorOrCondenser) && (?curvedatas<2 || ?xvalue1<0)) ||
        ((?type=cim:SynchronousMachineKind.motor || ?type=cim:SynchronousMachineKind.motorOrCondenser) && (?curvedatas<2 || ?xvalue1>0)) ||
        ((?type=cim:SynchronousMachineKind.generatorOrMotor || ?type=cim:SynchronousMachineKind.generatorOrCondenserOrMotor) && (?curvedatas<3 || !(?maxxvalue>=0 && ?minxvalue<=0))))
        ) .
        
        } 
```
  - Messages: `["Reactive capability curve does not have the required number of points or the CurveData.xvalue is not in the defined range."]`

### eq452c:ReactiveCapabilityCurve-xvalue

**Path:** `rdf:type`  
**Name:** C:452:EQ:ReactiveCapabiltyCurve.CurveData:xvalue  
All CurveData.xvalue for a given ReactiveCapabilityCurve shall be unique, e.g. it is not allowed for two or more .xvalue to have the same float value for a given ReactiveCapabilityCurve.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
          {
          SELECT $this (COUNT(?xvalue1) AS ?c1)
          WHERE {
              $this ^cim:CurveData.Curve/cim:CurveData.xvalue ?xvalue1.
            }
            GROUP BY $this ?xvalue1
          }
          
          {
          SELECT DISTINCT $this (COUNT(?xvalue2) AS ?c2)
          WHERE {
              $this ^cim:CurveData.Curve/cim:CurveData.xvalue ?xvalue2.
            }
            GROUP BY $this ?xvalue2
          }

          FILTER (?c1!=?c2).
        }
        LIMIT 1
        
```
  - Messages: `["CurveData.xvalue for a given ReactiveCapabilityCurve are not unique."]`

## eq452c:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

## eq452c:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

## eq452c:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

## eq452c:StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator

**Nested Properties:**

### eq452c:StaticVarCompensator-controlMode

**Path:** `rdf:type`  
**Name:** C:452:EQ:StaticVarCompensator:controlMode  
For StaticVarCompensator, the association RegulatingCondEq.RequlatingControl is required and shall only point to a RequlatingControl that has the following control modes for RegulatingControl.mode: voltage and reactivePower.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:RegulatingCondEq.RegulatingControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:RegulatingCondEq.RegulatingControl/cim:RegulatingControl.mode ?value .
        BIND(EXISTS{$this cim:StaticVarCompensator.sVCControlMode ?a} AS ?hassvcmode).
        BIND(EXISTS{$this cim:StaticVarCompensator.voltageSetPoint ?b} AS ?hasvsetpoint).
        #OPTIONAL {$this cim:StaticVarCompensator.sVCControlMode ?svcmode }.
        #OPTIONAL {$this cim:StaticVarCompensator.voltageSetPoint ?vsetpoint }.
        FILTER ((?value!=cim:RegulatingControlModeKind.reactivePower && ?value!=cim:RegulatingControlModeKind.voltage) || ?hassvcmode=true || ?hasvsetpoint=true).
        }
```
  - Messages: `["Unallowed regulating control mode for a StaticVarCompensator or not allowed usage of StaticVarCompensator.sVCControlMode or StaticVarCompensator.voltageSetPoint."]`

## eq452c:Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Switch

**Nested Properties:**

### eq452c:Switch-connection

**Path:** `rdf:type`  
**Name:** C:452:EQ:Switch:connection  
Switch and its subclasses shall only connect to ConnectivityNode-s that are contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
        {
          SELECT $this ?cnc2 ?cnc1
          WHERE {
            ?term1 cim:Terminal.ConductingEquipment $this .
            ?term2 cim:Terminal.ConductingEquipment $this .
            ?term1 cim:ACDCTerminal.sequenceNumber 1 .
            ?term2 cim:ACDCTerminal.sequenceNumber 2 .
            #OPTIONAL {?term1 cim:Terminal.ConnectivityNode ?cn1 } .
            #OPTIONAL {?cn1 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 } .
            ?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1 .
            #BIND(EXISTS{?term1 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc1a} AS ?hascnc1).
            #OPTIONAL {?term2 cim:Terminal.ConnectivityNode ?cn2 } .
            #OPTIONAL {?cn2 cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 } .
            ?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2 .
            #BIND(EXISTS{?term2 cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer ?cnc2a} AS ?hascnc2).
            #FILTER (?hascnc1=true && ?hascnc2=true).
            }
        }
        
        OPTIONAL {?cnc1 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .
        OPTIONAL {?cnc1 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn1nv } .

        
        OPTIONAL {?cnc2 cim:Bay.VoltageLevel/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 ^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        OPTIONAL {?cnc2 cim:DCConverterUnit.Substation/^cim:VoltageLevel.Substation/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?cn2nv } .
        
        #FILTER (bound(?cn1) && bound(?cn2) && bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        FILTER (bound(?cn1nv) && bound(?cn2nv) && ?cn1nv!=?cn2nv).
        }
```
  - Messages: `["Switch (or its subclasses) connects ConnectivityNode-s that are not contained in either the same VoltageLevel or in different VoltageLevel-s which have the same BaseVoltage."]`

## eq452c:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### eq452c:GeneratingUnit-typeDependency

**Path:** `cim:SynchronousMachine.type`  
**Name:** C:452:EQ:GeneratingUnit:typeDependency  
GeneratingUnit.maxOperatingP and GeneratingUnit.minOperatingP shall depend on the SynchronousMachine.type of the associated SynchronousMachine as follows:- condenser: GeneratingUnit.minOperatingP and GeneratingUnit.maxOperatingP shall equal zero.- generator or generatorOrCondenser: GeneratingUnit.minOperatingP shall be greater than or equal to zero and GeneratingUnit.maxOperatingP shall be greater than zero.- motor or motorOrCondenser: GeneratingUnit.minOperatingP shall be a negative value and GeneratingUnit.maxOperatingP shall be a negative value or zero.- generatorOrMotor or generatorOrCondenserOrMotor: GeneratingUnit.minOperatingP shall be a negative value and GeneratingUnit.maxOperatingP shall be greater than zero.

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
        $this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.maxOperatingP ?maxp .
        $this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.minOperatingP ?minp .
        #OPTIONAL {$this cim:RotatingMachine.GeneratingUnit ?genunit } .
        #OPTIONAL {?genunit cim:GeneratingUnit.maxOperatingP ?maxp } .
        #OPTIONAL {?genunit cim:GeneratingUnit.minOperatingP ?minp } .
        #BIND(EXISTS{$this cim:RotatingMachine.GeneratingUnit ?a} AS ?hasgenunit).
        #BIND(EXISTS{$this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.maxOperatingP ?b} AS ?hasmaxp).
        #BIND(EXISTS{$this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.minOperatingP ?c} AS ?hasminp).
        
        
        #FILTER ((?hasgenunit=true && ?hasmaxp=true && ?hasminp=true && ?value=cim:SynchronousMachineKind.condenser && (?maxp!=0 || ?minp!=0)) ||
        #(?hasgenunit=true && ?hasmaxp=true && ?hasminp=true && (?value=cim:SynchronousMachineKind.generator || ?value=cim:SynchronousMachineKind.generatorOrCondenser) && (?maxp<=0 || ?minp<0)) ||
        #(?hasgenunit=true && ?hasmaxp=true && ?hasminp=true && (?value=cim:SynchronousMachineKind.motor || ?value=cim:SynchronousMachineKind.motorOrCondenser) && (?maxp>0 || ?minp>=0)) ||
        #(?hasgenunit=true && ?hasmaxp=true && ?hasminp=true && (?value=cim:SynchronousMachineKind.generatorOrMotor || ?value=cim:SynchronousMachineKind.generatorOrCondenserOrMotor) && (?maxp<=0 || ?minp>=0))
        #).
         FILTER ((?value=cim:SynchronousMachineKind.condenser && (?maxp!=0 || ?minp!=0)) ||
        ((?value=cim:SynchronousMachineKind.generator || ?value=cim:SynchronousMachineKind.generatorOrCondenser) && (?maxp<=0 || ?minp<0)) ||
        ((?value=cim:SynchronousMachineKind.motor || ?value=cim:SynchronousMachineKind.motorOrCondenser) && (?maxp>0 || ?minp>=0)) ||
        ((?value=cim:SynchronousMachineKind.generatorOrMotor || ?value=cim:SynchronousMachineKind.generatorOrCondenserOrMotor) && (?maxp<=0 || ?minp>=0))
        ).
        }
```
  - Messages: `["Inconsistancy between GeneratingUnit.maxOperatingP and GeneratingUnit.minOperatingP and SynchronousMachine.type."]`

### eq452c:SynchronousMachine.type-condenser

**Path:** `cim:SynchronousMachine.type`  
**Name:** C:452:EQ:SynchronousMachine.type:condenser  
The SynchronousMachine is not required to be associated with a GeneratingUnit via the association RotatingMachine.GeneratingUnit in cases where a synchronous condenser is being modelled as there is no capability for real power output. In this case, the SynchronousMachine.type shall be set to condenser. The following SynchronousMachine.type-s: motorOrCondenser, generatorOrCondenser, and generatorOrCondenserOrMotor are not allowed to use.

**Severity:** sh:Info

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Info)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        $this $PATH ?value .
        $this $PATH cim:SynchronousMachineKind.condenser  .
        OPTIONAL {$this cim:RotatingMachine.GeneratingUnit ?genunit } .
        #BIND(EXISTS{$this cim:RotatingMachine.GeneratingUnit ?genunit} AS ?opt).
        #FILTER (?opt=true && ?value=cim:SynchronousMachineKind.condenser ).
        FILTER (bound(?genunit) ).
        }
```
  - Messages: `["SynchronousMachine of type condenser with associated GeneratingUnit."]`

### eq452c:SynchronousMachine-reactiveLimits

**Path:** `rdf:type`  
**Name:** C:452:EQ:SynchronousMachine:reactiveLimits  
ReactiveCapabilityCurve-s are not required if the reactive power limits of the SynchronousMachine do not vary with real power output. SynchronousMachine.minQ and SynchronousMachine.maxQ are required if SynchronousMachine.InitialReactiveCapabilityCurve is missing. If the association SynchronousMachine.InitialReactiveCapabilityCurve is provided it takes precedence to the information provided by the attributes SynchronousMachine.minQ and SynchronousMachine.maxQ. However, if both SynchronousMachine.minQ, SynchronousMachine.maxQ and ReactiveCapabilityCurve are present, the SynchronousMachine.minQ shall be equal to min of CurveData.y1value-s and SynchronousMachine.maxQ shall be equal to max CurveData.y2value-s.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

        SELECT $this 
      WHERE {
        OPTIONAL {$this cim:SynchronousMachine.minQ ?minq } .
        OPTIONAL {$this cim:SynchronousMachine.maxQ ?maxq } .
        #OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
        BIND(EXISTS{$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcca} AS ?hasrcc).
        
        {
        SELECT $this (MAX(?y2value) AS ?my2value)  (MIN(?y1value) AS ?my1value)
          WHERE {
            #OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            #?rcc1 ^cim:CurveData.Curve ?curvedata .
            $this cim:SynchronousMachine.InitialReactiveCapabilityCurve/^cim:CurveData.Curve ?curvedata .
            #BIND(EXISTS{$this cim:SynchronousMachine.InitialReactiveCapabilityCurve/^cim:CurveData.Curve ?curvedataa} AS ?hascurvedata).
            ?curvedata rdf:type ?cdtype .
            ?curvedata cim:CurveData.y1value ?y1value .
            ?curvedata cim:CurveData.y2value ?y2value .
            #FILTER (?hascurvedata=true && ?cdtype=cim:CurveData ) .
            FILTER (?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        FILTER ((?hasrcc=false && !(bound(?minq) && bound(?maxq))) || (?hasrcc=true && bound(?minq) && bound(?maxq) && !(?maxq=?my2value && ?minq=?my1value))) .
        } 
```
  - Messages: `["One of the following is not fulfilled: 1)Neither SynchronousMachine.minQ,  SynchronousMachine.maxQ nor SynchronousMachine.InitialReactiveCapabilityCurve are provided 2) Either SynchronousMachine.minQ is not equal to min of CurveData.y1value-s or  SynchronousMachine.maxQ is not equal to max CurveData.y2value-s."]`

### eq452c:CurveData.xvalue-value

**Path:** `rdf:type`  
**Name:** C:452:EQ:CurveData.xvalue:value  
The GeneratingUnit.minOperatingP shall be equal of the minimum of the CurveData.xvalue among all points defined for a ReactveCapabilityCurve. The GeneratingUnit.maxOperatingP shall be equal of the maximum of the CurveData.xvalue among all points defined for a ReactveCapabilityCurve.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	    SELECT $this ?value
      WHERE {      
        $this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.minOperatingP ?minp.
        $this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.maxOperatingP ?maxp.
        #OPTIONAL {$this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.minOperatingP ?minp } .
        #OPTIONAL {$this cim:RotatingMachine.GeneratingUnit/cim:GeneratingUnit.maxOperatingP ?maxp } .
        #OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
        BIND(EXISTS{$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcca} AS ?hasrcc).
        
        {
        SELECT $this (MAX(?xvalue) AS ?maxxvalue)  (MIN(?xvalue) AS ?minxvalue)
          WHERE {
            #OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            #?rcc1 ^cim:CurveData.Curve ?curvedata .
            $this cim:SynchronousMachine.InitialReactiveCapabilityCurve/^cim:CurveData.Curve ?curvedata .
            #BIND(EXISTS{$this cim:SynchronousMachine.InitialReactiveCapabilityCurve/^cim:CurveData.Curve ?curvedataa} AS ?hascurvedata).
            ?curvedata rdf:type ?cdtype .
            ?curvedata cim:CurveData.xvalue ?xvalue .
            #FILTER (?hascurvedata=true && ?cdtype=cim:CurveData ) .
            FILTER (?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        #FILTER ((?hasrcc=true && bound(?minp) && bound(?maxp) && ?maxp!=?maxxvalue && ?minp!=?minxvalue)) .
        FILTER (?hasrcc=true && !(?maxp=?maxxvalue && ?minp=?minxvalue)) .
        } 
```
  - Messages: `["The CurveData.xvalue for ReactveCapabilityCurve are not consistent with GeneratingUnit.minOperatingP and GeneratingUnit.maxOperatingP."]`

### eq452c:SynchronousMachine-controlMode

**Path:** `rdf:type`  
**Name:** C:452:EQ:SynchronousMachine:controlMode  
For SynchronousMachine, the association RegulatingCondEq.RequlatingControl shall only point to a RequlatingControl that has the following control modes for RegulatingControl.mode: voltage, reactivePower and powerFactor.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this ?value 
        WHERE {
        #?rcontrol ^cim:RegulatingCondEq.RegulatingControl $this  .
        #?rcontrol cim:RegulatingControl.mode ?value  .
        $this cim:RegulatingCondEq.RegulatingControl/cim:RegulatingControl.mode ?value  .
        FILTER (?value!=cim:RegulatingControlModeKind.reactivePower && ?value!=cim:RegulatingControlModeKind.voltage && ?value!=cim:RegulatingControlModeKind.powerFactor).
        }
```
  - Messages: `["Unallowed regulating control mode for a SynchronousMachine."]`

## eq452c:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### eq452c:TapChangerControl-remoteQcontrol

**Path:** `rdf:type`  
**Name:** C:452:EQ:TapChangerControl:remoteQcontrol  
A power transformer cannot efficiently control reactive power flow on remote terminals. Therefore, a TapChangerControl controlling reactive power flow shall only control the flow at one of the Terminal-s associated with PowerTransformerEnd-s of the PowerTransformer where the TapChanger is located. Control of a remote Terminal not associated with the PowerTransformer that has the TapChanger is not allowed. This constraint defines that multiple TapChanger-s cannot be controlled by the same TapChangerControl.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  
        WHERE {
          $this cim:RegulatingControl.mode ?mode .
          $this cim:RegulatingControl.Terminal ?rcterm .
          OPTIONAL {$this ^cim:TapChanger.TapChangerControl/cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.Terminal ?tcterm1 }.
          OPTIONAL {$this ^cim:TapChanger.TapChangerControl/cim:PhaseTapChanger.TransformerEnd/cim:TransformerEnd.Terminal ?tcterm2 }.
        
          FILTER (?mode=cim:RegulatingControlModeKind.reactivePower && ((?rcterm!=?tcterm1 && !bound(?tcterm2) && bound(?tcterm1)) || (?rcterm!=?tcterm2 && !bound(?tcterm1) && bound(?tcterm2)))).
        }
```
  - Messages: `["TapChangerControl with RegulatingControl.mode equals reactivePower controls a Terminal which is not associated with PowerTransformerEnd-s of the PowerTransformer where the TapChanger is located."]`

## eq452c:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

## eq452c:VsCapabilityCurve

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsCapabilityCurve

**Nested Properties:**

### eq452c:VsCapabilityCurve-VsCapabilityCurveCount

**Path:** `rdf:type`  
**Name:** C:452:EQ:CurveData.Curve:VsCapabilityCurveCount  
If CurveData.Curve is a VsCapabilityCurve at least two CurveData shall be associated.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this (COUNT(?typecd) AS ?curvedatas)
        WHERE {
        ?curvedata cim:CurveData.Curve $this .
        ?curvedata rdf:type ?typecd .
        }
        GROUP BY $this ?typecd
        HAVING(?curvedatas<2)
      
```
  - Messages: `["Less than two instances of CurveData are associated."]`

### eq452c:VsCapabilityCurve-yvalues

**Path:** `rdf:type`  
**Name:** C:452:EQ:CurveData.Curve:VsCapabilityCurve  
If CurveData.Curve is a VsCapabilityCurve, the CurveData.y2value shall be greater than CurveData.y1value.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this 
        WHERE {
        ?curvedata cim:CurveData.Curve $this .
        ?curvedata cim:CurveData.y1value ?y1value .
        ?curvedata cim:CurveData.y2value ?y2value .
        FILTER (?y2value<=?y1value).
        }
```
  - Messages: `["CurveData.y2value is not greater than CurveData.y1value"]`

## eq452c:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### eq452c:GeneratingUnit.maxOperatingP-ratedS

**Path:** `rdf:type`  
**Name:** C:452:EQ:GeneratingUnit:maxOperatingP:ratedS  
GeneratingUnit.maxOperatingP shall be less than or equal to the sum of RotatingMachine.ratedS for RotatingMachine-s associated to the GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value 
        WHERE {
          $this cim:GeneratingUnit.maxOperatingP ?value .
          {
          SELECT $this (SUM(?rmrateds) AS ?sumrs)
          WHERE {

             $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rmrateds .
             
             #?rm cim:RotatingMachine.GeneratingUnit $this .
             #?rm rdf:type ?rmtype .
             #?rm cim:RotatingMachine.ratedS ?rmrateds.
             }
             #GROUP BY $this ?rmtype
             GROUP BY $this 
          }    
          FILTER (?value>?sumrs).
        } 
        
```
  - Messages: `["GeneratingUnit.maxOperatingP is greater than the sum of RotatingMachine.ratedS for  RotatingMachine-s associated to GeneratingUnit."]`

