Algorithm 1 Discrete prompt optimization: SI-based EVOPROMPT

Require: Initial prompts \( P_0 = \{p_1, p_2, \ldots, p_N\} \), size of population \( N \), a dev set \( D \), \( f_D(\cdot) \) denotes the score of a prompt on the desired LLM evaluated on \( D \), a pre-defined number of iterations \( T \), carefully designed swarm intelligence operators to generate a new prompt SwarmEvo(\cdot)
1: Initial evaluation scores: \( S_0 \leftarrow \{ s_i = f_D(p_i) \mid i \in [1, N] \} \)
2: Initialize velocity \( V_0 \) for each particle (prompt) in the population
3: Initialize personal best \( P_{best} \) and global best \( G_{best} \) positions
4: for \( t = 1 \) to \( T \) do
5:    for each prompt \( p_i \in P_t \) do
6:        Update velocity \( V_i \) based on \( P_{best} \) and \( G_{best} \)
7:        Update position (content) of \( p_i \) based on updated velocity \( V_i \)
8:        Generate a new prompt \( p'_i \) based on the updated position
9:        Evaluation: \( s'_i \leftarrow f_D(p'_i, D) \)
10:       Update personal best \( P_{best}[i] \) if \( s'_i > P_{best}[i] \)
11:    end for
12:    Update global best \( G_{best} \) based on the best personal best in \( P_{best} \)
13:    Update: \( P_t \leftarrow \{ P_t, p'_i \} \) and \( S_t \leftarrow \{ S_t, s'_i \} \) based on the evaluation scores
14: end for
15: Return the best prompt, \( p^* \), among the final population \( P_T \): \( p^* \leftarrow \arg\max_{p \in P_T} f(p, D) \)
