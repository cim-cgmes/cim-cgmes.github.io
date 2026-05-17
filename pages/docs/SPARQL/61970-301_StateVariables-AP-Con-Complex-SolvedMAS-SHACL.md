# 61970-301_StateVariables-AP-Con-Complex-SolvedMAS-SHACL

## <http://iec.ch/TC57/ns/CIM/StateVariable-EU/constraints/IEC61970-301/solved/3.0#SvTapStep>

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvTapStep

**Nested Properties:**

### <http://iec.ch/TC57/ns/CIM/StateVariable-EU/constraints/IEC61970-301/solved/3.0#SvTapStep.position-valueRange>

**Path:** `cim:SvTapStep.position`  
This is not the tap ratio, but rather the tap step position as defined by the related tap changer model and normally is constrained to be within the range of minimum and maximum tap positions.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value 
			WHERE {
             $this $PATH ?value .
             $this cim:SvTapStep.TapChanger ?tapchanger .
             ?tapchanger cim:TapChanger.lowStep ?lowstep .
             ?tapchanger cim:TapChanger.highStep ?highstep .
				FILTER (?value<?lowstep || ?value>?highstep) .
			}
```
  - Messages: `["The value is out of range [TapChanger.lowStep,TapChanger.highStep]."]`

