# 61970-600_Equipment-AP-Con-Complex-NotSolvedMAS-SHACL

## eq600n:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

**Nested Properties:**

### eq600n:ACLineSegment-BaseVoltageDiff

**Path:** `rdf:type`  
CGMES exchanges allow 10 % difference of the BaseVoltage.nominalVoltage at the two ends of an ACLineSegment representing a complete tie-line or connecting to a boundary node.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?tp1nv ?tp2nv
			WHERE {
        ?term1 cim:Terminal.ConductingEquipment $this .
        ?term2 cim:Terminal.ConductingEquipment $this .
        ?term1 cim:ACDCTerminal.sequenceNumber 1.
        ?term2 cim:ACDCTerminal.sequenceNumber 2.
        ?tp1  ^cim:Terminal.TopologicalNode ?term1 .
        ?tp1 cim:TopologicalNode.BaseVoltage/cim:BaseVoltage.nominalVoltage ?tp1nv .
        ?tp2  ^cim:Terminal.TopologicalNode ?term2 .
        ?tp2 cim:TopologicalNode.BaseVoltage/cim:BaseVoltage.nominalVoltage ?tp2nv .
        
        FILTER ((?tp1nv<?tp2nv && (ABS(?tp1nv-?tp2nv)/?tp1nv)>0.1) || (?tp1nv>?tp2nv && (ABS(?tp1nv-?tp2nv)/?tp2nv)>0.1)) .        
			}
```
  - Messages: `["More that 10% difference of the BaseVoltage.nominalVoltage at the two ends of an ACLineSegment. Voltage 1: {?tp1nv}; Voltage 2: {?tp2nv}"]`

## eq600n:BoundaryPoint

**Severity:** sh:Violation

**Nested Properties:**

### eq600n:BoundaryPoint-bppl1Bppl2

**Path:** `rdf:type`  
BPPL1 EquivalentInjection classes are used to represent the power flow exchanges through Boundary points. These classes are included in the individual model MAS (e.g. Model Authority MAS) and refer to the Boundary points (ConnectivityNode-s) in the Boundary set. The SvInjection class is not used for this purpose. BPPL2 In case the use cases require the exchange of multiple SSH, TP, SV, etc. instance files (distribution) which are dependent on an EQ instance file, this EQ shall always include an instance of EquivalentInjection per Boundary point. Therefore, in a multi MAS (among TSOs, DSOs or mixed) exchange a Boundary point shall always have two EquivalentInjections per Boundary point which are contained in different MAS connecting to the Boundary point. mRIDs of those EquivalentInjections are kept persistent.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:IdentifiedObject.name ?value .
        
        {
          SELECT $this 
          WHERE {
            $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type ?bptype.
            
            FILTER (bound(?bptype) && ?bptype IN (cim:ACLineSegment , cim:PowerTransformer, cim:DCLineSegment, cim:DCSeriesDevice, cim:DCSwitch, cim:DCDisconnector, cim:DCBreaker, cim:DCChopper, cim:Switch, cim:Disconnector, cim:Fuse, cim:GroundDisconnector, cim:Jumper, cim:Breaker, cim:LoadBreakSwitch, cim:DisconnectingCircuitBreaker, cim:Cut, cim:SeriesCompensator, cim:EquivalentBranch)) .
          }
        }
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:EquivalentInjection 
        }.
			}
```
  - Messages: `["ConnectivityNode which is designated as BoundaryPoint does not have EquivalentInjection connected to it."]`

### eq600n:BoundaryPoint-bppl3

**Path:** `rdf:type`  
A ConnectivityNode and a TopologicalNode representing a Boundary point may connect various branches.

**Severity:** sh:Info

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Info)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:IdentifiedObject.name ?value .
        
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:ACLineSegment 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:PowerTransformer 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCLineSegment 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCSeriesDevice 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCSwitch 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCDisconnector 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCBreaker 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DCChopper 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Switch 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Disconnector 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Fuse 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:GroundDisconnector 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Jumper 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Breaker 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:LoadBreakSwitch 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:DisconnectingCircuitBreaker 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:Cut 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:SeriesCompensator 
        }.
        FILTER NOT EXISTS {
        $this ^cim:Terminal.ConnectivityNode/cim:Terminal.ConductingEquipment/rdf:type cim:EquivalentBranch 
        }.
			}
```
  - Messages: `["ConnectivityNode which is designated as BoundaryPoint does not have a two-Terminal ConductingEquipment connected to it."]`

## eq600n:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### eq600n:EquivalentInjection.regulationCapability-notHVDC

**Path:** `cim:EquivalentInjection.regulationCapability`  
If EquivalentInjection connects to a BoundaryPoint with flag isDirectCurrent=false (meaning this is not HVDC), the EquivalentInjection.regulationCapability in EQ shall be set to false and there shall not be a ReactiveCapabilityCurve associated.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value.
        OPTIONAL {$this cim:EquivalentInjection.ReactiveCapabilityCurve ?curve}.
        OPTIONAL {$this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/^eu:BoundaryPoint.ConnectivityNode ?bp } .
        OPTIONAL {?bp eu:BoundaryPoint.isDirectCurrent ?ishvdc } .
        FILTER (bound(?bp) && bound(?ishvdc) && ?ishvdc=false && (bound(?curve) || ?value=true)) .        
			}
```
  - Messages: `["EquivalentInjection connects to a BoundaryPoint with flag isDirectCurrent=false (meaning this is not HVDC), but either EquivalentInjection.regulationCapability is set to true or there is a ReactiveCapabilityCurve associated."]`

