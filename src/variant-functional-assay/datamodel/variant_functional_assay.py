# Auto generated from variant_functional_assay.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-20T21:17:36
# Schema: functional-assay
#
# id: https://dataexchange.clinicalgenome.org/variant-functional-assay
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Decimal, Integer, String
from linkml_runtime.utils.metamodelcore import Bool, Decimal

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CAID = CurieNamespace('CAID', 'http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
HGNC = CurieNamespace('HGNC', 'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id=')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCBIGENE = CurieNamespace('NCBIGene', 'http://www.ncbi.nlm.nih.gov/gene/')
OMIM = CurieNamespace('OMIM', 'http://purl.obolibrary.org/obo/OMIM_')
ORPHANET = CurieNamespace('Orphanet', 'http://www.orpha.net/ORDO/Orphanet_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/biolink-model')
DC = CurieNamespace('dc', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SDO = CurieNamespace('sdo', 'https://schema.org/')
SEPIO_CG = CurieNamespace('sepio-cg', 'http://purl.obolibrary.org/obo/SEPIOCG_')
DEFAULT_ = SEPIO-CG


# Types
class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = SEPIO-CG.Unit


# Class references
class DocumentPmid(extended_str):
    pass


class VariantCanonicalAlleleId(extended_str):
    pass


class Disease(YAMLRoot):
    """
    A recognizable grouping of pathological observed phenotypes occuring from a common cause
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-CG.Disease
    class_class_curie: ClassVar[str] = "sepio-cg:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.Disease


class PhenotypicFeature(YAMLRoot):
    """
    An expressed characteristic of an organism
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-CG.PhenotypicFeature
    class_class_curie: ClassVar[str] = "sepio-cg:PhenotypicFeature"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.PhenotypicFeature


@dataclass
class Gene(YAMLRoot):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A
    gene may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0000704"]
    class_class_curie: ClassVar[str] = "SO:0000704"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.Gene

    symbol: Optional[str] = None
    synonym: Optional[str] = None
    xref: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.synonym is not None and not isinstance(self.synonym, str):
            self.synonym = str(self.synonym)

        if self.xref is not None and not isinstance(self.xref, str):
            self.xref = str(self.xref)

        super().__post_init__(**kwargs)


@dataclass
class GeneticCondition(YAMLRoot):
    """
    A disease, or a set of one or more co-occurring phenotypes, typically controlled by a single locus with a defined
    inheritance pattern.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO["0000219"]
    class_class_curie: ClassVar[str] = "SEPIO:0000219"
    class_name: ClassVar[str] = "genetic condition"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.GeneticCondition

    associated_disease: Optional[Union[Union[dict, Disease], List[Union[dict, Disease]]]] = empty_list()
    has_phenotype: Optional[Union[Union[dict, PhenotypicFeature], List[Union[dict, PhenotypicFeature]]]] = empty_list()
    has_gene: Optional[Union[dict, Gene]] = None
    inheritance_pattern: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    comment: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.associated_disease, list):
            self.associated_disease = [self.associated_disease] if self.associated_disease is not None else []
        self.associated_disease = [v if isinstance(v, Disease) else Disease(**as_dict(v)) for v in self.associated_disease]

        if not isinstance(self.has_phenotype, list):
            self.has_phenotype = [self.has_phenotype] if self.has_phenotype is not None else []
        self.has_phenotype = [v if isinstance(v, PhenotypicFeature) else PhenotypicFeature(**as_dict(v)) for v in self.has_phenotype]

        if self.has_gene is not None and not isinstance(self.has_gene, Gene):
            self.has_gene = Gene(**as_dict(self.has_gene))

        if self.inheritance_pattern is not None and not isinstance(self.inheritance_pattern, str):
            self.inheritance_pattern = str(self.inheritance_pattern)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        super().__post_init__(**kwargs)


@dataclass
class Document(YAMLRoot):
    """
    A collection of information content entities intended to be understood together as a whole
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000310"]
    class_class_curie: ClassVar[str] = "IAO:0000310"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.Document

    pmid: Union[str, DocumentPmid] = None
    pmc_id: Optional[str] = None
    comment: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.pmid):
            self.MissingRequiredField("pmid")
        if not isinstance(self.pmid, DocumentPmid):
            self.pmid = DocumentPmid(self.pmid)

        if self.pmc_id is not None and not isinstance(self.pmc_id, str):
            self.pmc_id = str(self.pmc_id)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        super().__post_init__(**kwargs)


@dataclass
class Variant(YAMLRoot):
    """
    A genetic variant, preferably identified by a canonical allele id
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-CG.Variant
    class_class_curie: ClassVar[str] = "sepio-cg:Variant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.Variant

    canonical_allele_id: Union[str, VariantCanonicalAlleleId] = None
    has_gene: Optional[Union[dict, Gene]] = None
    hgvs_c: Optional[str] = None
    hgvs_p: Optional[str] = None
    clinvar_id: Optional[str] = None
    legacy_name: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.canonical_allele_id):
            self.MissingRequiredField("canonical_allele_id")
        if not isinstance(self.canonical_allele_id, VariantCanonicalAlleleId):
            self.canonical_allele_id = VariantCanonicalAlleleId(self.canonical_allele_id)

        if self.has_gene is not None and not isinstance(self.has_gene, Gene):
            self.has_gene = Gene(**as_dict(self.has_gene))

        if self.hgvs_c is not None and not isinstance(self.hgvs_c, str):
            self.hgvs_c = str(self.hgvs_c)

        if self.hgvs_p is not None and not isinstance(self.hgvs_p, str):
            self.hgvs_p = str(self.hgvs_p)

        if self.clinvar_id is not None and not isinstance(self.clinvar_id, str):
            self.clinvar_id = str(self.clinvar_id)

        if not isinstance(self.legacy_name, list):
            self.legacy_name = [self.legacy_name] if self.legacy_name is not None else []
        self.legacy_name = [v if isinstance(v, str) else str(v) for v in self.legacy_name]

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssay(YAMLRoot):
    """
    Experimental evaluation of the functional effect of one or more genetic variants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-CG.FunctionalAssay
    class_class_curie: ClassVar[str] = "sepio-cg:FunctionalAssay"
    class_name: ClassVar[str] = "FunctionalAssay"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.FunctionalAssay

    replication: str = None
    statistical_analysis_description: str = None
    general_class: Optional[Union[str, List[str]]] = empty_list()
    material_used: Optional[Union[str, List[str]]] = empty_list()
    patient_derived_material_used: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    document: Optional[str] = None
    additional_document: Optional[Union[str, List[str]]] = empty_list()
    read_out_description: Optional[str] = None
    range: Optional[str] = None
    normal_range: Optional[str] = None
    abnormal_range: Optional[str] = None
    indeterminate_range: Optional[str] = None
    validation_control_pathogenic: Optional[str] = None
    validation_control_benign: Optional[str] = None
    significance_threshold: Optional[str] = None
    comment: Optional[Union[str, List[str]]] = empty_list()
    range_type: Optional[Union[str, "RangeType"]] = None
    units: Optional[Union[str, Unit]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.replication):
            self.MissingRequiredField("replication")
        if not isinstance(self.replication, str):
            self.replication = str(self.replication)

        if self._is_empty(self.statistical_analysis_description):
            self.MissingRequiredField("statistical_analysis_description")
        if not isinstance(self.statistical_analysis_description, str):
            self.statistical_analysis_description = str(self.statistical_analysis_description)

        if not isinstance(self.general_class, list):
            self.general_class = [self.general_class] if self.general_class is not None else []
        self.general_class = [v if isinstance(v, str) else str(v) for v in self.general_class]

        if not isinstance(self.material_used, list):
            self.material_used = [self.material_used] if self.material_used is not None else []
        self.material_used = [v if isinstance(v, str) else str(v) for v in self.material_used]

        if not isinstance(self.patient_derived_material_used, list):
            self.patient_derived_material_used = [self.patient_derived_material_used] if self.patient_derived_material_used is not None else []
        self.patient_derived_material_used = [v if isinstance(v, str) else str(v) for v in self.patient_derived_material_used]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.document is not None and not isinstance(self.document, str):
            self.document = str(self.document)

        if not isinstance(self.additional_document, list):
            self.additional_document = [self.additional_document] if self.additional_document is not None else []
        self.additional_document = [v if isinstance(v, str) else str(v) for v in self.additional_document]

        if self.read_out_description is not None and not isinstance(self.read_out_description, str):
            self.read_out_description = str(self.read_out_description)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        if self.normal_range is not None and not isinstance(self.normal_range, str):
            self.normal_range = str(self.normal_range)

        if self.abnormal_range is not None and not isinstance(self.abnormal_range, str):
            self.abnormal_range = str(self.abnormal_range)

        if self.indeterminate_range is not None and not isinstance(self.indeterminate_range, str):
            self.indeterminate_range = str(self.indeterminate_range)

        if self.validation_control_pathogenic is not None and not isinstance(self.validation_control_pathogenic, str):
            self.validation_control_pathogenic = str(self.validation_control_pathogenic)

        if self.validation_control_benign is not None and not isinstance(self.validation_control_benign, str):
            self.validation_control_benign = str(self.validation_control_benign)

        if self.significance_threshold is not None and not isinstance(self.significance_threshold, str):
            self.significance_threshold = str(self.significance_threshold)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        if self.range_type is not None and not isinstance(self.range_type, RangeType):
            self.range_type = RangeType(self.range_type)

        if self.units is not None and not isinstance(self.units, Unit):
            self.units = Unit(self.units)

        super().__post_init__(**kwargs)


@dataclass
class FunctionalAssayResult(YAMLRoot):
    """
    The result of assessing a genetic variant's effect under a single instance of a functional assay.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SEPIO-CG.FunctionalAssayResult
    class_class_curie: ClassVar[str] = "sepio-cg:FunctionalAssayResult"
    class_name: ClassVar[str] = "FunctionalAssayResult"
    class_model_uri: ClassVar[URIRef] = SEPIO-CG.FunctionalAssayResult

    result: str = None
    result_assertion: Optional[str] = None
    assay: Optional[Union[dict, FunctionalAssay]] = None
    variant: Optional[Union[str, VariantCanonicalAlleleId]] = None
    units: Optional[Union[str, Unit]] = None
    validation_control: Optional[Union[str, "ValidationControlType"]] = None
    replicate_count: Optional[int] = None
    standard_deviation: Optional[Decimal] = None
    standard_error_of_mean: Optional[Decimal] = None
    range: Optional[str] = None
    intraquartile_range: Optional[str] = None
    p_value: Optional[Decimal] = None
    is_approximation_by_curator: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.result):
            self.MissingRequiredField("result")
        if not isinstance(self.result, str):
            self.result = str(self.result)

        if self.result_assertion is not None and not isinstance(self.result_assertion, str):
            self.result_assertion = str(self.result_assertion)

        if self.assay is not None and not isinstance(self.assay, FunctionalAssay):
            self.assay = FunctionalAssay(**as_dict(self.assay))

        if self.variant is not None and not isinstance(self.variant, VariantCanonicalAlleleId):
            self.variant = VariantCanonicalAlleleId(self.variant)

        if self.units is not None and not isinstance(self.units, Unit):
            self.units = Unit(self.units)

        if self.validation_control is not None and not isinstance(self.validation_control, ValidationControlType):
            self.validation_control = ValidationControlType(self.validation_control)

        if self.replicate_count is not None and not isinstance(self.replicate_count, int):
            self.replicate_count = int(self.replicate_count)

        if self.standard_deviation is not None and not isinstance(self.standard_deviation, Decimal):
            self.standard_deviation = Decimal(self.standard_deviation)

        if self.standard_error_of_mean is not None and not isinstance(self.standard_error_of_mean, Decimal):
            self.standard_error_of_mean = Decimal(self.standard_error_of_mean)

        if self.range is not None and not isinstance(self.range, str):
            self.range = str(self.range)

        if self.intraquartile_range is not None and not isinstance(self.intraquartile_range, str):
            self.intraquartile_range = str(self.intraquartile_range)

        if self.p_value is not None and not isinstance(self.p_value, Decimal):
            self.p_value = Decimal(self.p_value)

        if self.is_approximation_by_curator is not None and not isinstance(self.is_approximation_by_curator, Bool):
            self.is_approximation_by_curator = Bool(self.is_approximation_by_curator)

        super().__post_init__(**kwargs)


# Enumerations
class RangeType(EnumDefinitionImpl):

    qualitative = PermissibleValue(text="qualitative")
    quantitative = PermissibleValue(text="quantitative")

    _defn = EnumDefinition(
        name="RangeType",
    )

class ValidationControlType(EnumDefinitionImpl):

    pathogenic = PermissibleValue(text="pathogenic")
    benign = PermissibleValue(text="benign")

    _defn = EnumDefinition(
        name="ValidationControlType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "wild-type",
                PermissibleValue(text="wild-type") )

# Slots
class slots:
    pass

slots.associated_disease = Slot(uri=SEPIO-CG['98901'], name="associated disease", curie=SEPIO-CG.curie('98901'),
                   model_uri=SEPIO-CG.associated_disease, domain=None, range=Optional[Union[dict, Disease]])

slots.has_phenotype = Slot(uri=RO['0002200'], name="has phenotype", curie=RO.curie('0002200'),
                   model_uri=SEPIO-CG.has_phenotype, domain=None, range=Optional[Union[dict, PhenotypicFeature]])

slots.has_gene = Slot(uri=SEPIO-CG.has_gene, name="has gene", curie=SEPIO-CG.curie('has_gene'),
                   model_uri=SEPIO-CG.has_gene, domain=None, range=Optional[Union[dict, Gene]])

slots.gene__symbol = Slot(uri=SEPIO-CG.symbol, name="gene__symbol", curie=SEPIO-CG.curie('symbol'),
                   model_uri=SEPIO-CG.gene__symbol, domain=None, range=Optional[str])

slots.gene__synonym = Slot(uri=SEPIO-CG.synonym, name="gene__synonym", curie=SEPIO-CG.curie('synonym'),
                   model_uri=SEPIO-CG.gene__synonym, domain=None, range=Optional[str])

slots.gene__xref = Slot(uri=SEPIO-CG.xref, name="gene__xref", curie=SEPIO-CG.curie('xref'),
                   model_uri=SEPIO-CG.gene__xref, domain=None, range=Optional[str])

slots.geneticCondition__inheritance_pattern = Slot(uri=RO['0000091'], name="geneticCondition__inheritance_pattern", curie=RO.curie('0000091'),
                   model_uri=SEPIO-CG.geneticCondition__inheritance_pattern, domain=None, range=Optional[str])

slots.geneticCondition__label = Slot(uri=RDFS.label, name="geneticCondition__label", curie=RDFS.curie('label'),
                   model_uri=SEPIO-CG.geneticCondition__label, domain=None, range=Optional[str])

slots.geneticCondition__description = Slot(uri=DC.description, name="geneticCondition__description", curie=DC.curie('description'),
                   model_uri=SEPIO-CG.geneticCondition__description, domain=None, range=Optional[str])

slots.geneticCondition__comment = Slot(uri=SEPIO-CG.comment, name="geneticCondition__comment", curie=SEPIO-CG.curie('comment'),
                   model_uri=SEPIO-CG.geneticCondition__comment, domain=None, range=Optional[Union[str, List[str]]])

slots.document__pmid = Slot(uri=SEPIO-CG.pmid, name="document__pmid", curie=SEPIO-CG.curie('pmid'),
                   model_uri=SEPIO-CG.document__pmid, domain=None, range=URIRef)

slots.document__pmc_id = Slot(uri=SEPIO-CG.pmc_id, name="document__pmc_id", curie=SEPIO-CG.curie('pmc_id'),
                   model_uri=SEPIO-CG.document__pmc_id, domain=None, range=Optional[str])

slots.document__comment = Slot(uri=SEPIO-CG.comment, name="document__comment", curie=SEPIO-CG.curie('comment'),
                   model_uri=SEPIO-CG.document__comment, domain=None, range=Optional[Union[str, List[str]]])

slots.variant__canonical_allele_id = Slot(uri=SEPIO-CG.canonical_allele_id, name="variant__canonical_allele_id", curie=SEPIO-CG.curie('canonical_allele_id'),
                   model_uri=SEPIO-CG.variant__canonical_allele_id, domain=None, range=URIRef)

slots.variant__hgvs_c = Slot(uri=SEPIO-CG.hgvs_c, name="variant__hgvs_c", curie=SEPIO-CG.curie('hgvs_c'),
                   model_uri=SEPIO-CG.variant__hgvs_c, domain=None, range=Optional[str])

slots.variant__hgvs_p = Slot(uri=SEPIO-CG.hgvs_p, name="variant__hgvs_p", curie=SEPIO-CG.curie('hgvs_p'),
                   model_uri=SEPIO-CG.variant__hgvs_p, domain=None, range=Optional[str])

slots.variant__clinvar_id = Slot(uri=SEPIO-CG.clinvar_id, name="variant__clinvar_id", curie=SEPIO-CG.curie('clinvar_id'),
                   model_uri=SEPIO-CG.variant__clinvar_id, domain=None, range=Optional[str])

slots.variant__legacy_name = Slot(uri=SEPIO-CG.legacy_name, name="variant__legacy_name", curie=SEPIO-CG.curie('legacy_name'),
                   model_uri=SEPIO-CG.variant__legacy_name, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__general_class = Slot(uri=SEPIO-CG.general_class, name="functionalAssay__general_class", curie=SEPIO-CG.curie('general_class'),
                   model_uri=SEPIO-CG.functionalAssay__general_class, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__material_used = Slot(uri=SEPIO-CG.material_used, name="functionalAssay__material_used", curie=SEPIO-CG.curie('material_used'),
                   model_uri=SEPIO-CG.functionalAssay__material_used, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__patient_derived_material_used = Slot(uri=SEPIO-CG.patient_derived_material_used, name="functionalAssay__patient_derived_material_used", curie=SEPIO-CG.curie('patient_derived_material_used'),
                   model_uri=SEPIO-CG.functionalAssay__patient_derived_material_used, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__description = Slot(uri=DC.description, name="functionalAssay__description", curie=DC.curie('description'),
                   model_uri=SEPIO-CG.functionalAssay__description, domain=None, range=Optional[str])

slots.functionalAssay__document = Slot(uri=SEPIO-CG.document, name="functionalAssay__document", curie=SEPIO-CG.curie('document'),
                   model_uri=SEPIO-CG.functionalAssay__document, domain=None, range=Optional[str])

slots.functionalAssay__additional_document = Slot(uri=SEPIO-CG.additional_document, name="functionalAssay__additional_document", curie=SEPIO-CG.curie('additional_document'),
                   model_uri=SEPIO-CG.functionalAssay__additional_document, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__read_out_description = Slot(uri=SEPIO-CG.read_out_description, name="functionalAssay__read_out_description", curie=SEPIO-CG.curie('read_out_description'),
                   model_uri=SEPIO-CG.functionalAssay__read_out_description, domain=None, range=Optional[str])

slots.functionalAssay__range = Slot(uri=SEPIO-CG.range, name="functionalAssay__range", curie=SEPIO-CG.curie('range'),
                   model_uri=SEPIO-CG.functionalAssay__range, domain=None, range=Optional[str])

slots.functionalAssay__normal_range = Slot(uri=SEPIO-CG.normal_range, name="functionalAssay__normal_range", curie=SEPIO-CG.curie('normal_range'),
                   model_uri=SEPIO-CG.functionalAssay__normal_range, domain=None, range=Optional[str])

slots.functionalAssay__abnormal_range = Slot(uri=SEPIO-CG.abnormal_range, name="functionalAssay__abnormal_range", curie=SEPIO-CG.curie('abnormal_range'),
                   model_uri=SEPIO-CG.functionalAssay__abnormal_range, domain=None, range=Optional[str])

slots.functionalAssay__indeterminate_range = Slot(uri=SEPIO-CG.indeterminate_range, name="functionalAssay__indeterminate_range", curie=SEPIO-CG.curie('indeterminate_range'),
                   model_uri=SEPIO-CG.functionalAssay__indeterminate_range, domain=None, range=Optional[str])

slots.functionalAssay__validation_control_pathogenic = Slot(uri=SEPIO-CG.validation_control_pathogenic, name="functionalAssay__validation_control_pathogenic", curie=SEPIO-CG.curie('validation_control_pathogenic'),
                   model_uri=SEPIO-CG.functionalAssay__validation_control_pathogenic, domain=None, range=Optional[str])

slots.functionalAssay__validation_control_benign = Slot(uri=SEPIO-CG.validation_control_benign, name="functionalAssay__validation_control_benign", curie=SEPIO-CG.curie('validation_control_benign'),
                   model_uri=SEPIO-CG.functionalAssay__validation_control_benign, domain=None, range=Optional[str])

slots.functionalAssay__replication = Slot(uri=SEPIO-CG.replication, name="functionalAssay__replication", curie=SEPIO-CG.curie('replication'),
                   model_uri=SEPIO-CG.functionalAssay__replication, domain=None, range=str)

slots.functionalAssay__statistical_analysis_description = Slot(uri=SEPIO-CG.statistical_analysis_description, name="functionalAssay__statistical_analysis_description", curie=SEPIO-CG.curie('statistical_analysis_description'),
                   model_uri=SEPIO-CG.functionalAssay__statistical_analysis_description, domain=None, range=str)

slots.functionalAssay__significance_threshold = Slot(uri=SEPIO-CG.significance_threshold, name="functionalAssay__significance_threshold", curie=SEPIO-CG.curie('significance_threshold'),
                   model_uri=SEPIO-CG.functionalAssay__significance_threshold, domain=None, range=Optional[str])

slots.functionalAssay__comment = Slot(uri=SEPIO-CG.comment, name="functionalAssay__comment", curie=SEPIO-CG.curie('comment'),
                   model_uri=SEPIO-CG.functionalAssay__comment, domain=None, range=Optional[Union[str, List[str]]])

slots.functionalAssay__range_type = Slot(uri=SEPIO-CG.range_type, name="functionalAssay__range_type", curie=SEPIO-CG.curie('range_type'),
                   model_uri=SEPIO-CG.functionalAssay__range_type, domain=None, range=Optional[Union[str, "RangeType"]])

slots.functionalAssay__units = Slot(uri=SEPIO-CG.units, name="functionalAssay__units", curie=SEPIO-CG.curie('units'),
                   model_uri=SEPIO-CG.functionalAssay__units, domain=None, range=Optional[Union[str, Unit]])

slots.functionalAssayResult__result = Slot(uri=SEPIO-CG.result, name="functionalAssayResult__result", curie=SEPIO-CG.curie('result'),
                   model_uri=SEPIO-CG.functionalAssayResult__result, domain=None, range=str)

slots.functionalAssayResult__result_assertion = Slot(uri=SEPIO-CG.result_assertion, name="functionalAssayResult__result_assertion", curie=SEPIO-CG.curie('result_assertion'),
                   model_uri=SEPIO-CG.functionalAssayResult__result_assertion, domain=None, range=Optional[str])

slots.functionalAssayResult__assay = Slot(uri=SEPIO-CG.assay, name="functionalAssayResult__assay", curie=SEPIO-CG.curie('assay'),
                   model_uri=SEPIO-CG.functionalAssayResult__assay, domain=None, range=Optional[Union[dict, FunctionalAssay]])

slots.functionalAssayResult__variant = Slot(uri=SEPIO-CG.variant, name="functionalAssayResult__variant", curie=SEPIO-CG.curie('variant'),
                   model_uri=SEPIO-CG.functionalAssayResult__variant, domain=None, range=Optional[Union[str, VariantCanonicalAlleleId]])

slots.functionalAssayResult__units = Slot(uri=SEPIO-CG.units, name="functionalAssayResult__units", curie=SEPIO-CG.curie('units'),
                   model_uri=SEPIO-CG.functionalAssayResult__units, domain=None, range=Optional[Union[str, Unit]])

slots.functionalAssayResult__validation_control = Slot(uri=SEPIO-CG.validation_control, name="functionalAssayResult__validation_control", curie=SEPIO-CG.curie('validation_control'),
                   model_uri=SEPIO-CG.functionalAssayResult__validation_control, domain=None, range=Optional[Union[str, "ValidationControlType"]])

slots.functionalAssayResult__replicate_count = Slot(uri=SEPIO-CG.replicate_count, name="functionalAssayResult__replicate_count", curie=SEPIO-CG.curie('replicate_count'),
                   model_uri=SEPIO-CG.functionalAssayResult__replicate_count, domain=None, range=Optional[int])

slots.functionalAssayResult__standard_deviation = Slot(uri=SEPIO-CG.standard_deviation, name="functionalAssayResult__standard_deviation", curie=SEPIO-CG.curie('standard_deviation'),
                   model_uri=SEPIO-CG.functionalAssayResult__standard_deviation, domain=None, range=Optional[Decimal])

slots.functionalAssayResult__standard_error_of_mean = Slot(uri=SEPIO-CG.standard_error_of_mean, name="functionalAssayResult__standard_error_of_mean", curie=SEPIO-CG.curie('standard_error_of_mean'),
                   model_uri=SEPIO-CG.functionalAssayResult__standard_error_of_mean, domain=None, range=Optional[Decimal])

slots.functionalAssayResult__range = Slot(uri=SEPIO-CG.range, name="functionalAssayResult__range", curie=SEPIO-CG.curie('range'),
                   model_uri=SEPIO-CG.functionalAssayResult__range, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[<>]?[-\d]+(.\d+)? - [<>]?[-\d]+(.\d+)?'))

slots.functionalAssayResult__intraquartile_range = Slot(uri=SEPIO-CG.intraquartile_range, name="functionalAssayResult__intraquartile_range", curie=SEPIO-CG.curie('intraquartile_range'),
                   model_uri=SEPIO-CG.functionalAssayResult__intraquartile_range, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[<>]?[-\d]+(.\d+)? - [<>]?[-\d]+(.\d+)?'))

slots.functionalAssayResult__p_value = Slot(uri=SEPIO-CG.p_value, name="functionalAssayResult__p_value", curie=SEPIO-CG.curie('p_value'),
                   model_uri=SEPIO-CG.functionalAssayResult__p_value, domain=None, range=Optional[Decimal])

slots.functionalAssayResult__is_approximation_by_curator = Slot(uri=SEPIO-CG.is_approximation_by_curator, name="functionalAssayResult__is_approximation_by_curator", curie=SEPIO-CG.curie('is_approximation_by_curator'),
                   model_uri=SEPIO-CG.functionalAssayResult__is_approximation_by_curator, domain=None, range=Optional[Union[bool, Bool]])

slots.genetic_condition_associated_disease = Slot(uri=SEPIO-CG['98901'], name="genetic condition_associated disease", curie=SEPIO-CG.curie('98901'),
                   model_uri=SEPIO-CG.genetic_condition_associated_disease, domain=GeneticCondition, range=Optional[Union[Union[dict, Disease], List[Union[dict, Disease]]]])

slots.genetic_condition_has_phenotype = Slot(uri=RO['0002200'], name="genetic condition_has phenotype", curie=RO.curie('0002200'),
                   model_uri=SEPIO-CG.genetic_condition_has_phenotype, domain=GeneticCondition, range=Optional[Union[Union[dict, PhenotypicFeature], List[Union[dict, PhenotypicFeature]]]])

slots.genetic_condition_has_gene = Slot(uri=SEPIO['0000278'], name="genetic condition_has gene", curie=SEPIO.curie('0000278'),
                   model_uri=SEPIO-CG.genetic_condition_has_gene, domain=GeneticCondition, range=Optional[Union[dict, Gene]])