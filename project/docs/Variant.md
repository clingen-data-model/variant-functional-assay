
# Class: Variant


A genetic variant, preferably identified by a canonical allele id

URI: [sepio-cg:Variant](http://purl.obolibrary.org/obo/SEPIOCG_Variant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Gene],[Gene]<has%20gene%200..1-++[Variant&#124;canonical_allele_id:string;hgvs_c:string%20%3F;hgvs_p:string%20%3F;clinvar_id:string%20%3F;legacy_name:string%20*],[FunctionalAssayResult]-%20variant%200..1>[Variant],[FunctionalAssayResult])](https://yuml.me/diagram/nofunky;dir:TB/class/[Gene],[Gene]<has%20gene%200..1-++[Variant&#124;canonical_allele_id:string;hgvs_c:string%20%3F;hgvs_p:string%20%3F;clinvar_id:string%20%3F;legacy_name:string%20*],[FunctionalAssayResult]-%20variant%200..1>[Variant],[FunctionalAssayResult])

## Referenced by Class

 *  **None** *[➞variant](functionalAssayResult__variant.md)*  <sub>0..1</sub>  **[Variant](Variant.md)**

## Attributes


### Own

 * [has gene](has_gene.md)  <sub>0..1</sub>
     * Description: Connects an entity associated with one or more genes
     * Range: [Gene](Gene.md)
 * [➞canonical_allele_id](variant__canonical_allele_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [➞hgvs c](variant__hgvs_c.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞hgvs p](variant__hgvs_p.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞clinvar id](variant__clinvar_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞legacy name](variant__legacy_name.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
