
# functional-assay


**metamodel version:** 1.7.0

**version:** 0.0.1





### Classes

 * [Document](Document.md) - A collection of information content entities intended to be understood together as a whole
 * [FunctionalAssay](FunctionalAssay.md) - Experimental evaluation of the functional effect of one or more genetic variants.
 * [FunctionalAssayResult](FunctionalAssayResult.md) - The result of assessing a genetic variant's effect under a single instance of a functional assay.
 * [Variant](Variant.md) - A genetic variant, preferably identified by a canonical allele id
 * [Disease](Disease.md) - A recognizable grouping of pathological observed phenotypes occuring from a common cause
 * [Gene](Gene.md) - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions.
 * [GeneticCondition](GeneticCondition.md) - A disease, or a set of one or more co-occurring phenotypes, typically controlled by a single locus with a defined inheritance pattern.
 * [PhenotypicFeature](PhenotypicFeature.md) - An expressed characteristic of an organism

### Mixins


### Slots

 * [associated disease](associated_disease.md) - A recognizible grouping of pathological observed phenotypes occuring from a common cause
     * [genetic condition➞associated disease](genetic_condition_associated_disease.md)
 * [➞comment](document__comment.md)
 * [➞pmc_id](document__pmc_id.md) - Identifier of a manuscript in PubMedCentral database
 * [➞pmid](document__pmid.md) - Identifier of a manuscript in PubMed database
 * [➞assay](functionalAssayResult__assay.md)
 * [➞intraquartile range](functionalAssayResult__intraquartile_range.md)
 * [➞is approximation by curator](functionalAssayResult__is_approximation_by_curator.md) - A flag to indicate that the curator had to use some method of approximation of the `result` (e.g., by reading the value from a graph when numerical values were not provided by the authors reporting the `assay`).
 * [➞p value](functionalAssayResult__p_value.md)
 * [➞range](functionalAssayResult__range.md)
 * [➞replicate count](functionalAssayResult__replicate_count.md) - The number of times the `variant` was evaluated using the `assay` to produce the reported `result`.
 * [➞result](functionalAssayResult__result.md) - The measured value of this variant's effect on function. The value must be consistent with the `range` of the referenced `assay`.
 * [➞result assertion](functionalAssayResult__result_assertion.md) - An assertion as to the categorized impact of the variant's effect, as described by the authors reporting the `assay` (if provided).
 * [➞standard deviation](functionalAssayResult__standard_deviation.md)
 * [➞standard error of mean](functionalAssayResult__standard_error_of_mean.md)
 * [➞units](functionalAssayResult__units.md) - For qualtitatve assays, the units of the `result`. This may be omitted if the referenced `assay` provides a default value for the units of its measurements. Values must be from the Units of Measurement Ontology (UO)
 * [➞validation control](functionalAssayResult__validation_control.md) - Optional field used to indicate if this result is for a variant that was used as a validation control for the `assay` either as a `benign` or `pathogenic` variant.
 * [➞variant](functionalAssayResult__variant.md)
 * [➞abnormal range](functionalAssay__abnormal_range.md) - The subset of possible output values which the authors of an assay classify as indicative of abnormal function.
 * [➞additional document](functionalAssay__additional_document.md) - External document referenced in this document as providing details about the assay
 * [➞comment](functionalAssay__comment.md) - Any additional information that a curator would like to provide about the FunctionalAssay that is not adequately captured by other fields
 * [➞description](functionalAssay__description.md) - Free-text description/summary of the assay
 * [➞document](functionalAssay__document.md) - The primary document or manuscript in which the assay and its results are described. Supplementary descriptions can be recorded in "additional publication"
 * [➞general class](functionalAssay__general_class.md) - The type or class of assay as identified using structured language or ontology terms. BAO or ECO terms are preferred when available.
 * [➞indeterminate range](functionalAssay__indeterminate_range.md) - The subset of possible output values which the authors of an assay classify as indeterminante with respect to function.
 * [➞material used](functionalAssay__material_used.md) - Reagents (biological or non-biological) that were use as comparators or other inputs to an assay. CLO, CO and BAI terms are preferred when available.
 * [➞normal range](functionalAssay__normal_range.md) - The subset of possible output values which the authors of an assay classify as indicative of normal function.
 * [➞patient derived material used](functionalAssay__patient_derived_material_used.md) - Material used as inputs or comparators within an assay that were derived/sourced from a patient. These are differentiated from other materials used in an assay because of the possibility that use of such materials may involved confounding variables (e.g.,  other genetic variants) that may be difficult to account for in validation. CLO, CO and BAI terms are preferred when available.
 * [➞range](functionalAssay__range.md) - Range of all possible output values of the assay. If qualitative this will comprise a list of terms indicating the observable results. If quantitative, this will indicate the units used.
 * [➞range type](functionalAssay__range_type.md) - The type of values that can be expected from results of this assay (quantitative or qualitative). This could be inferred from the assay's range, but is encoded here to simplify searches.
 * [➞read out description](functionalAssay__read_out_description.md) - Free-text description of the type of readout of the assay
 * [➞replication](functionalAssay__replication.md) - Description of the process for replication of an assay as provided by the document, or "not reported" if not specified.
 * [➞significance threshold](functionalAssay__significance_threshold.md) - The threshold for significance of measurements under this assay, as defined by the authors of the document (if provided).
 * [➞statistical analysis description](functionalAssay__statistical_analysis_description.md) - Description of the statistical analysis performed for validation and determination of thresholds of the assay, or "not reported" if the document does not specify.
 * [➞units](functionalAssay__units.md) - For quantitative assays, the default unit to be applied to individual results if not overridden.
 * [➞validation control benign](functionalAssay__validation_control_benign.md)
 * [➞validation control pathogenic](functionalAssay__validation_control_pathogenic.md)
 * [➞symbol](gene__symbol.md)
 * [➞synonym](gene__synonym.md)
 * [➞xref](gene__xref.md)
 * [➞comment](geneticCondition__comment.md)
 * [➞description](geneticCondition__description.md) - Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.
 * [➞inheritance_pattern](geneticCondition__inheritance_pattern.md) - The manner in which a genetic condition is inherited
 * [➞label](geneticCondition__label.md) - A name given to the resource
 * [has gene](has_gene.md) - Connects an entity associated with one or more genes
     * [genetic condition➞has gene](genetic_condition_has_gene.md) - The gene associated with a genetic condition
 * [has phenotype](has_phenotype.md) - An expressed characteristic of an organism
     * [genetic condition➞has phenotype](genetic_condition_has_phenotype.md)
 * [➞canonical_allele_id](variant__canonical_allele_id.md)
 * [➞clinvar id](variant__clinvar_id.md)
 * [➞hgvs c](variant__hgvs_c.md)
 * [➞hgvs p](variant__hgvs_p.md)
 * [➞legacy name](variant__legacy_name.md)

### Enums

 * [RangeType](RangeType.md)
 * [ValidationControlType](ValidationControlType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Unit](types/Unit.md)  ([String](types/String.md)) 
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
