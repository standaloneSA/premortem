# PreMortem

PreMortem will evaluate plans submitted against a library of post-mortems and make suggestions based on lessons learned. 

## How it works 

There are two phases to the process: 

1. Training 

    In the training phase, examples of post-mortems are provided. The full text is vectorized, as well as each individual paragraph. Key words and concepts are produced and vectorized. All of this is then stored in a vector database for later retrieval.

2. Evaluation

    During evaluation, a plan is submitted. The plan has the same breakout and treatment as the post-mortems were during training, and then a similarity search is done for each of the concepts and key words, with the top matches presented to the user.


