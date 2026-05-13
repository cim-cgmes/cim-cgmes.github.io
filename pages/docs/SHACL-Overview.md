<style>
  /* Local override for this page only */
  .container {
    max-width: 100% !important;
  }

  th {
    max-width: 120px;       /* Adjust this number based on your text */
    white-space: normal;    /* Ensures text is allowed to wrap */
    word-wrap: break-word;  /* Breaks very long words if necessary */
    vertical-align: bottom; /* Keeps text aligned at the bottom of the cell */
    line-height: 1.2;       /* Tightens the space between the 2-3 lines */
    padding: 8px 4px;
  }

  /* Target all tables within the Markdown content area */
.markdown table {
  display: table;
  width: 100%;
}

/* Row highlight */
tr:hover {
  background-color: #bdbdbd;
  color: black;
}

/* 1. Remove the overflow constraint from the default table wrapper */
.markdown > div {
  overflow: visible !important;
}

/* 2. Target the header cells specifically */
.markdown table thead th {
  position: -webkit-sticky; /* Support for Safari */
  position: sticky;
  
  /* 3. Push it down so it doesn't hide behind the Docusaurus Navbar */
  top: var(--ifm-navbar-height); 
  
  /* 4. Ensure it has a background so text below doesn't bleed through */
  background-color: var(--ifm-background-color);
  
  /* 5. Keep it on top of body cells */
  z-index: 10;
  
  /* 6. Fix for border disappearing on sticky elements */
  border-bottom: 2px solid var(--ifm-table-border-color);
}
</style>

# SHACL Overview

