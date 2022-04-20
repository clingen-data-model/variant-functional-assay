

CREATE TABLE "Document" (
	pmid TEXT NOT NULL, 
	pmc_id TEXT, 
	PRIMARY KEY (pmid)
);

CREATE TABLE "FunctionalAssay" (
	general_class TEXT, 
	material_used TEXT, 
	patient_derived_material_used TEXT, 
	description TEXT, 
	document TEXT, 
	additional_document TEXT, 
	read_out_description TEXT, 
	range TEXT, 
	normal_range TEXT, 
	abnormal_range TEXT, 
	indeterminate_range TEXT, 
	validation_control_pathogenic TEXT, 
	validation_control_benign TEXT, 
	replication TEXT NOT NULL, 
	statistical_analysis_description TEXT NOT NULL, 
	significance_threshold TEXT, 
	comment TEXT, 
	range_type VARCHAR(12), 
	units TEXT, 
	PRIMARY KEY (general_class, material_used, patient_derived_material_used, description, document, additional_document, read_out_description, range, normal_range, abnormal_range, indeterminate_range, validation_control_pathogenic, validation_control_benign, replication, statistical_analysis_description, significance_threshold, comment, range_type, units)
);

CREATE TABLE gene (
	symbol TEXT, 
	synonym TEXT, 
	xref TEXT, 
	PRIMARY KEY (symbol, synonym, xref)
);

CREATE TABLE genetic_condition (
	associated_disease TEXT, 
	has_phenotype TEXT, 
	has_gene TEXT, 
	inheritance_pattern TEXT, 
	label TEXT, 
	description TEXT, 
	comment TEXT, 
	PRIMARY KEY (associated_disease, has_phenotype, has_gene, inheritance_pattern, label, description, comment)
);

CREATE TABLE "Variant" (
	has_gene TEXT, 
	canonical_allele_id TEXT NOT NULL, 
	hgvs_c TEXT, 
	hgvs_p TEXT, 
	clinvar_id TEXT, 
	PRIMARY KEY (canonical_allele_id)
);

CREATE TABLE "FunctionalAssayResult" (
	result TEXT NOT NULL, 
	result_assertion TEXT, 
	assay TEXT, 
	variant TEXT, 
	units TEXT, 
	validation_control VARCHAR(10), 
	replicate_count INTEGER, 
	standard_deviation TEXT, 
	standard_error_of_mean TEXT, 
	range TEXT, 
	intraquartile_range TEXT, 
	p_value TEXT, 
	is_approximation_by_curator BOOLEAN, 
	PRIMARY KEY (result, result_assertion, assay, variant, units, validation_control, replicate_count, standard_deviation, standard_error_of_mean, range, intraquartile_range, p_value, is_approximation_by_curator), 
	FOREIGN KEY(variant) REFERENCES "Variant" (canonical_allele_id)
);

CREATE TABLE "Document_comment" (
	backref_id TEXT, 
	comment TEXT, 
	PRIMARY KEY (backref_id, comment), 
	FOREIGN KEY(backref_id) REFERENCES "Document" (pmid)
);

CREATE TABLE "Variant_legacy_name" (
	backref_id TEXT, 
	legacy_name TEXT, 
	PRIMARY KEY (backref_id, legacy_name), 
	FOREIGN KEY(backref_id) REFERENCES "Variant" (canonical_allele_id)
);
