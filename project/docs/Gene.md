
# Class: gene


A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions.

URI: [sepio-cg:Gene](http://purl.obolibrary.org/obo/SEPIOCG_Gene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneticCondition],[GeneticCondition]++-%20has%20gene%200..1>[Gene&#124;symbol:string%20%3F;synonym:string%20%3F;xref:string%20%3F],[GeneticCondition]++-%20has%20gene(i)%200..1>[Gene],[Variant]++-%20has%20gene%200..1>[Gene],[Variant])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneticCondition],[GeneticCondition]++-%20has%20gene%200..1>[Gene&#124;symbol:string%20%3F;synonym:string%20%3F;xref:string%20%3F],[GeneticCondition]++-%20has%20gene(i)%200..1>[Gene],[Variant]++-%20has%20gene%200..1>[Gene],[Variant])

## Identifier prefixes

 * HGNC
 * NCBIGene

## Referenced by Class

 *  **[GeneticCondition](GeneticCondition.md)** *[genetic condition➞has gene](genetic_condition_has_gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[has gene](has_gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**

## Attributes


### Own

 * [➞symbol](gene__symbol.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞synonym](gene__synonym.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞xref](gene__xref.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SO:0000704 |