| File | sh:AndConstraintComponent | sh:ClassConstraintComponent | sh:DatatypeConstraintComponent | sh:HasValueConstraintComponent | sh:InConstraintComponent | sh:LessThanConstraintComponent | sh:LessThanOrEqualsConstraintComponent | sh:MaxCountConstraintComponent | sh:MaxExclusiveConstraintComponent | sh:MaxInclusiveConstraintComponent | sh:MaxLengthConstraintComponent | sh:MinCountConstraintComponent | sh:MinExclusiveConstraintComponent | sh:MinInclusiveConstraintComponent | sh:MinLengthConstraintComponent | sh:NodeKindConstraintComponent | sh:NotConstraintComponent | sh:OrConstraintComponent | sh:XoneConstraintComponent |
| --- |  --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [61968-13_GeographicalLocation-AP-Con-Complex-SHACL](SHACL/61968-13_GeographicalLocation-AP-Con-Complex-SHACL.md) | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [61970-301_DiagramLayout-AP-Con-Complex-NotSolvedMAS-SHACL](SHACL/61970-301_DiagramLayout-AP-Con-Complex-NotSolvedMAS-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | 1 | - | - |
| [61970-301_DiagramLayout-AP-Con-Complex-SHACL](SHACL/61970-301_DiagramLayout-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | 1 | - | - | - |
| [61970-301_Equipment-AP-Con-Complex-SHACL](SHACL/61970-301_Equipment-AP-Con-Complex-SHACL.md) | 2 | 5 | - | - | 3 | 1 | 5 | 6 | 1 | 1 | 8 | 6 | 27 | 13 | 4 | - | - | 3 | - |
| [61970-301_EquipmentBoundary-AP-Con-Complex-SHACL](SHACL/61970-301_EquipmentBoundary-AP-Con-Complex-SHACL.md) | - | - | - | - | 2 | - | - | - | - | - | 8 | - | 1 | - | 4 | - | - | - | - |
| [61970-301_Operation-AP-Con-Complex-SHACL](SHACL/61970-301_Operation-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | - | 2 | - | - | - | - | - | - |
| [61970-301_ShortCircuit-AP-Con-Complex-SHACL](SHACL/61970-301_ShortCircuit-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | 3 | - | - | 1 | 7 | - | - | - | - | - |
| [61970-301_StateVariables-AP-Con-Complex-SHACL](SHACL/61970-301_StateVariables-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | - | 7 | 2 | - | - | - | - | - |
| [61970-301_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL](SHACL/61970-301_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL.md) | - | - | - | - | - | 1 | 3 | - | - | - | - | - | - | - | - | - | - | - | - |
| [61970-301_SteadyStateHypothesis-AP-Con-Complex-SHACL](SHACL/61970-301_SteadyStateHypothesis-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | - | 11 | 12 | - | - | - | - | - |
| [61970-302_Dynamics-AP-Con-Complex-SHACL](SHACL/61970-302_Dynamics-AP-Con-Complex-SHACL.md) | - | - | - | - | 7 | 130 | 6 | - | 53 | 16 | - | - | 322 | 792 | - | - | - | - | 2 |
| [61970-452_Equipment-AP-Con-Complex-SHACL](SHACL/61970-452_Equipment-AP-Con-Complex-SHACL.md) | - | - | - | - | 31 | - | 2 | 31 | - | 1 | - | 32 | 3 | 4 | - | - | - | - | - |
| [61970-452_Operation-AP-Con-Complex-SHACL](SHACL/61970-452_Operation-AP-Con-Complex-SHACL.md) | - | - | - | - | 7 | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [61970-452_ShortCircuit-AP-Con-Complex-CrossProfile-SHACL](SHACL/61970-452_ShortCircuit-AP-Con-Complex-CrossProfile-SHACL.md) | - | - | - | - | 2 | - | - | - | - | - | - | - | - | - | - | 2 | - | - | - |
| [61970-453_DiagramLayout-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-453_DiagramLayout-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - |
| [61970-453_DiagramLayout-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-453_DiagramLayout-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - |
| [61970-453_DiagramLayout-AP-Con-Complex-SHACL](SHACL/61970-453_DiagramLayout-AP-Con-Complex-SHACL.md) | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [61970-456_StateVariables-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-456_StateVariables-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 10 | - | - | - | - | - | - | - | - | - | - | 10 | - | - | - |
| [61970-456_StateVariables-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-456_StateVariables-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 10 | - | - | - | - | - | - | - | - | - | - | - | - | - | 10 | - | - | - |
| [61970-456_StateVariables-AP-Con-Complex-SHACL](SHACL/61970-456_StateVariables-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-456_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL](SHACL/61970-456_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL.md) | - | - | - | - | - | - | - | 1 | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-456_SteadyStateHypothesis-AP-Con-Complex-SHACL](SHACL/61970-456_SteadyStateHypothesis-AP-Con-Complex-SHACL.md) | 1 | - | - | - | - | - | - | - | - | - | - | - | - | 2 | - | - | - | - | - |
| [61970-456_Topology-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-456_Topology-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 3 | - | - | - | - | - | - | - | - | - | - | 3 | - | - | - |
| [61970-456_Topology-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-456_Topology-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 3 | - | - | - | - | - | - | - | - | - | - | - | - | - | 3 | - | - | - |
| [61970-456_Topology-AP-Con-Complex-SHACL](SHACL/61970-456_Topology-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | 1 | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-457_Dynamics-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-457_Dynamics-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 8 | - | - | - | - | - | - | - | - | - | - | 8 | - | - | - |
| [61970-457_Dynamics-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-457_Dynamics-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 8 | - | - | - | - | - | - | - | - | - | - | - | - | - | 8 | - | - | - |
| [61970-552-Header-AP-Con-Simple-SHACL](SHACL/61970-552-Header-AP-Con-Simple-SHACL.md) | - | - | 9 | - | 5 | - | - | 8 | - | - | - | 12 | - | - | - | 14 | - | - | - |
| [61970-600-1_AllProfiles-AP-Con-Complex-SHACL](SHACL/61970-600-1_AllProfiles-AP-Con-Complex-SHACL.md) | - | - | - | - | 1 | - | - | 1 | - | - | - | 1 | - | - | - | - | - | 1 | - |
| [61970-600-1_Equipment-AP-Con-Complex-SHACL](SHACL/61970-600-1_Equipment-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | 1 | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-600-1_Prof10-Header-AP-Con-Complex-SHACL](SHACL/61970-600-1_Prof10-Header-AP-Con-Complex-SHACL.md) | 9 | - | - | 1 | 2 | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - |
| [61970-600-2_DiagramLayout-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_DiagramLayout-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-600-2_DiagramLayout-AP-Con-Simple-SHACL](SHACL/61970-600-2_DiagramLayout-AP-Con-Simple-SHACL.md) | - | - | 18 | - | 8 | - | - | 25 | - | - | - | 9 | - | - | - | 26 | - | - | - |
| [61970-600-2_Dynamics-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_Dynamics-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 57 | - | - | - | 25 | - | - | - | - | - | - | - |
| [61970-600-2_Dynamics-AP-Con-Simple-SHACL](SHACL/61970-600-2_Dynamics-AP-Con-Simple-SHACL.md) | - | - | 2662 | - | 117 | - | - | 2786 | - | - | - | 2706 | - | - | - | 2779 | - | - | - |
| [61970-600-2_Equipment-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_Equipment-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 8 | - | - | - | 14 | - | - | - | - | - | - | - |
| [61970-600-2_Equipment-AP-Con-Complex-SHACL](SHACL/61970-600-2_Equipment-AP-Con-Complex-SHACL.md) | - | - | - | - | - | - | - | 2 | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-600-2_Equipment-AP-Con-Simple-SHACL](SHACL/61970-600-2_Equipment-AP-Con-Simple-SHACL.md) | - | - | 187 | - | 99 | - | - | 286 | - | - | - | 148 | - | - | - | 286 | - | - | - |
| [61970-600-2_EquipmentBoundary-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_EquipmentBoundary-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - |
| [61970-600-2_EquipmentBoundary-AP-Con-Simple-SHACL](SHACL/61970-600-2_EquipmentBoundary-AP-Con-Simple-SHACL.md) | - | - | 16 | - | 11 | - | - | 27 | - | - | - | 17 | - | - | - | 27 | - | - | - |
| [61970-600-2_GeographicalLocation-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-600-2_GeographicalLocation-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - |
| [61970-600-2_GeographicalLocation-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-600-2_GeographicalLocation-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - |
| [61970-600-2_GeographicalLocation-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_GeographicalLocation-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - |
| [61970-600-2_GeographicalLocation-AP-Con-Complex-SHACL](SHACL/61970-600-2_GeographicalLocation-AP-Con-Complex-SHACL.md) | 1 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [61970-600-2_GeographicalLocation-AP-Con-Simple-SHACL](SHACL/61970-600-2_GeographicalLocation-AP-Con-Simple-SHACL.md) | - | - | 32 | - | 6 | - | - | 39 | - | - | - | 7 | - | - | - | 38 | - | - | - |
| [61970-600-2_Operation-AP-Con-Complex-Explicit-CrossProfile-SHACL](SHACL/61970-600-2_Operation-AP-Con-Complex-Explicit-CrossProfile-SHACL.md) | - | - | - | - | 3 | - | - | - | - | - | - | - | - | - | - | 3 | - | - | - |
| [61970-600-2_Operation-AP-Con-Complex-Implicit-CrossProfile-SHACL](SHACL/61970-600-2_Operation-AP-Con-Complex-Implicit-CrossProfile-SHACL.md) | - | 3 | - | - | - | - | - | - | - | - | - | - | - | - | - | 3 | - | - | - |
| [61970-600-2_Operation-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_Operation-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 4 | - | - | - | 2 | - | - | - | - | - | - | - |
| [61970-600-2_Operation-AP-Con-Simple-SHACL](SHACL/61970-600-2_Operation-AP-Con-Simple-SHACL.md) | - | - | 30 | - | 25 | - | - | 55 | - | - | - | 30 | - | - | - | 55 | - | - | - |
| [61970-600-2_ShortCircuit-AP-Con-Simple-SHACL](SHACL/61970-600-2_ShortCircuit-AP-Con-Simple-SHACL.md) | - | - | 101 | - | 2 | - | - | 105 | - | - | - | 75 | - | - | - | 103 | - | - | - |
| [61970-600-2_StateVariables-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_StateVariables-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | 9 | - | - | - | - | - | - | - | - | - | - | - |
| [61970-600-2_StateVariables-AP-Con-Simple-SHACL](SHACL/61970-600-2_StateVariables-AP-Con-Simple-SHACL.md) | - | - | 20 | - | 1 | - | - | 28 | - | - | - | 29 | - | - | - | 21 | - | - | - |
| [61970-600-2_SteadyStateHypothesis-AP-Con-Simple-SHACL](SHACL/61970-600-2_SteadyStateHypothesis-AP-Con-Simple-SHACL.md) | - | - | 57 | - | 8 | - | - | 65 | - | - | - | 44 | - | - | - | 65 | - | - | - |
| [61970-600-2_Topology-AP-Con-Complex-InverseAssociation-SHACL](SHACL/61970-600-2_Topology-AP-Con-Complex-InverseAssociation-SHACL.md) | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - |
| [61970-600-2_Topology-AP-Con-Simple-SHACL](SHACL/61970-600-2_Topology-AP-Con-Simple-SHACL.md) | - | - | 5 | - | 4 | - | - | 13 | - | - | - | 7 | - | - | - | 9 | - | - | - |
| **Total** | **13** | **31** | **3137** | **1** | **369** | **132** | **16** | **3561** | **54** | **21** | **16** | **3171** | **375** | **832** | **8** | **3479** | **1** | **4** | **2** |
