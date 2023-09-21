# GA_for_feature_selection

Genetic Algorithm for feature selection

In the context of feature selection,

### Parameter

`pop `represents the population size in one generation. Generally, a higher population size results in greater diversity.

The `lower bound` is set to 0 (indicating the feature is not chosen), while the `upper bound` is set to 1 (indicating it is chosen).

The `cr `parameter represents the crossover rate, where a higher value indicates a greater probability of exchanging information with other chromosomes.

The `mt `parameter represents the mutation rate, with higher values indicating increased randomness and diversity.

Step

1. initial is the first step of the GA
2. Use crossover and mutation to get the new generation chromosome.
3. Evaluate the accuracy of each chromosome.
