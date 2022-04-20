
# Class: Document


A collection of information content entities intended to be understood together as a whole

URI: [sepio-cg:Document](http://purl.obolibrary.org/obo/SEPIOCG_Document)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Document&#124;pmid:string;pmc_id:string%20%3F;comment:string%20*])](https://yuml.me/diagram/nofunky;dir:TB/class/[Document&#124;pmid:string;pmc_id:string%20%3F;comment:string%20*])

## Attributes


### Own

 * [➞pmid](document__pmid.md)  <sub>1..1</sub>
     * Description: Identifier of a manuscript in PubMed database
     * Range: [String](types/String.md)
 * [➞pmc_id](document__pmc_id.md)  <sub>0..1</sub>
     * Description: Identifier of a manuscript in PubMedCentral database
     * Range: [String](types/String.md)
 * [➞comment](document__comment.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | IAO:0000310 |

