# 61970-456_StateVariables-AP-Con-Complex-SHACL

## sv456c:TopologicalIslandCountShape

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:TopologicalIsland

**Nested Properties:**

### sv456c:TopologicalIsland-instance

**Path:** `^rdf:type`  
**Name:** C:456:SV:TopologicalIsland:instance  
At least one TopologicalIsland instance shall be present per SV instance. The TopologicalIsland-s for a merged model which are defined in the state variables instance file for the merged model are created with the solving on the power flow of the merged model, i.e. there are no TopologicalIsland-s defined per MAS in a merged model. In case a solved merged model is exchanged for a single MAS the state variables instance file shall include at least one instance of TopologicalIsland.

**Severity:** sh:Violation

**Messages:**
- "No TopologicalIsland instantiated."

**Constraints:**

- **sh:MinCountConstraintComponent** (Severity: sh:Violation)
  - MinCount: `1` 

