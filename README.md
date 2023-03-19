# garden-path-gpt2

Use the make_sents_{type}() method to build a list of sentences.
Arguments such as context and extension can be used to extend the length of a garden path effect
Arguments such as sent_type, comma, unreduced, and that can be used to negate garden path effects in various ways, as discussed in the paper.

Refer to this paper for more information about the methods used and key takeaways here: https://aclanthology.org/2022.blackboxnlp-1.25

# Acknowledgments:
The sentences and file structure in this repo are adapted from the datasets provided by Futrell et al. (2019), Neural Language Models as Psycholinguistic Subjects: Representations of Syntactic State (https://arxiv.org/abs/1903.03260); and van Schnidel & Linzen (2018): Modeling garden path effects without explicit hierarchical syntax (https://tallinzen.net/media/papers/vanschijndel_linzen_2018_cogsci.pdf), many of which were originally taken from Grodner et al., 2003:

Grodner, D., Gibson, E., Argaman, V., & Babyonyshev, M. (2003). Against repair-based reanalysis in sentence comprehension. Journal of Psycholinguistic Research, 32(2), 141–166. https://doi.org/10.1023/A:1022496223965


# Citation:
Please cite this paper as:

```
@inproceedings{jurayj-etal-2022-garden,
    title = "Garden Path Traversal in {GPT}-2",
    author = "Jurayj, William  and
      Rudman, William  and
      Eickhoff, Carsten",
    booktitle = "Proceedings of the Fifth BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.blackboxnlp-1.25",
    pages = "305--313",
}
```
