Paper: [Talent vs Luck: the role of randomness in success and failure](https://arxiv.org/abs/1802.07068)

[powerlaw: A Python Package for Analysis of Heavy-Tailed Distributions](https://github.com/jeffalstott/powerlaw)

[What does the distribution of IQ scores look like?](https://www.quora.com/What-does-the-distribution-of-IQ-scores-look-like)

[Power Laws: How Nonlinear Relationships Amplify Results](https://fs.blog/2017/11/power-laws/)

[Pareto distribution](https://en.wikipedia.org/wiki/Pareto_distribution)

[Power law](https://en.wikipedia.org/wiki/Power_law)

Recreate a simulations based on a model Talent vs Luck:

1. First task is to implement the simulation process from the paper Talent vs Luck.
    - create a grid 
    - use random module to fill the grid with random numbers, populate grid with n-times of certain number
    - real randomness
    
    - find out how generate numbers from the normal distribution: function normalvariate(mean, sd)
    
    - check `powerlaw`. It's a toolbox using the statistical methods developed to define if a probability
      distribution fits a power law. A small change in the value of x leads to proportionally change in the value of y.

2. Second task is to build a web app where user can configure their own parameters and experience.
    - team players game (more then one user)
    - for each new user the backend will create new instance of a simulation;
    