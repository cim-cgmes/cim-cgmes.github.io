# 61970-301_DiagramLayout-AP-Con-Complex-SHACL

## dl:DiagramObject.IdentifiedObject-additionalValueType

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:TextDiagramObjectDiagramObject

**Nested Properties:**

### dl:DiagramObject.IdentifiedObject-DLvalueType

**Path:** `rdf:type`  
**Name:** C:301:DL:DiagramObject.IdentifiedObject:internalValueType  
The association end role description stated that: The domain object to which this diagram object is associated. Therefore, the association cannot point to cim:Diagram, cim:DiagramObject, cim:VisibilityLayer, cim:DiagramStyle, cim:DiagramObjectStyle or cim:TextDiagramObject.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

	      SELECT $this  ?value
        WHERE {
          ?value cim:DiagramObject.IdentifiedObject/rdf:type ?valueType .  
          {
            SELECT $this ?value
            WHERE {
              ?value rdf:type ?classtype .
              FILTER (?classtype IN (cim:TextDiagramObject , cim:DiagramObject)).
              }
          }
          FILTER (?valueType IN (cim:Diagram , cim:DiagramObject, cim:VisibilityLayer , cim:DiagramStyle , cim:DiagramObjectStyle , cim:TextDiagramObject)).
        } 
        
```
  - Messages: `["One of the following does not conform: 1) The value type shall be IRI; 2) The value type shall not be an instance of the class: cim:Diagram, cim:DiagramObject, cim:VisibilityLayer, cim:DiagramStyle, cim:DiagramObjectStyle or cim:TextDiagramObject."]`

## dl:DiagramObjectPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiagramObjectPoint

