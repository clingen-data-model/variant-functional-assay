
# Class: genetic condition


A disease, or a set of one or more co-occurring phenotypes, typically controlled by a single locus with a defined inheritance pattern.

URI: [sepio-cg:GeneticCondition](http://purl.obolibrary.org/obo/SEPIOCG_GeneticCondition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature],[Gene]<has%20gene%200..1-++[GeneticCondition&#124;inheritance_pattern:string%20%3F;label:string%20%3F;description:string%20%3F;comment:string%20*],[PhenotypicFeature]<has%20phenotype%200..*-++[GeneticCondition],[Disease]<associated%20disease%200..*-++[GeneticCondition],[Gene],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature],[Gene]<has%20gene%200..1-++[GeneticCondition&#124;inheritance_pattern:string%20%3F;label:string%20%3F;description:string%20%3F;comment:string%20*],[PhenotypicFeature]<has%20phenotype%200..*-++[GeneticCondition],[Disease]<associated%20disease%200..*-++[GeneticCondition],[Gene],[Disease])

## Referenced by Class


## Attributes


### Own

 * [genetic condition➞associated disease](genetic_condition_associated_disease.md)  <sub>0..\*</sub>
     * Description: A recognizible grouping of pathological observed phenotypes occuring from a common cause
     * Range: [Disease](Disease.md)
 * [genetic condition➞has phenotype](genetic_condition_has_phenotype.md)  <sub>0..\*</sub>
     * Description: An expressed characteristic of an organism
     * Range: [PhenotypicFeature](PhenotypicFeature.md)
 * [genetic condition➞has gene](genetic_condition_has_gene.md)  <sub>0..1</sub>
     * Description: The gene associated with a genetic condition
     * Range: [Gene](Gene.md)
 * [➞inheritance_pattern](geneticCondition__inheritance_pattern.md)  <sub>0..1</sub>
     * Description: The manner in which a genetic condition is inherited
     * Range: [String](types/String.md)
 * [➞label](geneticCondition__label.md)  <sub>0..1</sub>
     * Description: A name given to the resource
     * Range: [String](types/String.md)
 * [➞description](geneticCondition__description.md)  <sub>0..1</sub>
     * Description: Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.

     * Range: [String](types/String.md)
 * [➞comment](geneticCondition__comment.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SEPIO:0000219 |

