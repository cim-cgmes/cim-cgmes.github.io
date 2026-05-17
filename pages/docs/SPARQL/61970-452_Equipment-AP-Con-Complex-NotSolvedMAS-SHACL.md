# 61970-452_Equipment-AP-Con-Complex-NotSolvedMAS-SHACL

## eq452n:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### eq452n:RegulatingControl.targetValue-tapChanger

**Path:** `rdf:type`  
In cases where RequlatingControl.mode is voltage and both TapChanger.controlEnabled and RequlatingControl.enabled are true, The RegulatingControl.targetValue in per unit value is calculated by RegulatingControl.targetValue/BaseVoltage.nominalVoltage. shall be within the regulating capability limits:	The tap changer upper capability limit in per unit value is calculated by 1+RatioTapChanger.stepVoltageIncrement/100*(TapChanger.highStep-TapChanger.neutralStep). The tap changer lower capability limit in per unit value is calculated by 1-RatioTapChanger.stepVoltageIncrement/100*(TapChanger.neutralStep-TapChanger.lowStep).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT $this ?value
			WHERE {
        $this cim:RegulatingControl.targetValue ?value .
        $this cim:RegulatingControl.mode ?mode .
        $this ^cim:TapChanger.TapChangerControl/cim:TapChanger.controlEnabled ?contrenabled .
        $this cim:RegulatingControl.enabled ?enabled .
        $this ^cim:TapChanger.TapChangerControl/cim:RatioTapChanger.stepVoltageIncrement ?svi .
        $this ^cim:TapChanger.TapChangerControl/cim:TapChanger.highStep ?highstep .
        $this ^cim:TapChanger.TapChangerControl/cim:TapChanger.lowStep ?lowstep .
        $this ^cim:TapChanger.TapChangerControl/cim:TapChanger.neutralStep ?neutralstep .
        #$this ^cim:TapChanger.TapChangerControl/cim:RatioTapChanger.TransformerEnd/cim:TransformerEnd.BaseVoltage/cim:BaseVoltage.nominalVoltage ?valuenomu .
        $this cim:RegulatingControl.Terminal/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.ConnectivityNodeContainer/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?valuenomu .
        
				FILTER (?mode=cim:RegulatingControlModeKind.voltage && ?contrenabled=true && ?enabled=true && !( ?value/?valuenomu>=(1-(?svi/100)*(?neutralstep-?lowstep)) && ?value/?valuenomu<=(1+(?svi/100)*(?highstep-?neutralstep)) ) ) .
			}
```
  - Messages: `["The RegulatingControl.targetValue is outside the TapChanger capability."]`

