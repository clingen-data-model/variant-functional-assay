
# Class: FunctionalAssayResult


The result of assessing a genetic variant's effect under a single instance of a functional assay.

URI: [sepio-cg:FunctionalAssayResult](http://purl.obolibrary.org/obo/SEPIOCG_FunctionalAssayResult)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Variant]<variant%200..1-%20[FunctionalAssayResult&#124;result:string;result_assertion:string%20%3F;units:unit%20%3F;validation_control:ValidationControlType%20%3F;replicate_count:integer%20%3F;standard_deviation:decimal%20%3F;standard_error_of_mean:decimal%20%3F;range:string%20%3F;intraquartile_range:string%20%3F;p_value:decimal%20%3F;is_approximation_by_curator:boolean%20%3F],[FunctionalAssay]<assay%200..1-++[FunctionalAssayResult],[FunctionalAssay])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Variant]<variant%200..1-%20[FunctionalAssayResult&#124;result:string;result_assertion:string%20%3F;units:unit%20%3F;validation_control:ValidationControlType%20%3F;replicate_count:integer%20%3F;standard_deviation:decimal%20%3F;standard_error_of_mean:decimal%20%3F;range:string%20%3F;intraquartile_range:string%20%3F;p_value:decimal%20%3F;is_approximation_by_curator:boolean%20%3F],[FunctionalAssay]<assay%200..1-++[FunctionalAssayResult],[FunctionalAssay])

## Attributes


### Own

 * [➞result](functionalAssayResult__result.md)  <sub>1..1</sub>
     * Description: The measured value of this variant's effect on function. The value must be consistent with the `range` of the referenced `assay`.
     * Range: [String](types/String.md)
 * [➞result assertion](functionalAssayResult__result_assertion.md)  <sub>0..1</sub>
     * Description: An assertion as to the categorized impact of the variant's effect, as described by the authors reporting the `assay` (if provided).
     * Range: [String](types/String.md)
 * [➞assay](functionalAssayResult__assay.md)  <sub>0..1</sub>
     * Range: [FunctionalAssay](FunctionalAssay.md)
 * [➞variant](functionalAssayResult__variant.md)  <sub>0..1</sub>
     * Range: [Variant](Variant.md)
 * [➞units](functionalAssayResult__units.md)  <sub>0..1</sub>
     * Description: For qualtitatve assays, the units of the `result`. This may be omitted if the referenced `assay` provides a default value for the units of its measurements. Values must be from the Units of Measurement Ontology (UO)
     * Range: [Unit](types/Unit.md)
 * [➞validation control](functionalAssayResult__validation_control.md)  <sub>0..1</sub>
     * Description: Optional field used to indicate if this result is for a variant that was used as a validation control for the `assay` either as a `benign` or `pathogenic` variant.
     * Range: [ValidationControlType](ValidationControlType.md)
 * [➞replicate count](functionalAssayResult__replicate_count.md)  <sub>0..1</sub>
     * Description: The number of times the `variant` was evaluated using the `assay` to produce the reported `result`.
     * Range: [Integer](types/Integer.md)
 * [➞standard deviation](functionalAssayResult__standard_deviation.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [➞standard error of mean](functionalAssayResult__standard_error_of_mean.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [➞range](functionalAssayResult__range.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞intraquartile range](functionalAssayResult__intraquartile_range.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞p value](functionalAssayResult__p_value.md)  <sub>0..1</sub>
     * Range: [Decimal](types/Decimal.md)
 * [➞is approximation by curator](functionalAssayResult__is_approximation_by_curator.md)  <sub>0..1</sub>
     * Description: A flag to indicate that the curator had to use some method of approximation of the `result` (e.g., by reading the value from a graph when numerical values were not provided by the authors reporting the `assay`).
     * Range: [Boolean](types/Boolean.md)
