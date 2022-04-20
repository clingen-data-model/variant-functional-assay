
# Class: FunctionalAssay


Experimental evaluation of the functional effect of one or more genetic variants.

URI: [sepio-cg:FunctionalAssay](http://purl.obolibrary.org/obo/SEPIOCG_FunctionalAssay)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[FunctionalAssayResult]++-%20assay%200..1>[FunctionalAssay&#124;general_class:string%20*;material_used:string%20*;patient_derived_material_used:string%20*;description:string%20%3F;document:string%20%3F;additional_document:string%20*;read_out_description:string%20%3F;range:string%20%3F;normal_range:string%20%3F;abnormal_range:string%20%3F;indeterminate_range:string%20%3F;validation_control_pathogenic:string%20%3F;validation_control_benign:string%20%3F;replication:string;statistical_analysis_description:string;significance_threshold:string%20%3F;comment:string%20*;range_type:RangeType%20%3F;units:unit%20%3F],[FunctionalAssayResult])](https://yuml.me/diagram/nofunky;dir:TB/class/[FunctionalAssayResult]++-%20assay%200..1>[FunctionalAssay&#124;general_class:string%20*;material_used:string%20*;patient_derived_material_used:string%20*;description:string%20%3F;document:string%20%3F;additional_document:string%20*;read_out_description:string%20%3F;range:string%20%3F;normal_range:string%20%3F;abnormal_range:string%20%3F;indeterminate_range:string%20%3F;validation_control_pathogenic:string%20%3F;validation_control_benign:string%20%3F;replication:string;statistical_analysis_description:string;significance_threshold:string%20%3F;comment:string%20*;range_type:RangeType%20%3F;units:unit%20%3F],[FunctionalAssayResult])

## Referenced by Class

 *  **None** *[➞assay](functionalAssayResult__assay.md)*  <sub>0..1</sub>  **[FunctionalAssay](FunctionalAssay.md)**

## Attributes


### Own

 * [➞general class](functionalAssay__general_class.md)  <sub>0..\*</sub>
     * Description: The type or class of assay as identified using structured language or ontology terms. BAO or ECO terms are preferred when available.
     * Range: [String](types/String.md)
 * [➞material used](functionalAssay__material_used.md)  <sub>0..\*</sub>
     * Description: Reagents (biological or non-biological) that were use as comparators or other inputs to an assay. CLO, CO and BAI terms are preferred when available.
     * Range: [String](types/String.md)
 * [➞patient derived material used](functionalAssay__patient_derived_material_used.md)  <sub>0..\*</sub>
     * Description: Material used as inputs or comparators within an assay that were derived/sourced from a patient. These are differentiated from other materials used in an assay because of the possibility that use of such materials may involved confounding variables (e.g.,  other genetic variants) that may be difficult to account for in validation. CLO, CO and BAI terms are preferred when available.
     * Range: [String](types/String.md)
 * [➞description](functionalAssay__description.md)  <sub>0..1</sub>
     * Description: Free-text description/summary of the assay
     * Range: [String](types/String.md)
 * [➞document](functionalAssay__document.md)  <sub>0..1</sub>
     * Description: The primary document or manuscript in which the assay and its results are described. Supplementary descriptions can be recorded in "additional publication"
     * Range: [String](types/String.md)
 * [➞additional document](functionalAssay__additional_document.md)  <sub>0..\*</sub>
     * Description: External document referenced in this document as providing details about the assay
     * Range: [String](types/String.md)
 * [➞read out description](functionalAssay__read_out_description.md)  <sub>0..1</sub>
     * Description: Free-text description of the type of readout of the assay
     * Range: [String](types/String.md)
 * [➞range](functionalAssay__range.md)  <sub>0..1</sub>
     * Description: Range of all possible output values of the assay. If qualitative this will comprise a list of terms indicating the observable results. If quantitative, this will indicate the units used.
     * Range: [String](types/String.md)
 * [➞normal range](functionalAssay__normal_range.md)  <sub>0..1</sub>
     * Description: The subset of possible output values which the authors of an assay classify as indicative of normal function.
     * Range: [String](types/String.md)
 * [➞abnormal range](functionalAssay__abnormal_range.md)  <sub>0..1</sub>
     * Description: The subset of possible output values which the authors of an assay classify as indicative of abnormal function.
     * Range: [String](types/String.md)
 * [➞indeterminate range](functionalAssay__indeterminate_range.md)  <sub>0..1</sub>
     * Description: The subset of possible output values which the authors of an assay classify as indeterminante with respect to function.
     * Range: [String](types/String.md)
 * [➞validation control pathogenic](functionalAssay__validation_control_pathogenic.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞validation control benign](functionalAssay__validation_control_benign.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞replication](functionalAssay__replication.md)  <sub>1..1</sub>
     * Description: Description of the process for replication of an assay as provided by the document, or "not reported" if not specified.
     * Range: [String](types/String.md)
 * [➞statistical analysis description](functionalAssay__statistical_analysis_description.md)  <sub>1..1</sub>
     * Description: Description of the statistical analysis performed for validation and determination of thresholds of the assay, or "not reported" if the document does not specify.
     * Range: [String](types/String.md)
 * [➞significance threshold](functionalAssay__significance_threshold.md)  <sub>0..1</sub>
     * Description: The threshold for significance of measurements under this assay, as defined by the authors of the document (if provided).
     * Range: [String](types/String.md)
 * [➞comment](functionalAssay__comment.md)  <sub>0..\*</sub>
     * Description: Any additional information that a curator would like to provide about the FunctionalAssay that is not adequately captured by other fields
     * Range: [String](types/String.md)
 * [➞range type](functionalAssay__range_type.md)  <sub>0..1</sub>
     * Description: The type of values that can be expected from results of this assay (quantitative or qualitative). This could be inferred from the assay's range, but is encoded here to simplify searches.
     * Range: [RangeType](RangeType.md)
 * [➞units](functionalAssay__units.md)  <sub>0..1</sub>
     * Description: For quantitative assays, the default unit to be applied to individual results if not overridden.
     * Range: [Unit](types/Unit.md)
